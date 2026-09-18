---
name: CLAUDE.md
type: entry_point
version: 1.0.0
description: "Master brief for J and H — AI reads this first"
---

# WIGGLEEZ OPERATIONS SYSTEM

## What This Repository Does

Autonomous business operations for Wiggleez (ecommerce nursery software) toward a $1B goal in 12 months.

**Three components:**
1. **Wiggleez** — Ecommerce + nursery outreach automation
2. **Market Intelligence** — Qatar DSX, global stocks, crypto, AI tools monitoring
3. **Team Collaboration** — J executes, H delivers briefings, Captain approves

---

## Who Runs This System

- **J (Mac mini Pro):** Executor. Runs skills, sends emails/WhatsApp, gathers market data.
- **H (VPS):** Intelligence delivery. Formats briefings, sends 7 AM & 8 AM reports to Captain.
- **Captain:** Strategy + approvals. Reviews briefings, approves campaigns, makes final decisions.

---

## How It Works (Daily Cycle)

### 6:00 AM — Morning Begins

1. J runs market analysis skills (Qatar DSX, S&P 500, crypto, AI news)
2. J gathers Wiggleez metrics (orders, revenue, traffic from yesterday)
3. J compiles everything into JSON files

### 6:40 AM — J Syncs to H

```bash
rsync -avz ~/.hermes/data/ root@100.123.112.75:/data/wiggleez-operations/
```

### 6:43 AM — H Processes Brief

1. H reads synced data
2. H runs brief-generator-morning skill
3. H formats for WhatsApp
4. H queues for delivery at 7:00 AM sharp

### 7:00 AM — Brief Arrives on Captain's WhatsApp

**Morning Brief contains:**
- Wiggleez sales (orders, revenue from yesterday)
- Market intel (Qatar DSX moves, global stock trends, crypto volatility, new AI tools)
- Campaign status (emails sent, responses received, calls scheduled)
- System health (J status, H status, any errors)
- Action items (what to do today)

### 7:00 AM - 9:00 PM — Captain Uses Brief to Make Decisions

- Reviews campaigns
- Approves new email batches ✓ or suggests changes
- Checks market opportunities
- Makes strategic calls

### 9:00 PM — Evening Standup

1. J reports day's results (emails sent, responses, calls completed)
2. H acknowledges receipt
3. Both sync back

### 10:00 PM - 6:00 AM — Rest

Both agents idle until morning.

---

## Folder Structure

```
wiggleez-operations/
├── README.md                        (Human-friendly guide)
├── CLAUDE.md                        (THIS FILE — AI reads first)
├── .gitignore                       (Secrets stay out of git)
├── .github/workflows/               (GitHub Actions — automated scheduling)
│
├── /skills/                         (REUSABLE TASKS)
│   ├── wiggleez-email-outreach/
│   ├── wiggleez-whatsapp-campaign/
│   ├── market-analysis-qatar-dsx/
│   ├── market-analysis-global-stocks/
│   ├── market-analysis-crypto/
│   ├── ai-tools-hunter/
│   ├── brief-generator-morning/
│   └── brief-generator-weekly/
│
├── /agents/                         (SEQUENCES OF SKILLS)
│   ├── wiggleez-email-campaign-agent.md
│   ├── market-intelligence-daily-agent.md
│   ├── morning-brief-agent.md
│   └── weekly-report-agent.md
│
├── /context/                        (BUSINESS KNOWLEDGE)
│   ├── business/
│   │   ├── WIGGLEEZ_ICP.md
│   │   ├── WIGGLEEZ_MESSAGING.md
│   │   └── WIGGLEEZ_TONEOFVOICE.md
│   ├── market/
│   │   ├── QATAR_DSX_ANALYSIS.md
│   │   ├── GLOBAL_MARKET_INDICATORS.md
│   │   └── AI_SERVICES_LANDSCAPE.md
│   ├── operations/
│   │   ├── SHOPIFY_SETUP.md
│   │   ├── CANVA_AUTOMATION.md
│   │   ├── NURSERY_CONTACTS.md
│   │   ├── EMAIL_TEMPLATES.md
│   │   └── J_H_SYNC_PROTOCOL.md
│   └── governance/
│       ├── APPROVAL_GATES.md
│       └── COST_TRACKING.md
│
├── /data/                           (LIVE METRICS)
│   ├── wiggleez_metrics_daily.csv
│   ├── market_indicators_daily.csv
│   ├── campaign_tracking.csv
│   └── api_usage.json
│
└── /docs/                           (REFERENCE)
    ├── ARCHITECTURE.md
    ├── PLAYBOOK.md
    ├── DECISION_LOG.md
    └── TROUBLESHOOTING.md
```

---

## How AI Should Approach This

### Before Any Action

1. **Read THIS file (CLAUDE.md)** first
2. **Load relevant `/context/` files** for the task
3. **Check `/data/`** for latest metrics
4. **Check `/docs/DECISION_LOG.md`** for Captain's past decisions
5. **Execute skill** from `/skills/`
6. **Log result** to `/data/campaign_tracking.csv` or `/docs/DECISION_LOG.md`

### Before Any Outreach (Email, WhatsApp, Social)

1. Read `/context/business/WIGGLEEZ_MESSAGING.md` (what to say)
2. Read `/context/governance/APPROVAL_GATES.md` (does it need approval?)
3. If Tier 1: Ask Captain first
4. Execute skill
5. Log to `/data/campaign_tracking.csv`

### Before Market Analysis

1. Read `/context/market/` files
2. Execute skill from `/skills/market-*`
3. Write results to `/data/market_indicators_daily.csv`
4. Include in brief if notable

---

## Critical Rules (Never Break)

1. **Always ask Captain before Tier 1 decisions** (email >10, WhatsApp any, social posts, spend >50 QAR)
2. **Sync data every 6 hours** (morning 6:40 AM, evening 9:00 PM)
3. **Validate all data before sync** (valid JSON/CSV, no secrets, <10MB total)
4. **Log everything** (DECISION_LOG.md, campaign_tracking.csv, api_usage.json)
5. **No hardcoded secrets** (use .env file, not git)

---

## Success Metrics

By end of Q4 2026:
- ✓ 50+ nurseries contacted
- ✓ 10+ customers converted
- ✓ 1,500 QAR revenue
- ✓ System running 99%+ uptime

By end of 2027:
- ✓ 500+ nurseries (GCC-wide)
- ✓ 100+ customers
- ✓ $15K+ monthly recurring revenue
- ✓ Path to $1B clear

---

**START:** Load `/context/business/WIGGLEEZ_ICP.md` to understand who you're reaching.
