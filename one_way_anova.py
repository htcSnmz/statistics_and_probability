# Her bir grup verisi normal dağılım göstermeli ya da n >= 30
# Normal dağılım sağlanıyorsa One Way F Testi, sağlanmıyorsa Welch's Anova Testi  ya da Kruskal Testi kullanılabilir.
# Anova testi sonucunda anlamlı farklılık çıkarsa, farklılığın hangi gruplar arasında olduğunu test etmek için Post Hoc Analizi uygulanır.
# Varyanslar homojense Post Hoc Analizi için Tukey Testi, homojen değilse Tamhane Testi kullanılır.
# Gözlemler rassal seçilmedilir.

from scipy import stats
import pandas as pd

# One Way Anova için Basit Örnek
grupA = [1, 2, 3, 6]
grupB = [1, 3, 5, 7]
grupC = [2, 4, 6, 8]
# H0: MA = MB = MC
# H1: En az bir tanesi farklıdır.
f_stats, pvalue = stats.f_oneway(grupA, grupB, grupC)
f_stats, pvalue  # p value: 0.5370433168702269

#######################################################################################################################

# Eğitim düzeyi ile Tv izleme süreleri arasında ist. ol. anl. fark var mıdır?
data = pd.read_excel("datasets/tv_time.xlsx")
data.head()
ilkokul = data[data["Eğitim"] == "İlkokul"]["Tv İzleme"]
lise = data[data["Eğitim"] == "Lise"]["Tv İzleme"]
univ = data[data["Eğitim"] == "Üniversite"]["Tv İzleme"]
yl = data[data["Eğitim"] == "Yüksek Lisans"]["Tv İzleme"]

# Normallik Kontrolü
# H0: Veriler normal dağılım göstermektedir.
# H1: Veriler normal dağılım göstermemektedir.
stats.shapiro(ilkokul)  # pvalue=0.4409874379634857
stats.shapiro(lise)     # pvalue=0.34658148884773254
stats.shapiro(univ)     # pvalue=0.4002574682235718
stats.shapiro(yl)       # pvalue=0.16459572315216064
# Her grup için normallik varsayımı sağlanmaktadır.

# Varyans Homojenliği Kontrolü
# H0: Varyans homojenliği sağlanmaktadır.
# H1: Varyans homojenliği sağlanmamaktadır.
stats.bartlett(ilkokul, lise, univ, yl)     # pvalue=0.9342671027651219
# pvalue > 0.05 -- > H0 Reddedilemez. Varyans homojenliği sağlanmaktadır.

# Hipotez Testi
stats.f_oneway(ilkokul, lise, univ, yl)     # pvalue=0.9342671027651219
# pvalue > 0.05 H0 Reddedilemez. Gruplar arası anlamlı fark vardır.

# Post Hoc Analizi
# Farklılık hangi gruplardan kaynaklanıyor?
# Varyanslar homojen ise Tukey testi, değilse Tamhane Testi
from statsmodels.stats.multicomp import pairwise_tukeyhsd
posthoc = pairwise_tukeyhsd(endog=data["Tv İzleme"], groups=data["Eğitim"])
print(posthoc)
"""
Multiple Comparison of Means - Tukey HSD, FWER=0.05        
===================================================================
    group1        group2    meandiff p-adj   lower    upper  reject
-------------------------------------------------------------------
         Lise Yüksek Lisans     -9.0 0.3867 -24.7226  6.7226  False
         Lise    Üniversite     10.0 0.3005  -5.7226 25.7226  False
         Lise       İlkokul     11.0 0.2283  -4.7226 26.7226  False
Yüksek Lisans    Üniversite     19.0 0.0154   3.2774 34.7226   True
Yüksek Lisans       İlkokul     20.0 0.0107   4.2774 35.7226   True
   Üniversite       İlkokul      1.0 0.9978 -14.7226 16.7226  False
-------------------------------------------------------------------
"""
# Tabloya göre Yüksek Lisans ve Üniversite, Yüksek Lisans ve İlkokul arasında anlamlı bir fark vardır.

data.groupby("Eğitim").mean()
#               Tv İzleme
# Eğitim
# Lise                  62
# Yüksek Lisans         53
# Üniversite            72
# İlkokul               73

# Varyansların homojen olmadığını varsayalım (Welch's Anova testi)
# !pip install pingouin
import pingouin as pg
test = pg.welch_anova(data=data, dv="Tv İzleme", between="Eğitim")
print(test) # p-unc 0.033

# Varyanslar homojen olmadığı için Post Hoc Analizi için Tamhane testi
# pip install scikit-posthoc
import scikit_posthocs as sp
tamhane = sp.posthoc_tamhane(data, val_col="Tv İzleme", group_col="Eğitim")
print(tamhane)
"""
                İlkokul    Lise     Üniversite      Yüksek Lisans
İlkokul        1.000000  0.249431    0.999679       0.038531
Lise           0.249431  1.000000    0.295004       0.420232
Üniversite     0.999679  0.295004    1.000000       0.044404
Yüksek Lisans  0.038531  0.420232    0.044404       1.000000
"""
# 0.05'in altında olanlar arasında anlamlı farklılık vardır. (Yüksek Lisans ve İlkokul, Yüksek Lisans ve Üniversite)

#######################################################################################################################

# Anasayfa İçerik Stratejisi Belirlemek
# Problem: Anasayfada geçirilen süre arttırılmak isteniyor.
# Detaylar:
    # Bir web sitesi için başarı kriterleri: ortalama ziyaret süresi, hemen çıkış oranı vb.
    # Uzun zaman geçiren kullanıcıların reklamlara daha fazla tıkladığı ve markaya olan bağlılıklarının arttığı biliniyor.
    # Buna yönelik olarak benzer haberler farklı resimler ya da farklı formatlarda hazırlanarak oluşturulan test gruplarına gösteriliyor.
    # A: Doğal Şekilde      B: Yönlendirici     C: İlgi Çekici

A = pd.DataFrame([28, 33, 30, 29, 28, 29, 27, 31, 30, 32, 28, 33, 25, 29, 27, 31, 31, 30, 31, 34, 30, 32, 31])
B = pd.DataFrame([31, 32, 30, 30, 33, 32, 34, 27, 36, 30, 31, 30, 38, 29, 30, 34, 34, 31, 35, 35, 33, 30, 28])
C = pd.DataFrame([40, 33, 38, 41, 42, 43, 38, 35, 39, 39, 36, 34, 35, 40, 38, 36, 39, 36, 33, 35, 38, 35, 40])
dfs = [A, B, C]
ABC = pd.concat(dfs, axis=1)
ABC.columns = ["A", "B", "C"]
ABC.head()

# Normallik Varsayımı Kontrolü
# H0: Veriler normal dağılım göstermektedir.
# H1: Veriler normal dağılım göstermemektedir.
stats.shapiro(ABC["A"])     # pvalue=0.8526690006256104
stats.shapiro(ABC["B"])     # pvalue=0.5784821510314941
stats.shapiro(ABC["C"])     # pvalue=0.4721103310585022
# pvalues < 0.05 --> 3 grup için de normallik varsayımı sağlanmaktadır

# Varyans Homojenliği Kontrolü
# H0: Varyans homojenliği sağlanmaktadır.
# H1: Varyans homojenliği sağlanmamaktadır.
stats.levene(ABC["A"], ABC["B"], ABC["C"])     # pvalue=0.39399787531140673
# pvalue > 0.05 --> H0 Reddedilemez. Varyans homojenliği sağlanmaktadır.

# Hipotez Testi
# H0: MA = MB = MC
# H1: En az bir tanesi farklıdır.
stats.f_oneway(ABC["A"], ABC["B"], ABC["C"])
print('{:.5f}'.format(stats.f_oneway(ABC["A"], ABC["B"], ABC["C"])[1])) # pvalue=0.00000
# pvalue < 0.05 --> H0 Reddedilir. Web sitelerinde geçirilen süreler arasında anlamlı farklılık vardır.
ABC.describe().T

# Varsayımlar sağlanmasaydı Anova için Kruskal Testi
stats.kruskal(ABC["A"], ABC["B"], ABC["C"])     # pvalue=1.014190318754816e-09