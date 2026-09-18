# SKILL: Brief Generator — Weekly

Compile 7-day summary for Sunday 8 AM report.

## What It Does

Aggregate 7 days of data and create weekly summary.

## Inputs

- 7 days of market_indicators_daily.csv
- 7 days of campaign_tracking.csv
- 7 days of wiggleez_metrics_daily.csv

## Outputs

- weekly_report.txt (WhatsApp-friendly)
- weekly_report.json (for archiving)

## Format

```
📅 WEEKLY REPORT — Week of [Dates]

🏪 Wiggleez Performance
• Total orders: [N]
• Total revenue: [QAR]
• Growth vs last week: [%]

📊 Campaign Funnel
• Emails sent: [N]
• Responses: [N] ([%])
• Calls completed: [N]
• Conversions: [N]

📈 Market Trends
• Winners: [list]
• Losers: [list]
• Opportunities: [list]

⏰ Next Week
• Actions: [list]
• Targets: [list]
```

## Steps

1. Aggregate 7 days data
2. Calculate totals + %
3. Identify trends
4. Format into report template
5. Write outputs
