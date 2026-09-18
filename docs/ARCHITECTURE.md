# System Architecture

## Data Flow

```
J (Mac mini) ────rsync───→ H (VPS)
     ↑                        ↓
  Execute             Format + Deliver
  Tasks          (7 AM brief to Captain)
     ↑                        ↓
  Market           Captain Reviews
  Analysis         & Approves
```

## Morning Cycle (6:00 AM - 7:00 AM)

1. **6:00-6:30:** J gathers intel (market analysis, Wiggleez metrics)
2. **6:30-6:40:** J compiles data into JSON files
3. **6:40-6:43:** J syncs to H via rsync
4. **6:43-6:58:** H processes data, formats brief
5. **7:00:** H delivers brief to Captain via WhatsApp

## Evening Cycle (8:50 PM - 9:05 PM)

1. **8:50-8:55:** J logs daily results
2. **8:55-8:58:** J syncs to H
3. **9:00-9:02:** H acknowledges receipt
4. **9:02-9:05:** H syncs confirmation back to J

## Campaign Workflow

```
Day 0: Email sent
       ↓
Day 2: WhatsApp follow-up
       ↓
Day 2-9: Monitor responses
         ↓
Day 7+: Schedule demo calls
        ↓
Day 8-14: Conduct 15-min calls
          ↓
Day 15+: Onboard converted customers
```

## Approval Gates

- **Tier 1 (Ask first):** Email >10, WhatsApp any, social posts, spend >50 QAR
- **Tier 2 (Ask, proceed if timeout):** Retries, time adjustments, contact removals
- **Tier 3 (J decides):** Single emails, response logging, rescheduling

## Data Ownership

- **J owns:** Execution data (emails sent, WhatsApp delivered, responses received)
- **H owns:** Delivery data (brief delivered timestamp, read receipt)
- **Both sync:** Market intel, Wiggleez metrics, campaign status
