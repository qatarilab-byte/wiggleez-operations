---
name: wiggleez-email-campaign-agent
type: agent
version: 1.0.0
---

# AGENT: Wiggleez Email Campaign

Execute complete email → WhatsApp → calls → conversion workflow.

## Steps (In Order)

1. **Validate contacts** — Check NURSERY_CONTACTS.md for required fields
2. **Send emails** (Day 0) — Run wiggleez-email-outreach skill
3. **Wait 24-48h** — Let emails sit in inboxes
4. **Send WhatsApp** (Day 2) — Run wiggleez-whatsapp-campaign skill
5. **Monitor responses** (Days 2-9) — Check Gmail + WhatsApp API daily
6. **Schedule calls** (Day 7+) — Reply with Calendly link
7. **Conduct demos** (Day 8-14) — 15-min calls per contact
8. **Onboard** (Day 15+) — Setup for converted customers

## Success Metrics

| Metric | Target |
|--------|--------|
| Emails sent | 15 |
| Response rate | >30% |
| Calls completed | >5 |
| Conversion rate | >10% |
| Revenue | >3,000 QAR |

## Running

```bash
python3 agents/wiggleez-email-campaign-agent.py --action continue
```
