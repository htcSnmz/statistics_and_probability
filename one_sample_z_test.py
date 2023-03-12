# n > 30
# Popülasyon std sapma ya da varyans biliniyor (n < 30 olsa bile)

from statsmodels.stats.weightstats import ztest

# H0: M = 80
# H1: M > 80
sample = [95, 70, 120, 65, 130, 38, 110, 90, 60]
test_stat, pvalue = ztest(sample, value=80, alternative="larger")
print(pvalue) # pvalue = 0.26,      0.26 > 0.05 --> H0 reddedilemez.