from scipy import stats

# Bir otobüs durağına X otobüsünün her 15 dakikada bir geldiğini biliyoruz.
# Bir kişi bu otobüsü ortalama olarak kaç dakika bekler ?
q1 = 0
q2 = 15
dist = stats.uniform(q1, q2)
exp_value = dist.expect()
print(exp_value)
# Bir kişinin bu otobüsü 12.5 dakikadan daha az bekleme olasılığı?
prob = dist.cdf(x=12.5)
print(prob)

# Bir ürünün tamir süresinin 1.5 ile 4 saat arasında değiştiğini gözlemliyoruz.
# Rastgele seçilen bir arızalı ürünün tamir süresinin 2 saatten fazla sürme olasılığı?
q1 = 1.5
q2 = 4
dist = stats.uniform(q1, q2)
prob = 1 - dist.cdf(x=2)
print(prob)