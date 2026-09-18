---
name: EMAIL_TEMPLATES
type: context
version: 1.0.0
last_updated: 2026-09-18
---

# Email Templates & Copy

**See WIGGLEEZ_MESSAGING.md for full email templates.**

## Template File Locations

```
context/
├── email_templates/
│   ├── intro.html (Day 0 — First contact)
│   ├── followup_3day.html (Day 3 — Gentle reminder)
│   ├── followup_7day.html (Day 7 — Urgency: October peak)
│   ├── demo_request.html (Post-call — Demo scheduling)
│   └── testimonial.html (Proof — Case study)
```

## Email Variables (Personalization)

```
{CONTACT_NAME}     → Recipient first name
{NURSERY_NAME}     → Business name
{LOCATION}         → City (Doha, Al-Wakrah, Lusail)
{NURSERY_SIZE}     → "50-200 plants" or "500+ plants"
{SENDER_NAME}      → "Wiggleez Team" or individual
{SENDER_PHONE}     → +974-XXXX
{DEMO_LINK}        → Calendly link for booking
{TESTIMONIAL_NAME} → Customer name (when available)
```

## WhatsApp Message Template

**Language:** English (can localize to Arabic if needed)
**Timing:** 24-48 hours after email sent
**Format:** Keep under 160 chars for single message (or break into 2-3)

```
Template: Initial WhatsApp
"Hi {NURSERY_NAME} 👋 Saw your nursery in {LOCATION}. We help manage inventory + reach customers on WhatsApp. Interested in a quick chat? Reply here or call +974-XXXX"

Template: Follow-up WhatsApp (Day 3)
"October rush coming? Wiggleez gets you ready in 2 weeks. 15-min call to see if it fits? wa.me/974XXXX"

Template: Demo Confirmation
"Thanks! Your demo is {DATE} at {TIME}. Link: {DEMO_LINK}. Any questions, reply here 👇"
```

## Call Script Sections (See WIGGLEEZ_MESSAGING.md)

- Opener
- Discovery questions
- Value pitch
- Objection handling
- Close

## Design Approval Gate

**BEFORE sending any email/WhatsApp:**
1. Write copy ✓
2. Format (HTML if email, plain text if WhatsApp) ✓
3. Test personalization (check 1-2 sample outputs) ✓
4. **CAPTAIN APPROVAL** ← REQUIRED (reply "approved" or "revise")
5. Send batch (max 10/day to avoid spam flags)

**Who approves?** Captain (you)  
**Approval format?** Reply to brief with ✓ emoji or "approved"
