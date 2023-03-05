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
