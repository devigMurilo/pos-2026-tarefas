import json
from pathlib import Path


def imprimir_lista(titulo, itens):
    if itens:
        print(f"{titulo}:")
        for item in itens:
            print(f"- {item}")


def imprimir_imovel(imovel):
    proprietario = imovel["proprietario"]
    endereco = imovel["endereco"]
    caracteristicas = imovel["caracteristicas"]

    print("\nDescricao:", imovel["descricao"])
    print("Valor:", imovel["valor"])

    print("\nProprietario:")
    print("Nome:", proprietario["nome"])
    imprimir_lista("Emails", proprietario.get("emails", []))
    imprimir_lista("Telefones", proprietario.get("telefones", []))

    print("\nEndereco:")
    print("Rua:", endereco["rua"])
    print("Bairro:", endereco["bairro"])
    print("Cidade:", endereco["cidade"])
    if "numero" in endereco:
        print("Numero:", endereco["numero"])

    print("\nCaracteristicas:")
    print("Tamanho:", caracteristicas["tamanho"], "m2")
    print("Numero de quartos:", caracteristicas["numQuartos"])
    print("Numero de banheiros:", caracteristicas["numBanheiros"])


arquivo_json = Path(__file__).parent / "imobiliaria.json"

with open(arquivo_json, encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

imoveis = dados["imobiliaria"]["imoveis"]

print("---IMOVEIS---")
for indice, imovel in enumerate(imoveis, start=1):
    endereco = imovel["endereco"]
    print(f"{indice} - {imovel['descricao']} ({endereco['cidade']})")

opcao = input("Digite o id do imovel para saber mais: ")

if opcao.isdigit() and 1 <= int(opcao) <= len(imoveis):
    imprimir_imovel(imoveis[int(opcao) - 1])
else:
    print("Imovel nao encontrado.")
