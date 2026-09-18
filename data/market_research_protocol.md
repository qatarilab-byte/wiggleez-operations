# Qatar DSX Market Research Protocol
## Daily Research for Solid Market Intelligence

---

## SOURCES (Verified, Official)
1. **qatar-stock-exchange.com.qa** — Official DSX announcements
2. **qatar-news.com** — Market news
3. **gulf-times.com** — Business section
4. **peninsula.com.qa** — Local news
5. **arabianbusiness.com** — Regional market intelligence
6. **dohanews.co** — Business community news

---

## DAILY RESEARCH CHECKLIST

### Morning (6:30 AM)
- [ ] Visit QSE official website
- [ ] Check DSX index movement (last 24h, last week, last month)
- [ ] Search: New contract announcements
- [ ] Search: CEO/board leadership changes
- [ ] Search: M&A activity (who's buying, who's selling)
- [ ] Document: EXACT dates, company names, amounts

### Key Data Points to Track
```
Date: [YYYY-MM-DD]
Company: [Name]
Type: [Contract/Leadership/M&A/IPO/Funding]
Details: [What exactly happened]
Amount: [QAR/USD if applicable]
Source: [Which website, article link]
Impact: [Why this matters for business opportunities]
Action: [What business can do with this info]
```

### Example (What Good Research Looks Like)
```
Date: 2026-09-18
Company: Doha Bank
Type: Leadership change
Details: New CEO appointed, Ali Al-Marri (ex-Qatar National Bank)
Amount: N/A
Source: qatar-stock-exchange.com.qa
Impact: Indicates expansion into retail/corporate banking
Action: Opportunity for fintech partnerships, corporate tech sales
```

---

## WHAT NOT TO DO
- ❌ Don't guess or assume
- ❌ Don't use old news
- ❌ Don't miss dates
- ❌ Don't forget sources
- ❌ Don't skip verification

---

## OUTPUT FORMAT
Every morning, create: `data/qatar_dsx_research_[DATE].json`

```json
{
  "date": "2026-09-19",
  "dsx_index": {"current": 10850, "change": 0.15, "trend": "up"},
  "contracts": [
    {
      "company": "Qatar Petroleum",
      "type": "Government contract",
      "details": "New offshore drilling contract signed",
      "amount": "500M QAR",
      "date": "2026-09-19",
      "source": "qatar-stock-exchange.com.qa",
      "business_opportunity": "Supply chain vendors needed"
    }
  ],
  "leadership_changes": [...],
  "mergers_acquisitions": [...],
  "sector_trends": [...],
  "investment_alerts": [...]
}
```

---

## MONEY RULE
**Every investment decision backed by this research = VERIFIED, DATED, SOURCED**
**No guessing. No losses from bad intel.**

