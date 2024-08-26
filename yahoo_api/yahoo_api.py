#  sudo pip3 install yfinance

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def moving_average(data, window_size):
    return data.rolling(window=window_size).mean()





# Завантажуємо дані за X років для акцій 
name = "NVDA"
nvda = yf.Ticker(name)
data = nvda.history(period="5y")
data = data['Close']



#data = moving_average(data, window_size=5)


#print(data.shape)
#data = data[:-250]



# Виводимо графік
plt.figure(figsize=(14, 7))
plt.plot(data.index, data, label='Stock Price')
plt.title(name+' Stock Price (Last 5 Years)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()





def analyze_growth(data):
    growth_amounts = []
    difference_ninth_sixth_month = []

    for i in range(len(data) - 11):  # Проходимо по всьому ряду даних, залишаючи місце для 8 місяців
        window = data.iloc[i:i+6]  # Вибираємо 6-місячне вікно
        if window[-1] > window[0]:  # Перевіряємо, чи є ріст (останнє значення більше за перше у вікні)
            growth = window[-1] - window[0]  # Обчислюємо ріст
            growth_amounts.append(growth)
            # Зберігаємо різницю між значенням дев'ятого(сьомого) місяця та шостого місяця
            difference = data.iloc[i+9] - window[-1]
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


def extract_growth_windows(data):
    # Переводимо дані до середньомісячних значень
    monthly_data = data.resample('M').mean()

    # Список для збереження "вікон"
    growth_windows = []

    # Перевірка довжини даних
    if len(monthly_data) < 9:
        print("Недостатньо даних для аналізу.")
        return growth_windows
    
    # Прохід по даним з кроком в один місяць
    for i in range(len(monthly_data) - 8):
        window = monthly_data[i:i+9]  # Вікно з 9 місяців
        if window.iloc[0] < window.iloc[6]:
            growth_windows.append(window)
    
    return growth_windows



growth_windows = extract_growth_windows(data)

if growth_windows:

	show_windows = 0
	show_last3 = 1
	
	
	if show_windows:
		for i in range(len(growth_windows)):
			plt.figure(figsize=(10, 10))
			
			price = growth_windows[i]
			dates = growth_windows[i].index
			#dates = dates-dates[0]              # norm dates from 0 to 9
			
			plt.plot( dates,price, marker='o')
			plt.title("вікнa зростання")
			plt.xlabel("Дата")
			plt.ylabel("Ціна")
			plt.grid(True)
			plt.show()



	plus=0
	minus=0
	if show_last3:
		num = len(growth_windows)
		for i in range(num):      # show only last 3 monts
			#plt.figure(figsize=(10, 10))
			
			price = growth_windows[i]
			price = price[6:]
			price = (price-price[0])/price[0]
				
			dates = growth_windows[i].index
			dates = dates[6:]
			dates = dates-dates[0]
			
			plt.plot( dates,price)
			#plt.title("вікнa зростання")
			#plt.xlabel("Дата")
			#plt.ylabel("Ціна")
			#plt.grid(True)
			
			if price[-1]>0:
				plus+=price[-1]
			else:
				minus+=price[-1]
		
		print(plus/num,minus/num)	
		plt.show()
		
		
		
