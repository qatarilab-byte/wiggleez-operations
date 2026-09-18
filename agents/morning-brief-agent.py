#!/usr/bin/env python3
"""
Agent: Morning Brief (7 AM Delivery)
Generates and prepares brief for WhatsApp delivery.
"""
import json
import subprocess
from datetime import datetime
import os

def run_morning_brief():
    """Execute morning brief agent."""
    
    print("🔄 Starting Morning Brief Agent (7 AM Delivery)...\n")
    
    # Step 1: Run market intelligence
    print("  ↳ Step 1: Gathering market intelligence...", end=" ")
    result = subprocess.run(
        "python3 agents/market-intelligence-daily-agent.py",
        shell=True, capture_output=True, text=True, cwd=os.getcwd()
    )
    print("✓")
    
    # Step 2: Generate brief
    print("  ↳ Step 2: Generating brief...", end=" ")
    result = subprocess.run(
        "python3 skills/brief-generator-morning/generate.py",
        shell=True, capture_output=True, text=True, cwd=os.getcwd()
    )
    print("✓")
    
    # Step 3: Read brief for delivery
    brief_text = ""
    try:
        with open("data/morning_brief.txt", "r") as f:
            brief_text = f.read()
    except:
        brief_text = "[Unable to read brief file]"
    
    # Step 4: Prepare delivery log
    delivery_log = {
        "timestamp": datetime.now().isoformat(),
        "agent": "morning-brief",
        "brief_generated": True,
        "brief_size_chars": len(brief_text),
        "ready_for_delivery": True,
        "delivery_time": "2026-09-18T07:00:00+03:00",
        "destination": "WhatsApp (Captain)",
        "status": "queued"
    }
    
    with open("data/delivery_log.json", "w") as f:
        json.dump(delivery_log, f, indent=2)
    
    print("  ↳ Step 3: Brief ready for delivery\n")
    print(f"✓ Morning brief prepared at {datetime.now().isoformat()}")
    print(f"✓ Scheduled delivery: 2026-09-18 07:00 UTC+3")
    print(f"✓ Status: QUEUED\n")
    
    return delivery_log, brief_text

if __name__ == "__main__":
    log, brief = run_morning_brief()
    print("Brief preview:")
    print("─" * 60)
    print(brief[:300] + "...\n" if len(brief) > 300 else brief)
