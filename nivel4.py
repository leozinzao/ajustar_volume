import csv
import requests

url = "https://webhook.site/f7c03f51-6f4d-4f07-b1be-812927de76a9"

with open("veiculos.csv") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")
    next(leitor)  

    for placa, volume in leitor:
        try:
            volume = int(volume)
            if volume < 0 or volume > 100:
                print(f"{placa}: volume fora do intervalo (0 a 100)")
            else:
                resposta = requests.post(url, json={"placa": placa, "volume": volume})
                if resposta.status_code == 200:
                    print(f"{placa}: Volume ajustado com sucesso!")
                else:
                    print(f"{placa}: erro ao ajustar volume (Status {resposta.status_code})")
        except ValueError:
            print(f"{placa}: erro ao processar volume")
        except requests.exceptions.RequestException as e:
            print(f"{placa}: erro de conexão com o servidor")
