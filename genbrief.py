#!/usr/bin/env python3
"""
D4 harness deck brief generator.

Reads the filled-in D4 MD forms:
  - one enterprise form  (D4_Enterprise_Harness_Form.md)
  - up to five application forms (D4_Application_Harness_Form*.md)

Writes one instruction file, D4_Harness_Deck_Brief.md, which is handed to Claude to
generate the D4 harness deck in the style of the Claude Code reference architecture.

Usage:
  python3 genbrief.py --enterprise enterprise.md --apps app1.md app2.md ... [--out brief.md]

The parser is tolerant of hand formatting. Any value still left as <...> is carried through
marked NOT PROVIDED rather than failing, so an incomplete form still produces a usable brief
that shows exactly what is missing.
"""
import argparse, re, sys, os, datetime

PLACEHOLDER = re.compile(r'^<.*>$')

def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

def is_unset(v):
    if v is None: return True
    v = v.strip().strip('`')
    return v == '' or PLACEHOLDER.match(v) is not None or v.lower() in ('<...>', 'tbd', 'n/a')

def clean(v):
    return v.strip().strip('`').strip() if v else ''

def sections(md):
    """Split a form into {heading: body} on '## ' boundaries."""
    out, cur, buf = {}, '_preamble', []
    for line in md.splitlines():
        m = re.match(r'^##\s+(.*)', line)
        if m:
            out[cur] = '\n'.join(buf); cur = m.group(1).strip(); buf = []
        else:
            buf.append(line)
    out[cur] = '\n'.join(buf)
    return out

def kv_from_tables(body):
    """Pull two-column | key | value | rows out of a section body."""
    pairs = {}
    for line in body.splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 2:
            continue
        k = cells[0]
        if not k or set(k) <= set('-: '):   # separator row
            continue
        if k.lower() in ('field', 'control', 'decision', '#', 'category', 'role',
                         'rule file', 'skill', 'eval setting', 'source', 'purpose',
                         'tier', 'hook', 'mechanism', 'candidate'):
            continue
        pairs[k] = cells[1]
    return pairs

def find(pairs, *needles):
    for k, v in pairs.items():
        kl = k.lower()
        if all(n in kl for n in needles):
            return v
    return None

# ---------- enterprise extraction ----------
def parse_enterprise(path):
    md = read(path); S = sections(md)
    e = {'_source': os.path.basename(path)}
    dec = kv_from_tables(S.get('0. Decisions that gate everything', ''))
    ident = kv_from_tables(S.get('1. Identity of the enterprise set', ''))
    e['plugin_name'] = clean(find(ident, 'plugin', 'name'))
    e['version'] = clean(find(ident, 'version'))
    e['tech_lead'] = clean(find(ident, 'technical lead'))
    e['marketplace'] = clean(find(ident, 'marketplace', 'name'))
    e['route'] = 'B (server-managed, no MDM)' if (find(dec, 'device management') and 'no' in clean(find(dec, 'device management')).lower()) else 'A (managed file) or B — confirm'
    e['gateway'] = clean(find(dec, 'gateway'))
    e['retention'] = clean(find(dec, 'retention'))
    e['hooks_policy'] = clean(find(dec, 'hooks'))
    e['kpi_frozen'] = clean(find(dec, 'kpi'))
    e['tiers_agreed'] = clean(find(dec, 'memory tier') or find(dec, 'tier'))
    otel = kv_from_tables(S.get('10. Observability (primitive 10)', ''))
    e['otlp'] = clean(find(otel, 'otlp'))
    e['open_items'] = []
    for label, val in [('KPI definitions frozen', e['kpi_frozen']),
                       ('Memory tiers agreed', e['tiers_agreed']),
                       ('Gateway routing', e['gateway'])]:
        if is_unset(val) or (val and val.lower().startswith('no')):
            e['open_items'].append(label)
    return e

# ---------- application extraction ----------
def parse_application(path):
    md = read(path); S = sections(md)
    a = {'_source': os.path.basename(path)}
    idt = kv_from_tables(S.get('0. Application identity and prerequisites', ''))
    a['name'] = clean(find(idt, 'application name'))
    a['ent_version'] = clean(find(idt, 'enterprise plugin version'))
    a['dev_lead'] = clean(find(idt, 'dev lead'))
    a['autonomy'] = clean(find(idt, 'autonomy target'))
    a['kpis'] = clean(find(idt, 'kpi'))
    a['stack'] = clean(find(idt, 'languages'))
    a['repos'] = clean(find(idt, 'repository set'))
    # command contract passes?
    ctx = S.get('2. The knowledge connection (primitives 2, 3) \u2192 `.claude/context/`', '') or \
          next((v for k, v in S.items() if 'knowledge connection' in k.lower()), '')
    a['cmd_rows'] = []
    for line in ctx.splitlines():
        if line.strip().startswith('|') and any(w in line for w in ('Build', 'Test', 'Lint', 'Type check')):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) >= 3:
                a['cmd_rows'].append((cells[0], cells[-1]))
    # write test
    ex = next((v for k, v in S.items() if 'execution environment' in k.lower()), '')
    exk = kv_from_tables(ex)
    a['write_attempt'] = clean(find(exk, 'what you attempted'))
    a['write_refused'] = clean(find(exk, 'how it was refused'))
    a['write_trace'] = clean(find(exk, 'trace reference'))
    # profile: count unset critical fields
    a['missing'] = []
    for label, val in [('application name', a['name']), ('enterprise version', a['ent_version']),
                       ('autonomy target', a['autonomy']), ('D3 KPIs', a['kpis']),
                       ('stack', a['stack']), ('write-attempt test', a['write_attempt'])]:
        if is_unset(val):
            a['missing'].append(label)
    return a

def show(v):
    return clean(v) if not is_unset(v) else '**NOT PROVIDED**'

def build_brief(ent, apps):
    d = datetime.date.today().isoformat()
    L = []
    P = L.append
    P("# D4 Harness Deck — generation brief")
    P("")
    P(f"> Generated {d} from {ent['_source']} and {len(apps)} application form(s).")
    P("> Hand this file to Claude with the instruction: *build the D4 harness deck from this brief.*")
    P("")
    P("---")
    P("")
    P("## Instruction to Claude")
    P("")
    P("Build a PowerPoint deck titled **D4 Harness — Deployed** for RRD Autonomous Development.")
    P("Use the **exact visual language of the Claude Code Reference Architecture deck**: white")
    P("background, Accenture purple palette (deep `#460073`, mid `#7500C0`, accent `#A100FF`),")
    P("Segoe UI, tier bands, rounded-rect component boxes, primitive tags, plateau/gap notation,")
    P("and the eyebrow + title + rule header. This deck is the **delivery instance** of that")
    P("architecture, so it should look like it came from the same family.")
    P("")
    P("Every value below is already resolved from the filled forms. Where a value reads")
    P("**NOT PROVIDED**, render the slide with a visible placeholder chip so the gap is obvious")
    P("in review — do not invent a value.")
    P("")
    P("---")
    P("")
    P("## Slide plan")
    P("")
    P("| # | Slide | Source in the reference architecture | Content |")
    P("|---|---|---|---|")
    P("| 1 | Title | scope slide | D4 Harness Deployed; enterprise + " + str(len(apps)) + " apps; plateau P1 |")
    P("| 2 | What D4 delivered | plateau view (slide 16) | P1 reached: the components that now exist |")
    P("| 3 | Enterprise layer | enterprise harness (slide 11) | tiers 0–1 as configured, from the enterprise form |")
    P("| 4 | Primitive coverage | primitive map (slide 4) | all ten primitives → the artefact realizing each |")
    P("| 5 | Tool access | MCP access control (slide 7) | route chosen, admitted catalogue |")
    P("| 6 | Per-application status | profiles (slide 19) | one row per app: profile + write-test evidence |")
    for i, a in enumerate(apps):
        P(f"| {7+i} | {show(a['name']) } | application instance (slide 12) | tier-3 config for this app |")
    P(f"| {7+len(apps)} | Read-only boundary | deployment view (slide 14) | how the boundary is held + write-test results |")
    P(f"| {8+len(apps)} | Open items | — | what must close before Phase 3 |")
    P("")
    P("---")
    P("")
    P("## Enterprise layer — resolved values")
    P("")
    P(f"- **Plugin**: {show(ent['plugin_name'])} version {show(ent['version'])}")
    P(f"- **Technical lead**: {show(ent['tech_lead'])}")
    P(f"- **Marketplace**: {show(ent['marketplace'])}")
    P(f"- **MCP access route**: {show(ent['route'])}")
    P(f"- **Gateway routing**: {show(ent['gateway'])}")
    P(f"- **Transcript retention**: {show(ent['retention'])}")
    P(f"- **Hook policy**: {show(ent['hooks_policy'])}")
    P(f"- **Telemetry endpoint**: {show(ent['otlp'])}")
    P("")
    P("Render slide 3 as the tier-0 and tier-1 bands from the enterprise harness slide, with")
    P("these values placed on the matching components.")
    P("")
    P("---")
    P("")
    P("## Applications — resolved values")
    P("")
    for a in apps:
        P(f"### {show(a['name'])}  ({a['_source']})")
        P("")
        P(f"- **Inherits enterprise version**: {show(a['ent_version'])}")
        P(f"- **RRD Dev Lead**: {show(a['dev_lead'])}")
        P(f"- **Autonomy target (D2)**: {show(a['autonomy'])}")
        P(f"- **D3 KPIs**: {show(a['kpis'])}")
        P(f"- **Stack**: {show(a['stack'])}")
        P(f"- **Repositories**: {show(a['repos'])}")
        if a['cmd_rows']:
            passes = ', '.join(f"{c[0]}={c[1]}" for c in a['cmd_rows'])
            P(f"- **Command contract**: {passes}")
        P(f"- **Write-attempt test**: attempted `{show(a['write_attempt'])}`, refused by "
          f"`{show(a['write_refused'])}`, trace `{show(a['write_trace'])}`")
        prof = 'Full' if not a['missing'] else ('Substituted' if len(a['missing']) > 3 else 'Reduced')
        P(f"- **Implementation profile (derived)**: {prof}")
        if a['missing']:
            P(f"- **Missing before this app is complete**: {', '.join(a['missing'])}")
        P("")
    P("---")
    P("")
    P("## Per-application status slide (slide 6)")
    P("")
    P("Render as the implementation-profiles table. One row per application:")
    P("")
    P("| Application | Profile | Write-test | KPIs | Notes |")
    P("|---|---|---|---|---|")
    for a in apps:
        prof = 'Full' if not a['missing'] else ('Substituted' if len(a['missing']) > 3 else 'Reduced')
        wt = 'passed' if not is_unset(a['write_attempt']) else 'NOT PROVIDED'
        kp = 'set' if not is_unset(a['kpis']) else 'NOT PROVIDED'
        note = '' if not a['missing'] else 'gaps: ' + '; '.join(a['missing'])
        P(f"| {show(a['name'])} | {prof} | {wt} | {kp} | {note} |")
    P("")
    P("> A **Substituted** profile on execution or assurance is a stop condition. Flag it red.")
    P("")
    P("---")
    P("")
    P("## Open items for the closing slide")
    P("")
    allopen = list(ent['open_items'])
    for a in apps:
        if is_unset(a['kpis']):
            allopen.append(f"{show(a['name'])}: D3 KPIs not frozen")
        if is_unset(a['write_attempt']):
            allopen.append(f"{show(a['name'])}: write-attempt test not recorded")
    if not allopen:
        P("- None outstanding. All forms complete.")
    else:
        for o in allopen:
            P(f"- {o}")
    P("")
    P("> KPI freeze and the write-attempt test are the two that block Phase 3. Put them first.")
    P("")
    return '\n'.join(L) + '\n'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--enterprise', required=True)
    ap.add_argument('--apps', nargs='+', required=True)
    ap.add_argument('--out', default='D4_Harness_Deck_Brief.md')
    args = ap.parse_args()
    if len(args.apps) > 5:
        print('warning: more than five application forms supplied', file=sys.stderr)
    ent = parse_enterprise(args.enterprise)
    apps = [parse_application(p) for p in args.apps]
    brief = build_brief(ent, apps)
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write(brief)
    print(f'wrote {args.out}  ({len(brief)} bytes, {len(apps)} apps)')

if __name__ == '__main__':
    main()
