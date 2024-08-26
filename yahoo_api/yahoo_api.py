#  sudo pip3 install yfinance


import yfinance as yf
import matplotlib.pyplot as plt

# Завантажуємо дані за 5 років для акцій NVIDIA (символ NVDA)

name = "AMD"
nvda = yf.Ticker(name)
data = nvda.history(period="max")

# Виводимо графік
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Close'], label='Stock Price')
plt.title(name+' Stock Price (Last 5 Years)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()




import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def analyze_growth(data):
    growth_amounts = []
    difference_ninth_sixth_month = []

    for i in range(len(data) - 8):  # Проходимо по всьому ряду даних, залишаючи місце для 8 місяців
        window = data['Close'].iloc[i:i+6]  # Вибираємо 6-місячне вікно
        if window[-1] > window[0]:  # Перевіряємо, чи є ріст (останнє значення більше за перше у вікні)
            growth = window[-1] - window[0]  # Обчислюємо ріст
            growth_amounts.append(growth)
            # Зберігаємо різницю між значенням дев'ятого(сьомого) місяця та шостого місяця
            difference = data['Close'].iloc[i+6] - window[-1]
            difference_ninth_sixth_month.append(difference)

    return np.array(growth_amounts), np.array(difference_ninth_sixth_month)

def plot_growth_vs_difference(growth_amounts, difference_ninth_sixth_month):
    plt.figure(figsize=(10, 6))
    plt.scatter(growth_amounts, difference_ninth_sixth_month, color='blue', label='9th Month - 6th Month')
    
    plt.title("Relationship between Growth over 6 Months and more")
    plt.xlabel("Growth over 6 months")
    plt.ylabel("Difference (Xth Month - 6th Month)")
    plt.legend()
    plt.grid(True)
    plt.show()



# Викликаємо функцію для аналізу
growth_amounts, difference_ninth_sixth_month = analyze_growth(data)

# Виводимо графік
plot_growth_vs_difference(growth_amounts, difference_ninth_sixth_month)

def sum_positive_negative_differences(differences):
    positive_sum = np.sum(differences[differences > 0])
    negative_sum = np.sum(differences[differences < 0])
    return positive_sum, negative_sum

# Обчислюємо і виводимо суми позитивних та негативних різниць
positive_sum, negative_sum = sum_positive_negative_differences(difference_ninth_sixth_month)
print(f"Sum of positive differences: {positive_sum}")
print(f"Sum of negative differences: {negative_sum}")



