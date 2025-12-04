# ------------------------------
# Hole People Product Analysis
# Milestone 1 – Segment & Funnel Analysis + APA Stats
# ------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import f_oneway, pearsonr

save_folder = "milestone1_results"
os.makedirs(save_folder, exist_ok=True)

#  Veri Yükleme
df = pd.read_excel('hole_people_data.csv (1).xlsx')  


df.rename(columns={
    'retention_day1 (%)': 'retention_day1',
    'retention_day7 (%)': 'retention_day7',
    'levels_completed': 'level',
    'ads_watched': 'ads'
}, inplace=True)

# 4 Segment Analizleri
ads_groups = df.groupby('ads_segment')['retention_day7']
level_groups = pd.qcut(df['level'], 3, labels=['low','medium','high'])
df['level_segment'] = level_groups

# 5Funnel Analizi – Level dağılımı
funnel = df['level'].value_counts().sort_index()
funnel_percent = funnel / funnel.sum() * 100

# Görselleştirmeler
sns.set(style="whitegrid")

# Ads Segment vs Day7 Retention
plt.figure(figsize=(8,6))
sns.boxplot(x='ads_segment', y='retention_day7', data=df, palette="pastel")
plt.title("Ads Segment vs Day7 Retention")
plt.savefig(os.path.join(save_folder, "ads_segment_vs_retention_day7.png"))
plt.close()

# Level Segment vs Day7 Retention
plt.figure(figsize=(8,6))
sns.boxplot(x='level_segment', y='retention_day7', data=df, palette="muted")
plt.title("Level Segment vs Day7 Retention")
plt.savefig(os.path.join(save_folder, "level_segment_vs_retention_day7.png"))
plt.close()

# Level Funnel
plt.figure(figsize=(8,6))
sns.barplot(x=funnel.index, y=funnel_percent.values, palette="viridis")
plt.title("Level Funnel (%)")
plt.ylabel("Percentage (%)")
plt.savefig(os.path.join(save_folder, "level_funnel.png"))
plt.close()

#  APA Testleri
# ANOVA: Ads Segment vs Day7 Retention
low_ads = df[df['ads_segment']=='Low Viewer']['retention_day7']
medium_ads = df[df['ads_segment']=='Medium Viewer']['retention_day7']
high_ads = df[df['ads_segment']=='High Viewer']['retention_day7']

anova_result_ads = f_oneway(low_ads, medium_ads, high_ads)

# ANOVA: Level Segment vs Day7 Retention
low_level = df[df['level_segment']=='low']['retention_day7']
medium_level = df[df['level_segment']=='medium']['retention_day7']
high_level = df[df['level_segment']=='high']['retention_day7']

anova_result_level = f_oneway(low_level, medium_level, high_level)

# Pearson korelasyon: Ads Watched vs Day7 Retention
corr, pval = pearsonr(df['ads'], df['retention_day7'])

# 8️⃣ Sonuçları yazdır
print("ANOVA Result - Ads Segment vs Day7 Retention:", anova_result_ads)
print("ANOVA Result - Level Segment vs Day7 Retention:", anova_result_level)
print(f"Pearson correlation (ads vs retention_day7): r={corr:.2f}, p={pval:.3f}")

#  Wide Format CSV kaydet
df_wide = df.copy()
df_wide.to_csv(os.path.join(save_folder, "wide_format_data.csv"), index=False)

print(f"\nTüm görseller ve wide format CSV '{save_folder}' klasörüne kaydedildi.")
