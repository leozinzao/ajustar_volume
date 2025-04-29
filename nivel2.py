import csv
import requests

url = "	https://webhook.site/f7c03f51-6f4d-4f07-b1be-812927de76a9"

with open("veiculos.csv") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";") 
    next(leitor) 

    for linha in leitor:
        if len(linha) < 2:
            continue 

        placa = linha[0]
        volume = int(linha[1])
        dados = {"placa": placa, "volume_alerta": volume}
        resposta = requests.post(url, json=dados)
        print(f"{placa}: {resposta.status_code}")
