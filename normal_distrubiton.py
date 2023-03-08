from scipy import stats
from numpy import sqrt

# Bir fabrikada üretilen ürünün ortalama ağırlığı 500 gr ve varyansı 100 gr'dır.
# Veriler normal dağıldığı bilindiğine göre rassal olarak seçilen bir ürünün 518 gr'dan az olma olasılığı ?
avg = 500
var = 100
dist = stats.norm(avg, sqrt(var))
prob = dist.cdf(x=518)
print(prob)


# Bir üretim yerinde A isimli ürüne gelen günlük talep ortalama 100 adettir.
# Varyansı ise 3000 adettir.
# Normal dağılım sağlanıyor.
# Stoklarda 3500 adet A ürünü bulunmaktadır.
# Üretimin olmadığı herhangi bir anda elimizdeki stoğun 1 ay içinde bitme olasılığı nedir?
avg = 30 * 100 # Aylık ortama satış
var = 30 * 3000
dist = stats.norm(avg, sqrt(var))
prob = 1 - dist.cdf(x=3500)
print(prob)


# A ülkesinde yıllık ortalama olarak yangından dolayı 4300 dönümün yok olduğu tespit edilmiştir.
# Varyans ise 562.5 dönümdür.
# Normal dağılım varsayımı ile herhangi bir yılda 2500 ile 4200 dönümün yanma olasılığı nedir?
avg = 4300
var = 562.5
dist = stats.norm(avg, sqrt(var))
prob = dist.cdf(4200) - dist.cdf(2500)
print(prob)
# 3000 dönümden fazla yanma olasılığı
prob = 1 - dist.cdf(x=3000)  # ya da dist.sf(x=3000)
print(prob)


# Ürettiğimiz bir ürünün ortalama ömrü 58 aydır. Varyans ise 100 aydır.
# Arızalı bir ürünü yenisi ile değiştirmek için 3 yıl garanti veriyoruz.
# 1 yılda 1 milyon ürün ürettiğimizi varsayalım.
# 1 yılda kaç ürünün garantiye gelebileceğini tahmin ediniz.
avg = 58
var = 100
dist = stats.norm(avg, sqrt(var))
prob = dist.cdf(x=36) # 3 yıl
print(prob)


# Bir lokanta verilen siparişten sonra ortalama 30 dk'da ürünü teslim etmektedir.
# Varyansı ise 25 dk'dır.
# Bunlar ve verilerin normal dağıldığı bilindiğine göre herhangi bir teslimatın 20-40 dk arasında olma olasılığı?
avg = 30
var = 25
dist = stats.norm(avg, sqrt(var))
prob = dist.cdf(x=40) - dist.cdf(x=20)
print(prob)


# Bir yatırım/toplantı öncesinde gelecek ay ile ilgili satışların belirli değerlerde gerçekleşmesi olasılığı belirlenmek isteniyor.
# Dağılımın normal olduğu biliniyor.
# Aylık ortalama satış sayısı 80k ve std sapması 5k
# 90k'dan fazla satış yapma olasılığı?
print(1 - stats.norm.cdf(90, 80, 5))
# 70k'dan fazla olma olasılığı?
print(1 - stats.norm.cdf(70, 80, 5))
# 70k'dan az olması olaıslığı
print(stats.norm.cdf(73, 80, 5))
# 85k ile 95k arasında olma olasılığı?
print(stats.norm.cdf(95, 80, 5) - stats.norm.cdf(85, 80, 5))