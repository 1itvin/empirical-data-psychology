import scipy.stats as stats
import colorama
from colorama import Fore

colorama.init()

#! ДО
# Глубина переживания одиночества
depthLonelinessBefore = [29, 29, 32, 32, 30, 28, 28, 32, 29, 30, 28, 29, 29, 32, 32, 31, 28, 37, 28]
# Физическая агрессия
physicalAggressionBefore = [29, 34, 19, 24, 12, 19, 14, 17, 23, 27, 17, 23, 32, 32, 19, 21, 14, 21, 32]
# Гнев
AngerBefore = [23, 11, 10, 12, 12, 11, 17, 10, 22, 17, 10, 14, 15, 22, 23, 11, 12, 36, 15]
# Враждебность
HostilityBefore = [30, 16, 16, 12, 20, 14, 30, 11, 21, 18, 22, 15, 22, 25, 25, 19, 14, 45, 22]

#! ПОСЛЕ 
# Глубина переживания одиночества
depthLonelinessAfter = [25, 25, 28, 28, 26, 23, 24, 27, 24, 25, 24, 25, 25, 27, 27, 26, 24, 31, 24]
# Физическая агрессия
physicalAggressionAfter = [25, 29, 16, 21, 11, 16, 12, 14, 19, 23, 14, 20, 27, 27, 16, 18, 12, 18, 27]
# Гнев
AngerAfter = [20, 9, 9, 11, 11, 9, 15, 8, 18, 14, 8, 12, 13, 19, 20, 9, 10, 30, 13]
# Враждебность
HostilityAfter = [26, 14, 14, 11, 18, 11, 26, 9, 18, 15, 19, 13, 19, 21, 21, 16, 12, 38, 19]


# Вычисляем U статистику и p-значение
print(Fore.BLACK + "")
print("ГЛУБИНА ПЕРЕЖИВАНИЯ ОДИНОЧЕСТВА")
U, p = stats.mannwhitneyu(depthLonelinessBefore, depthLonelinessAfter, alternative='two-sided')
print(f'U Манна-Уитни: {U}')
print(f'Асимп. знач. (двухсторонняя): {p}')

print(Fore.MAGENTA + "")
print("ФИЗИЧЕСКАЯ АГРЕССИЯ")
U, p = stats.mannwhitneyu(physicalAggressionBefore, physicalAggressionAfter, alternative='two-sided')
print(f'U Манна-Уитни: {U}')
print(f'Асимп. знач. (двухсторонняя): {p}')

print(Fore.CYAN + "")
print("ГНЕВ")
U, p = stats.mannwhitneyu(AngerBefore, AngerAfter, alternative='two-sided')
print(f'U Манна-Уитни: {U}')
print(f'Асимп. знач. (двухсторонняя): {p}')

print(Fore.RED + "")
print("ВРАЖДЕБНОСТЬ")
U, p = stats.mannwhitneyu(HostilityBefore, HostilityAfter, alternative='two-sided')
print(f'U Манна-Уитни: {U}')
print(f'Асимп. знач. (двухсторонняя): {p}')
