# !!! n1>30 ve n2>30 şartı vardır.

import pandas as pd
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








# # UYGULAMA 3: Yeni tasarımın dönüşüm oranı ile eski tasarımın dönüşüm oranı arasında ist. ol. an. fark var mı?
# Veri Seti
# Grup Değişkeni: Deneysel, Kontrol
# Sayfa Değişkeni: Yeni Tasarım, Eski Tasarım
# Satış Değişkeni: 1, 0
# # H0: P1 = P2
# # H1: P1 != P2
data = pd.read_excel("datasets/ornekAB.xlsx")
data.head()
kontrol = data[data["Grup"] == "Kontrol"].sample(n=5000, random_state=42)
deneysel = data[data["Grup"] == "Deneysel"].sample(n=5000, random_state=42)
new_data = pd.concat([kontrol, deneysel], axis=0)
new_data = new_data.reset_index(drop=True)
new_data.head()
new_data.groupby("Grup").mean()
# Deneysel  0.1198
# Kontrol   0.1318
kontrol_satis = new_data[new_data["Grup"] == "Kontrol"]["Satış"]
deneysel_satis = new_data[new_data["Grup"] == "Deneysel"]["Satış"]
basari_kontrol = [kontrol_satis.sum(), deneysel_satis.sum()]
gozlem = [kontrol_satis.count(), deneysel_satis.count()]
test_stat, pvalue = proportions_ztest(count=basari_kontrol, nobs=gozlem)
print("Test Stat= %.4f, p-value= %.4f" % (test_stat, pvalue)) # p-value= 0.0704 --> H0 REDDEDİLEMEZ.
# Yeni tasarımın satış oranları üzerinde ist. ol. anlamlı bir etkisi yoktur.
