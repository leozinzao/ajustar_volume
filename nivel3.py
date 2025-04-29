import csv
import requests

url = "https://webhook.site/f7c03f51-6f4d-4f07-b1be-812927de76a9"

with open("veiculos.csv") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")
    next(leitor) 

    for placa, volume in leitor:
        try:
            volume = int(volume)
            if 0 <= volume <= 100:
                resposta = requests.post(url, json={"placa": placa, "volume": volume})
                print(f"{placa}: {resposta.status_code}")
            else:
                print(f"{placa}: volume fora do intervalo (0 a 100)")
        except:
            print(f"{placa}: erro ao processar")
