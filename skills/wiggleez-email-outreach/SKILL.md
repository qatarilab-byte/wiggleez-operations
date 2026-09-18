# SKILL: Wiggleez Email Outreach

Send personalized emails to nursery contacts via Gmail API.

## What It Does

Batch email sending to Segment A/B/C contacts with personalized copy, rate limiting, and delivery logging.

## Inputs

- contact_list: NURSERY_CONTACTS.md
- template: EMAIL_TEMPLATES.md
- segment: A | B | C
- batch_size: 1-10

## Outputs

- delivery_report.json (timestamp, message IDs, status)
- campaign_tracking.csv (updated)

## Steps

1. Load contacts from segment
2. For each contact: personalize + send
3. Log delivery timestamp + message ID
4. Update tracking CSV
5. Report summary

## Approval

Tier 1: Captain must approve copy + recipients before send.
