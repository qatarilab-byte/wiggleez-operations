# SKILL: Brief Generator — Morning

Format market intel + Wiggleez metrics into 7 AM brief.

## What It Does

Take raw data (market intel, sales metrics, campaign status) and format for WhatsApp delivery.

## Inputs

- market_intel_today.json (from market-intelligence-daily-agent)
- wiggleez_metrics_today.json (orders, revenue, traffic)
- campaign_status.json (emails sent, responses)

## Outputs

- morning_brief.txt (WhatsApp-friendly format)
- morning_brief.json (structured data for delivery logging)

## Format

```
📊 MORNING BRIEF — [Date]

🏪 Wiggleez
• Orders: [N]
• Revenue: [QAR]
• Traffic: [%]

📈 Markets
• Qatar DSX: [trend]
• S&P 500: [trend]
• Bitcoin: [trend]

💼 Campaigns
• Emails sent: [N]
• Responses: [N]
• Calls scheduled: [N]

⚠️ System
• J: [status]
• H: [status]

🎯 Today
1. [action 1]
2. [action 2]
```

## Steps

1. Read all input JSONs
2. Format into brief template
3. Calculate key highlights
4. Write TXT + JSON outputs
