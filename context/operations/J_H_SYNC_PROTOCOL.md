---
name: J_H_SYNC_PROTOCOL
type: governance
version: 1.0.0
description: "How J and H exchange data daily for briefing delivery"
---

# J ↔ H Sync Protocol

**Purpose:** J executes tasks, H delivers briefings. They must be synchronized.  
**Sync frequency:** Twice daily (morning + evening standups)  
**Transport:** SSH rsync (encrypted, secure)  
**Data ownership:** J owns execution data, H owns delivery/metrics

---

## Daily Sync Schedule

### Morning Standup: 6:45 AM UTC+3 (15 min before 7 AM brief)

**Sequence:**
1. **J prepares intel** (6:30 AM - 6:40 AM)
   - Run market analysis skills
   - Gather Wiggleez metrics
   - Compile overnight changes
   - Write to JSON files in `~/.hermes/data/`

2. **J syncs to H** (6:40 AM - 6:43 AM)
   ```bash
   rsync -avz --delete \
     ~/.hermes/data/ \
     ~/.hermes/context/ \
     root@100.123.112.75:/data/wiggleez-operations/
   ```

3. **H processes brief** (6:43 AM - 6:58 AM)
   - Read synced data from /data/wiggleez-operations/
   - Run brief-generator-morning skill
   - Format for WhatsApp
   - Queue for 7:00 AM delivery

4. **H delivers brief** (7:00 AM UTC+3)
   - Send to Captain via WhatsApp
   - Log delivery timestamp
   - Verify receipt (check if delivered ✓ / read ✓)

5. **H syncs back to J** (7:05 AM - 7:08 AM)
   ```bash
   rsync -avz \
     root@100.123.112.75:/data/wiggleez-operations/delivery-log.json \
     ~/.hermes/context/h-delivery-status/
   ```

**If J is late (<6:45 AM):**
- H waits max 15 minutes (until 6:45 AM)
- If no sync by 6:45 AM, H uses yesterday's data + "data stale" warning
- Brief still goes out at 7:00 AM (on time is more important than perfect)

### Evening Standup: 9:00 PM UTC+3 (J ↔ H sync check)

**Sequence:**
1. **J reports daily results** (8:50 PM - 8:55 PM)
   - Emails sent count
   - WhatsApps delivered
   - Campaign responses received
   - Any errors/blockers
   - Write to `/data/j-daily-report.json`

2. **J syncs to H** (8:55 PM - 8:58 PM)
   ```bash
   rsync -avz ~/.hermes/data/j-daily-report.json \
     root@100.123.112.75:/data/wiggleez-operations/j-reports/
   ```

3. **H acknowledges** (9:00 PM - 9:02 PM)
   - Confirm receipt of report
   - Flag any missing data
   - Write `/data/h-ack.json`

4. **H syncs back to J** (9:02 PM - 9:05 PM)
   ```bash
   rsync -avz \
     root@100.123.112.75:/data/wiggleez-operations/h-ack.json \
     ~/.hermes/data/
   ```

---

## Data Files Exchanged

### J → H (Morning, before 6:43 AM)

```
~/.hermes/data/
├── wiggleez_metrics_today.json      (orders, revenue, traffic, conversion)
├── market_intel_today.json          (Qatar DSX, S&P, crypto, AI news)
├── campaign_status.json             (emails sent, responses received)
└── overnight_alerts.json            (any critical issues)

~/.hermes/context/
├── business/WIGGLEEZ_MESSAGING.md   (updated if messaging changed)
└── operations/NURSERY_CONTACTS.md   (updated if contacts added)
```

### H → J (Evening, after 7:05 AM)

```
/data/wiggleez-operations/
├── delivery_log.json                (7 AM brief: delivered? read? errors?)
└── engagement_metrics.json          (Captain opened brief? How long read?)
```

### J → H (Evening, before 8:58 PM)

```
/data/wiggleez-operations/j-reports/
└── j-daily-report.json
    {
      "date": "2026-09-18",
      "emails_sent": 10,
      "emails_delivered": 10,
      "whatsapps_sent": 8,
      "whatsapps_delivered": 8,
      "responses_received": 2,
      "calls_scheduled": 1,
      "errors": ["Gmail rate limit hit at 14:00"],
      "next_actions": ["Resume email batch at 15:00", "WhatsApp followups queued"]
    }
```

### H → J (Evening, after 9:02 PM)

```
/data/wiggleez-operations/h-ack.json
{
  "timestamp": "2026-09-18T21:02:00+03:00",
  "j_report_received": true,
  "data_complete": true,
  "issues": [],
  "ready_for_morning_brief": true
}
```

---

## Sync Failure Handling

### If J doesn't sync by 6:40 AM

**Action:**
1. H waits until 6:45 AM for retry
2. If still no sync, H checks:
   - Is Mac mini down? (ping 100.103.89.63)
   - Is J locked? (check ~/.hermes/gateway.lock)
   - Is SSH key working? (test SSH tunnel)
3. If J is down:
   - H uses yesterday's data
   - Brief goes out with "⚠️ Data from yesterday (J offline)"
   - H alerts Captain: "J offline at [time]"
4. If J is locked:
   - Wait 30 more seconds, retry sync
   - If still locked, use backup data

### If H doesn't receive sync by 6:45 AM

**Action:**
1. H tries manual SSH pull:
   ```bash
   ssh root@100.103.89.63 'cat ~/.hermes/data/wiggleez_metrics_today.json'
   ```
2. If this works, H continues with briefing
3. If SSH fails, H alerts Captain: "H-J sync failed at [time]"

### If brief delivery fails (7:00 AM)

**Action:**
1. H retries at 7:05 AM (WhatsApp queue retry)
2. If still fails, H logs error with timestamp
3. H sends Captain alert on next successful delivery: "Brief from [DATE] failed to deliver"

---

## Data Validation Rules

**Before syncing, J MUST verify:**
- ✓ All JSON files are valid (no syntax errors)
- ✓ All dates are ISO 8601 format
- ✓ No sensitive data in files (passwords, API keys)
- ✓ File sizes <10MB total (sanity check)

**H MUST verify on receipt:**
- ✓ All expected files present
- ✓ Files newer than 12 hours old
- ✓ No corruption (SHA256 hash check)

**Validation script (J runs before sync):**
```bash
#!/bin/bash
# Validate before syncing to H

for file in ~/.hermes/data/*.json; do
  if ! python3 -m json.tool "$file" >/dev/null 2>&1; then
    echo "ERROR: $file is invalid JSON"
    exit 1
  fi
done

echo "✓ All files valid, safe to sync"
```

---

## Sync Security

- **SSH key:** ~/.ssh/id_ed25519 (already loaded in ssh-agent)
- **SSH host:** root@100.123.112.75 (VPS)
- **Data encryption:** SSH tunnel (encrypted in transit)
- **No passwords:** Use public-key auth only
- **Audit:** Every sync logged with timestamp + file count

---

## Sync Monitoring

**Weekly (Sunday 8 PM):**
- Count total syncs completed: [X]/14 (2/day × 7 days)
- Count sync failures: [Y]
- Sync success rate: [X-Y]/X × 100%
- Target: >99% success rate
- If below target: Debug & report findings

**Monthly (Last day of month):**
- Total syncs: [X]/56+ (assuming 8+ syncs/day)
- Total failures: [Y]
- MTTR (mean time to recovery): [mins]
- Improvements made: [list]
