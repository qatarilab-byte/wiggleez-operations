#!/usr/bin/env python3
"""
Market Analysis: Global Stocks
Tracks S&P 500, tech sector, and global indices.
"""
import json
from datetime import datetime

def analyze_global_stocks():
    """Analyze global stock markets for trends."""
    
    # MVP: Mock data (real would use yfinance or Alpha Vantage API)
    data = {
        "date": datetime.now().isoformat(),
        "sp500": {
            "current": 5847.23,
            "change_pct": 1.2,
            "trend": "up",
            "52week_high": 6094.50,
            "52week_low": 5248.80
        },
        "tech_sector": {
            "current": 19234.56,
            "change_pct": 2.1,
            "trend": "up",
            "components": ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]
        },
        "nasdaq": {
            "current": 18456.78,
            "change_pct": 1.8,
            "trend": "up"
        },
        "dax": {
            "current": 18234.45,
            "change_pct": 0.9,
            "trend": "neutral"
        },
        "nikkei": {
            "current": 38456.23,
            "change_pct": -0.3,
            "trend": "down"
        },
        "insights": [
            "Tech sector momentum continues",
            "AI stocks leading gains",
            "Bond yields stable"
        ],
        "timestamp": datetime.now().isoformat()
    }
    
    return data

if __name__ == "__main__":
    result = analyze_global_stocks()
    
    # Write to data file
    output_path = "data/market_intel_global_stocks.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"✓ Global stocks analysis saved to {output_path}")
    print(json.dumps(result, indent=2))
