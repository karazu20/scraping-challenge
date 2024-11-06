import json
from urllib.request import urlopen
import csv 


def writter_csv(data_dict: dict):
    #Guardamos la salida en un formato csv
    with open('output.csv', 'w', newline='') as file: 
        writer = csv.DictWriter(file, data_dict.keys())
        writer.writeheader()
        writer.writerow(data_dict)

def search_attr (attrs: list, name_attr: str)->str:
    for att in attrs:
        if att['name']==name_attr:
            return att


def parser_url_json(url_json: str) -> dict:
    data = urlopen(url_json)
    data = str (data.read(), encoding='utf-8')
    data = json.loads(data)

    properties_to_format = [
            'allergens',
            'sku',
            'vegan',
            'kosher',
            'organic',
            'vegetarian',
            'gluten_free',
            'lactose_free',
            'package_quantity',
            'unit_size',
            'net_weight',
    ]
    #Se obtiene el valor del campo custom_attributes para obtener las properties_to_format
    attributes_raw = data['allVariants'][0]['attributesRaw']
    attributes_cust = search_attr(attributes_raw,  'custom_attributes')
    properties = json.loads(attributes_cust['value']['es-CR'])

    #Generamos un dic con los valores de la propiedades properties_to_format
    data={} 
    for p in properties_to_format:
        if p == 'allergens':
            data [p]= properties[p]['value'][0]['name']
        else:    
            data [p]= properties[p]['value']

    return data


if __name__ == "__main__":
    url = 'https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json'
    data = parser_url_json(url)
    writter_csv(data)

