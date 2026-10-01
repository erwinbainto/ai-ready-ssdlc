# Hooks — Lifecycle Automation

**Purpose:** Hooks are shell scripts that run at specific lifecycle points, automating setup, validation, and policy enforcement without requiring human intervention each time.

**Key Point:** Hooks are optional but powerful. Only configure hooks you actually need; don't create hooks just to create them.

---

## Hook Lifecycle

Claude Code invokes hooks at these points:

```
Session Start
  ├─ [session-start.sh] ← Run setup, check prerequisites
  └─ Load .claude/ configuration
     
User Issues Tool Command
  ├─ [pre-tool-use.sh] ← Validate permissions, check security policy
  └─ Execute tool
     
Tool Execution Completes
  ├─ Tool result returned
  └─ [post-tool-use.sh] ← Optional logging, audit trail (rarely used)
  
User Approves Action
  ├─ [<action>-approved.sh] ← Optional automation after approval
  └─ Action executed
```

---

## Available Hooks

| Hook | When | Purpose | Example |
|---|---|---|---|
| `session-start.sh` | Session loads | Setup, prerequisites, welcome message | Check Java version, verify git config |
| `pre-tool-use.sh` | Before tool runs | Validate permissions, enforce policy | Block secrets exposure, verify commit message |
| `pre-<action>-approved.sh` | After user approval | Auto-run follow-up steps | Auto-commit after edit approval |

---

## Hook Configuration

### 1. Create the Hook File

Create a shell script in `.claude/hooks/`:

```bash
# .claude/hooks/session-start.sh
#!/bin/bash

set -e  # Exit on error

echo "🔧 Verifying prerequisites for <APPLICATION_NAME>..."

# Check Java version
java_version=$(java -version 2>&1 | grep "version" | awk '{print $3}' | tr -d '"')
if [[ ! "$java_version" =~ ^21 ]]; then
    echo "❌ Java 21 required; you have $java_version"
    exit 1
fi

echo "✅ Prerequisites verified"
```

### 2. Register Hook in settings.json

Edit `.claude/settings.json`:

```json
{
  "hooks": {
    "session-start": ".claude/hooks/session-start.sh",
    "pre-tool-use": ".claude/hooks/pre-tool-use.sh"
  }
}
```

### 3. Test the Hook

```bash
# Make executable
chmod +x .claude/hooks/session-start.sh

# Test manually
bash .claude/hooks/session-start.sh
```

---

## How to Write Hooks

### Basic Hook Template

```bash
#!/bin/bash

# Set strict mode: exit on error, undefined vars
set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'  # No color

# Logging functions
log_info() { echo -e "${GREEN}ℹ️  $1${NC}"; }
log_warn() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# Main logic
log_info "Checking prerequisites..."

# Check command exists
if ! command -v git &> /dev/null; then
    log_error "git not found in PATH"
fi

log_info "All checks passed"
exit 0
```

### Example 1: session-start.sh — Prerequisites Check

```bash
#!/bin/bash
set -euo pipefail

echo "🔧 Initializing <APPLICATION_NAME>..."

# Check Java version (required for backend)
if command -v java &> /dev/null; then
    java_version=$(java -version 2>&1 | grep "version" | awk '{print $3}' | tr -d '"')
    if [[ ! "$java_version" =~ ^21 ]]; then
        echo "❌ Java 21 required; you have $java_version"
        exit 1
    fi
    echo "✅ Java 21 found"
else
    echo "⚠️  Java not found (needed for backend development)"
fi

# Check Node.js version (required for frontend)
if command -v node &> /dev/null; then
    node_version=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
    if [ "$node_version" -lt 20 ]; then
        echo "❌ Node.js 20+ required; you have $node_version"
        exit 1
    fi
    echo "✅ Node.js 20+ found"
else
    echo "⚠️  Node.js not found (needed for frontend development)"
fi

# Check git config
if ! git config user.email &> /dev/null; then
    echo "⚠️  Git not configured. Set it up:"
    echo "   git config --global user.name 'Your Name'"
    echo "   git config --global user.email 'you@example.com'"
fi

# Check for required environment files
if [ ! -f ".env.local" ]; then
    echo "⚠️  .env.local not found. Create it from .env.example:"
    echo "   cp .env.example .env.local"
    echo "   Edit .env.local with your configuration"
fi

echo ""
echo "✅ Setup complete. Ready to develop!"
exit 0
```

### Example 2: pre-tool-use.sh — Security Policy Enforcement

```bash
#!/bin/bash
set -euo pipefail

# This hook runs BEFORE Claude Code executes any tool
# Use it to enforce security policies

RED='\033[0;31m'
NC='\033[0m'

# Prevent secrets exposure via Edit tool
# (This is an example; real secret scanning should use git-secrets)

TOOL=$1  # Tool being called (e.g., "Edit", "Write", "Bash")
FILE=$2  # File being edited (if applicable)

# Block editing of sensitive files
SENSITIVE_FILES=(".env" "secrets.yaml" "*.pem" "*.key")

for pattern in "${SENSITIVE_FILES[@]}"; do
    if [[ "$FILE" == *"$pattern"* ]]; then
        echo -e "${RED}❌ Cannot edit $FILE (sensitive file)${NC}"
        echo "   Use environment variables or secrets manager instead"
        exit 1
    fi
done

# Block Bash commands that might leak secrets
if [ "$TOOL" = "Bash" ]; then
    # Check if command contains password or secret keywords
    COMMAND=$3
    if [[ "$COMMAND" =~ (password|secret|api_key|token) ]]; then
        echo -e "${RED}⚠️  Warning: Command contains secret-like keywords${NC}"
        echo "   Do not paste credentials in commands"
        # Note: In real deployment, you might exit 1 here
    fi
fi

exit 0
```

### Example 3: pre-write-approved.sh — Auto-format After Approval

```bash
#!/bin/bash
set -euo pipefail

# Run after user approves a Write/Edit action
# Used for auto-formatting, linting, or cleanup

FILE=$1  # File that was edited

echo "🎯 Post-approval actions for $FILE..."

# Auto-format based on file type
case "$FILE" in
    *.java)
        if command -v google-java-format &> /dev/null; then
            echo "  Formatting Java..."
            google-java-format --in-place "$FILE"
        fi
        ;;
    *.json)
        if command -v jq &> /dev/null; then
            echo "  Formatting JSON..."
            jq . "$FILE" > "${FILE}.tmp" && mv "${FILE}.tmp" "$FILE"
        fi
        ;;
    *.md)
        echo "  Markdown written; remember to verify links"
        ;;
esac

echo "✅ Done"
exit 0
```

---

## Common Hook Use Cases

### 1. Enforce Security Policy

```bash
# .claude/hooks/pre-tool-use.sh
# Prevent committing code with TODO/FIXME comments in security-critical paths

if [ "$TOOL" = "Bash" ]; then
    if echo "$COMMAND" | grep -q "git commit"; then
        if grep -r "TODO.*SECRET\|FIXME.*PASSWORD" --include="*.java" --include="*.js"; then
            echo "❌ Cannot commit: Found TODO/FIXME in security-sensitive code"
            exit 1
        fi
    fi
fi
```

### 2. Auto-Generate Documentation

```bash
# .claude/hooks/pre-write-approved.sh
# Auto-generate API docs after code changes

if [[ "$FILE" == "src/api/"* && "$FILE" == "*.java" ]]; then
    echo "📚 Regenerating API docs..."
    cd backend
    mvn clean javadoc:javadoc -q
    echo "✅ API docs updated in target/site/apidocs/"
fi
```

### 3. Enforce Code Review

```bash
# .claude/hooks/pre-tool-use.sh
# Require PR link in commit message

if [ "$TOOL" = "Bash" ] && echo "$COMMAND" | grep -q "git commit"; then
    if ! echo "$COMMAND" | grep -q "\(#[0-9]\+\|PR-[0-9]\+\)"; then
        echo "❌ Commit message must include PR number (e.g., 'Fix login #123')"
        exit 1
    fi
fi
```

### 4. Run Tests Before Commit

```bash
# .claude/hooks/pre-tool-use.sh
# Run tests before allowing git commit

if [ "$TOOL" = "Bash" ] && echo "$COMMAND" | grep -q "git commit"; then
    echo "🧪 Running tests before commit..."
    
    if [ -f "pom.xml" ]; then
        mvn test -q || { echo "❌ Tests failed; fix before committing"; exit 1; }
    elif [ -f "package.json" ]; then
        npm test -- --passWithNoTests || { echo "❌ Tests failed"; exit 1; }
    fi
    
    echo "✅ Tests passed"
fi
```

---

## Testing Hooks

### Manual Testing

```bash
# Test hook directly
bash .claude/hooks/session-start.sh

# Check exit code
echo $?  # 0 = success, non-zero = failure
```

### Verify Hook Registration

```bash
# Check settings.json has hook registered
grep -A 5 '"hooks"' .claude/settings.json

# Verify hook file is executable
ls -la .claude/hooks/session-start.sh
# Should show: -rwxr-xr-x
```

### Debug Hook Execution

If hook isn't running:

1. **Check file permissions:** `chmod +x .claude/hooks/*.sh`
2. **Check registration:** Verify in `settings.json`
3. **Check syntax:** Run `bash -n .claude/hooks/hook-name.sh` (no-execute check)
4. **Check logs:** Claude Code logs hook execution (if verbose mode enabled)

---

## Hook Best Practices

### ✅ Do

- **Keep hooks fast** (< 1 second) so they don't slow down workflow
- **Provide clear feedback** (echo what you're checking/doing)
- **Exit cleanly** (exit 0 on success, exit 1 on failure)
- **Log important info** (user should understand what happened)
- **Reference docs** (link to policy or requirement in hook output)
- **Make hooks idempotent** (safe to run multiple times)

### ❌ Don't

- **Modify files without permission** (ask user first)
- **Run expensive operations** (DB queries, API calls, lengthy compiles)
- **Have hooks with side effects** (don't auto-commit without asking)
- **Make hooks mandatory for basic work** (optional, convenience features)
- **Hardcode paths or credentials** (use env vars, config files)

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| Hook not running | Not registered in settings.json | Add `"hooks": { "session-start": ".claude/hooks/session-start.sh" }` |
| "Permission denied" | File not executable | `chmod +x .claude/hooks/*.sh` |
| "Command not found" | Shebang line missing | Add `#!/bin/bash` at top of file |
| Hook fails silently | Exit code not checked | Add `set -e` at top; test with `bash -x` for debug |
| Slows down every session | Hook too expensive | Optimize or run only on specific triggers |

---

## Hook Examples by Stack

### Java/Spring Boot

```bash
#!/bin/bash
# .claude/hooks/session-start.sh

echo "🔧 Java Backend Setup"

# Check Maven
if ! command -v mvn &> /dev/null; then
    echo "❌ Maven not found. Install with: brew install maven"
    exit 1
fi

# Check Java 21
java_version=$(java -version 2>&1 | grep "version" | sed 's/.*"\(.*\)".*/\1/' | cut -d'.' -f1)
[ "$java_version" -ge 21 ] || { echo "❌ Java 21+ required"; exit 1; }

echo "✅ Environment OK"
```

### Node.js/React

```bash
#!/bin/bash
# .claude/hooks/session-start.sh

echo "🔧 Node.js Frontend Setup"

# Check Node 20+
node_version=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
[ "$node_version" -ge 20 ] || { echo "❌ Node 20+ required"; exit 1; }

# Check npm
npm -v > /dev/null || { echo "❌ npm not found"; exit 1; }

echo "✅ Environment OK"
```

### Python

```bash
#!/bin/bash
# .claude/hooks/session-start.sh

echo "🔧 Python Setup"

# Check Python 3.11+
python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
[[ "$python_version" > "3.10" ]] || { echo "❌ Python 3.11+ required"; exit 1; }

# Check virtualenv
[ -d "venv" ] || { echo "⚠️  Creating virtualenv..."; python3 -m venv venv; }

echo "✅ Environment OK"
```

---

## Related Documentation

- **Settings.json:** `.claude/settings.json` — where hooks are registered
- **Rules:** `.claude/rules/` — policy that hooks enforce
- **Context:** `.claude/context/` — hazards that might warrant hooks

---

**Maintained by:** <Platform Team / DevOps Lead>  
**Last updated:** <YYYY-MM-DD>  
**Examples tested:** <YYYY-MM-DD>
