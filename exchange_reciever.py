import requests
import json
import datetime
import bs4 as bs

# response = requests.get("https://tse.ir/json/Indices/Plot/plot_IRX6XTPI0006.json", verify=False,
#                         headers={"content-type": "application/json"})
# data = json.loads(response.text.encode().decode("utf-8-sig"))

# response = requests.get("https://coinmarketcap.com/")
response = requests.get("https://coinmarketcap.com/currencies/bitcoin/markets/")
soup = bs.BeautifulSoup(response.text, 'lxml')
# bitcoin_a_tag = soup.find("a", attrs={"href": "/currencies/bitcoin/markets/", "class": "cmc-link"})
bitcoin = soup.find("div", attrs={"class": "priceValue"}).find("span").text[1:].replace(",", "")
# index = data["plotData"][0]["yData"][-1]
timestamp = datetime.datetime.now().timestamp()

new_data = {
    "index": bitcoin,
    "datetime": timestamp
}
requests.post("http://localhost:8000/bourse/index/", json=new_data)

tel_data = {
    "chat_id":"-823775964",
    "text": f"bitcoin = {bitcoin}"
}
requests.post("https://api.telegram.org/bot5913296732:AAH56G8GyN0HBYrN7Ph3JkVlR2zmYm8EEMQ/sendMessage", json=tel_data)
