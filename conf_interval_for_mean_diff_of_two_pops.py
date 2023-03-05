# İki Popülasyon Ortalama Güven Aralığı Z ve T
# Confidence Interval for The Mean Difference of Two Populations

import numpy as np
from scipy import stats

"""
Bir fabrikada A ve B ürünlerinin ağırlıklarının varyansları sırasıyla
164 gr ve 216 gr'dır. A ürününden 28 adet, B ürününden 30 adet örneklem alındığında;
A ürününün ortalama ağırlığı 32 gr, B ürününün ortalama ağırlığı 28 gr çıkmıştır.
Bu verilere göre A ve B ürünlerinin ortalama ağırlıklarının farkını %95 güven
aralığında tahmin ediniz.
"""
n_a = 28
n_b = 30
var_a = 164
var_b = 216
mean_a = 32
mean_b = 26
conf = 0.95
interval = stats.norm.interval(confidence=conf, loc=(mean_a - mean_b), scale=np.sqrt((var_a / n_a) + (var_b / n_b)))
print(interval)

"""
İngilizce ve Fransızca eğitim alan iki öğrenci grubundan sırasıyla
30 ve 40 öğrenci seçiliyor. İngilizce grubu öğrencilerinin dili öğrenme
süresi ortalaması 182 gün, Fransızca grubu için 176 gün olarak hesaplanıyor.
Aynı gruplar için varyanslar sırasıyla 196 gün ve 144 gün olarak hesaplanıyor.
Bu iki farklı dil kursuna giden ekiplerin öğrenme süreleri arasındaki fark %95
güven ile kaç gündür?
"""
n_en  = 30
n_fr = 40
mean_en = 182
mean_fr = 176
var_en = 196
var_fr = 144
conf = 0.95
interval = stats.norm.interval(confidence=conf, loc=(mean_en-mean_fr), scale=np.sqrt((var_en / n_en) + (var_fr / n_fr)))
print(interval)

"""
İki farklı hasta grubu arasında 8 ve 10 bireylerden oluşan örneklemler
çekilmiştir. Bu iki grubun bir virüse karşı reaksiyon verme zaman ortalamaları
sırasıyla 3 ve 2.7'dir. Birleştirilmiş varyans 0.05  olarak hesaplandığına göre,
bu iki farklı hasta grubunun virüse karşı verdiği reaksiyon zaman farklarını
%95 güven ile bulunuz.
"""
n1 = 8
n2 = 10
var = 0.05
mean_1 = 3
mean_2 = 2.7
conf = 0.95
n = (1 / n1) + (1 / n2)
interval = stats.t.interval(confidence=conf, df=(n1 + n2 - 2), loc=(mean_1 - mean_2), scale = np.sqrt(n * var))
print(interval)