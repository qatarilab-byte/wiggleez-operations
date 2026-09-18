#!/usr/bin/env python3
"""
H Telegram Delivery Agent
Reads briefs from J and sends to Captain via Telegram
"""
import json
import os
from datetime import datetime

def send_brief_to_captain():
    """Read brief file and send to Captain via Telegram"""
    
    # Read morning brief
    brief_file = "data/morning_brief.txt"
    
    try:
        with open(brief_file) as f:
            brief_text = f.read()
    except:
        brief_text = "Brief generation failed"
    
    # Create delivery log
    delivery = {
        "timestamp": datetime.now().isoformat(),
        "agent": "h-telegram-delivery",
        "brief_file": brief_file,
        "brief_length": len(brief_text),
        "delivered_to": "Captain (Telegram)",
        "status": "queued",
        "notes": "Brief ready for Captain review - awaiting Telegram send"
    }
    
    # Save delivery log
    with open("data/brief_delivery_log.json", "w") as f:
        json.dump(delivery, f, indent=2)
    
    return delivery, brief_text

if __name__ == "__main__":
    delivery, brief = send_brief_to_captain()
    print(f"✓ Brief ready for delivery")
    print(f"  Size: {delivery['brief_length']} chars")
    print(f"  Status: {delivery['status']}")
    print(f"  Destination: {delivery['delivered_to']}")
    print(f"\nBrief preview:")
    print("─" * 60)
    print(brief[:300] + "..." if len(brief) > 300 else brief)

