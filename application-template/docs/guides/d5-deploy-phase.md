# Phase D5: Deploy

**Deploying your harness-configured application to staging environment**

---

## Understanding the D5 Acronym

**D = Development Phase** (in the AI-Ready Secure Software Development Lifecycle framework)

| Phase | Full Name | Focus | Duration | Owner | Status |
|-------|-----------|-------|----------|-------|--------|
| **D1** | Development Phase 1: Intake | Gather requirements | 1-2 weeks | Product Lead | Earlier phase |
| **D2** | Development Phase 2: Shape | Design solution | 1-2 weeks | Tech Lead | Earlier phase |
| **D3** | Development Phase 3: Capability Candidates | AI assistant specs | 1-2 weeks | Dev Lead | Earlier phase |
| **D4** | Development Phase 4: Harness | Setup Claude Code governance | 1-2 weeks | Dev + Tech Lead | Previous phase |
| **D5** | Development Phase 5: **Deploy** | Release to staging environment | 2-4 weeks | DevOps + QA | **← YOU ARE HERE** |
| **D6** | Development Phase 6: Gate | Compliance audit & sign-off | 1-2 weeks | Security Lead | Next phase |
| **D7** | Development Phase 7: Operate | Production monitoring & support | Ongoing | DevOps + SRE | Later phase |

---

## What is Phase D5?

**D5 = Development Phase 5: Deploy**

Phase D5 is where you take the working code (from Phase D4: Harness) and deploy it to a **staging environment** for comprehensive testing.

### Prerequisites for D5

Before starting D5, you must have completed:
- ✅ **Phase D4 (Harness)** — Configuration complete and verified (see `d4-completion-checklist.md`)
- ✅ **All D4 sign-offs** — Tech Lead, Security Lead, Dev Lead approved
- ✅ **No blockers** — No critical security issues or build failures

**If not complete:** Stop and finish D4 first

---

## D5 Overview

### Goal
Move from development environment to **staging environment** with full verification

### Outcomes
- ✅ Application deployed to staging
- ✅ Verified build artifacts
- ✅ Tests passing in staging
- ✅ Security scanning completed
- ✅ Deployment automated (or documented)
- ✅ Monitoring and alerting active
- ✅ Ready for compliance audit (Phase D6)

### Timeline
**Typical duration:** 2-4 weeks (depending on DevOps readiness)

### Responsible Parties
- **DevOps/Infrastructure Lead** — Deployment infrastructure
- **QA Lead** — Test verification in staging
- **Security Lead** — Security scanning and validation
- **Tech Lead** — Oversees deployment process
- **Dev Team** — Fix any issues discovered

---

## D5 Phases Breakdown

### Phase D5.1: Build Artifact Creation

**Goal:** Create a production-ready build artifact

**Time:** 1 day  
**Owner:** Dev Team + DevOps

#### Steps

**Step 1: Verify Build in Development**

```bash
# From your project root
cd /Users/erwin.t.bainto/ai_projects/rrd-ir

# Run build command (from .claude/context/commands.md)
[YOUR_BUILD_COMMAND]
# Example: mvn clean package

# Expected: Build succeeds with exit code 0
```

**Validation:** [ ] Build passes locally

---

**Step 2: Run All Tests**

```bash
# Run tests (from .claude/context/commands.md)
[YOUR_TEST_COMMAND]
# Example: mvn test

# Expected: All tests pass, >80% coverage
```

**Validation:** [ ] Tests pass [ ] Coverage >80%

---

**Step 3: Run Lint/Code Quality**

```bash
# Run linting (from .claude/context/commands.md)
[YOUR_LINT_COMMAND]
# Example: mvn checkstyle:check

# Expected: No errors or warnings
```

**Validation:** [ ] Linting passes

---

**Step 4: Run Security Scan**

```bash
# Run security scan (from .claude/context/commands.md or docs/security/)
[YOUR_SECURITY_COMMAND]
# Example: mvn dependency-check:check

# Expected: No critical vulnerabilities
```

**Validation:** [ ] Security scan passes

---

**Step 5: Create Build Artifact**

```bash
# For Java: Create JAR/WAR
mvn clean package
# Output: target/app.jar

# For Node.js: Build distribution
npm run build
# Output: dist/

# For Python: Create wheel/docker
python -m build
# Output: dist/*.whl

# For Go: Compile binary
go build -o app
# Output: ./app
```

**Validation:** [ ] Artifact created

---

**Step 6: Document Build Information**

Create a `BUILD_INFO.md` file:

```markdown
# Build Information

**Date:** [Date of build]
**Commit:** [git hash]
**Branch:** [branch name]
**Built by:** [Developer name]
**Build tool:** [Maven/npm/cargo/etc]
**Build command:** [exact command run]
**Output artifact:** [JAR/wheel/binary location]
**Artifact size:** [size]
**Java version:** [if applicable]
**Node version:** [if applicable]
**Security scan:** PASS / FAIL
**Test coverage:** X%
**Lint status:** PASS / FAIL

## Artifact Details

**Filename:** app.jar  
**Checksum:** [SHA256]  
**Location:** [s3://bucket/app.jar or /releases/app-v1.0.0.jar]

## Notes
[Any special build instructions]
```

**Validation:** [ ] BUILD_INFO.md created

---

**Step 7: Commit Build Metadata (Optional)**

```bash
# If desired, commit build info (don't commit binary artifact)
git add BUILD_INFO.md
git commit -m "docs: record build information for D5 deployment"
```

**Validation:** [ ] Build metadata committed

---

### Phase D5.2: Staging Infrastructure Setup

**Goal:** Prepare staging environment to receive deployment

**Time:** 1-2 days  
**Owner:** DevOps/Infrastructure Lead

#### Staging Environment Requirements

**Checklist:**

- [ ] **Staging server(s) provisioned**
  - VM/container with adequate resources
  - Same OS/environment as production
  - Network connectivity verified

- [ ] **Database setup**
  - Staging database instance
  - Same schema as production
  - Test data loaded (if needed)
  - Backups configured

- [ ] **Configuration management**
  - Staging configuration separate from production
  - Environment variables set up
  - Secrets management in place (Vault/Secrets Manager)
  - No hardcoded credentials

- [ ] **Logging & Monitoring**
  - Log aggregation configured (ELK, DataDog, etc.)
  - Metrics collection enabled (Prometheus, CloudWatch, etc.)
  - Alerts configured (for critical errors)
  - Dashboard created

- [ ] **Security**
  - Firewalls configured
  - HTTPS/TLS certificates in place
  - API rate limiting configured
  - DDoS protection enabled (if applicable)

- [ ] **Backups & Recovery**
  - Backup strategy defined
  - Restore tested
  - DR procedure documented

- [ ] **Documentation**
  - Staging environment documented
  - Access procedures documented
  - Runbook for common issues
  - Rollback procedure documented

#### Infrastructure as Code (Recommended)

Store infrastructure configuration in git:

```
infrastructure/
├── terraform/
│   ├── staging.tf
│   ├── variables.tf
│   └── outputs.tf
├── kubernetes/
│   └── staging/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── configmap.yaml
└── docker/
    └── Dockerfile
```

**Validation:** [ ] Staging environment ready

---

### Phase D5.3: Deployment Process

**Goal:** Deploy built artifact to staging

**Time:** 1 day  
**Owner:** DevOps Lead

#### Deployment Methods

**Option A: Manual Deployment (for small teams)**

```bash
# 1. SSH into staging server
ssh staging-server

# 2. Stop running application
systemctl stop app
# or
docker stop app-container

# 3. Backup current version
cp /opt/app/app.jar /opt/app/app.jar.bak

# 4. Deploy new version
cp app.jar /opt/app/app.jar

# 5. Start application
systemctl start app
# or
docker start app-container

# 6. Verify startup
sleep 5
curl http://staging-server:8080/health
# Expected: 200 OK

# 7. Check logs
tail -f /var/log/app/application.log
```

---

**Option B: Automated Deployment (recommended)**

```bash
# Using deployment automation (GitLab CI, GitHub Actions, Jenkins)

# 1. Create deployment pipeline:
.gitlab-ci.yml
# or
.github/workflows/deploy.yml
# or
Jenkinsfile

# 2. Pipeline stages:
  - Build
  - Test
  - Security Scan
  - Deploy to Staging
  - Verify Deployment
  - Run E2E Tests

# 3. Example GitHub Actions workflow:
name: Deploy to Staging

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build
        run: mvn clean package
      - name: Deploy to Staging
        run: ./scripts/deploy-staging.sh
      - name: Verify
        run: ./scripts/verify-staging.sh
```

---

**Option C: Container-Based Deployment (Docker/Kubernetes)**

```bash
# 1. Build Docker image
docker build -t myapp:latest .

# 2. Tag for staging
docker tag myapp:latest myregistry.azurecr.io/myapp:staging

# 3. Push to registry
docker push myregistry.azurecr.io/myapp:staging

# 4. Deploy to Kubernetes
kubectl apply -f k8s/staging/deployment.yaml

# 5. Verify rollout
kubectl rollout status deployment/myapp-staging

# 6. Check logs
kubectl logs -f deployment/myapp-staging
```

---

#### Deployment Verification Checklist

After deployment, verify:

- [ ] **Application started**
  ```bash
  curl -i http://staging-server:port/health
  # Expected: 200 OK
  ```

- [ ] **Logs show no errors**
  ```bash
  tail -50 /var/log/app/application.log | grep -i error
  # Expected: No errors
  ```

- [ ] **Database connectivity**
  ```bash
  # Application should connect to database without errors
  # Check logs or metrics
  ```

- [ ] **Configuration loaded correctly**
  ```bash
  # Check that environment-specific config applied
  # Example: staging database endpoint, not production
  ```

- [ ] **Monitoring data flowing**
  ```bash
  # Metrics should appear in monitoring system
  # Check Prometheus/CloudWatch/DataDog
  ```

**Validation:** [ ] Deployment successful

---

### Phase D5.4: Comprehensive Testing

**Goal:** Verify application works correctly in staging

**Time:** 3-5 days  
**Owner:** QA Lead + Dev Team

#### Test Categories

**Test 1: Smoke Tests (Quick sanity check)**

```bash
# Basic functionality tests
# Does the app start? Can we reach it? Can we log in?

# Example:
pytest tests/smoke/
# or
npm run test:smoke
# or
./scripts/smoke-tests.sh
```

**Expected:** All tests pass

**Validation:** [ ] Smoke tests pass

---

**Test 2: Unit & Integration Tests**

```bash
# Run full test suite in staging environment
[YOUR_TEST_COMMAND]
# Example: mvn test

# Should test:
# - All API endpoints
# - Database operations
# - Authentication/authorization
# - Error handling
```

**Expected:** All tests pass

**Validation:** [ ] Integration tests pass

---

**Test 3: End-to-End (E2E) Tests**

```bash
# Test complete user workflows
# Example: "User logs in → Creates resource → Views it → Deletes it"

npm run test:e2e
# or
pytest tests/e2e/
# or
./scripts/e2e-tests.sh
```

**Expected:** All workflows work

**Validation:** [ ] E2E tests pass

---

**Test 4: Performance Testing**

```bash
# Load test the application
# Example: Can it handle 100 concurrent users?

# Using Apache JMeter:
jmeter -n -t load-test.jmx -l results.jtl -j log.txt

# Or using k6:
k6 run load-test.js
```

**Expected:** 
- Response time <500ms for most endpoints
- No errors under load
- Database handles concurrent connections

**Validation:** [ ] Performance acceptable

---

**Test 5: Security Testing**

```bash
# Run security-specific tests
# Example: OWASP Top 10 vulnerability scans

# SAST (Static Analysis):
sonar-scanner
# or
bandit -r src/

# DAST (Dynamic Analysis):
owasp-zap -t staging-server:8080
# or
burp-scan staging-server:8080
```

**Expected:** 
- No critical vulnerabilities
- All OWASP top 10 addressed
- Security headers present

**Validation:** [ ] Security testing passes

---

**Test 6: Compliance Testing**

```bash
# Verify compliance controls work in staging
# Example: Data encryption, audit logging, access control

# Checklist:
[ ] Data encrypted at rest
[ ] Data encrypted in transit (TLS)
[ ] Audit logs recording access
[ ] Role-based access control working
[ ] Sensitive data not in logs
[ ] Rate limiting working
```

**Validation:** [ ] Compliance controls verified

---

**Test 7: Backup & Recovery Testing**

```bash
# Test that backups work and can be restored
# Example: Backup database, delete it, restore it

# 1. Create backup
./scripts/backup.sh

# 2. Verify backup exists
ls -lh /backups/

# 3. Delete database (in test environment)
# ⚠️ DO NOT do this in production!

# 4. Restore backup
./scripts/restore.sh /backups/app-latest.backup

# 5. Verify restored data
SELECT COUNT(*) FROM users;  # Should match original count
```

**Validation:** [ ] Backup/restore works

---

### Phase D5.5: Documentation & Runbooks

**Goal:** Document deployment and operational procedures

**Time:** 1 day  
**Owner:** DevOps + Tech Lead

#### Required Documentation

**Create these files:**

```
docs/operations/
├── deployment-runbook.md      ← Step-by-step deployment
├── monitoring-runbook.md      ← How to monitor
├── troubleshooting.md         ← Common issues & fixes
├── incident-response.md       ← What to do when things break
├── rollback-procedure.md      ← How to roll back
├── scaling-guide.md           ← How to scale the system
└── disaster-recovery.md       ← Full recovery procedure
```

---

**1. Deployment Runbook (`deployment-runbook.md`)**

```markdown
# Deployment Runbook

## Pre-Deployment Checklist
- [ ] All tests passing
- [ ] Security scan passed
- [ ] Staging environment healthy
- [ ] Backups recent and tested
- [ ] On-call person notified

## Deployment Steps

### Step 1: Build Artifact
```bash
mvn clean package
```

### Step 2: Deploy to Staging
```bash
./scripts/deploy-staging.sh
```

### Step 3: Verify Deployment
```bash
curl http://staging/health
```

### Step 4: Run Smoke Tests
```bash
npm run test:smoke
```

## Post-Deployment Verification
- [ ] Application running
- [ ] Logs show no errors
- [ ] Monitoring dashboard healthy
- [ ] Database connected
- [ ] All endpoints responding

## Rollback (if needed)
See rollback-procedure.md

## Escalation
If issues occur, escalate to: [On-call contact]
```

---

**2. Monitoring Runbook (`monitoring-runbook.md`)**

```markdown
# Monitoring Runbook

## Access Dashboards
- Production Dashboard: [URL]
- Staging Dashboard: [URL]
- Logs: [CloudWatch/ELK URL]
- Metrics: [Prometheus/DataDog URL]

## Key Metrics to Watch
- **Response Time:** Should be <500ms
- **Error Rate:** Should be <0.1%
- **CPU Usage:** Should be <80%
- **Memory Usage:** Should be <85%
- **Database Connections:** Should be <80% of limit

## Alerts Configured
- [ ] High error rate (>1%)
- [ ] High latency (>1000ms)
- [ ] High CPU (>90%)
- [ ] Database connection pool exhausted
- [ ] Disk space critically low

## Common Alert Responses
**Alert: High Error Rate**
1. Check recent deployments
2. Review error logs
3. Check database connectivity
4. Restart service if needed
5. Escalate if not resolved in 15 minutes

[Continue for each alert type]
```

---

**3. Troubleshooting Guide (`troubleshooting.md`)**

```markdown
# Troubleshooting Guide

## "Application won't start"
1. Check logs: `tail -100 /var/log/app/app.log`
2. Verify configuration: `echo $DATABASE_URL`
3. Check database connectivity: `psql $DATABASE_URL`
4. Restart service: `systemctl restart app`
5. If still failing, escalate

## "Database connection timeout"
1. Check database is running
2. Verify firewall rules allow connection
3. Check connection pool settings
4. Restart connection pool
5. Scale database if needed

[Continue for common issues]
```

---

**4. Incident Response (`incident-response.md`)**

```markdown
# Incident Response Procedure

## Classification
- **Severity 1 (Critical):** System down, data loss
- **Severity 2 (Major):** Significant functionality broken
- **Severity 3 (Minor):** Degraded performance, non-critical features

## Response Steps
1. **Assess:** What is broken? Severity level?
2. **Alert:** Notify stakeholders
3. **Investigate:** Root cause analysis
4. **Mitigate:** Temporary fix if possible
5. **Resolve:** Permanent fix
6. **Communicate:** Update status
7. **Post-mortem:** Document and learn

## Escalation Matrix
[Contact info for on-call, team lead, manager]

## Communication
- Public status page updates every 30 minutes
- Internal Slack channel #incidents
- All hands meeting if Severity 1
```

---

**5. Rollback Procedure (`rollback-procedure.md`)**

```markdown
# Rollback Procedure

## When to Rollback
- Critical bugs introduced in deployment
- Severe performance degradation
- Data corruption
- Security vulnerability
- Any Severity 1 incident

## Quick Rollback (within minutes)

### For container-based deployments:
```bash
# Rollback to previous image
kubectl rollout undo deployment/myapp-staging
```

### For traditional deployments:
```bash
# Restore backup
cp /opt/app/app.jar.bak /opt/app/app.jar
systemctl restart app
```

## Full Rollback (if data changes)

1. Restore database from backup
2. Verify backup integrity
3. Restore application code
4. Run smoke tests
5. Verify all systems operational

## Post-Rollback
- Investigate root cause
- Fix the issue
- Test thoroughly
- Re-deploy when ready
- Post-mortem meeting
```

---

**Validation:** [ ] All operational documentation created

---

### Phase D5.6: Monitoring & Alerting Setup

**Goal:** Set up continuous monitoring for staging

**Time:** 1 day  
**Owner:** DevOps Lead

#### Monitoring Stack Options

**Option 1: Cloud-Native**
- **Compute Metrics:** CloudWatch / Azure Monitor
- **Logs:** CloudWatch Logs / Application Insights
- **Traces:** X-Ray / Application Insights
- **Dashboards:** CloudWatch Dashboards

**Option 2: Open Source**
- **Metrics:** Prometheus
- **Logs:** ELK Stack (Elasticsearch, Logstash, Kibana)
- **Traces:** Jaeger
- **Dashboards:** Grafana

**Option 3: Third-Party SaaS**
- **DataDog:** All-in-one
- **New Relic:** APM focused
- **Splunk:** Log-focused

#### Required Monitoring Metrics

```
Application Metrics:
├── Request count
├── Response time (p50, p95, p99)
├── Error rate
├── Error type breakdown
├── Request size
├── Response size
└── Endpoint latency breakdown

System Metrics:
├── CPU usage
├── Memory usage
├── Disk space
├── Network I/O
├── Process count
└── File descriptor usage

Database Metrics:
├── Connection pool usage
├── Query latency
├── Slow query count
├── Transaction count
├── Replication lag
└── Backup status

Business Metrics:
├── Users online
├── Active sessions
├── Transaction count
├── Revenue (if applicable)
└── Error impact on users
```

#### Required Alerts

```yaml
Alerts:
  - name: HighErrorRate
    threshold: error_rate > 1%
    severity: critical
    action: page on-call
  
  - name: HighLatency
    threshold: p95_latency > 1000ms
    severity: warning
    action: notify team
  
  - name: HighCPU
    threshold: cpu_usage > 90%
    severity: warning
    action: notify ops
  
  - name: LowDiskSpace
    threshold: disk_free < 5%
    severity: critical
    action: page on-call
  
  - name: DatabaseDown
    threshold: db_unreachable
    severity: critical
    action: page on-call
```

**Validation:** [ ] Monitoring and alerting configured

---

### Phase D5.7: Final QA Sign-Off

**Goal:** Get approval to proceed to Phase D6

**Time:** 1 day  
**Owner:** QA Lead + Tech Lead

#### QA Checklist

| Item | Pass? | Notes |
|------|-------|-------|
| All tests passing | [ ] | Smoke, integration, E2E |
| Performance acceptable | [ ] | <500ms response time |
| Security scanning clean | [ ] | No critical vulnerabilities |
| Compliance controls verified | [ ] | All mapped controls working |
| Backup/restore tested | [ ] | Recovery procedure works |
| Monitoring active | [ ] | Alerts configured |
| Runbooks complete | [ ] | Operational procedures documented |
| No critical bugs | [ ] | Open issues list reviewed |

#### Sign-Off Form

```markdown
# Phase D5 Sign-Off

**Deployment Date:** [Date]
**Application Version:** [Version/Build #]
**Deployed by:** [Name]
**Tested by:** [QA Lead]
**Verified by:** [Tech Lead]

## Testing Summary
- Unit Tests: X passed, 0 failed
- Integration Tests: X passed, 0 failed
- E2E Tests: X passed, 0 failed
- Performance Tests: PASS
- Security Tests: PASS
- Compliance Tests: PASS

## Issues Found
- [ ] No critical issues
- [ ] Issues found: [List]

## Approval
- [ ] QA Lead: Approves deployment __________ (signature) Date: ___
- [ ] Tech Lead: Approves deployment __________ (signature) Date: ___
- [ ] Ops Lead: Approves deployment __________ (signature) Date: ___

## Sign-Off
✅ **Ready for Phase D6: Gate (Compliance Audit)**
```

**Validation:** [ ] QA sign-off received

---

## D5 Completion Checklist

### Build & Artifact
- [ ] Build passes locally
- [ ] All tests pass
- [ ] Linting passes
- [ ] Security scan passes
- [ ] Build artifact created
- [ ] BUILD_INFO.md documented

### Staging Environment
- [ ] Infrastructure provisioned
- [ ] Database configured
- [ ] Configuration management in place
- [ ] Logging & monitoring setup
- [ ] Security measures in place
- [ ] Backups configured

### Deployment
- [ ] Deployment automation in place (or manual procedure documented)
- [ ] Application deployed to staging
- [ ] Application started successfully
- [ ] No errors in logs

### Testing
- [ ] Smoke tests pass
- [ ] Integration tests pass
- [ ] E2E tests pass
- [ ] Performance tests pass
- [ ] Security tests pass
- [ ] Compliance tests pass
- [ ] Backup/restore tested

### Documentation
- [ ] Deployment runbook complete
- [ ] Monitoring runbook complete
- [ ] Troubleshooting guide complete
- [ ] Incident response procedure complete
- [ ] Rollback procedure complete

### Monitoring
- [ ] Monitoring dashboard created
- [ ] Alerts configured
- [ ] Log aggregation working
- [ ] Metrics collection working

### Sign-Off
- [ ] QA Lead signed off
- [ ] Tech Lead signed off
- [ ] Ops Lead signed off
- [ ] All blockers resolved

---

## What's Next: Phase D6 (Gate)

After D5 is complete, proceed to **Phase D6: Gate (Compliance Audit)**

See: Documentation (to be created) or contact Security Lead

### D6 Activities
- **Security audit** — Verify compliance controls
- **Compliance review** — Check control mappings
- **Sign-off from security/compliance** — Formal approval
- **Prepare for production** — Phase D7

---

## Troubleshooting D5 Issues

### "Deployment failed"
1. Check build artifact exists
2. Verify staging environment ready
3. Check logs for specific error
4. Try manual deployment steps
5. Escalate if unresolved

### "Tests failing in staging"
1. Check if same tests pass locally
2. Verify staging configuration correct
3. Verify staging database has test data
4. Check for environment-specific issues
5. Fix tests or configuration

### "Performance degraded"
1. Check monitoring dashboard
2. Identify bottleneck (CPU/memory/database)
3. Optimize slow queries or code
4. Scale infrastructure if needed
5. Re-test after fix

### "Monitoring not working"
1. Verify monitoring agent installed
2. Check agent connectivity to backend
3. Verify dashboards configured
4. Check for firewall rules blocking metrics
5. Restart monitoring agent

---

**Last Updated:** 2026-10-04  
**Maintained by:** DevOps/Infrastructure Lead  
**Related:** `d4-completion-checklist.md`, `developer-setup-guide.md`, Phase D6 (Gate) documentation
