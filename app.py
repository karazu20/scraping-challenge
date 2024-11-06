import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request 


def scraping_products(url: str)->list:
    #Se inicia el drive de selenium
    driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(10)

    body = driver.find_element(By.TAG_NAME, "body")

    no_of_pagedowns = 7

    #Bajamos el scroll para que se carguen los productos
    while no_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        no_of_pagedowns-=1

    #Parseamos con BeautifulSoup la página del driver y obtenemos los productos
    bsObj = BeautifulSoup(driver.page_source,  'html5lib')
    articles = bsObj.find_all('article') 
    products = []
    for i in range(15):
        products.append({'product': articles[i].find('span', class_="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body").text,
                            'brand': articles[i].find('span', class_='vtex-product-summary-2-x-productBrandName').text,
                            'price': articles[i].find('div', class_='tiendasjumboqaio-jumbo-minicart-2-x-price').text})

        i+=1
    return products


app = Flask(__name__) 

@app.route('/products', methods=['POST']) 
def get_products(): 
    if(request.method == 'POST'): 
        url = request.form['url']
        data = scraping_products(url)
        return jsonify(data) 
  
  
if __name__ == '__main__': 
    app.run(debug=True) 