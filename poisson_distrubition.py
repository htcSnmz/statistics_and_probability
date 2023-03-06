# Sürekli bir zaman aralığında, bir alanda ya da hacimde başarının sayılması söz konusu (nadir olaylar)
# n >= 50 ve n*p < 5 => nadir olay
# n*p = ortalama (lambda)

from scipy import stats

# Bir çağrı merkezine 1 dakikada ortalama 10 adet arama gelmektedir.
# Hiç arama gelmeme olasılığı?
avg = 10
dist = stats.poisson(avg)
prob = dist.pmf(k=0)
print(prob)


# Elektronik ürün satılan bir mağazada X markanın Y seri TV'si 1 yılda 1825 tane satmıştır.
# Herhangi bir günde 9 adet satılma olasılığı nedir ?
avg = 1825 / 365 # ortalama günlük satış
dist = stats.poisson(avg)
prob = dist.pmf(k=9)
print(prob)


# Bir X ülkesine bir çatı malzemesi üretmek istiyoruz.
# Bu X ülkesinde yılda ortalama 2 fırtına çıkmaktadır.
# Garanti süresini belirlemek için 1 yılda 1, 3 ve 5 fırtına çıkma olasılıkları nedir?
avg = 2
dist = stats.poisson(avg)
# 1 fırtına çıkma olasılığı
prob = dist.pmf(k=1)
print(prob)
# 3 fırtına çıkma olasılığı
prob = dist.pmf(k=3)
print(prob)
# 5 fırtına çıkma olasılığı
prob = dist.pmf(k=5)
print(prob)


# Marmara Bölgesi'nde yılda ortalama 6 deprem olduğu biliniyor.
# Önümüzdeki 1 yılda en fazla ve en az 3 deprem olma olasılığı nedir ?
avg = 6
dist = stats.poisson(avg)
# en fazla 3 deprem olma olasılığı
prob = dist.cdf(3)
print(prob)
# en az 3 deprem olma olasılığı
prob = 1 - dist.cdf(3)
print(prob)


# Bir ülkenin borsa endeksi incelendiğinde 1 yılda ortalama olarak 2 defa %10'dan daha fazla yükseldiği tespit edilmiştir.
# Önümüzdeki yılda 1 defadan fazla %10'dan yüksek olma olasılığı nedir?
avg = 2
dist = stats.poisson(avg)
prob = 1 - dist.cdf(1)
print(prob)


# Bir ilan sitesine ilan girişleri yapılıyor.
# Hatalı ilan girişi olasılıkları hesaplanmak istiyor.
# 1 yıl ölçüm yapılıyor ve ortalama hata sayısı 0.1 olarak belirleniyor.
# Hiç hata olmamaması, 3 hata olması ve 5 hata olması olasılıkları nedir?
avg = 0.1
dist = stats.poisson(mu=avg)
# Hiç hata olmama olasılığı
prob = dist.pmf(k=0)
print(prob)
# 3 hata olma olasılığı
prob = dist.pmf(k=3)
print(prob)
# 5 hata olma olasılığı
prob = dist.pmf(k=5)
print(prob)