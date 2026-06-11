import zeep

# define a URL do WSDL
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

numero = input("Digite um número para converter em palavras: ")


# faz a chamada do serviço
result = client.service.NumberToWords(ubiNum=numero)
# imprime o resultado
print(f"O número {numero} em palavras é {result}")


