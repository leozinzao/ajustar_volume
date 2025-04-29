import csv
import requests

with open('veiculos.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')
    next(leitor) 

    for linha in leitor:
        if len(linha) < 2:
            continue

        placa = linha[0].strip()
        try:
            volume = int(linha[1])
        except:
            print(f"{placa}: volume inválido")
            continue

        if 0 <= volume <= 100:
            try:
                r = requests.post('https://webhook.site/f7c03f51-6f4d-4f07-b1be-812927de76a9', json={'placa': placa, 'volume': volume})
                print(f"{placa}: enviado ({r.status_code})")
            except:
                print(f"{placa}: erro ao conectar")
        else:
            print(f"{placa}: volume fora do intervalo")
