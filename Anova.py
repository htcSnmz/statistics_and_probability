# İkiden fazla grup için
# !!! Normallik ve varyans homojenliği varsayımı.

import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import MultiComparison

# Günlere göre ödenen hesap ortalamaları arasında anlamlı bir farklılık var mı ?
df = sns.load_dataset("tips")
df.head()
df.groupby("day")["total_bill"].mean()

# 1) Hipotez
# H0: M1 = M2 = M3 = M4
# H1: En az bir tanesi farklıdır.

# 2) Varsayım kontrolü
# Varsayım sağlanıyorsa one way anova
# Varsayım sağlanmıyorsa kruskal

# Normallik varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
for group in list(df["day"].unique()):
    pvalue = stats.shapiro(df.loc[df["day"] == group, "total_bill"])[1]
    print(group, "p-value= %.4f" % pvalue)
# Her bir grup p-value < 0.05'tir.

# Varyans homojenliği varsayımı
# H0: Varyanslar homojendir.
# H0: Varyanslar homojen değildir.
test_stat, pvalue = stats.levene(df.loc[df["day"] == "Sun", "total_bill"],
                                 df.loc[df["day"] == "Sat", "total_bill"],
                                 df.loc[df["day"] == "Thur", "total_bill"],
                                 df.loc[df["day"] == "Fri", "total_bill"])
print("Test Stat= %.4f, p-value= %.4f" % (test_stat, pvalue)) # p-value= 0.5741 => H0 REDDEDİLEMEZ. Varyanslar homojendir.

# 3) Hipotez testi
# Normallik varsayımı sağlanmadığı için non parametrik test kullanılacak ancak parametrik testi de deneyeceğiz.

# Parametrik anova testi
stats.f_oneway(df.loc[df["day"] == "Sun", "total_bill"],
                df.loc[df["day"] == "Sat", "total_bill"],
                df.loc[df["day"] == "Thur", "total_bill"],
                df.loc[df["day"] == "Fri", "total_bill"])
# F_onewayResult(statistic=2.7674794432863363, pvalue=0.04245383328951916)

# Nonparametrik anova testi
stats.kruskal(df.loc[df["day"] == "Sun", "total_bill"],
                df.loc[df["day"] == "Sat", "total_bill"],
                df.loc[df["day"] == "Thur", "total_bill"],
                df.loc[df["day"] == "Fri", "total_bill"])
# KruskalResult(statistic=10.403076391436972, pvalue=0.015433008201042065)

# Farklılık hangi gruptan kaynaklanmaktadır.
comparasion = MultiComparison(df["total_bill"], df["day"])
tukey = comparasion.tukeyhsd(0.05)
print(tukey.summary())
# reject: H0 red mi ?
"""
Multiple Comparison of Means - Tukey HSD, FWER=0.05 
====================================================
group1 group2 meandiff p-adj   lower   upper  reject
----------------------------------------------------
   Fri    Sat   3.2898 0.4541 -2.4799  9.0595  False
   Fri    Sun   4.2584 0.2371 -1.5856 10.1025  False
   Fri   Thur   0.5312 0.9957 -5.4434  6.5057  False
   Sat    Sun   0.9686 0.8968 -2.6088   4.546  False
   Sat   Thur  -2.7586 0.2374 -6.5455  1.0282  False
   Sun   Thur  -3.7273 0.0668 -7.6264  0.1719  False
----------------------------------------------------
"""