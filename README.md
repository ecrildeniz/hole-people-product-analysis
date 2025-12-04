
# Hole People — Product Analysis

**Author:** Ecril Deniz  
**Role targeted:** Product Intern — Rollic

## Summary
This repository contains a small product analytics case study for the hyper-casual game *Hole People*. It includes:
- `analysis.py` — Python script using pandas to compute retention, level progression, and ad-watching metrics.
- `hole_people_full.xlsx` — Simulated 100-player dataset.
- `hole_people_results.xlsx` — Summary output produced by the script.

## Key findings
- **Day1 Retention:** 61% — strong FTUE.
- **Day7 Retention:** 15% — heavy drop during first week.
- **Average Level Reached:** 4.53 — early drop-offs (33% of users at level 1).
- **Average Ads Watched:** 1.2 per user.

## Recommendations
1. Improve early level pacing and add small early-session rewards to increase Day1→Day7 conversion.
2. Introduce short progression (Hole Upgrades / daily challenges) to extend session depth.
3. Run small A/B tests on onboarding & reward mechanics; track Day1/Day7 retention and session length.

## How to reproduce
1. Install dependencies: `pip install pandas openpyxl matplotlib`  
2. Run: `python analysis.py`  
3. Outputs: `hole_people_results.xlsx` and printed summary.

## License
MIT
