# Hooks — Lifecycle Automation Guide

**Full detailed guide for creating and wiring `.claude/hooks/` files.**

For quick reference in `.claude/hooks/`, see hook scripts that are deployed.

---

## Hook Lifecycle

Claude Code invokes hooks at these points:

```
Session Start
  ├─ [session-start.sh] ← Run setup, check prerequisites
  └─ Load .claude/ configuration
     
User Issues Tool Command
  ├─ [pre-tool-use.sh] ← Validate permissions, check security
  └─ Execute tool
  
Tool Execution Completes
  ├─ Tool result returned
  └─ [post-tool-use.sh] ← Optional logging
  
User Approves Action
  ├─ [<action>-approved.sh] ← Optional automation after approval
  └─ Action executed
```

---

## Available Hooks

| Hook | When | Purpose | Example |
|---|---|---|---|
| `session-start.sh` | Session loads | Setup, prerequisites | Check Java version, verify git |
| `pre-tool-use.sh` | Before tool runs | Validate permissions, enforce policy | Block secrets, verify commit |
| `pre-<action>-approved.sh` | After approval | Auto-run follow-up | Auto-format after edit |

---

## Hook Configuration

### 1. Create the Hook File

```bash
# .claude/hooks/session-start.sh
#!/bin/bash
set -euo pipefail

echo "🔧 Verifying prerequisites..."

# Check Java version
java_version=$(java -version 2>&1 | grep "version" | awk '{print $3}' | tr -d '"')
if [[ ! "$java_version" =~ ^21 ]]; then
    echo "❌ Java 21 required; you have $java_version"
    exit 1
fi

echo "✅ Prerequisites verified"
exit 0
```

### 2. Register Hook in settings.json

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
chmod +x .claude/hooks/session-start.sh
bash .claude/hooks/session-start.sh
```

---

## How to Write Hooks

### Basic Hook Template

```bash
#!/bin/bash

# Set strict mode
set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}ℹ️  $1${NC}"; }
log_warn() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

log_info "Checking prerequisites..."

if ! command -v git &> /dev/null; then
    log_error "git not found in PATH"
fi

log_info "All checks passed"
exit 0
```

---

## Common Hook Use Cases

### 1. Prerequisites Check (session-start.sh)

```bash
#!/bin/bash
set -euo pipefail

echo "🔧 Initializing <APPLICATION_NAME>..."

# Check Java
if ! java -version 2>&1 | grep -q "21"; then
    echo "❌ Java 21 required"
    exit 1
fi

# Check Node.js
if ! node -v | grep -q "v20"; then
    echo "❌ Node.js 20+ required"
    exit 1
fi

# Check git config
git config user.email > /dev/null || {
    echo "⚠️  Git not configured. Run:"
    echo "   git config --global user.name 'Your Name'"
    exit 1
}

echo "✅ Setup complete"
exit 0
```

### 2. Security Policy Enforcement (pre-tool-use.sh)

```bash
#!/bin/bash
set -euo pipefail

TOOL=$1
FILE=$2

# Block editing sensitive files
SENSITIVE_FILES=(".env" "secrets.yaml" "*.pem" "*.key")

for pattern in "${SENSITIVE_FILES[@]}"; do
    if [[ "$FILE" == *"$pattern"* ]]; then
        echo "❌ Cannot edit $FILE (sensitive file)"
        exit 1
    fi
done

exit 0
```

### 3. Auto-Format After Approval (pre-write-approved.sh)

```bash
#!/bin/bash
set -euo pipefail

FILE=$1

case "$FILE" in
    *.java)
        if command -v google-java-format &> /dev/null; then
            google-java-format --in-place "$FILE"
        fi
        ;;
    *.json)
        if command -v jq &> /dev/null; then
            jq . "$FILE" > "${FILE}.tmp" && mv "${FILE}.tmp" "$FILE"
        fi
        ;;
esac

exit 0
```

### 4. Enforce Code Review (pre-tool-use.sh)

```bash
#!/bin/bash

TOOL=$1
COMMAND=$2

if [ "$TOOL" = "Bash" ] && echo "$COMMAND" | grep -q "git commit"; then
    if ! echo "$COMMAND" | grep -q "\(#[0-9]\+\|PR-[0-9]\+\)"; then
        echo "❌ Commit message must include PR number (e.g., 'Fix login #123')"
        exit 1
    fi
fi

exit 0
```

### 5. Run Tests Before Commit (pre-tool-use.sh)

```bash
#!/bin/bash
set -euo pipefail

TOOL=$1
COMMAND=$2

if [ "$TOOL" = "Bash" ] && echo "$COMMAND" | grep -q "git commit"; then
    echo "🧪 Running tests..."
    
    if [ -f "pom.xml" ]; then
        mvn test -q || { echo "❌ Tests failed"; exit 1; }
    elif [ -f "package.json" ]; then
        npm test -- --passWithNoTests || { echo "❌ Tests failed"; exit 1; }
    fi
    
    echo "✅ Tests passed"
fi

exit 0
```

---

## Testing Hooks

### Manual Testing

```bash
# Test directly
bash .claude/hooks/session-start.sh

# Check exit code
echo $?  # 0 = success, non-zero = failure
```

### Verify Registration

```bash
# Check settings.json
grep -A 5 '"hooks"' .claude/settings.json

# Verify executable
ls -la .claude/hooks/session-start.sh
# Should show: -rwxr-xr-x
```

### Debug

If hook isn't running:
1. Check permissions: `chmod +x .claude/hooks/*.sh`
2. Check registration: Verify in `settings.json`
3. Check syntax: `bash -n .claude/hooks/hook-name.sh`

---

## Hook Best Practices

### ✅ DO

- Keep hooks fast (< 1 second)
- Provide clear feedback
- Exit cleanly (0 on success, 1 on failure)
- Log important info
- Reference docs/policies in output
- Make idempotent (safe to run multiple times)

### ❌ DON'T

- Modify files without permission
- Run expensive operations (DB, API, long compiles)
- Have unintended side effects
- Make hooks mandatory for basic work
- Hardcode paths or credentials

---

## Hook Examples by Stack

### Java/Spring Boot

```bash
#!/bin/bash
echo "🔧 Java Setup"

! command -v mvn &> /dev/null && { echo "❌ Maven not found"; exit 1; }

java_version=$(java -version 2>&1 | grep "version" | sed 's/.*"\(.*\)".*/\1/' | cut -d'.' -f1)
[ "$java_version" -ge 21 ] || { echo "❌ Java 21+ required"; exit 1; }

echo "✅ Environment OK"
```

### Node.js/React

```bash
#!/bin/bash
echo "🔧 Node.js Setup"

node_version=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
[ "$node_version" -ge 20 ] || { echo "❌ Node 20+ required"; exit 1; }

npm -v > /dev/null || { echo "❌ npm not found"; exit 1; }

echo "✅ Environment OK"
```

### Python

```bash
#!/bin/bash
echo "🔧 Python Setup"

python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
[[ "$python_version" > "3.10" ]] || { echo "❌ Python 3.11+ required"; exit 1; }

[ -d "venv" ] || { echo "⚠️  Creating virtualenv"; python3 -m venv venv; }

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
