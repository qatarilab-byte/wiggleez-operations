# SKILL: Wiggleez WhatsApp Campaign

Send WhatsApp messages to nursery contacts.

## What It Does

Send personalized WhatsApp messages with HTML brochure link + follow-up sequence.

## Inputs

- contact_list: NURSERY_CONTACTS.md
- template: MESSAGE_TEMPLATES.md
- segment: A | B | C
- brochure_url: Link to ACTIVE_wiggleez_nursery_brochure.html

## Outputs

- whatsapp_delivery_report.json
- campaign_tracking.csv (updated)

## Steps

1. Load contacts from segment
2. Format message with brochure link
3. Send via WhatsApp Business API
4. Log delivery status (✓ delivered, pending, failed)
5. Update tracking CSV

## Approval

Tier 1: Captain must approve message + recipients before send.
