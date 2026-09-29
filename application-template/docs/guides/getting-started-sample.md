# Getting Started — New Developer Guide

Welcome to the team! This guide will help you get your development environment set up and running your first task using Claude Code.

**Time estimate:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Basic git and terminal experience

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Clone and Setup](#clone-and-setup)
3. [Environment Configuration](#environment-configuration)
4. [Run the Application](#run-the-application)
5. [Verify Your Setup](#verify-your-setup)
6. [Next Steps by Role](#next-steps-by-role)
7. [Troubleshooting](#troubleshooting)
8. [Getting Help](#getting-help)

---

## Prerequisites

Before starting, ensure you have:

### Development Tools
- **Git** (v2.30+) — Source control
- **Java/Node.js** (see tech stack below) — Language runtimes
- **Docker** — Container runtime (optional but recommended)
- **IDE** — IntelliJ IDEA, VS Code, or similar
- **Claude Code** — Claude's command-line interface (CLI)

### Tech Stack

**Replace these with your actual tech stack:**

| Component | Version | Download |
|---|---|---|
| Java | 21 LTS | [java.com](https://java.com) |
| Node.js | 20 LTS | [nodejs.org](https://nodejs.org) |
| Maven | 3.9+ | [maven.apache.org](https://maven.apache.org) |
| Docker | 25.0+ | [docker.com](https://docker.com) |

### Accounts & Access

Verify you have:
- [ ] GitHub/Bitbucket access to the repository
- [ ] Jira account for issue tracking
- [ ] VPN access (if required)
- [ ] Slack invite to team channels
- [ ] Claude Code access (request if needed)

### System Requirements

- **Disk space:** 20 GB free (source code, build artifacts, Docker images)
- **RAM:** 8 GB minimum (16 GB recommended)
- **CPU:** Multi-core processor
- **OS:** macOS, Linux, or Windows (with WSL2)

---

## Clone and Setup

### Step 1: Clone the Repository

```bash
# Clone the repo
git clone <REPOSITORY_URL>
cd <APPLICATION_NAME>

# Verify you're on the main branch
git branch
```

### Step 2: Create a Feature Branch

```bash
# Create your first working branch
git checkout -b feature/initial-setup

# Or if you're fixing a bug:
git checkout -b fix/issue-description
```

### Step 3: Install Dependencies

```bash
# Backend dependencies (Java/Maven)
cd backend
mvn clean install

# Frontend dependencies (Node/npm)
cd ../frontend
npm install

# Return to root
cd ..
```

### Step 4: Verify Installation

```bash
# Check Java
java -version
# Expected output: Java version 21.x

# Check Maven
mvn --version
# Expected output: Maven 3.9.x

# Check Node
node --version
# Expected output: v20.x

# Check npm
npm --version
# Expected output: 10.x
```

---

## Environment Configuration

### Step 1: Create Local Environment Files

```bash
# Copy environment template
cp .env.example .env.local

# Edit with your local values
nano .env.local  # or use your preferred editor
```

### Step 2: Configure Required Variables

Edit `.env.local` with these values (ask your team lead for specifics):

```bash
# Database (LOCAL)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=<application>_dev
DB_USER=postgres
DB_PASSWORD=<ask-team-lead>

# API Keys (local development)
API_KEY_GITHUB=<your-personal-token>  # Optional for local dev
JWT_SECRET=<local-dev-secret>

# Ports
BACKEND_PORT=8080
FRONTEND_PORT=3000

# Environment
NODE_ENV=development
SPRING_PROFILES_ACTIVE=local
```

⚠️ **Never commit `.env.local` to version control.** It's in `.gitignore` for a reason.

### Step 3: Start Supporting Services (Optional)

If your app uses Docker Compose:

```bash
# Start PostgreSQL, Redis, RabbitMQ, etc.
docker-compose -f docker-compose.local.yml up -d

# Verify services are running
docker-compose ps

# View logs
docker-compose logs -f
```

---

## Run the Application

### Backend (Java/Spring Boot)

```bash
cd backend

# Build
mvn clean compile

# Run tests (optional)
mvn test

# Start the server
mvn spring-boot:run

# Expected output:
# Started Application in X seconds
# Server running at http://localhost:8080
```

The API will be available at:
- **Swagger UI:** http://localhost:8080/swagger-ui.html
- **Actuator health:** http://localhost:8080/actuator/health

### Frontend (Node/Angular or React)

In a **new terminal** (keep backend running):

```bash
cd frontend

# Start development server
npm start

# Expected output:
# Application running at http://localhost:3000

# Your app will auto-reload when you save files
```

Open your browser to **http://localhost:3000** — you should see the application.

### Running Both Together

Option 1: Two terminals (shown above)

Option 2: One terminal with concurrency (if configured):

```bash
npm run dev  # Starts both backend and frontend
```

---

## Verify Your Setup

### 1. Health Checks

```bash
# Backend is running
curl http://localhost:8080/actuator/health
# Expected: {"status":"UP"}

# Frontend is accessible
curl http://localhost:3000
# Expected: 200 OK (HTML response)

# Database connection
curl http://localhost:8080/api/health/db
# Expected: {"database":"UP"}
```

### 2. Run Local Tests

```bash
# Backend unit tests
cd backend
mvn test

# Frontend unit tests
cd ../frontend
npm run test

# Both should report coverage and pass/fail count
```

### 3. Lint & Format Check

```bash
# Backend code style
cd backend
mvn checkstyle:check

# Frontend linting
cd ../frontend
npm run lint
```

### 4. Claude Code Verification

```bash
# Check Claude Code is set up
claude /status
# Expected: Enterprise policy active, harness loaded

# Check agents are available
claude /agents
# Expected: List of agent roles

# Check skills are available
claude /skills
# Expected: List of callable skills

# Confirm read-only boundary
claude /verify-boundary
# Expected: Write-attempt test passed, boundary holds
```

---

## Quickstart: Your First Feature

Once your environment is running, create a simple feature to verify the workflow:

### Using Claude Code

```bash
# Navigate to your branch
git checkout -b feature/hello-world

# Start a new feature workflow
claude /new-feature

# When prompted, describe your feature:
# "Add a new API endpoint GET /api/hello that returns {message: 'Hello World'}"

# Follow the workflow:
# 1. Review the execution plan (type: approve)
# 2. Review generated code (type: approve)
# 3. Run tests (should pass automatically)
# 4. Review code changes (inspect files)
# 5. Commit and push (Claude handles this)
```

### Manual Alternative

If you prefer to do it manually:

1. **Backend:** Create `HelloController.java`
   ```java
   @RestController
   @RequestMapping("/api")
   public class HelloController {
       @GetMapping("/hello")
       public Map<String, String> hello() {
           return Collections.singletonMap("message", "Hello World");
       }
   }
   ```

2. **Frontend:** Create a component that calls the endpoint

3. **Test:** Write unit and integration tests

4. **Commit & Push**
   ```bash
   git add .
   git commit -m "Add hello endpoint"
   git push -u origin feature/hello-world
   ```

5. **Create PR:** Open pull request and request review

---

## Next Steps by Role

### Backend Developer

1. ✅ **You are here:** Getting started with local environment
2. **Next:** Read [`docs/guides/project-structure-guide.md`](project-structure-guide.md) — Understand the codebase
3. **Then:** Read [`docs/architecture/ARCHITECTURE.md`](../architecture/ARCHITECTURE.md) — System design
4. **Finally:** Read relevant ADRs for your area (e.g., `ADR-001`, `ADR-007`)

**Your first task:** Create a new API endpoint or fix a bug in your assigned area

### Frontend Developer

1. ✅ **You are here:** Getting started with local environment
2. **Next:** Read [`docs/guides/development-workflow.md`](development-workflow.md) — Component patterns
3. **Then:** Read [`docs/guides/project-structure-guide.md`](project-structure-guide.md) — Folder organization
4. **Finally:** Review relevant ADRs (state management, component patterns)

**Your first task:** Create a new Angular/React component or fix a bug in your assigned area

### QA Engineer

1. ✅ **You are here:** Getting started with local environment
2. **Next:** Read [`docs/testing/test-plan.md`](../testing/test-plan.md) — Test scenarios
3. **Then:** Read [`docs/guides/debugging-guide.md`](debugging-guide.md) — How to debug
4. **Finally:** Set up test running in your IDE

**Your first task:** Review test coverage and identify gaps

### DevOps/Operations

1. ✅ **You are here:** Getting started with local environment
2. **Next:** Read [`docs/guides/deployment-runbook.md`](deployment-runbook.md) — Deployment steps
3. **Then:** Read [`docs/guides/incident-response.md`](incident-response.md) — How to respond to issues
4. **Finally:** Run a practice deployment to staging

**Your first task:** Review deployment pipeline and document any changes needed

---

## Troubleshooting

### Java/Maven Issues

**Problem:** `java: command not found`

**Solution:** Install Java or add to PATH
```bash
# Check if Java is installed
java -version

# If not, install (macOS with Homebrew)
brew install openjdk@21

# Add to PATH (if needed)
export PATH="/usr/local/opt/openjdk@21/bin:$PATH"
```

**Problem:** Maven build fails with "Java version mismatch"

**Solution:** Set JAVA_HOME
```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 21)
mvn clean install
```

### Node/npm Issues

**Problem:** `npm ERR! code ERESOLVE`

**Solution:** Force resolution
```bash
npm install --legacy-peer-deps
```

**Problem:** Port 3000 is already in use

**Solution:** Use a different port
```bash
PORT=3001 npm start
```

### Database Issues

**Problem:** "Connection refused" on database startup

**Solution:** Restart Docker and database
```bash
docker-compose down
docker-compose -f docker-compose.local.yml up -d
```

**Problem:** Database migrations failed

**Solution:** Check migration logs and manually run
```bash
# Reset database (careful! deletes local data)
docker-compose exec postgres dropdb <app>_dev
docker-compose exec postgres createdb <app>_dev

# Re-run migrations
mvn flyway:migrate  # or liquibase:update
```

### Claude Code Issues

**Problem:** `/status` command not found

**Solution:** Install Claude Code
```bash
npm install -g @anthropic-ai/claude-code
```

**Problem:** Permission denied on `/verify-boundary`

**Solution:** Check permission mode
```bash
claude /status
# Should show: Permission mode: read-only
```

---

## Getting Help

### Resources

- **Slack:** #development channel (general help), #deployment channel (ops help)
- **Wiki:** [Confluence/Wiki link] for internal documentation
- **GitHub Issues:** [Project link] for bug reports and feature requests
- **Office hours:** Every Wednesday 2 PM for Q&A

### Ask Your Team Lead

When you're stuck:
1. Check troubleshooting section above
2. Search Slack for similar issues
3. Check the relevant guide or ADR
4. Ask in #development Slack channel
5. Book 1:1 time with your team lead

### Common Questions

**Q: How do I add a new dependency?**  
A: Edit `pom.xml` (backend) or `package.json` (frontend), then run `mvn install` or `npm install`

**Q: How do I run tests for my changes?**  
A: See "Verify Your Setup" → "Run Local Tests" section above

**Q: How do I create a pull request?**  
A: See [`docs/guides/development-workflow.md`](development-workflow.md)

**Q: Where do I find the API documentation?**  
A: OpenAPI/Swagger UI at http://localhost:8080/swagger-ui.html (when backend is running)

**Q: Can I use Claude Code to help me code?**  
A: Yes! See [`docs/guides/agent-guide.md`](agent-guide.md) for how to use slash commands

---

## Success Criteria

You're ready to move forward when:

- [ ] Repository cloned locally
- [ ] Backend builds successfully (`mvn clean install` passes)
- [ ] Frontend builds successfully (`npm install` passes)
- [ ] Backend runs on `http://localhost:8080` (health check responds)
- [ ] Frontend runs on `http://localhost:3000` (app loads in browser)
- [ ] Unit tests pass locally
- [ ] Code lint/format checks pass
- [ ] Claude Code `/status` shows harness is loaded
- [ ] You can see and interact with the application in your browser
- [ ] You understand how to start a Claude Code workflow

---

## Next Steps

1. **Introduce yourself in Slack** — Post in #general
2. **Set up your IDE** — Install extensions for linting, formatting, debugging
3. **Join team standup** — Attend next daily standup meeting
4. **Pick your first ticket** — Work with team lead to select an issue
5. **Review the architecture** — Read `docs/architecture/ARCHITECTURE.md`

**Welcome aboard!** 🎉 Feel free to ask questions in Slack or during office hours.

---

## Related Guides

- [Project Structure Guide](project-structure-guide.md) — Navigate the codebase
- [Development Workflow](development-workflow.md) — Day-to-day development
- [Agent Guide](agent-guide.md) — How to use Claude Code
- [Debugging Guide](debugging-guide.md) — How to troubleshoot
- [Security Best Practices](security-best-practices.md) — Keep code secure

---

## Feedback

Found an issue with this guide? Help us improve!

- **Typo or outdated info?** Edit this file and submit a PR
- **Missing a step?** Comment in Slack #development channel
- **General feedback?** Fill out the [feedback form](example.com/feedback)
