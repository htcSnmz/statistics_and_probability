# Rassal değişkenlere karşılık gelen bütün olasılıklar eşit olduğu durumlarda.

from scipy import stats

# Zar atma örneği
n = 6
dist = stats.randint(1, n+1)
prob = dist.pmf(k=5) # 5 gelme olasılığı = 0.16
print(prob)
prob = dist.pmf(k=1) # 1 gelme olasılığı = 0.16
print(prob)
prob = dist.pmf(k=3) # 3 gelme olasılığı = 0.16
print(prob)
# Beklenen değeri
exp_value = dist.expect()
print(exp_value)
# Varyansı
var = dist.var()
print(var)
# 3 ya da 3'ten küçük olma olasılığı
prob = dist.cdf(x=3)
print(prob)