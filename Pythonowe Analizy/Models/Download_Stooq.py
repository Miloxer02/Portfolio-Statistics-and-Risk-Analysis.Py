
import pandas as pd
import datetime

# Funkcje na pobieranie danych ze Stooq
def download_stooq(ticker, start_date, end_date, interval="d"):
    print(f"Pobieranie danych z Stooq: {ticker}")

    # Formatowanie dat
    d1 = pd.to_datetime(start_date).strftime("%Y%m%d")
    d2 = pd.to_datetime(end_date).strftime("%Y%m%d")

    # Budowanie URL do Stooq
    url = f"https://stooq.pl/q/d/l/?s={ticker}&d1={d1}&d2={d2}&i={interval}"

    try:
        df = pd.read_csv(url)

        # Wybór i zmiana nazw kolumn
        df = df[['Data', 'Zamkniecie', 'Wolumen']]
        df.rename(columns={'Data': 'Date'}, inplace=True)

        # Konwersja daty i sortowanie
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date').reset_index(drop=True)

        return df

    except Exception as e:
        print(f"❌ Błąd podczas pobierania danych z Stooq dla {ticker}: {e}")
        return pd.DataFrame()