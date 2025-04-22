import pandas as pd
import matplotlib.pyplot as plt

# Parametry
ticker = "etfsp500.pl"
start_date = "2010-01-01"
end_date = "2024-01-01"
interval = "d"

# Formatowanie dat
d1 = pd.to_datetime(start_date).strftime("%Y%m%d")
d2 = pd.to_datetime(end_date).strftime("%Y%m%d")

# Budowanie URL
url = f"https://stooq.pl/q/d/l/?s={ticker}&d1={d1}&d2={d2}&i={interval}"

# Pobieranie danych
df = pd.read_csv(url)

# Sprawdzenie i przygotowanie
df = df[['Data', 'Zamkniecie', 'Wolumen']]
df.rename(columns={'Data': 'Date'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').reset_index(drop=True)

# Wyświetlenie danych
print(df.head())

# Wykres
plt.plot(df['Date'], df['Zamkniecie'])
plt.xlabel('Data')
plt.ylabel('Zamknięcie')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
