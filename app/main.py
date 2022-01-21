from bs4 import BeautifulSoup
import requests

url = requests.get(
    "http://www.meteo.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml"
)

print(url)
arso = BeautifulSoup(url.content, "xml")

entries = arso.find_all("metData")

for metData in entries:
    title = metData.domain_longTitle.text
    temperature = metData.t.text
    print(f" City: {title} \n Temperature: {temperature}°C \n --------------------")

   
