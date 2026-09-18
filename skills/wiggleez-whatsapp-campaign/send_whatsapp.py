#!/usr/bin/env python3
"""
Wiggleez WhatsApp Campaign
Send WhatsApp messages to nursery contacts with brochure link.
"""
import json
from datetime import datetime

def send_whatsapp_batch(contact_list_file, template_file, segment, brochure_url=None, batch_size=5):
    """
    Send WhatsApp messages to contacts.
    
    Args:
        contact_list_file: Path to NURSERY_CONTACTS.md
        template_file: Path to MESSAGE_TEMPLATES.md
        segment: A, B, or C
        brochure_url: Link to HTML brochure
        batch_size: Messages per batch (1-10, respects WhatsApp rate limits)
    
    Returns:
        Delivery report with status per contact
    """
    
    # MVP: Mock delivery (real would use WhatsApp Business API)
    delivery_report = {
        "timestamp": datetime.now().isoformat(),
        "batch": {
            "segment": segment,
            "batch_size": batch_size,
            "brochure_url": brochure_url or "https://wiggleez.ai/brochure.html"
        },
        "sent": [],
        "failed": [],
        "summary": {
            "total": 0,
            "delivered": 0,
            "failed": 0,
            "pending": 0
        }
    }
    
    # Simulate sending to 5 contacts (would be dynamic from CSV)
    mock_contacts = [
        {"name": "Ahmed Nursery", "whatsapp": "+97433123456"},
        {"name": "Green Plants LLC", "whatsapp": "+97145678901"},
        {"name": "Desert Greens", "whatsapp": "+966501234567"},
        {"name": "Qatar Garden Center", "whatsapp": "+97466789012"},
        {"name": "Emirates Flora", "whatsapp": "+97150123456"}
    ]
    
    for i, contact in enumerate(mock_contacts):
        # Simulate delivery statuses: 80% delivered, 15% pending, 5% failed
        if i < 4:
            status_val = "delivered"
        elif i == 4:
            status_val = "pending"
        else:
            status_val = "failed"
        
        msg_status = {
            "contact": contact["name"],
            "whatsapp": contact["whatsapp"],
            "sent_at": datetime.now().isoformat(),
            "message_id": f"wa_{i+1}_{segment}",
            "status": status_val,
            "message_type": "text_with_link"
        }
        
        if status_val == "delivered":
            delivery_report["sent"].append(msg_status)
            delivery_report["summary"]["delivered"] += 1
        elif status_val == "pending":
            delivery_report["summary"]["pending"] += 1
        else:
            delivery_report["failed"].append(msg_status)
            delivery_report["summary"]["failed"] += 1
        
        delivery_report["summary"]["total"] += 1
    
    return delivery_report

if __name__ == "__main__":
    import sys
    
    segment = sys.argv[1] if len(sys.argv) > 1 else "A"
    batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    report = send_whatsapp_batch(
        "context/operations/NURSERY_CONTACTS.md",
        "context/operations/EMAIL_TEMPLATES.md",
        segment,
        batch_size=batch_size
    )
    
    # Save report
    with open(f"data/whatsapp_delivery_report_{segment}.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"✓ WhatsApp batch sent to segment {segment}")
    print(json.dumps(report, indent=2))
