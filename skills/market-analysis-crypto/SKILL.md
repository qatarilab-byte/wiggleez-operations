# SKILL: Market Analysis — Crypto

Track Bitcoin, Ethereum, and DeFi volatility.

## What It Does

Monitor major crypto assets for volatility + volume spikes.

## Inputs

- None (public APIs like CoinMarketCap)

## Outputs

- market_intel_crypto.json
- Alert if >10% daily move on major coins

## Steps

1. Fetch BTC, ETH, top 10 coins
2. Calculate 24h % change
3. Check volume
4. Write to JSON with timestamp

## Notes

Update daily 6:00 AM before syncing to H.
