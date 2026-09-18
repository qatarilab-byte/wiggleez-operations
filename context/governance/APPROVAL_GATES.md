---
name: APPROVAL_GATES
type: governance
version: 1.0.0
description: "What needs Captain approval before execution"
---

# Approval Gates & Decision Authority

**Purpose:** Ensure Captain maintains control over high-risk/high-impact decisions  
**Approval format:** Reply to brief with ✓ emoji or "approved"  
**Max wait time:** 2 hours (if no response, J proceeds with caution)

---

## Tier 1: CRITICAL (Always Ask Captain)

| Decision | Who decides | Timeline | How |
|---|---|---|---|
| **Send email to >10 contacts** | Captain | Before send | Captain approves copy + list |
| **Send WhatsApp to any contact** | Captain | Before send | Captain approves message + recipients |
| **Post to Instagram/social** | Captain | Before post | Captain approves design + caption |
| **Change pricing** | Captain | Before update | Captain approves new price |
| **Partner with company** | Captain | Before signing | Captain approves terms |
| **Spend >50 QAR on new service** | Captain | Before purchase | Captain approves justification + ROI |

**How to ask:**
```
📋 APPROVAL NEEDED
Copy: [email text]
Recipients: [list]
Estimated response: [X%]
ROI expectation: [Y]

Approve? Reply ✓ or suggest changes.
```

---

## Tier 2: OPERATIONAL (Ask, Proceed After 2h Timeout)

| Decision | Who decides | Timeline | How |
|---|---|---|---|
| **Retry failed email** | J | After 1st failure | J retries, informs Captain in daily report |
| **Adjust email time** | J | If performance low | J changes send time, tests, reports results |
| **Skip a contact** | J | If email bounces | J removes from list, logs reason |
| **Extend campaign by 1 week** | J | If <30% response | J extends, informs Captain |
| **Use backup API** | J | If primary API down | J switches, logs incident |

**How to ask:**
```
📋 INFO: Email to [contact] bounced (invalid address). Removing from list.
Will update campaign_tracking.csv.
```

---

## Tier 3: ROUTINE (J Decides)

| Decision | Who decides | Timeline | How |
|---|---|---|---|
| **Send 1-5 emails** | J | Daily | J sends, logs in daily report |
| **Update contact info** | J | As needed | J updates NURSERY_CONTACTS.md |
| **Log response** | J | When received | J updates campaign_tracking.csv |
| **Reschedule call** | J | If contact asks | J reschedules, updates tracking |
| **Run market analysis** | J | Daily 6 AM | J runs, includes in brief |
| **Update briefing data** | J | Daily 6 AM | J gathers data, H formats |

---

## Special: Design Approval (Pre-Canva)

**BEFORE creating or posting ANY design:**

1. **Write copy** (what the design should say)
2. **Describe design** (layout, colors, elements)
3. **Ask Captain:**
   ```
   🎨 DESIGN APPROVAL
   Platform: Instagram
   Copy: [text]
   Design: [description]
   
   Approve? Or changes?
   ```
4. **Only after ✓:** Create in Canva and post

---

## Escalation Path

**If Captain doesn't respond within 2 hours:**

```
Tier 1 (critical): WAIT. Do not proceed. Alert Captain again at 3h.
Tier 2 (operational): Proceed with caution. Log decision. Report in daily brief.
Tier 3 (routine): Proceed normally.
```

**If urgent and Captain still no response:**
```
1. Try WhatsApp (quicker than email)
2. If still no response at 4h: Proceed, note "Captain unavailable"
3. Report fully in next daily brief with photos/evidence
```

---

## Decision Log

**Every Captain decision logged to:** `~/.hermes/docs/DECISION_LOG.md`

```markdown
## 2026-09-18

### Decision 1: Email to 10 nurseries approved
- **Time:** 07:00 UTC+3
- **Content:** Intro email (see EMAIL_TEMPLATES.md)
- **Recipients:** Segment A (5 contacts)
- **Captain approval:** ✓ (approved at 06:58)
- **Outcome:** [Pending - will update on response]

### Decision 2: Instagram post approved
- **Time:** 14:00 UTC+3
- **Content:** Back-to-school campaign
- **Design:** [Link to Canva]
- **Captain approval:** ✓ (approved at 13:55)
- **Posted:** 14:05 UTC+3
- **Engagement:** [TBD]
```

---

## Monthly Approval Summary

**Last day of month:** Captain reviews ALL decisions made that month

```
September 2026 Decisions:
- Total requests: 45
- Approved: 44 (98%)
- Modified: 1 (2%)
- Declined: 0 (0%)
- Timeout (proceeded anyway): 0
- Outcomes:
  - Email campaigns: 3 (total 30 emails sent)
  - Social posts: 8 (total 16 posts)
  - Budget decisions: 2
  - Partnership decisions: 0
```

---

## If Captain Declines a Decision

**J action:**
1. Acknowledge: "Understood. Not proceeding with [decision]."
2. Ask for feedback: "Want me to modify and re-submit?"
3. Log decline: `DECISION_LOG.md` shows "Captain declined: [reason]"
4. Adjust approach for next time

---

## Trust Building

Over time, if Tier 1 decisions have 100% positive outcomes:
- Tier 1 can shift to Tier 2 (J notifies, Captain approves in daily brief)
- Tier 2 can shift to Tier 3 (J decides, logs in brief)
- This requires 30 days of zero errors

**Reset to Tier 1 if:**
- A decision leads to negative outcome (customer complaint, wasted budget, etc.)
- Captain requests it
