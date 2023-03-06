import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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

def high_corr_cols(dataframe, plot=False, corr_th=0.9):
    corr = dataframe.corr()
    corr_matrix = corr.abs()
    upper_triangle_matrix = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype("bool"))
    drop_cols = [col for col in upper_triangle_matrix.columns if (upper_triangle_matrix[col] > corr_th).any()]
    if plot:
        sns.set(rc={"figure.figsize": (12, 12)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_cols
  
df2 = pd.read_csv("datasets/breast_cancer.csv")
df.head()
high_corr_cols(df)
high_corr_cols(df2)
