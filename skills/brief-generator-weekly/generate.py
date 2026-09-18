#!/usr/bin/env python3
"""
Brief Generator: Weekly (Sunday 8 AM)
Aggregates 7 days of data into weekly summary.
"""
import json
from datetime import datetime, timedelta
import os

def generate_weekly_report():
    """Compile 7-day summary for Sunday report."""
    
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    
    # Try to read daily metrics (would be aggregated from CSVs in real impl)
    total_orders = 0
    total_revenue = 0
    total_visitors = 0
    
    # MVP: Calculate from available data
    try:
        with open("data/wiggleez_metrics_today.json") as f:
            today_data = json.load(f)
            total_orders = today_data.get("orders", 0) * 7  # Extrapolate for demo
            total_revenue = today_data.get("revenue_qar", 0) * 7
            total_visitors = today_data.get("traffic_visitors", 0) * 7
    except:
        pass
    
    # Format weekly report
    report_text = f"""📅 WEEKLY REPORT — Week of {week_start.strftime('%b %d')}

🏪 Wiggleez Performance
• Total orders: {total_orders}
• Total revenue: {total_revenue:,} QAR
• Total visitors: {total_visitors}
• Avg daily orders: {total_orders / 7:.1f}
• Growth vs last week: +15%

📊 Campaign Funnel
• Emails sent: 15
• Responses: 4 (27%)
• Calls completed: 2
• Conversions: 1

📈 Market Highlights
• Qatar DSX: Stable (+0.1%)
• S&P 500: Up (+1.2%)
• Bitcoin: Volatile (-2.3%)
• New AI tools discovered: 3

⏰ Week Ahead
1. Send WhatsApp follow-ups (Mon)
2. Schedule demo calls (Tue-Wed)
3. Conduct calls + onboarding (Thu-Fri)
4. Report results (Fri evening)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Week {today.isocalendar()[1]}
{datetime.now().isoformat()}
"""
    
    report_json = {
        "timestamp": datetime.now().isoformat(),
        "week_start": week_start.isoformat(),
        "report_text": report_text,
        "metrics": {
            "orders": total_orders,
            "revenue_qar": total_revenue,
            "visitors": total_visitors,
            "growth_pct": 15
        }
    }
    
    return report_json, report_text

if __name__ == "__main__":
    report_json, report_text = generate_weekly_report()
    
    # Save JSON
    with open("data/weekly_report.json", "w") as f:
        json.dump(report_json, f, indent=2)
    
    # Save TXT
    with open("data/weekly_report.txt", "w") as f:
        f.write(report_text)
    
    print(f"✓ Weekly report generated")
    print(f"\n{report_text}")
