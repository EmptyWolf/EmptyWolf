from bs4 import BeautifulSoup
import requests

url = "https://www.ikea.com/be/fr/p/pax-fardal-combinaison-armoire-blanc-gris-clair-brillant-s49329213/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(class_="range-revamp-price__integer")
price = prices[0].text

currency = doc.find_all(class_="range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript")
currencysym = currency[0].text

print(currencysym + str(price))