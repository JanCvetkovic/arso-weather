from bs4 import BeautifulSoup
import requests

url = requests.get(
    "http://www.meteo.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml"
)

arso = BeautifulSoup(url.content, "xml")

entries = arso.find_all("metData")

for metData in entries:
    title = metData.domain_longTitle.text
    temperature = metData.t.text

    moisture = metData.rh.text
    altitude = float(metData.domain_altitude.text)
    altitude = round(altitude)
    print(
        f" City: {title} ({altitude}m) \n Temperature: {temperature}°C \n Moisture: {moisture}%\n --------------------"
    )
