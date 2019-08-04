import csv
from bs4 import BeautifulSoup as bs4
import requests
import re


def write_output(data):
    with open('data.csv', mode='w') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # Header
        writer.writerow(["locator_domain", "location_name", "street_address", "city", "state", "zip", "country_code",
                         "store_number", "phone", "location_type", "latitude", "longitude", "hours_of_operation"])
        # Body
        for row in data:
            writer.writerow(row)



def fetch_data():
    url = 'http://www.mccarthytire.com/Locations'
    base_url = 'http://www.mccarthytire.com' + '/Locations'
    r = requests.get('http://www.mccarthytire.com/Locations')
    soup = bs4(r.text, 'lxml')
    return_main_object = []
    zip = [a.text[124:200].strip().replace('PA', '').replace('ville', '').replace('MD','').replace('V','').replace('SC','').replace('NY','').replace('Horseheads','').replace('NC','').replace('A','').replace('G','').replace('reen', '').replace('g', '').replace('n', '') for a in soup.find_all("div", {'class': 'locationInfo'})]
    mess = ['PA', 'ville', 'MD', 'V', 'SC', 'NY', 'Horseheads', 'NC', 'A', 'G','reen']
    state = [a.text[121:130].strip().replace('\r\n', '').split('br') for a in soup.find_all("div", {'class': 'locationInfo'})]
    name = [a.text.replace("<", " <").replace(">", ">\n").replace('\r\n', '').replace('\n', '').strip()[:13] for a in soup.find_all('div', {'class': 'locationInfo'})]
    ad = [a.text.replace("<", " <").replace(">", ">\n").replace('\r\n', '').replace('\n', '').strip()[55:90] for a in
            soup.find_all('div', {'class': 'locationInfo'})]
    # Seperate the city and the zip
    city_zip = [a.text.replace("<", " <").replace(">", ">\n").replace('\r\n', '').replace('\n', '').replace('PA', '').replace('MD','').replace('V','').replace('SC','').replace('NY','').replace('NJ', '').replace(',', '').strip()[96: 133] for a in
            soup.find_all('div', {'class': 'locationInfo'})]
    phone = [a.text.replace("<", " <").replace(">", ">\n").replace('\r\n', '').replace('\n', '').strip() for a in soup.find_all('div', {'class':'locphone'})]
    hours = [a.text.replace("<", " <").replace(">", ">\n").replace('\r\n', '').replace('\n', '').strip() for a in soup.find_all('div', {'class': 'locationhours'})]
    page = 'http://www.mccarthytire.com/Locations'
    country_code = 'US'
    store = []
    store.append(base_url)
    store.append(name)
    store.append(ad)
    store.append(city_zip)
    store.append(state)
    store.append(city_zip)
    store.append(country_code)
    store.append('<MISSING>')
    store.append(phone)
    store.append('<MISSING>')
    store.append('<MISSING>')
    store.append('<MISSING>')
    store.append(hours)
    return_main_object.append(store)
    return return_main_object

def scrape():
    data = fetch_data()
    write_output(data)



scrape()