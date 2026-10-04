# Phase D4 Completion Checklist

**Complete verification that your harness configuration is production-ready**

---

## Understanding the D4 Acronym

**D = Development Phase** (in the AI-Ready Secure Software Development Lifecycle framework)

| Phase | Full Name | Focus | Duration | Owner | Status |
|-------|-----------|-------|----------|-------|--------|
| **D1** | Development Phase 1: Intake | Gather requirements | 1-2 weeks | Product Lead | Earlier phase |
| **D2** | Development Phase 2: Shape | Design solution | 1-2 weeks | Tech Lead | Earlier phase |
| **D3** | Development Phase 3: Capability Candidates | AI assistant specs | 1-2 weeks | Dev Lead | Earlier phase |
| **D4** | Development Phase 4: **Harness** | Setup Claude Code governance | 1-2 weeks | Dev + Tech Lead | **← YOU ARE HERE** |
| **D5** | Development Phase 5: Deploy | Release to staging | 2-4 weeks | DevOps + QA | Next phase |
| **D6** | Development Phase 6: Gate | Compliance audit | 1-2 weeks | Security Lead | Later phase |
| **D7** | Development Phase 7: Operate | Production monitoring | Ongoing | DevOps + SRE | Later phase |

---

## What is Phase D4?

**D4 = Development Phase 4: Harness**

Phase D4 is where you set up the governance framework (`.claude/` configuration) that allows Claude Code to work safely and effectively for your team.

When D4 is complete, your project has:
- ✅ Security baseline documented
- ✅ Code conventions established
- ✅ Compliance mapped to controls
- ✅ Claude Code fully configured
- ✅ Team trained and ready

---

## Pre-Completion: Have You Done All 8 Phases?

Before using this checklist, verify you've completed all 8 setup phases:

### Phase 1: Project Foundation ✅ / ❌
- [ ] Project details documented
- [ ] Technology stack identified
- [ ] Compliance requirements assessed
- [ ] Git repository initialized
- **Deliverable:** `docs/PROJECT_INFO.md` (if not present, stop and complete Phase 1)

### Phase 2: Architecture & Specifications ✅ / ❌
- [ ] System architecture documented
- [ ] Detailed architecture created
- [ ] Architectural decisions recorded (ADRs)
- **Deliverables:**
  - [ ] `.claude/context/architecture.md` exists
  - [ ] `docs/architecture/ARCHITECTURE.md` exists
  - [ ] `docs/architecture/adr/ADR-*.md` files exist

### Phase 3: Security & Compliance ✅ / ❌
- [ ] Security posture defined
- [ ] Threat model completed
- [ ] Compliance mapping done
- **Deliverables:**
  - [ ] `.claude/context/security-posture.md` exists
  - [ ] `docs/security/threat-model.md` exists
  - [ ] `docs/security/compliance-mapping.md` exists

### Phase 4: Configure `.claude/` Folder ✅ / ❌
- [ ] Context files completed (glossary, commands, hazards)
- [ ] Rules files completed (conventions, security guardrails)
- [ ] Hooks configured
- [ ] Settings configured
- [ ] CLAUDE.md completed
- **Deliverables:**
  - [ ] `.claude/context/glossary.md` exists
  - [ ] `.claude/context/commands.md` exists
  - [ ] `.claude/context/hazards.md` exists
  - [ ] `.claude/rules/10-app.md` exists
  - [ ] `.claude/rules/security-guardrails.md` exists
  - [ ] `.claude/hooks/session-start.sh` exists
  - [ ] `.claude/settings.json` exists and is valid JSON
  - [ ] `CLAUDE.md` exists

### Phase 5: Source Code & Application ✅ / ❌
- [ ] Source code in `src/` directory
- [ ] Build process works
- [ ] Tests pass
- [ ] Linting passes
- **Deliverables:**
  - [ ] `src/` directory with code
  - [ ] Build command runs successfully
  - [ ] Test command runs successfully
  - [ ] Lint command runs successfully

### Phase 6: Agents & Skills (Optional) ✅ / ❌
- [ ] Custom agents planned (if needed)
- [ ] Custom skills planned (if needed)
- **Deliverables:**
  - [ ] `docs/agents/README.md` (if creating agents)
  - [ ] `evals/*/` folders (if creating skills)

### Phase 7: Agent Workflow (Optional) ✅ / ❌
- [ ] Agent workflow documented (if needed)
- **Deliverables:**
  - [ ] `docs/agent-workflow/workflow.md` (if applicable)

---

## D4 Completion Verification Checklist

Use this comprehensive checklist to verify Phase D4 harness completion:

---

## Section 1: Configuration Files Exist

### `.claude/context/` Files

**Purpose:** Knowledge base for Claude Code about your project

| File | Exists? | Valid? | Notes |
|------|---------|--------|-------|
| `.claude/context/architecture.md` | [ ] | [ ] | System design & components |
| `.claude/context/security-posture.md` | [ ] | [ ] | Compliance & security baseline |
| `.claude/context/commands.md` | [ ] | [ ] | Available commands contract |
| `.claude/context/glossary.md` | [ ] | [ ] | Domain terminology |
| `.claude/context/hazards.md` | [ ] | [ ] | Security risks & incidents |

**Verification:**
```bash
# Check all context files exist
ls -la .claude/context/

# Expected output should show all 5 files
```

### `.claude/rules/` Files

**Purpose:** Code standards Claude enforces

| File | Exists? | Valid? | Notes |
|------|---------|--------|-------|
| `.claude/rules/10-app.md` | [ ] | [ ] | Application conventions |
| `.claude/rules/security-guardrails.md` | [ ] | [ ] | Mandatory security rules |

**Verification:**
```bash
# Check all rules files exist
ls -la .claude/rules/

# Expected output should show both files
```

### `.claude/hooks/` Files

**Purpose:** Automation scripts

| File | Exists? | Executable? | Notes |
|------|---------|-------------|-------|
| `.claude/hooks/session-start.sh` | [ ] | [ ] | Prerequisite checks |

**Verification:**
```bash
# Check hook exists and is executable
ls -la .claude/hooks/session-start.sh

# Should show: -rwxr-xr-x (executable)
# If not executable, run: chmod +x .claude/hooks/session-start.sh
```

### `.claude/settings.json`

**Purpose:** Permissions and environment

| Check | Pass? | Notes |
|-------|-------|-------|
| File exists | [ ] | `.claude/settings.json` |
| Valid JSON syntax | [ ] | `python3 -m json.tool .claude/settings.json` |
| Has `permissions` section | [ ] | With `deny` and `allow` lists |
| Has `hooks` section | [ ] | SessionStart hook configured |
| Has `env` section | [ ] | Environment variables defined |

**Verification:**
```bash
# Validate JSON syntax
python3 -m json.tool .claude/settings.json

# Expected: No errors, shows formatted JSON
```

### Root Level Files

| File | Exists? | Valid? | Notes |
|------|---------|--------|-------|
| `CLAUDE.md` | [ ] | [ ] | Project instructions |
| `docs/PROJECT_INFO.md` | [ ] | [ ] | Project metadata |

---

## Section 2: Configuration Content Validation

### `.claude/context/architecture.md` Content

**Required sections:**
- [ ] "What it is" — System purpose (2-3 sentences)
- [ ] "How it fits" — Upstream/downstream dependencies
- [ ] "Internal structure" — Component table with tech stack
- [ ] "Interfaces" — API/event endpoints with consumers
- [ ] "Key Decisions" — Why major choices were made
- [ ] "Data & State" — What data is stored where

**Validation:**
```bash
# Check file size (should be >50 lines of real content)
wc -l .claude/context/architecture.md

# Check for required sections
grep -E "^## (What it is|How it fits|Internal structure|Interfaces|Key Decisions|Data)" .claude/context/architecture.md
```

### `.claude/context/security-posture.md` Content

**Required sections:**
- [ ] "Compliance Requirements" — Which frameworks apply
- [ ] "Authentication & Authorization" — Auth method, provider, TTL
- [ ] "Data Classification" — What data types, how protected
- [ ] "Secrets Management" — Where secrets stored, rotation

**Validation:**
```bash
# Check for compliance frameworks
grep -E "^##.*Compliance" .claude/context/security-posture.md

# Check for auth configuration
grep -E "provider|authorization|token" .claude/context/security-posture.md
```

### `.claude/context/commands.md` Content

**Required sections:**
- [ ] Command contract table with purpose, command, expected output
- [ ] At least these commands documented:
  - [ ] Build command
  - [ ] Test command
  - [ ] Lint command
  - [ ] (Security scan - recommended)

**Validation:**
```bash
# Check for command table
grep -E "^\|.*command" .claude/context/commands.md

# Count commands (should be ≥3)
grep "^|" .claude/context/commands.md | wc -l
```

### `.claude/rules/10-app.md` Content

**Required sections:**
- [ ] Package/folder structure
- [ ] Naming conventions
- [ ] Key design patterns
- [ ] Code review checklist

**Validation:**
```bash
# Check for code conventions
grep -E "^##.*Convention|Package|Naming" .claude/rules/10-app.md
```

### `.claude/rules/security-guardrails.md` Content

**Required sections:**
- [ ] Secrets management rule
- [ ] Database query rule (parameterized statements)
- [ ] Authentication/authorization rule
- [ ] Encryption rule
- [ ] Code review security checklist

**Validation:**
```bash
# Check for security rules
grep -E "^##.*Secret|Query|Encrypt|Auth" .claude/rules/security-guardrails.md
```

### `CLAUDE.md` Content

**Required sections:**
- [ ] "What this application is" — Business purpose
- [ ] "Repository map" — Entry points and responsibilities
- [ ] "Domain terms" — Reference to glossary.md
- [ ] "Hazards" — Reference to hazards.md
- [ ] "Local conventions" — Departures from enterprise
- [ ] "Narrowed rules" — Stricter requirements
- [ ] "Write boundary" — Who approves writes

**Validation:**
```bash
# Check for required sections
grep -E "^## (What this|Repository|Domain|Hazards|Local|Narrowed|Write)" CLAUDE.md
```

---

## Section 3: Functionality Tests

### Test 1: Session Start Hook

**Purpose:** Verify prerequisites check works

**Steps:**
```bash
# Run the hook
bash .claude/hooks/session-start.sh

# Expected output should show:
# ✓ Checking [Language] version...
# ✓ Checking build tool...
# ✓ Checking Git...
# ✅ Environment ready!
```

**Result:** [ ] Pass [ ] Fail

**If failed:** Debug the hook script and fix any prerequisite issues

---

### Test 2: Claude Code Context Loading

**Purpose:** Verify Claude Code can read configuration

**Steps:**
```bash
# Check what Claude Code sees
claude context

# Or manually verify files are readable
cat .claude/context/architecture.md  # Should output content
cat .claude/settings.json | python3 -m json.tool  # Should be valid JSON
```

**Result:** [ ] Pass [ ] Fail

**If failed:** Check file permissions — all files should be readable by your user

---

### Test 3: Build/Test/Lint Verification

**Purpose:** Verify commands in `.claude/context/commands.md` actually work

**Steps:**

For each command in `.claude/context/commands.md`:

```bash
# From the phase-prompts.md commands section, verify these work:

# Build command
[BUILD_COMMAND]
# Expected: exit 0 or "Build successful"

# Test command
[TEST_COMMAND]
# Expected: All tests pass

# Lint command
[LINT_COMMAND]
# Expected: No errors/warnings or exit 0

# Security scan command (if documented)
[SECURITY_COMMAND]
# Expected: No critical vulnerabilities or exit 0
```

**Results:**
- [ ] Build command passes
- [ ] Test command passes
- [ ] Lint command passes
- [ ] Security scan passes (if documented)

**If any failed:** 
- Fix the code or configuration
- Update `.claude/context/commands.md` to reflect actual status
- Commit changes

---

### Test 4: Git Status Clean

**Purpose:** Verify all configuration is committed

**Steps:**
```bash
# Check git status
git status

# Expected: Should be clean or show only expected changes
# Bad: Uncommitted .claude/ changes
# Good: "nothing to commit, working tree clean"
```

**Result:** [ ] Clean [ ] Dirty

**If dirty:**
```bash
# See what's uncommitted
git status --porcelain

# Stage and commit
git add .
git commit -m "docs: complete D4 harness configuration"
```

---

### Test 5: First Development Task

**Purpose:** Verify Claude Code works effectively with your configuration

**Task:** Have a developer complete a real (simple) development task

**Steps:**
1. Pick a small, real task (e.g., "Add a new API endpoint")
2. Have developer ask Claude: "Help me [TASK]"
3. Verify Claude Code:
   - [ ] Understands project purpose and tech stack
   - [ ] Follows code conventions from `.claude/rules/10-app.md`
   - [ ] Respects security guardrails
   - [ ] Produces correct output

**Result:** [ ] Claude understood project configuration [ ] Claude did not understand

**If failed:** 
- Review Claude's understanding
- Update `.claude/` files if information is unclear
- Try again

---

## Section 4: Team Verification

### Tech Lead Sign-Off

**Responsible:** Tech Lead  
**Review:**
- [ ] Architecture is documented and clear
- [ ] Code conventions are documented
- [ ] All configuration files present and valid
- [ ] Build process works

**Sign-off:** _________________ Date: _________

**Comments:**
```
[Tech Lead notes]
```

---

### Security Lead Sign-Off

**Responsible:** Security Lead  
**Review:**
- [ ] Security baseline documented
- [ ] Compliance requirements identified
- [ ] Security guardrails defined
- [ ] Threat model completed
- [ ] Compliance controls mapped

**Sign-off:** _________________ Date: _________

**Comments:**
```
[Security Lead notes]
```

---

### Dev Lead Sign-Off

**Responsible:** Dev Lead  
**Review:**
- [ ] `.claude/` configuration complete
- [ ] Settings.json permissions correct
- [ ] Hooks working
- [ ] Team understands conventions
- [ ] Build/test commands working

**Sign-off:** _________________ Date: _________

**Comments:**
```
[Dev Lead notes]
```

---

### Team Sign-Off

**Question:** Is the team ready to start development with Claude Code?

- [ ] Yes, all ready
- [ ] No, needs more work

**Comments:**
```
[Team feedback]
```

---

## Section 5: Compliance & Governance Verification

### Security Baseline

- [ ] Authentication method defined
- [ ] Authorization model defined
- [ ] Data classification scheme defined
- [ ] Encryption requirements defined
- [ ] Audit logging requirements defined
- [ ] Secrets management strategy defined

**Status:** ✅ Complete / ❌ Incomplete

---

### Compliance Mapping

For each applicable compliance framework:

**Framework:** ________________

- [ ] Controls identified
- [ ] Implementation evidence linked
- [ ] Verification method defined
- [ ] Owner assigned

**Status:** ✅ Complete / ❌ Incomplete

---

### Documentation Completeness

| Document | Complete? | Current? | Accessible? |
|----------|-----------|----------|-------------|
| CLAUDE.md | [ ] | [ ] | [ ] |
| `.claude/context/*.md` | [ ] | [ ] | [ ] |
| `.claude/rules/*.md` | [ ] | [ ] | [ ] |
| `docs/architecture/` | [ ] | [ ] | [ ] |
| `docs/security/` | [ ] | [ ] | [ ] |
| `PROJECT_INFO.md` | [ ] | [ ] | [ ] |

**Overall:** ✅ Complete / ❌ Incomplete

---

## Section 6: Readiness for Phase D5 (Deploy)

### Pre-Deploy Verification

Before proceeding to Phase D5 (Deploy to Staging), confirm:

- [ ] All D4 checklist items completed
- [ ] All team sign-offs received
- [ ] No critical security issues
- [ ] Build process works consistently
- [ ] Tests passing
- [ ] Code follows conventions
- [ ] Git history clean
- [ ] No uncommitted changes

---

### Blockers to D5 Deployment

If any of these exist, resolve before proceeding to D5:

| Blocker | Resolved? | When? | By Whom? |
|---------|-----------|-------|---------|
| [ ] Security issues found | [ ] | ___ | ___ |
| [ ] Compliance gaps | [ ] | ___ | ___ |
| [ ] Build failures | [ ] | ___ | ___ |
| [ ] Test failures | [ ] | ___ | ___ |
| [ ] Missing documentation | [ ] | ___ | ___ |
| [ ] Team not trained | [ ] | ___ | ___ |
| [ ] Uncommitted changes | [ ] | ___ | ___ |

**No blockers remaining?** ✅ Ready for D5

---

## Final Step: Create Completion Tag

Once all items are checked off, mark D4 completion in git:

```bash
# Create a completion tag
git tag -a d4-harness-complete -m "Phase D4 Harness Configuration Complete

Verified:
- Configuration files complete and validated
- Security baseline established
- Code conventions documented
- Team trained and ready
- All tests passing
- Ready for Phase D5 deployment

Signed off by: [Tech Lead, Security Lead, Dev Lead]"

# Push tag to remote
git push origin d4-harness-complete

# Verify tag exists
git tag -l d4-harness-complete
```

**Tag created?** ✅ Yes / ❌ No

---

## Summary Scorecard

| Category | Score | Status |
|----------|-------|--------|
| Configuration Files | __/5 | [ ] Complete [ ] Incomplete |
| Configuration Content | __/5 | [ ] Complete [ ] Incomplete |
| Functionality Tests | __/5 | [ ] Complete [ ] Incomplete |
| Team Sign-Offs | __/4 | [ ] Complete [ ] Incomplete |
| Compliance Verification | __/3 | [ ] Complete [ ] Incomplete |
| Readiness for D5 | __/7 | [ ] Complete [ ] Incomplete |
| **Overall** | **__/29** | [ ] ✅ READY | [ ] ❌ NOT READY |

**Threshold for D5 readiness:** 27/29 or higher

---

## What's Next After D4 Completion?

### Immediately
✅ Tag completion in git  
✅ Announce to team  
✅ Update project status  

### Next Phase: Phase D5 (Deploy)
See: `docs/guides/d5-deploy-phase.md`

Key activities:
- Build and package application
- Deploy to staging environment
- Run comprehensive tests
- Verify monitoring and alerting
- Final QA sign-off

---

## Troubleshooting

**Problem:** Checklist items failing

**Solution:** See specific section and:
1. Identify root cause
2. Fix the issue
3. Retest
4. Document the fix in git commit

**Problem:** Team not ready

**Solution:**
1. Identify specific concerns
2. Provide training or documentation
3. Address gaps
4. Re-verify understanding

**Problem:** Security issues discovered

**Solution:**
1. Do NOT proceed to D5
2. File security issue
3. Plan remediation
4. Update hazards.md
5. Recommit and re-test

---

**Last Updated:** 2026-10-04  
**Maintained by:** Tech Lead  
**Related:** `developer-setup-guide.md`, `project-info-lifecycle.md`, `d5-deploy-phase.md`
