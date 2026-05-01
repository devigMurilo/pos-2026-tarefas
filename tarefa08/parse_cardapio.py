from pathlib import Path
from xml.dom.minidom import parse

dom = parse(str(Path(__file__).parent / "cardapio.xml"))

# Elemento raiz do XML (cardapio)
cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "prato"
pratos = cardapio.getElementsByTagName('prato')

print("---MENU---")
for prato in pratos:
    id = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f"{id} - {nome}")
opcao = input("Digite o id do prato para saber mais: ")

for prato in pratos:
    if opcao == prato.getAttribute("id"):
        nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
        preco = prato.getElementsByTagName("preco")[0].firstChild.nodeValue
        moeda = prato.getElementsByTagName("preco")[0].getAttribute("moeda")
        calorias = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue
        tempo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue
        ingredientes = prato.getElementsByTagName("ingrediente")

        print("\nNome:", nome)
        print("Descrição:", descricao)
        print("Ingredientes:")
        for ingrediente in ingredientes:
            print("-", ingrediente.firstChild.nodeValue)
        print("Preço:", moeda, preco)
        print("Calorias:", calorias, "kcal")
        print("Tempo de preparo:", tempo)
