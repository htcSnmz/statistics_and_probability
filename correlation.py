import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Bahşiş veri seti
# total_bill: yemeğin toplam fiyatı (bahşiş ve vergi dahil)
# tip: bahşiş
# sex: ücreti ödeyen kişinin cinsiyeti (0=male, 1=female)
# smoker: grupta sigara içen var mı? (0=no, 1=yes)
# day: gün (3=thur, 4=fri, 5=sat, 6=sun)
# time: ne zaman? (0=day, 1=night)
# size: grupta kaç kişi var?

df = sns.load_dataset("tips")
df.head()

# verilen bahşiş ile ödenen hesap arasında korelasyon var mı?
df["total_bill"] = df["total_bill"] - df["tip"]
df.plot.scatter("tip", "total_bill")
plt.show()

df["tip"].corr(df["total_bill"])