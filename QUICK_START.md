# Quick Start — AI-Ready SSDLC Harness

**TL;DR:** Commands and steps to get from zero to deployed.

---

## Phase 1: Enterprise Setup (Once)

### For: Technical Lead

```bash
# 1. Complete the form (answer sections 0-10)
open D4_Enterprise_Harness_Form.md

# 2. Answer gating decisions FIRST (section 0)
#    - 0.1: Gateway routing
#    - 0.2: MDM reliability
#    - 0.6: KPIs frozen? (escalate if no)
#    - 0.7: Memory tiers? (escalate if no)

# 3. Fill sections 1-10
#    For each section, follow GENERATE → VERIFY steps

# 4. Validate the enterprise plugin
cd enterprise
claude plugin validate .
# Expected: No errors

# 5. Deploy managed settings (choose Route A or B based on 0.1/0.2)
# Route A (MDM reliable):
cp enterprise/managed/managed-settings.json \
   /Library/Application\ Support/ClaudeCode/
cp enterprise/managed/managed-mcp.json \
   /Library/Application\ Support/ClaudeCode/

# Route B (no MDM):
# → Use admin console to deliver managed-settings.json

# 6. Test on one machine
claude /status
# Should show: "Setting source: enterprise"

# 7. Publish to marketplace
claude plugin publish enterprise

# 8. SAVE THE VERSION
#    From enterprise/.claude-plugin/plugin.json:
#    "version": "0.1.0"  ← Record this!

# 9. Verify everything
/status           # Enterprise source
/context          # Enterprise CLAUDE.md
/mcp              # Admitted servers
/agents           # Five roles
/skills           # Seed skills
/hooks            # Enterprise hooks
/doctor           # No issues
```

**✅ Enterprise is live. Record version number (e.g., 0.1.0) for applications.**

---

## Phase 2: Application Setup (Per App)

### For: Dev Lead + Team

```bash
# 1. Complete the app form
open D4_Application_Harness_Form.md

# 2. Fill section 0 (application identity)
#    - Application name: <my-app>
#    - Enterprise plugin version: 0.1.0  ← FROM PHASE 1
#    - Stack: Java, Node.js, Python, etc.

# 3. Fill section 2 (knowledge connection) - CRITICAL
#    Run explorer agent to draft architecture
#    Then dev lead corrects it
#    Results go into .claude/context/

# 4. Fill sections 1, 3-10 (follow GENERATE steps)

# 5. Copy template to app repo
cp -r application-template/* /path/to/app-repo/

# 6. Verify in app repo
cd /path/to/app-repo
claude /status           # Narrowed permissions
claude /context          # Enterprise + app CLAUDE.md
claude /mcp              # Enterprise + app servers
claude /agents           # Enabled roles
claude /doctor           # No issues

# 7. Run write-attempt test (from section 5)
#    Try to edit a file → should be REFUSED
#    Capture the refusal message + trace reference
#    This is your compliance evidence

# 8. Sign closeout (section 11 of form)
#    - Dev lead: _____ Date: _____
#    - Tech lead: _____ Date: _____
#    - App owner: _____ Date: _____

# 9. Archive completed form
```

**✅ Application configured and verified. Enterprise + app policies active.**

---

## Phase 3: Verification (Any Phase)

### Quick Checks

```bash
# From enterprise/ or app repo:

/status              # Shows source (enterprise / narrowed)
/context             # Lists auto-loaded files
/mcp                 # Lists MCP servers
/agents              # Lists enabled roles
/skills              # Lists available skills
/hooks               # Lists registered hooks
/doctor              # Finds problems

# Test write boundary:
# Try: Edit src/main.py → should be ALLOWED
# Try: Edit .env → should be REFUSED
```

---

## Phase 4: Optional — Generate PowerPoint Deck

### For: Leadership/Stakeholders

```bash
# After BOTH forms are completed:

python3 genbrief.py \
  --enterprise D4_Enterprise_Harness_Form.md \
  --apps D4_Application_Harness_Form.md \
  --out D4_Harness_Deck_Brief.md

# Result: D4_Harness_Deck_Brief.md (Claude-ready brief)

# Ask Claude Code to generate deck:
# "Generate a PowerPoint deck brief from this markdown"
# → Produces PPTX with deployment summary
```

---

## Common Issues

| Issue | Fix |
|---|---|
| Section 0.6 or 0.7 is "no" | STOP. Escalate before proceeding. |
| Plugin won't validate | Check `.claude-plugin/plugin.json` syntax |
| Enterprise source not in `/status` | Are managed settings in the right path? |
| Write-attempt test doesn't refuse | Run `claude /status` and check permission mode |
| App can't find enterprise version | Did you record the version from Phase 1? |

---

## Command Reference

```bash
# Validation
claude plugin validate enterprise

# Verification
/status /context /mcp /agents /skills /hooks /doctor

# Tests
make test
make build
make lint

# Git
git status
git add .
git commit -m "message"
git push origin main
```

---

## Key Files

| File | Purpose |
|---|---|
| `D4_Enterprise_Harness_Form.md` | Enterprise configuration (Phase 1) |
| `D4_Application_Harness_Form.md` | App configuration (Phase 2) |
| `DEPLOYMENT_GUIDE.md` | Full step-by-step procedures |
| `HARNESS_GUIDE.md` | Architecture & understanding |
| `VERIFY.md` | Verification checklist |
| `enterprise/` | Enterprise plugin files |
| `application-template/` | App template (copy to app repo) |

---

## Phase Timelines

**Enterprise:** 1-2 weeks (answer section 0 first!)  
**Per App:** 3-5 days (knowledge connection authoring is the longest)  
**Verification:** 30 minutes (run all checks)  

---

## Next Steps

1. **Enterprise team:** `open D4_Enterprise_Harness_Form.md` → Answer section 0
2. **Dev leads (wait for enterprise):** `open D4_Application_Harness_Form.md` → Fill section 0 with enterprise version
3. **Leadership:** After forms done, run `genbrief.py` → Generate deck

---

**Ready?** Start with `D4_Enterprise_Harness_Form.md` section 0.

**Need detail?** Read `DEPLOYMENT_GUIDE.md`.

**Need to understand?** Read `HARNESS_GUIDE.md`.
