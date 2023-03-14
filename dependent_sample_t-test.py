# Örneklem rastgele
# Veriler sürekli
# Her bir grup için veriler normal dağılmalı
# Varyanslar homojen (Göz ardı edilebiliyor)

import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Şirket içi Eğitimin Performans Etkisi Ölçümü
# Belirli uğraşlar sonucunda alınan bir satış eğitiminin katma değer sağlayıp sağlamadığı ölçülmek isteniyor.
# Eğitimden önce ve sonra olacak şekilde gerekli ölçümler yapılıyor.
# H0: MÖ = MS (Eğitimin satış adetlerine etkisi olmamıştır.)
# H1: MÖ != MS (Eğitimin satış adetlerine etkisi olmuştur.)
once = [123, 119, 119, 116, 123, 123, 121, 120, 117, 118, 121, 121,
                     123, 119, 121, 118, 124, 121, 125, 115, 115, 119, 118, 121,
                     117, 117, 120, 120, 121, 117, 118, 117, 123, 118, 124, 121,
                     115, 118, 125, 115]
sonra = [118, 127, 122, 132, 129, 123, 129, 132, 128, 130, 128, 138,
                      140, 130, 134, 134, 124, 140, 134, 129, 129, 138, 134, 124,
                      122, 126, 133, 127, 130, 130, 130, 132, 117, 130, 125, 129,
                      133, 120, 127, 123]
np.mean(once) # 119.65
np.mean(sonra) # 129.0
# Normallik Kontrolü
# H0: Normal dağılım sağlanmaktadır.
# H1: Normal dağılım sağlanmamaktadır.
stats.shapiro(once) # pvalue=0.10722016543149948
stats.shapiro(sonra) # pvalue=0.6159630417823792
# Varyans Homojenliği (Göz ardı edilebiliyor)
# H0: Varyasnlar homojendir.
# H1: Varyasnlar homojen değildir.
stats.levene(once, sonra) # pvalue=0.005084451180737039
# Hipotez Testi
stats.ttest_rel(once, sonra) # pvalue=2.0235251764440722e-11 --> (Eğitimin satış adetlerine etkisi olmuştur.)
# Normal Dağılım varsayımı sağlanmasaydı wilcoxon testi uygulanırdı.
stats.wilcoxon(once, sonra)







# Geliştirilen bir motor yağının yakıt tüketiminde farklılık yarattığı düşünülmektedir.
# H0: MÖ = MS
# H1: MÖ != MS
data = pd.read_excel("datasets/fuel consumption.xlsx")
data.head()
data["Önce"].mean() # 6.226
data["Sonra"].mean() # 4.949
# Normallik Testi
# H0: Normal dağılım sağlanmaktadır.
# H1: Normal dağılım sağlanmamaktadır.
stats.shapiro(data["Önce"]) # pvalue=0.49539485573768616
stats.shapiro(data["Sonra"]) # pvalue=0.49539485573768616
# Varyans Homojenliği (Göz ardı edilebiliyor)
# H0: Varyasnlar homojendir.
# H1: Varyasnlar homojen değildir.
stats.bartlett(data["Önce"], data["Sonra"]) # pvalue=0.006490793937200299)
# Hipotez Testi
stats.ttest_rel(data["Önce"], data["Sonra"]) # pvalue=0.010336613778589023)
# H0 REDDEDİLİR.

