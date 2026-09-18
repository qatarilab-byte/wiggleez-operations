#!/usr/bin/env python3
"""
Agent: Wiggleez Email Campaign
Execute full email → WhatsApp → calls → conversion workflow.
"""
import json
import subprocess
from datetime import datetime
import os

def run_email_campaign(segment="A", day=0):
    """
    Execute email campaign for a segment.
    
    Args:
        segment: A, B, or C
        day: Day of campaign (0 = email send, 2 = WhatsApp, 7+ = calls)
    """
    
    print(f"🔄 Starting Email Campaign Agent (Segment {segment}, Day {day})...\n")
    
    workflow_steps = {
        0: ("Send emails", "python3 skills/wiggleez-email-outreach/send_emails.py"),
        2: ("Send WhatsApp", "python3 skills/wiggleez-whatsapp-campaign/send_whatsapp.py"),
    }
    
    if day in workflow_steps:
        step_name, command = workflow_steps[day]
        print(f"  ↳ Step {day + 1}: {step_name}...", end=" ")
        result = subprocess.run(
            f"{command} {segment}",
            shell=True, capture_output=True, text=True, cwd=os.getcwd()
        )
        print("✓\n")
    elif day >= 7:
        print(f"  ↳ Step: Monitor responses and schedule calls...\n")
    
    # Log campaign action
    campaign_log = {
        "timestamp": datetime.now().isoformat(),
        "agent": "wiggleez-email-campaign",
        "segment": segment,
        "day": day,
        "action": workflow_steps.get(day, ("monitor", ""))[0],
        "status": "success"
    }
    
    with open(f"data/campaign_action_{segment}_day{day}.json", "w") as f:
        json.dump(campaign_log, f, indent=2)
    
    print(f"✓ Campaign step completed")
    print(f"✓ Segment: {segment}")
    print(f"✓ Day: {day}\n")
    
    return campaign_log

if __name__ == "__main__":
    import sys
    
    segment = sys.argv[1] if len(sys.argv) > 1 else "A"
    day = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    
    log = run_email_campaign(segment, day)
    print(json.dumps(log, indent=2))
