# Popülasyon std sapma ve ya varyansı bilinmiyor
# Veriler sürekli ve normal dağılıyor
# Uç değer barındırmamalı
# n < 30 ya da n > 30 için güçlü sonuçlar
# n büyüdükçe z dağılımına yakınsar.

from scipy import stats
import pandas as pd


# H0: M = 28
# H1: M != 8
sample = [28, 29, 35, 37, 32, 26, 37, 39, 22, 29, 36, 38]
test_stat, pvalue = stats.ttest_1samp(sample, popmean=28, alternative="two-sided")
print(pvalue) # pvalue = 0.01,  0.019 < 0.05 --> H0 Reddedilir



# Bir üretim raporunda bir ürünün günlük ortalama hatalı üretim sayısının 20 olduğu yazmaktadır.
# Müşteri şikayetlerinin artması üzerine bu sayı hakkında şüpheye düşülmektedir.
# Bu sayının doğruluğunu teyit etmek için hipotez testi yapılmak istenmektedir.
# Bunun için 25 günlük veri toplanıyor.
# H0: M = 20
# H1: M != 20
sample = [25, 26, 25, 20, 18,
          29, 30, 32, 17, 23,
          34, 27, 26, 30, 33,
          32, 21, 21, 20, 11,
          16, 14, 15, 18, 19]
test_stat, pvalue = stats.ttest_1samp(sample, popmean=20, alternative="two-sided")
print(pvalue) # pvalue = 0.01,  0.019 < 0.05 --> H0 Reddedilir



# Web Sitesinde Geçirilen Sürenin Testi
# Problem: Web sitemizde geçirilen ortalama süre gerçekten 170 saniye mi ?
# Yazılımlardan elde edilen web sitesinde geçirilen ortalama süreler var.
# Bu veriler incelendiğinde bir yönetici ya da çalışanımız bu değerlerin
# böyle olmadığına yönelik düşünceler taşıyor ve bu durumu test etmek istiyorlar.
# H0: M = 170
# H1: M != 170
sample = [17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119,
          157, 145, 127, 244, 163, 114, 145, 65, 112, 185, 202, 146,
          203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110,
          216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120]
stats.describe(sample)
# Normallik Varsayımı Kontrolü
# with histogram
pd.DataFrame(sample).plot.hist()
# with qqplot
import pylab
stats.probplot(sample, dist="norm", plot=pylab)
pylab.show()
# shapiro-wilks testi
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
stats.shapiro(sample) # pvalue = 0.78,    0.78 > 0.05 --> H0 Reddedilemez
# hipotez testi
stats.ttest_1samp(sample, popmean=170) # pvalue = 0.03,     0.03 < 0.05 --> H0 Reddedilir.

# Nonparametrik Tek Örneklem Testi (Normallik varsayımı sağlanmadığı durumlarda)
# Normallik sağlanmadığını varsayalım.
from statsmodels.stats.descriptivestats import sign_test
sign_test(sample, 170) # pvalue= 0.06,  0.06 > 0.05 --> H0 Reddedilemez.


###############################
# TEK ÖRNEKLEM ORAN TESTİ
###############################
# n > 30

# Dönüşüm Oranı Testi
# Problem: Bir yazılım ile bir mecrada reklam verilmiş ve bu reklama ilişkin yazılım tarafından 0.125 dönüşüm oranı
# elde edildiği ifa edilmiş. Fakat bu durum kontrol edilmek isteniyor. Çünkü bu yüksek bir oran ve gelirler
# incelendiğinde örtüşmüyor.
# 500 kişi dış mecrada reklamlara tıklamış, 40 tanesi sitemize gelip alışveriş yapmış.
# Örnek üzerinden elde edilen dönüşüm oranı: 40/500 = 0.08
# H0: P = 0.125
# H1: P != 0.125
from statsmodels.stats.proportion import proportions_ztest
count = 40
nobs = 500
value = 0.125
proportions_ztest(count, nobs, value) # pvalue = 0.000208,  0.000208 < 0.05 --> H0 Reddedilir.