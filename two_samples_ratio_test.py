# !!! n1>30 ve n2>30 şartı vardır.

import numpy as np
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest

# UYGULAMA 1: Yeni tasarımın dönüşüm oranı ile eski tasarımın dönüşüm oranı arasında ist. ol. an. fark var mı?

# H0: P1 = P2
# H1: P1 != P2

basari_sayilari = np.array([300, 250])
gozlem_sayilari = np.array([1000, 1100])
proportions_ztest(count=basari_sayilari, nobs=gozlem_sayilari) # (3.7857863233209255, 0.0001532232957772221) => H0 REDDEDİLİR.
basari_sayilari / gozlem_sayilari




# UYGULAMA 2: Titanic veri setindeki kadın ve erkeklerin hayatta kalma oranları arasında ist. ol. an. fark var mı?
# H0: P1 = P2
# H1: P1 != P2
df = sns.load_dataset("titanic")
df.head()
df.loc[df["sex"] == "female", "survived"].mean()
df.loc[df["sex"] == "male", "survived"].mean()
female_cucc_count = df.loc[df["sex"] == "female", "survived"].sum()
male_cucc_count = df.loc[df["sex"] == "male", "survived"].sum()
test_stat, pvalue = proportions_ztest(count=[female_cucc_count, male_cucc_count],
                                      nobs=[df.loc[df["sex"] == "female", "survived"].shape[0],
                                            df.loc[df["sex"] == "male", "survived"].shape[0]])
print("Test Stat= %.4f, p-value= %.4f" % (test_stat, pvalue)) # p-value= 0.0000 => H0 REDDEDİLİR.