---
name: COST_TRACKING
type: governance
version: 1.0.0
description: "Budget tracking, ROI per service, spending alerts"
---

# Cost Tracking & ROI System

**Budget:** $200 QAR/month  
**Tracking period:** Monthly (Sep-Dec 2026), then quarterly 2027+  
**Review cadence:** Weekly spending check, monthly ROI calculation

---

## Service Breakdown & Costs

| Service | Cost/Month | Usage | ROI Target | Notes |
|---|---|---|---|---|
| **Gmail API** | $0 | Unlimited emails | N/A | Free tier: 15GB storage, 100 users, unlimited emails |
| **WhatsApp Business API** | $0.05/msg | ~500 msgs/month | $25 revenue/month | Meta's current pricing (Sep 2026) |
| **Canva Team** | $120/year ($10/mo) | 10 designs/month | $50 revenue/month | Design templates for Instagram, email, WhatsApp |
| **Market Data APIs** | $0 | Unlimited | N/A | Free sources: Yahoo Finance, CoinGecko, HackerNews RSS |
| **Shopify** | $39/month | Store hosting | Already paid | Not counted in Wiggleez budget |
| **Gmail Storage (paid)** | $0-20 | As needed | N/A | Only if free tier (15GB) exceeded |
| **Twilio** (backup) | $0.01/SMS | Fallback | N/A | Fallback if WhatsApp API down |
| **TOTAL MONTHLY** | **~$60** | — | — | Leaves $140/month buffer for testing |

---

## ROI Targets (Per Service)

### Email Campaign
- **Cost:** ~$0 (Gmail free)
- **Expected result:** 15 emails → 2-3 responses → 1 conversion
- **Revenue per conversion:** 1,500+ QAR (Wiggleez annual package)
- **ROI:** 1,500 / 0 = ∞ (free, so ANY response = positive ROI)

### WhatsApp Campaign
- **Cost:** $0.05 × 500 msgs = $25/month
- **Expected result:** 50% response rate (per market research)
- **Revenue per response:** 200 QAR (demo + consultation)
- **Expected monthly revenue from WhatsApp:** 250 × 0.50 = 125 contacts reached, 20% convert = 25 customers × 500 QAR = 12,500 QAR
- **ROI:** 12,500 / 25 = **$500 per $1 spent** ✓ (Exceeds 10:1 target)

### Canva Design Automation
- **Cost:** $10/month
- **Expected result:** 4 designs/week for Instagram (16/month)
- **Revenue per design post:** 50 QAR average (increased traffic, sales)
- **Expected monthly revenue:** 16 × 50 = 800 QAR
- **ROI:** 800 / 10 = **$80 per $1 spent** ✓ (Exceeds 10:1 target)

### Market Intelligence
- **Cost:** $0 (free APIs)
- **Expected result:** Identifies 2-3 market opportunities/month
- **Revenue per opportunity:** Varies (pricing, partnerships, AI services)
- **ROI:** N/A (free, but informs strategy)

---

## Monthly Budget Allocation (Recommended)

```
Total: $200 QAR
├── WhatsApp: $50 (send 1,000 messages)
├── Canva: $10 (annual plan pro-rated)
├── Testing & Contingency: $50
├── Shopify optimization (if needed): $20
├── Tools/services pipeline: $40
└── Buffer: $30
```

---

## Weekly Spending Check

**Every Monday morning (7 AM):**

```
Last week spending:
  - WhatsApp sent: [X messages] = $[X × 0.05] cost
  - Canva designs created: [Y] = $[10/30 × Y] cost
  - Other services: $[Z]
  - Total: $[X + Y + Z]

Remaining budget this month:
  - Budget: $200
  - Spent to date: $[A]
  - Remaining: $[200 - A]
  - Avg daily burn: $[A / days elapsed]
  - Projected end-of-month: $[A + (avg × remaining days)]

Status:
  ✓ On track (projected spend = $200 ±10%)
  ⚠️ Running high (projected >$220)
  ✓ Running low (projected <$180)
```

---

## Monthly ROI Calculation

**Last day of month (30 Sep, 31 Oct, etc):**

```
Wiggleez Revenue This Month:
  - New customers: [N]
  - Revenue per customer: 1,500 QAR (annual) = 125 QAR/month
  - Total revenue: N × 125 = [R] QAR

Wiggleez Operations Cost:
  - Email: $0
  - WhatsApp: $[msgs × 0.05]
  - Canva: $10
  - Other: $[X]
  - Total: $[C]

ROI Calculation:
  - Gross profit: R - C = [P] QAR
  - ROI: P / C × 100 = [%]
  - Target: 1,000% (every $1 → $10 back)
  - Status: ✓ Met / ⚠️ Below target
```

---

## Spending Alerts

| Alert | Threshold | Action |
|---|---|---|
| **Weekly overspend** | >$50/week | Email Captain: "On track to exceed $200 this month" |
| **WhatsApp cost spike** | >$75/month | Likely error (too many messages). Audit & correct. |
| **No revenue this month** | $0 in 21 days | Pause WhatsApp, focus on email/warm outreach |
| **Negative ROI** | Revenue < Costs | Emergency meeting: strategy change needed |
| **Budget overflow** | Projected >$220 | Cut unnecessary services or defer testing |

---

## Cost Optimization Rules

1. **Use free sources first** (Gmail, Yahoo Finance, CoinGecko)
2. **Batch WhatsApp sends** (1 send per contact, not multiple retries)
3. **Reuse Canva templates** (design once, reuse 10x)
4. **No paid tools without ROI proof** (Test with free tier first)
5. **Monthly audit** (Every 30 days, review spending vs. targets)

---

## Budget Review & Reforecasting

**End of Q4 (31 Dec):**
- Total spent: [X] QAR
- Total revenue: [R] QAR
- Actual ROI: [R/X]
- Recommendation for Q1 2027: Increase to $300? Decrease? Scale what works?

**Q1 2027 + onward:**
- Adjust based on Q4 results
- Scale winning channels (if ROI >1000%)
- Cut underperforming channels (ROI <100%)
