# Bağımsız n deneme sonucu k başarılı olma olasılığı ile ilgilenildiğinde kullanılan dağılımdır.
from scipy import stats

# Bir oyuncunun penaltı atışlarının %80'inin gol olduğunu biliyoruz.
# Bu oyuncunun 5 penaltıdan 3 tanesini gole çevirrme olasılığı nedir?
p = 0.8
n = 5
k = 3
dist = stats.binom(n, p)
prob = dist.pmf(k=k)
print(prob)


# Bir fabrikada üretilen bir ürünün her 100 tanesinden 1 tanesinin kusurlu üretildiği tespit edilmiştir.
# Müşteriye satılan 10 tane ürünün tamamının kusursuz olma olasılığı nedir ?
# En fazla 2 tanesinin kusurlu olma olasılığı?
# En az 3 tanesinin kusursuz olma olasılığı?
p = 0.01
n = 10
k = 0
dist = stats.binom(n, p)
prob = dist.pmf(k=k)
print("10 ürünün tamamının kusursuz olma olasılığı " + str(prob))
prob = dist.cdf(x=2)
print("10 üründen en fazla 2 tanesinin kusursuz olma olasılığı " + str(prob))
prob = 1 - dist.cdf(x=3)
print("10 üründen en az 3 tanesinin kusursuz olma olasılığı " + str(prob))


# Bir mağazada haftalık ortalama olarak her 100 satışın 10 tanesi iade ediliyor.
# Haftalık ortalama sipariş sayımızın 50 olduğunu biliyoruz.
# 5 defa iade gelme olasılığı ?
# 15'ten az iade gelme olasılığı?
# En az 10 defa iade gelme olasılığı?
p = 0.1
n = 50
dist = stats.binom(n, p)
prob = dist.pmf(k=5)
print("50 satıştan 5 tanesinin iade gelme olasılığı " + str(prob))
prob = dist.cdf(x=15)
print("50 satışta 15 defadan az iade gelme olasılığı " + str(prob))
prob = 1 - dist.cdf(x=10)
print("50 satışta en az 10 defa iade gelme olasılığı " + str(prob))
