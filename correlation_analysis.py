# Korelasyon Anlamlılığı Testi
# H0: ρ = 0 (Değişkenler arasında korelasyon yoktur.)
# H1: ρ != 0 (Değişkenler arasında korelasyon vardır.)
# İki değişken için de normallik varsayımı
# Varsayım sağlanıyorsa Pearson Korelasyon Katsayısı
# Varsayım sağlanmıyorsa Spearman Korelasyon Katsayısı ya da Kendall Tau Korelasyon Katsayısı

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pingouin as pg

# Bahşiş ile ödenen hesap arasında korelasyon var mı?
# H0: ρ = 0
# H1: ρ != 0

tips = sns.load_dataset("tips")
df = tips.copy()
df.head()
df["total_bill"] = df["total_bill"] - df["tip"]
df.head()
df["tip"].corr(df["total_bill"])    # Pearson korelasyon katsayısı: 0.5766634471096374
# corr() fonksiyonu varsayılan olarak Pearson Korelasyon Katsayısı'nı hesaplar.
# method argümanı ile bu yöntem değiştirilebilir.


# Varsayım Kontrolü
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



# with pingouin lib.
##################################################################################################

# Sıcaklık ile dondurma satış adetleri arasında korelasyon var mıdır?
# H0: ρ = 0 (Değişkenler arasında korelasyon yoktur.)
# H1: ρ != 0 (Değişkenler arasında korelasyon vardır.)
df = pd.read_excel("datasets/ice_cream_sales.xlsx")
df.head()

# Varsayım Kontrolü
pg.normality(df)
#                       W      pval  normal
# Sıcaklık       0.975931  0.962042    True
# DondurmaSatış  0.961593  0.806313    True

sns.lmplot(x="Sıcaklık", y="DondurmaSatış", data=df, ci=None)
plt.show()

corr = pg.corr(df["Sıcaklık"], df["DondurmaSatış"], method="pearson")
print(corr)
#           n         r         CI95%     p-val       BF10     power
# pearson  12  0.957507  [0.85, 0.99]  0.000001  1.102e+04  0.999953
# r = 0.957507 --> güçlü pozitif ilişki
# p-val = 0.000001 --> H0 reddedilir. (Değişkenler arasında korelasyon vardır.)

##################################################################################################

df = pd.read_excel("datasets/corr_ornek.xlsx")
df.head()

# Varsayım Kontrolü
pg.normality(df)
#           W      pval  normal
# A  0.968391  0.869842    True
# B  0.792429  0.007479   False

sns.lmplot(x="A", y="B", data=df)
plt.show()

corr = pg.corr(df["A"], df["B"], method="spearman")
print(corr)
#            n         r           CI95%     p-val     power
# spearman  11 -0.918182  [-0.98, -0.71]  0.000067  0.995623
