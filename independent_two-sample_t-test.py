# !!! Normallik ve Varyans Homojenliği Varsayımı olmalıdır.
import seaborn as sns
from scipy import stats
import pandas as pd

# UYGULAMA 1: Sigara içenler ile içmeyenlerin hesap ortalamaları arasında istatistiksel olarak anlamlı bir fark var mı?
# Is there a statistically significant difference between the bill averages of smokers and non-smokers?
df = sns.load_dataset("tips")
df.head()
df.groupby("smoker").agg({"total_bill": "mean"})

# 1: Hipotez
# H0: M1 = M2
# H1: M1 != M2

# 2: Varsayım kontrolü
# Normal dağılım varsaıymı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
test_stat, pvalue = stats.shapiro(df.loc[df["smoker"] == "Yes", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))  # Test Stat = 0.9367, p-value = 0.0002 => H0 RED.
test_stat, pvalue = stats.shapiro(df.loc[df["smoker"] == "No", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 0.9045, p-value = 0.0000 => H0 RED.
# Normallik varsayımı sağlanmadığından direkt non-parametrik teste geçilebilir.

# Varyans homojenliği varsayımı
# H0: Varyanslar homojendir.
# H1: Varyanslar homojen değildir.
test_stat, pvalue = stats.levene(df.loc[df["smoker"] == "Yes", "total_bill"],
                                 df.loc[df["smoker"] == "No", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 4.0537, p-value = 0.0452 => HO RED.

# 3: Hipotezin uygulanması
# Varsayımlar sağlansaydı (parametrik test)
test_stat, pvalue = stats.ttest_ind(df.loc[df["smoker"] == "Yes", "total_bill"],
                                    df.loc[df["smoker"] == "No", "total_bill"],
                                    equal_var=True)
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 1.3384, p-value = 0.1820 => H0 REDDEDİLEMEZ.

# Varsayımlar sağlanmıyor (non-parametrik test)
test_stat, pvalue = stats.mannwhitneyu(df.loc[df["smoker"] == "Yes", "total_bill"],
                                        df.loc[df["smoker"] == "No", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 7531.5000, p-value = 0.3413 => H0 REDDEDİLEMEZ.










# UYGULAMA 2: Titanic kadın ve erkek yolcuların yaş ortalaması arasında ist. olarak. anlamlı bir farklılık var mı?
# Is there a statistically significant difference between the age averages of male and female in titanic ?
df = sns.load_dataset("titanic")
df.head()
df.groupby("sex").agg({"age": "mean"})

# 1: Hipotez
# H0: M1 = M2
# H1: M1 != M2

# 2: Varsayım kontrolü
# Normal dağılım varsaıymı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
test_stat, pvalue = stats.shapiro(df.loc[df["sex"] == "female", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 0.9848, p-value = 0.0071 => H0 REDDEDİLİR.
test_stat, pvalue = stats.shapiro(df.loc[df["sex"] == "male", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 0.9747, p-value = 0.0000 => H0 REDDEDİLİR.

# Varyans homojenliği varsayımı
# H0: Varyanslar homojendir.
# H1: Varyanslar homojen değildir.
test_stat, pvalue = stats.levene(df.loc[df["sex"] == "female", "age"].dropna(),
                                 df.loc[df["sex"] == "male", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 0.0013, p-value = 0.9712 => H0 REDDEDİLEMEZ.

# Normallik varsayımı sağlanmadığı için non-parametrik test
test_stat, pvalue = stats.mannwhitneyu(df.loc[df["sex"] == "female", "age"].dropna(),
                                        df.loc[df["sex"] == "male", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 53212.5000, p-value = 0.0261 => H0 REDDEDİLİR










# UYGULAMA 3: Diyabet hastası olan ve olmayanların yaşları arasında ist. ol. anlamlı bir farklılık var mı?
df = pd.read_csv("datasets/diabetes.csv")
df.head()
df.groupby("Outcome").agg({"Age": "mean"})

# 1: Hipotez
# H0: M1 = M2
# H1: M1 != M2

# 2: Varsayım kontrolü
# Normal dağılım varsaıymı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
test_stat, pvalue = stats.shapiro(df.loc[df["Outcome"] == 1, "Age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 0.9546, p-value = 0.0000 => H0 REDDEDİLİR
test_stat, pvalue = stats.shapiro(df.loc[df["Outcome"] == 0, "Age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = 0.8012, p-value = 0.0000 => H0 REDDEDİLİR.

# Normallik varsayımı sağlanmadığı için non-parametrik test
test_stat, pvalue = stats.mannwhitneyu(df.loc[df["Outcome"] == 1, "Age"].dropna(),
                                       df.loc[df["Outcome"] == 0, "Age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # p-value = 0.0000 => H0 REDDEDİLİR.









# Kursun büyük çoğunluğunu izleyenler ile izlemeyenlerin puanları birbirinden farklı mı?
df = pd.read_csv("datasets/course_reviews.csv")
df.head()
df[df["Progress"] > 75]["Rating"].mean()
df[df["Progress"] < 25]["Rating"].mean()

test_stat, pvalue = stats.shapiro(df[df["Progress"] > 75]["Rating"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # p-value = 0.0000 => H0 REDDEDİLİR.
test_stat, pvalue = stats.shapiro(df[df["Progress"] < 25]["Rating"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # p-value = 0.0000 => H0 REDDEDİLİR.

test_stat, pvalue = stats.mannwhitneyu(df[df["Progress"] > 75]["Rating"],
                                       df[df["Progress"] < 25]["Rating"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # p-value = 0.0000 => H0 REDDEDİLİR.









# Sigara içen grup ile içmeyenlerin nefeslerini tutma süreleri arasında ist. ol. anl. bir fark var mı?
# H0: M1 = M2
# H1: M1 != M2
data = pd.read_excel("datasets/smoke_breath.xlsx")
data.head()
data.groupby("Sigara")["Zaman"].mean()
smoker = data[data["Sigara"] == "Evet"]
non_smoker = data[data["Sigara"] == "Hayır"]
# Normallik Varsayımı Testi
# H0: Veriler normal dağılım göstermektedir.
# H1: Veriler normal dağılım göstermemektedir.
norm_smoker = stats.shapiro(smoker["Zaman"])
norm_non_smoker = stats.shapiro(non_smoker["Zaman"])
print(f"Smoker pvalue= {norm_smoker[1]}\nNon smoker pvalue= {norm_non_smoker[1]}")
# Smoker pvalue= 0.0089 , Non smoker pvalue= 0.0603  --> Smoker için H0 Red.
test_stat, pvalue = stats.mannwhitneyu(smoker["Zaman"], non_smoker["Zaman"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# p-value = 0.3514 --> H0 REDDEDİLEMEZ.








# Bir içeçek firması ürettiği yeni aromalı içeçek ile eski içecek için müşteri tutumları arasında bir fark olup olm. test etmek istiyor.
# H0: M1 = M2 (Eski içecek ile yeni içecek müşteri tutumları arasında anl. fark yoktur)
# H1: M1 != M2 (Fark vardır)
data = pd.read_excel("datasets/drink.xlsx")
data.head()
data.groupby("Grup")["Tutum"].mean()
old = data[data["Grup"] == "Eski"]["Tutum"]
new = data[data["Grup"] == "Yeni"]["Tutum"]
# Normallik Varsayımı Testi
norm_old = stats.shapiro(old)
norm_new = stats.shapiro(new)
print(f"Old pvalue= {norm_old[1]}\nNew pvalue= {norm_new[1]}")
# Old pvalue= 0.9838, New pvalue= 0.8389 --> H0 REDDEDİLEMEZ. Veriler normal dağılım göstermektedir.
# Varyans Homojenliği Testi
var = stats.bartlett(old, new)
print(var)
# BartlettResult(statistic=0.24784539637091021, pvalue=0.6185963027262229) --> H0 REDDEDİLEMEZ. Varyanslar homojendir.
# Parametrik Hipotez testi
test_stat, pvalue = stats.ttest_ind(old, new)
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# Test Stat = -2.1768, p-value = 0.0431 --> H0 REDDEDİLİR. Tutumlar arasında anlamlı fark vardır.








# Bir ML projesine yatırım yapılmış. Ürettiği tahminler neticesinde oluşan gelir ile eski sistemin ürettiği gelirler
# karşılaştırılıp anlamlı farklılık olup olmadığı test edilmek isteniyor.
# Model geliştirilmiş ve web sitesine entegre edilmiş.
# Site kullanıcıları belirli bir kurala göre ikiye bölünmüş olsun.
# A grubu eski, B grubu yeni sistem
# Gelir anlamında anlamlı bir iş yapılıp yapılmadığı test edilmek isteniyor.
# H0: M1 = M2
# H1: M1 != M2
A = [30, 27, 21, 27, 29, 30, 20, 20, 27, 32, 35, 22, 24, 23, 25,
    27, 23, 27, 23, 25, 21, 18, 24, 26, 33, 26, 27, 28, 19, 25]
B = [37, 39, 31, 31, 34, 38, 30, 36, 29, 28, 38, 28, 37, 37, 30,
    32, 31, 31, 27, 32, 33, 33, 33, 31, 32, 33, 26, 32, 33, 29]
import numpy as np
np.mean(A) # 25.46
np.mean(B) #  32.36
# Normallik Kontrolü
stats.shapiro(A) # pvalue=0.79628
stats.shapiro(B) # pvalue=0.24584
# Varyans Kontrolü
stats.levene(A, B) # pvalue=0.2964124900636569
# Hipotez Testi
test_stat, pvalue = stats.ttest_ind(A, B, equal_var=True)
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue)) # Test Stat = -7.0287, p-value = 0.0000
