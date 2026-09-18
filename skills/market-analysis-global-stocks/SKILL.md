# SKILL: Market Analysis — Global Stocks

Monitor S&P 500 + global market indices for trends.

## What It Does

Track S&P 500, tech sector, and global market movements.

## Inputs

- None (public APIs)

## Outputs

- market_intel_global_stocks.json
- Highlight significant moves (>2% daily, >5% weekly)

## Steps

1. Fetch S&P 500 + tech sector data
2. Calculate % change
3. Identify winners/losers
4. Write to JSON with timestamp

## Notes

Update daily 6:00 AM before syncing to H.
