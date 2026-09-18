---
name: weekly-report-agent
type: agent
version: 1.0.0
---

# AGENT: Weekly Report (Sunday 8 AM)

Compile 7-day summary for Captain.

## Steps (In Order)

1. **Aggregate** — Compile 7 days of market intel
2. **Summarize** — Run brief-generator-weekly skill
3. **Deliver** — Send to Captain via WhatsApp Sunday 8:00 AM UTC+3
4. **Archive** — Log to /docs/WEEKLY_REPORTS.md

## Content

- Weekly sales trend (orders, revenue, growth %)
- Market winners/losers
- Campaign performance (email → call → conversion funnel)
- System uptime + incidents
- Next week forecast
