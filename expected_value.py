from scipy import stats, integrate

# zar atma
x = [1, 2, 3, 4, 5, 6]
p = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
expected_value = stats.rv_discrete(values=([x, p])).expect()
print(expected_value)

# üç defa madeni para atma olayında yazı gelmesinin beklenen değeri
x = [0, 1, 2, 3]
p = [1/8, 3/8, 3/8, 1/8]
expected_value = stats.rv_discrete(values=([x, p])).expect()
print(expected_value)

# sürekli değişken için beklenen değer
expected_value = integrate.quad(lambda x: (3/7) * (x**3), 1, 2) # 1 ve 2 integra için alt ve üst sınır.
print(expected_value) #sol