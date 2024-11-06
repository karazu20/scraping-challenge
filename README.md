# Scraping Challenge

## Requerimientos previos
```sh
python 3.10
google-chrome
chromedriver
```

## Crear Entorno virtual

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Levantar con Docker

Actualmente se puede construir la imagen, pero tiene un error al tratar de ejecutar la api desde el container debido a una dependencia del chromedriver

```sh
docker build --tag scraping-challenge .
docker run  -p 5000:5000 scraping-challenge
```

## Ejecutar parser Json
Dentro del entorno virtual ejecutamos 

```sh
python format_json.py 
```
Este deja la salida en output.json

## Ejecutar API del scraping
Actualmente la versión actual sólo ejecuta por entorno virtual, para eso dentro del entorno virtual

```sh
python app.py 
```
esto levanta la app en 127.0.0.1:5000, posteriromente podemos probar desde un cliente rest como Postman o usando el comando curl, aqui un ejemplo:

```sh
curl --location 'http://127.0.0.1:5000/products' --form 'url="https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas"'
```