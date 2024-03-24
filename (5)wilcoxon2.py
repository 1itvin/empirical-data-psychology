import numpy as np
from scipy.stats import wilcoxon

before = np.array([29, 34, 19, 24, 12, 19, 14, 17, 23, 27, 17, 23, 32, 32, 19, 21, 14, 21, 32])
after = np.array([25, 29, 16, 21, 11, 16, 12, 14, 19, 23, 14, 20, 27, 27, 16, 18, 12, 18, 27])

# Вычисляем разность
diff = after - before

# Вычисляем ранги
ranks = np.abs(diff).argsort().argsort() + 1

# Вычисляем T-эмпирическое
T_empirical = ranks[diff < 0].sum()

# Вычисляем T-критическое и асимптотическое значение (двухстороннее)
T_critical, p_value = wilcoxon(before, after)

print(f"T-эмпирическое: {T_empirical}")
print(f"T-критическое: {T_critical}")
print(f"Асимптотическое значение (двухстороннее): {p_value}")
