# Troubleshooting Guide

## Common Issues

### Email send fails (Gmail rate limit)

**Symptom:** `429 Too Many Requests`

**Fix:**
1. Wait 1 hour for rate limit reset
2. Resume batch at Day 1 instead of Day 0
3. Update campaign_tracking.csv with delay note

### WhatsApp delivery timeout

**Symptom:** Message queued but not delivered after 5 min

**Fix:**
1. Check phone number format (must include country code +974)
2. Verify contact has WhatsApp account
3. Retry once, then mark as "delivery_failed"
4. Remove from active list, add to "retry_next_week"

### Brief delivery fails (H offline)

**Symptom:** 7 AM brief doesn't arrive by 7:05 AM

**Fix:**
1. H waits max 15 min for J sync (until 6:45 AM)
2. If no sync, H uses yesterday's data + "⚠️ Data stale" warning
3. Brief still goes out at 7:00 AM (on-time > perfect)
4. Log incident to /docs/INCIDENTS.md

### J ↔ H sync fails (SSH error)

**Symptom:** `ssh: Permission denied (publickey)`

**Fix:**
1. Check SSH key: `ls -la ~/.ssh/id_ed25519`
2. Check VPS authorized_keys: Ask Captain to add pub key
3. Fallback: Use Tailscale IP instead of direct SSH
4. Manual sync: Captain copies data via scp

### Campaign contact is invalid (bad email)

**Symptom:** Email bounces with `user unknown`

**Fix:**
1. Remove from NURSERY_CONTACTS.md
2. Log to campaign_tracking.csv: `status=invalid_email`
3. Move to dead-letter list for Q1 2027 re-validation

---

## Who To Ask

| Issue | Owner |
|-------|-------|
| Email/Gmail | J (execute), Captain (approve) |
| WhatsApp | J (execute), Captain (approve) |
| Market intel | J (run skills) |
| Brief delivery | H (check sync) |
| Contact data | Captain (verify sources) |
| System down | J (diagnose), Captain (escalate) |

---

## Incident Reporting

When something breaks:

1. **Log timestamp + symptoms**
2. **Note what was being executed**
3. **List remediation steps taken**
4. **Report in next daily brief**
5. **Append to /docs/INCIDENTS.md**
