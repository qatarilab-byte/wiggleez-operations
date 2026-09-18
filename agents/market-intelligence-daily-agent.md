---
name: market-intelligence-daily-agent
type: agent
version: 1.0.0
---

# AGENT: Market Intelligence Daily

Run all market analysis skills and compile intel for morning brief.

## Steps (In Order)

1. **Qatar DSX** — Run market-analysis-qatar-dsx skill
2. **Global stocks** — Run market-analysis-global-stocks skill
3. **Crypto** — Run market-analysis-crypto skill
4. **AI tools** — Run ai-tools-hunter skill
5. **Compile** — Write results to data/market_indicators_daily.csv

## Output

JSON file with all market indicators, ready for brief formatting.

## Running

```bash
python3 agents/market-intelligence-daily-agent.py
```
