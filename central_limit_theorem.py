import numpy as np
import random
import matplotlib.pyplot as plt

pop = np.random.uniform(15,75,40000)
orneklem = [np.mean(random.choices(pop, k=30)) for _ in range(1000)]
plt.hist(orneklem)
plt.show()