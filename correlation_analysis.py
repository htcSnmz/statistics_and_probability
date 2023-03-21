# Korelasyon Anlamlılığı Testi
# H0: ρ = 0 (Değişkenler arasında korelasyon yoktur.)
# H1: ρ != 0 (Değişkenler arasında korelasyon vardır.)
# İki değişken için de normallik varsayımı
# Varsayım sağlanıyorsa Pearson Korelasyon Katsayısı
# Varsayım sağlanmıyorsa Spearman Korelasyon Katsayısı ya da Kendall Tau Korelasyon Katsayısı


# Bahşiş ile ödenen hesap arasında korelasyon var mı?
# H0: ρ = 0
# H1: ρ != 0
import pandas as pd
import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()
df.head()
df["total_bill"] = df["total_bill"] - df["tip"]
df.head()
df["tip"].corr(df["total_bill"])    # Pearson korelasyon katsayısı: 0.5766634471096374
# corr() fonksiyonu varsayılan olarak Pearson Korelasyon Katsayısı'nı hesaplar.
# method argümanı ile bu yöntem değiştirilebilir.


# Varsayım Kontrolü
from scipy import stats
stats.shapiro(df["tip"])        # pvalue=8.200817629144819e-12
stats.shapiro(df["total_bill"]) # pvalue=1.1060685700670092e-10
# Normallik varsayımları sağlanmamaktadır.
df["tip"].corr(df["total_bill"], method="spearman") # Normallik sağlanmadığı için. Spearman korelasyon katsayısı: 0.593691939408997


# Korelasyon Anlamlılığı Testi
# Normallik varsayımı sağlansaydı parametrik test (Pearson):
stats.stats.pearsonr(df["tip"], df["total_bill"])
# PearsonRResult(statistic=0.5766634471096381, pvalue=5.018290084948419e-23)
# pvalue < 0.05 --> H0 red.

# Normallik varsayımı sağlanmadığında nonparametrik test (Spearman):
corr, pvalue = stats.spearmanr(df["tip"], df["total_bill"])
print(f"Korelasyon katsayısı: {corr}, pvalue: {pvalue}")
# Korelasyon katsayısı: 0.593691939408997, pvalue: 1.2452285137560276e-24
# pvalue < 0.05 --> H0 red.

# (Kendall Tau)
corr, pvalue = stats.kendalltau(df["tip"], df["total_bill"])
print(f"Korelasyon katsayısı: {corr}, pvalue: {pvalue}")
# Korelasyon katsayısı: 0.4400790074919885, pvalue: 7.131027725873621e-24