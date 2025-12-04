import pandas as pd

# -----------------------------
# 1) DATA OKUMA
# -----------------------------
df = pd.read_excel("hole_people_full.xlsx")

# -----------------------------
# 2) RETENTION ANALYSIS
# -----------------------------
total_installs = df.shape[0]

day1_retention_count = (df["day1_play"] == 1).sum()
day7_retention_count = (df["day7_play"] == 1).sum()

day1_retention_pct = (day1_retention_count / total_installs) * 100
day7_retention_pct = (day7_retention_count / total_installs) * 100

print("=== RETENTION METRICS ===")
print("Total Installs:", total_installs)
print("Day1 Retention Count:", day1_retention_count)
print("Day7 Retention Count:", day7_retention_count)
print("Day1 Retention %:", round(day1_retention_pct, 2), "%")
print("Day7 Retention %:", round(day7_retention_pct, 2), "%")
print()

# -----------------------------
# 3) LEVEL PROGRESSION ANALYSIS
# -----------------------------
avg_level = df["level_reached"].mean()
level_counts = df["level_reached"].value_counts().sort_index()

print("=== LEVEL PROGRESSION ===")
print("Average Level Reached:", round(avg_level, 2))
print("Level Distribution:")
print(level_counts)
print()

# -----------------------------
# 4) ADS WATCHED (MONETIZATION)
# -----------------------------
avg_ads = df["ads_watched"].mean()

print("=== MONETIZATION ===")
print("Average Ads Watched per User:", round(avg_ads, 2))
print()

# -----------------------------
# 5) RAPORU EXCEL'E KAYDETME
# -----------------------------
output = pd.DataFrame({
    "Metric": [
        "Total Installs",
        "Day1 Retention %",
        "Day7 Retention %",
        "Average Level Reached",
        "Average Ads Watched"
    ],
    "Value": [
        total_installs,
        round(day1_retention_pct, 2),
        round(day7_retention_pct, 2),
        round(avg_level, 2),
        round(avg_ads, 2)
    ]
})

output.to_excel("hole_people_results.xlsx", index=False)
print("Results saved to hole_people_results.xlsx")
