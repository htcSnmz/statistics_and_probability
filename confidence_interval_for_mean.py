import numpy as np
from scipy import stats
import seaborn as sns
import statsmodels.stats.api as sms

"""
Bir fabrikada rassal olarak seçilen 100 ürünün ortalama ağırlığı 1040 gr,
std sapması 25 gr olarak bulunmuştur. Bu fabrikada üretilen tüm ürünlerin
ortalama oğırlıkları %95 güven ile kaçtır?
"""
n = 100
x = 1040
s = 25
conf = 0.95
interval = stats.norm.interval(alpha=conf, loc=x, scale=s/np.sqrt(n))
print(interval)

"""
85 ev sahibi ile yapılan bir ankette, ev bakımına aylık ortalama 67$
(std sapma 14$) harcadıkları tespit edilmiştir. Tüm ev sahiplerinin
aylık ev bakım harcamaları için %95 güven aralığı oluşturunuz.
"""
interval = stats.norm.interval(alpha=0.95, loc=67, scale=14/np.sqrt(85))
print(interval)

"""
Piyasaya yeni sürülen bir ürünün uzunluğunun std sapması 2 cm'dir.
Rastgele seçilen 16 ürünün ortalama uzunluğu 4 cm olarak hesaplanmıştır.
%95 güvenle anakütle ortalamasını tahmin ediniz.(n<30 fakat pop. std sapması biliniyor)
"""
interval = stats.norm.interval(alpha=0.95, loc=4, scale=2/np.sqrt(16))
print(interval)

"""
Bir fabrikada üretilen margarin paketlerinin ağırlığının varyansı 100 gr'dır.
Rastgele seçilen 25 paketin ağırlığının ortalaması 120 gr'dır. Ana kütle ortalamasını
%90 ve %99 güvenle tahmin ediniz.
"""
interval = stats.norm.interval(alpha=0.9, loc=120, scale=np.sqrt(100)/np.sqrt(25))
print(interval)
interval = stats.norm.interval(alpha=0.99, loc=120, scale=np.sqrt(100)/np.sqrt(25))
print(interval)

"""
Bir firmanın ürettiği ürünlerin 100 tanesi rassal örneklem olarak seçilmiştir.
Ortalama ağırlık 385 gr ve std sapması 12 gr olarak hesaplanmıştır.
Üretilen ürünlerin ortalama ağırlığını %95 güven düzeyi ile tahmin ediniz.
"""
interval = stats.norm.interval(alpha=0.95, loc=385, scale=12/np.sqrt(100))
print(interval)

###########################################################################
# T Dist.
n = 30
x = 140
s = 25
conf = 0.95
df = n - 1
interval = stats.t.interval(alpha=conf, loc=x, df=df, scale=s/np.sqrt(n))
print(interval)

"""
Rassal olarak seçilen 20 bilgisayarın tamirat maliyetleri kaydedilmiştir.
Seçilen 20 bilgisayarın maliyet ortalamasının 216.53$ olduğu tespit edilmiştir.
Bu örneklemin std sapması 15.86$ olarak hesaplanmıştır.
Tüm bilgisayarların ortalama tamirat maliyetini %95 güven ile tahmin ediniz
"""
n = 20
x = 216.53
s = 15.86
conf = 0.95
df = n - 1
interval = stats.t.interval(alpha=conf, loc=x, df=df, scale=s/np.sqrt(n))
print(interval)

##########################################################################################
# tips veri setindeki sayısal değişkenler için güven aralığı
# confidence interval for numeric variables in tips dateset
df = sns.load_dataset("tips")
df.describe().T
sms.DescrStatsW(df["total_bill"]).tconfint_mean()
sms.DescrStatsW(df["tip"]).tconfint_mean()

# titanic veri setindeki sayısal değişkenler için güven aralığı
# confidence interval for numeric variables in titanic dateset
df = sns.load_dataset("titanic")
df.describe().T
sms.DescrStatsW(df["age"].dropna()).tconfint_mean()
sms.DescrStatsW(df["fare"].dropna()).tconfint_mean()