---
name: morning-brief-agent
type: agent
version: 1.0.0
---

# AGENT: Morning Brief (7 AM Delivery)

Generate and deliver morning brief to Captain.

## Steps (In Order)

1. **Gather intel** — Run market-intelligence-daily-agent
2. **Get metrics** — Read wiggleez_metrics_today.json
3. **Format brief** — Run brief-generator-morning skill
4. **Deliver** — Send to Captain via WhatsApp at 7:00 AM UTC+3
5. **Log delivery** — Timestamp + read receipt

## Delivery

Auto-scheduled via GitHub Actions at 6:40 AM (to hit 7 AM deadline).

## Content

- Wiggleez sales (orders, revenue)
- Market moves (Qatar DSX, S&P, crypto, AI)
- Campaign status (emails, responses, calls)
- System health
- Action items
