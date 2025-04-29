import requests

placa = input("Digite a placa do veículo: ").upper()
volume = int(input("Digite o volume (0 a 100): "))

# criei um link pra testar o envio de dados
url = "https://webhook.site/f7c03f51-6f4d-4f07-b1be-812927de76a9"

dados = {
    "placa": placa,
    "volume_alerta": volume
}

resposta = requests.post(url, json=dados)

if resposta.status_code == 200:
    print("Volume ajustado com sucesso!")
else:
    print("Erro ao ajustar o volume:", resposta.status_code)
