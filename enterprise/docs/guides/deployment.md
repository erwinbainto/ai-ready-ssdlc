# Deployment Procedures

**How to deploy `enterprise/managed/` to machines and verify it's working.**

---

## Prerequisites

✅ Enterprise form completed (sections 0-10)  
✅ Plugin validated: `claude plugin validate enterprise`  
✅ `managed/managed-settings.json` created  
✅ `managed/managed-mcp.json` created  
✅ Access to machines (or admin console)

---

## Choose Your Route

Your choice depends on **section 0.1 and 0.2** of the enterprise form:

### Route A: MDM + System Path (If MDM is reliable)

**When to use:**
- You have MDM (Jamf, Intune, etc.)
- MDM is reliable across your fleet
- You want exclusive control

**How:**
1. Copy files to system path (machine admin does this)
2. Files reach machine via MDM
3. Claude Code loads them automatically

**Complexity:** Low (copy files)

### Route B: Admin Console (If no MDM or unreliable)

**When to use:**
- No MDM, or MDM is unreliable
- You prefer server-managed delivery
- You have Claude admin console access

**How:**
1. Upload files to admin console
2. Admin console manages distribution
3. Claude Code loads them automatically

**Complexity:** Medium (admin console configuration)

---

## Route A: MDM + System Path

### Step 1: Copy Files to System Path

**On macOS:**

```bash
# Create directory if missing
mkdir -p "/Library/Application Support/ClaudeCode/"

# Copy managed settings
cp enterprise/managed/managed-settings.json \
   "/Library/Application Support/ClaudeCode/"

# Copy MCP catalogue
cp enterprise/managed/managed-mcp.json \
   "/Library/Application Support/ClaudeCode/"

# Verify
ls -la "/Library/Application Support/ClaudeCode/"
# Should show:
# -rw-r--r-- managed-settings.json
# -rw-r--r-- managed-mcp.json
```

**On Linux / WSL:**

```bash
# Create directory if missing
sudo mkdir -p /etc/claude-code

# Copy managed settings
sudo cp enterprise/managed/managed-settings.json /etc/claude-code/

# Copy MCP catalogue
sudo cp enterprise/managed/managed-mcp.json /etc/claude-code/

# Set permissions
sudo chmod 644 /etc/claude-code/managed-*.json

# Verify
ls -la /etc/claude-code/
```

**On Windows:**

```powershell
# Create directory if missing
New-Item -ItemType Directory -Path "C:\Program Files\ClaudeCode" -Force

# Copy managed settings
Copy-Item enterprise\managed\managed-settings.json "C:\Program Files\ClaudeCode\"

# Copy MCP catalogue
Copy-Item enterprise\managed\managed-mcp.json "C:\Program Files\ClaudeCode\"

# Verify
Get-ChildItem "C:\Program Files\ClaudeCode\"
# Should show:
# managed-settings.json
# managed-mcp.json
```

### Step 2: Test on One Machine

**Do NOT deploy to fleet yet.** Test on one machine first.

On test machine:

```bash
# Start Claude Code
claude

# Check status
/status

# Expected output (you should see):
# Setting source: enterprise
# Permission mode: read  (or your configured mode)
# Managed settings loaded: true
```

If you don't see "enterprise" in setting sources:

1. **Check file location:**
   - macOS: `/Library/Application Support/ClaudeCode/`
   - Linux: `/etc/claude-code/`
   - Windows: `C:\Program Files\ClaudeCode\`

2. **Check file permissions:**
   - Must be readable by Claude Code process
   - `chmod 644` on Unix, or standard read permissions on Windows

3. **Restart Claude Code:**
   - Close all sessions
   - Start Claude Code again
   - Try `/status` again

### Step 3: Verify All Checks

On test machine, run:

```bash
/status              # Shows enterprise source
/context             # Shows enterprise CLAUDE.md
/mcp                 # Shows admitted MCP servers
/agents              # Shows five roles
/skills              # Shows seed skills
/hooks               # Shows enterprise hooks
/doctor              # Checks for problems
```

All should pass. If any fail, see **Troubleshooting**.

### Step 4: Deploy to Fleet

Once test machine is verified:

**Deploy via MDM:**
- Push `managed-settings.json` to all machines
- Push `managed-mcp.json` to all machines
- Machines update automatically on next sync

**Monitor:**
- Check MDM dashboard for deployment status
- Spot-check a few machines with `/status`
- Monitor support tickets for issues

---

## Route B: Admin Console

### Step 1: Prepare Files

```bash
# Ensure files are ready
ls -la enterprise/managed/
# Should show:
# managed-settings.json
# managed-mcp.json
```

### Step 2: Upload to Admin Console

**In Claude Admin Console:**

1. Navigate to **Settings → Managed Settings**
2. Click **Upload File**
3. Upload `enterprise/managed/managed-settings.json`
4. Set distribution scope: **All users** (or your org)
5. Set deploy date: **Immediate** or **scheduled**
6. Click **Deploy**

Repeat for `managed-mcp.json`:

1. Navigate to **Settings → MCP Servers**
2. Click **Upload Catalogue**
3. Upload `enterprise/managed/managed-mcp.json`
4. Set scope: **All users**
5. Click **Deploy**

### Step 3: Test on One Machine

After ~5 minutes for deployment:

```bash
# On a test machine, start Claude Code
claude

/status
# Should show: "Setting source: enterprise"
```

If not loaded:

1. Wait another 5 minutes (admin console sync delay)
2. Restart Claude Code
3. Try `/status` again

### Step 4: Verify All Checks

```bash
/status /context /mcp /agents /skills /hooks /doctor
```

All should pass.

### Step 5: Monitor Rollout

**In Admin Console:**

1. Navigate to **Deployments**
2. Check status for managed-settings.json and managed-mcp.json
3. Monitor for failed deployments
4. Check support channel for issues

---

## What Gets Deployed

### managed-settings.json

Contains:

```json
{
  "permissionMode": "read",           // Tool access policy
  "toolAllowlist": ["Read", "Edit", "Bash"],  // What Claude can use
  "denialReasons": ["write_denied_by_policy"],
  "hooks": {
    "session-start": "path/to/session-start.sh",
    "pre-tool-use": "path/to/pre-tool-use.sh"
  },
  "env": {
    "OTEL_EXPORTER_OTLP_ENDPOINT": "https://otel.example.com:4317"
  }
}
```

### managed-mcp.json

Contains:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"]
    },
    "jira": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-jira"]
    }
    // ... more servers
  }
}
```

---

## Verification Checklist

After deployment:

- [ ] Files in correct system path
- [ ] File permissions readable
- [ ] Test machine shows `/status` = enterprise
- [ ] `/context` shows enterprise CLAUDE.md
- [ ] `/mcp` shows admitted servers
- [ ] `/agents` shows five roles
- [ ] `/skills` shows seed skills
- [ ] `/hooks` shows registered hooks
- [ ] `/doctor` shows no problems
- [ ] Write boundary test: attempt edit → denied
- [ ] Team receives enterprise policies

---

## Rollback Procedure

If something goes wrong:

**Route A (System Path):**

```bash
# Remove files from system path
# macOS:
rm -f "/Library/Application Support/ClaudeCode/managed-*.json"

# Linux:
sudo rm -f /etc/claude-code/managed-*.json

# Windows:
Remove-Item "C:\Program Files\ClaudeCode\managed-*.json"

# Restart Claude Code
# It will revert to user settings
```

**Route B (Admin Console):**

1. In admin console, click **Undeploy** on the managed settings
2. Choose **Rollback to previous version** (if available)
3. Click **Deploy**

---

## Common Issues

| Issue | Diagnosis | Fix |
|---|---|---|
| `/status` doesn't show enterprise | Files not in system path or wrong permissions | Check file location and `ls -la` permissions |
| MCP servers not loading | managed-mcp.json not deployed | Check Route A/B deployment status |
| Hooks not running | Hook script missing or not executable | Check `chmod +x` on Unix |
| `/doctor` reports problems | Setup incomplete | Run specific command from /doctor output |

---

## Monitoring After Deployment

**Week 1:**
- Daily: Check support channel for issues
- Spot-check 10% of machines with `/status`
- Review `/doctor` output on test machines

**Week 2-4:**
- 3x/week: Spot-check machines
- Monitor compliance (are write attempts being denied?)
- Gather feedback from teams

**Ongoing:**
- Monthly: Random sample verification
- After any Claude Code update: Re-test
- After any policy change: Full fleet re-test

---

## Scaling to Fleet

**Phase 1 (1 machine):** Test machine verify

**Phase 2 (10 machines):** Early adopter team

**Phase 3 (50% of fleet):** Staged rollout

**Phase 4 (100% of fleet):** Full deployment

**Time between phases:** 1 week minimum (monitor for issues)

---

## Next Steps

1. **Choose Route A or B** (based on section 0.1/0.2)
2. **Deploy to test machine**
3. **Run verification checks**
4. **Deploy to fleet**
5. **Monitor for issues**

---

**See also:** `setup.md`, `publishing.md`, `troubleshooting.md`
