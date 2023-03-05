import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(0)
data = np.random.normal(35, 2, 40000)
data_z = stats.zscore(data)
sns.displot(data_z, kde=True)
plt.title("Distribution", fontsize=15, loc="right", c="red")
plt.xlabel("Data", fontsize=15, c="red")
plt.ylabel("Frequency", fontsize=15, c="red")
plt.xlim(-3, 3)
plt.axvline(x=np.mean(data_z), linestyle="--", linewidth=2.5, label="Mean", c="red")
plt.axvline(x=np.mean(data_z) + np.std(data_z), linestyle="--", linewidth=2.5, label="1 Std. Dev.", c="black")
plt.axvline(x=np.mean(data_z) - np.std(data_z), linestyle="--", linewidth=2.5, c="black")
plt.legend()
plt.show()