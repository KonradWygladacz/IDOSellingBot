import ccxt
import time
import config

exchange = ccxt.bybit({
    'enableRateLimit': True,
    'apiKey': config.api_key,
    'secret': config.secret_key
})
symbol = "RLTM/USDT"
poczatkowa_ilosc_tokenow = 7142.857142857  # tyle chyba powinno ich byc za 250$ po cenie 0,035

def set_orders():
    try:
        exchange.create_spot_order(symbol, "limit", "sell", poczatkowa_ilosc_tokenow / 5, 0.175)  # wyciagniecie wkladu po cenie x5
        exchange.create_spot_order(symbol, "limit", "sell", poczatkowa_ilosc_tokenow / 5, 0.35)  # sprzedanie 1/5 tokenow na zysku x10
        exchange.create_spot_order(symbol, "limit", "sell", poczatkowa_ilosc_tokenow / 5, 0.7)  # sprzedanie 1/5 tokenow na zysku x20
        exchange.create_spot_order(symbol, "limit", "sell", poczatkowa_ilosc_tokenow / 5, 1.75)  # sprzedanie 1/5 tokenow na zysku x50
        exchange.create_spot_order(symbol, "limit", "sell", poczatkowa_ilosc_tokenow / 5, 3.5)  # sprzedanie 1/5 tokenow na zysku x100
    except Exception as e:
        print(e)

while 1 == 1:
    time.sleep(5)
    set_orders()
