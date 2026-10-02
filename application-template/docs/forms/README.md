# Deployment Forms

This directory contains **questionnaire forms** that drive harness deployment and generate artefacts.

## Files

### `D4_Application_Harness_Form.md`

**Purpose:** Capture application-specific configuration and context for D4 deployment.

**When to use:** 
- Once per application, when deploying the harness
- Completed by Dev Lead + RRD Application Owner
- Generates `.claude/` artefacts and deployment evidence

**Workflow:**
1. Duplicate this form: `D4_Application_Harness_Form.md` → `<your-app-repo>/D4_Application_Harness_Form.md`
2. Fill sections 0–10 with your application's identity, architecture, and configuration
3. Follow GENERATE and VERIFY steps in each section
4. Save completed form as deployment record

**Prerequisite:** Enterprise harness plugin must be published. Record its version in section 0.

**Output artefacts generated:**
- `.claude/CLAUDE.md` — Application instructions
- `.claude/settings.json` — Narrowed permissions
- `.claude/context/*.md` — Knowledge connection (must be authored with team)
- `.claude/rules/*.md` — Application-specific guardrails

## Related Documentation

- **Parent harness form:** See `../../../D4_Enterprise_Harness_Form.md` for enterprise-level deployment
- **Deployment guide:** See `../../../DEPLOYMENT_GUIDE.md` for step-by-step procedures
- **Architecture:** See `CLAUDE.md` in project root for tier structure
