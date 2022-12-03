import requests
import json
import datetime

response = requests.get("https://tse.ir/json/Indices/Plot/plot_IRX6XTPI0006.json", verify=False,
                        headers={"content-type": "application/json"})
data = json.loads(response.text.encode().decode("utf-8-sig"))

index = data["plotData"][0]["yData"][-1]
timestamp = datetime.datetime.now().timestamp()

new_data = {
    "index": index,
    "datetime": timestamp
}
requests.post("http://localhost:8000/bourse/index/", json=new_data)

tel_data = {
    "chat_id":"-823775964",
    "text": f"index = {index}"
}
requests.post("https://api.telegram.org/bot5913296732:AAH56G8GyN0HBYrN7Ph3JkVlR2zmYm8EEMQ/sendMessage", json=tel_data)