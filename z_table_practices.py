from scipy.stats import norm

"""
Bir kamu bankası personel alımı için ilana çıkmış ve iş için başvuran çok sayıda adaya
ekonomi, maliye, finans vs. alanlarında hazırlanan bir test uygulamıştır. Adayların
uygulanan testte aldıkları puanların ortalaması 60 ve standart sapması 12 hesaplanmıştır.
Adayların aldıkları puanların normal dağıldığı bilindiğine göre tesadüfen seçilecek bir adayın;
1) 60-70 arasında puan almış alma olasılığı kaçtır?
2) 45-60 arasında puan almış olma olasılğı kaçtır?
3) 45'den az puan almış olma olasılığı kaçtır?
"""
# 1)
up_limit = norm(loc=60, scale=12).cdf(70)
low_limit = norm(loc=60, scale=12).cdf(60)
prob = up_limit - low_limit
print(prob)
# 2)
up_limit = norm(loc=60, scale=12).cdf(60)
low_limit = norm(loc=60, scale=12).cdf(45)
prob = up_limit - low_limit
print(prob)
# 3)
prob = norm(loc=60, scale=12).cdf(45)
print(prob)



"""
İmal edilen ampullerin ortalama ömrü 800 saat, standart sapması 40 saattir.
Ampulün ömrünün normal dağılım gösterdiği bilindiğine göre bir ampulün;
1) 778 saatten daha fazla ömre
2) 834 saatten daha az ömre
3) 778 ile 834 saat arasında bir ömre sahip olma
olasılıkları nedir ?
"""
# 1)
prob = 1 - norm(loc=800, scale=40).cdf(778)
print(prob)
# 2)
prob = norm(loc=800, scale=40).cdf(834)
print(prob)
# 3)
low_limit = norm(loc=800, scale=40).cdf(778)
up_limit = norm(loc=800, scale=40).cdf(834)
prob = up_limit - low_limit
print(prob)



"""
Bir imalathanede üretilen millerin çapların ortalaması 3.0005 inç ve
standart sapmalarının ise 0.001 inç olan normal dağılıma uyduğu tespit
edilmiştir. Üretilen miller eğer 3.000 +/- 0.002 inç aralığının dışında
iseler bu miller hatalı üretim kabul edilmektedir. Buna göre toplam üretimdeki
hatalı ürün miktarını bulunuz.
"""
low_mil = 3 - 0.002
up_mil = 3 + 0.002
up_limit = norm(loc=3.0005, scale=0.001).cdf(up_mil)
low_limit = norm(loc=3.0005, scale=0.001).cdf(low_mil)
prob = 1 - (up_limit - low_limit)
print(prob)