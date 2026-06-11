import requests
from xml.dom import minidom

URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
ops = {
    "1": ("ListOfContinentsByName", "http://www.oorsprong.org/websamples.countryinfo/ListOfContinentsByName"),
    "2": ("ListOfContinentsByCode", "http://www.oorsprong.org/websamples.countryinfo/ListOfContinentsByCode"),
    "3": ("ListOfCurrenciesByName", "http://www.oorsprong.org/websamples.countryinfo/ListOfCurrenciesByName"),
}

def envelope(op):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.oorsprong.org/websamples.countryinfo">
  <soap:Body><web:{op}/></soap:Body>
</soap:Envelope>"""

menu = "1 ListOfContinentsByName\n2 ListOfContinentsByCode\n3 ListOfCurrenciesByName\n0 Sair\nEscolha: "

while True:
    print(menu)
    choice = input("Escolha uma opção: ")
    if choice == "0":
        break
    if choice in ops:
        op, url = ops[choice]
        response = requests.post(URL, data=envelope(op), headers={"Content-Type": "text/xml; charset=utf-8"})
        if response.status_code == 200:
            if op == "ListOfContinentsByName":
                print(minidom.parseString(response.text).documentElement.getElementsByTagName("ListOfContinentsByNameResult")[0].firstChild.data)
            elif op == "ListOfContinentsByCode":
                print(minidom.parseString(response.text).documentElement.getElementsByTagName("ListOfContinentsByCodeResult")[0].firstChild.data)
            elif op == "ListOfCurrenciesByName":
                print(minidom.parseString(response.text).documentElement.getElementsByTagName("ListOfCurrenciesByNameResult")[0].firstChild.data)
# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{op}> 
                        xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</{op}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", URL, headers=headers, data=payload)

