# AI Cloud Doctor – Autonomous Incident Triage

## 🚀 Overview

AI Cloud Doctor is an AI-powered cloud incident management system that automatically detects, analyzes, and responds to cloud incidents.

The system combines **Lyzr AI**, **Encrypt AI Guardrails**, and **Qdrant Vector Database** to provide intelligent, safe, and knowledge-driven incident triage.

Instead of simply detecting an error, AI Cloud Doctor analyzes the incident, identifies the likely root cause, evaluates the blast radius and confidence, and decides whether the issue can be safely remediated automatically or requires human approval.

---

## 🎯 Problem

Cloud applications continuously generate logs, metrics, alerts, and traces. When an incident occurs, DevOps engineers often need to manually:

* Identify the incident
* Analyze multiple telemetry sources
* Find the root cause
* Determine the impact
* Decide on a remediation
* Verify recovery

This process can be time-consuming and may delay incident resolution.

---

## 💡 Solution

AI Cloud Doctor provides an intelligent incident-response workflow:

**Detect → Analyze → Diagnose → Assess Risk → Decide → Remediate → Verify → Learn**

The agent uses previous incident knowledge to improve its analysis while applying safety guardrails before allowing automated actions.

---

## 🏗️ Architecture

```text
Cloud Application
       ↓
Logs / Metrics / Alerts / Traces
       ↓
┌───────────────────────────┐
│       Qdrant              │
│ Incident Knowledge Base   │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│       Lyzr AI Agent       │
│     AI Cloud Doctor       │
│                           │
│ Detection → Analysis      │
│ → Root Cause → Decision   │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│     Encrypt AI            │
│       Guardrail           │
│   Safety & Risk Check     │
└─────────────┬─────────────┘
              ↓
       ┌──────┴──────┐
       ↓             ↓
   Safe Action    Human Approval
       ↓             ↓
       └──────┬──────┘
              ↓
      Remediation
              ↓
    Recovery Verification
              ↓
       ┌──────┴──────┐
       ↓             ↓
 Incident Resolved   Escalation
       ↓
   Store Outcome
       ↓
     Qdrant
```

---

## 🧠 Core Components

### Lyzr AI

Lyzr powers the **AI Cloud Doctor Agent**.

It performs:

* Incident detection
* Log and metric analysis
* Root Cause Analysis
* Blast-radius assessment
* Confidence scoring
* Remediation decision-making
* Recovery verification

### Encrypt AI

Encrypt AI acts as the **safety and security guardrail**.

It evaluates proposed AI actions before risky operations are allowed.

The system separates:

* 🟢 Safe automatic actions
* 🟠 Human approval actions

### Qdrant

Qdrant acts as the **Incident Knowledge Base**.

It stores previous incidents, including:

* Symptoms
* Root cause
* Blast radius
* Remediation
* Outcome
* Confidence

When a new incident occurs, similar historical incidents can be retrieved to support the AI's analysis.

---

## 🔄 Incident Workflow

1. Receive an incident or alert.
2. Analyze available telemetry.
3. Retrieve similar incidents from Qdrant.
4. Perform Root Cause Analysis using Lyzr.
5. Calculate confidence.
6. Determine the blast radius.
7. Decide whether automatic remediation is safe.
8. Pass the proposed action through Encrypt AI Guardrails.
9. Execute a safe action or request human approval.
10. Verify system recovery.
11. Store the incident outcome in Qdrant.

---

## 🛠️ Possible Remediation Actions

The system can recommend safe actions such as:

* Restart Service
* Retry Connection
* Scale Service

High-risk or uncertain incidents are escalated to a DevOps engineer.

---

## 🧪 Example

### Input

```text
Payment service error rate increased from 2% to 18%.
Database connection timeouts are increasing.
One payment-service pod is unhealthy.
Other services are operating normally.
No recent deployment was made.
```

### AI Cloud Doctor Analysis

```text
Incident: Payment Service Failure

Likely Root Cause:
Database connection issue

Blast Radius:
Single Service

Confidence:
94%

Recommended Action:
Retry Connection / Restart Unhealthy Pod

Decision:
Safe Automatic Action

Recovery:
Verify error rate, latency, pod health, and database connectivity
```

### Critical Incident Example

If multiple customer-facing services fail simultaneously:

```text
Blast Radius:
Multi-service / Customer-facing

Decision:
Human Approval Required

Reason:
High-impact incident requires controlled remediation.
```

---

## 🔐 Security

Sensitive credentials such as API keys must never be committed to GitHub.

Environment variables should be stored in a local `.env` file.

Example:

```text
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
LYZR_API_KEY=your_lyzr_api_key
ENCRYPT_AI_API_KEY=your_encrypt_ai_api_key
```

The `.env` file should be included in `.gitignore`.

---

## 📁 Project Structure

```text
ai-cloud-doctor/
│
├── app.py
├── agents/
│   └── lyzr_agent.py
├── guardrails/
│   └── encrypt_guardrail.py
├── knowledge/
│   └── qdrant_client.py
├── data/
│   └── incidents.json
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🏆 Hackathon Innovation

AI Cloud Doctor goes beyond traditional alerting by combining:

**AI Reasoning + Historical Knowledge + Safety Guardrails + Controlled Autonomous Remediation**

The system does not blindly execute every AI recommendation.

It considers:

**Confidence + Blast Radius + Risk**

before deciding between autonomous remediation and human approval.

---

## 🔮 Future Scope

* Real-time cloud telemetry integration
* Kubernetes integration
* AWS / Azure / GCP monitoring integration
* Automated incident reporting
* Advanced incident prediction
* Continuous learning from resolved incidents
* Multi-agent DevOps workflows
* Real-time dashboards

---

## 👥 Project

**AI Cloud Doctor – Autonomous Incident Triage**

Built as a college hackathon project using AI-powered cloud incident analysis, safety guardrails, and vector-based incident knowledge retrieval.
