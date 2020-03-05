# Práctica 1 - Cloud Storage

Aquí se encuentran las tres fases de la práctica, la cual tiene como objetivo hacer uso de un KVS y un SDK de **Amazon Web Services** tanto en **Python** como en **JavaScript**.

Las tres fases son las siguientes:
* Interfaz CLI utilizando SQLite
* Interfaz CLI utilizando DynamoBB
* Aplicación web para consultas

## Fase 1 - Interfaz CLI utilizando SQLite

En esta primera fase se trabaja con **Python**. Se pueden cargar datos y hacer consultas a una base de datos SQLite.

Para probar el funcionamiento se espera que exitan los datasets: `./phase_1/storage/<nombre-del-dataset>.ttl`

Una vez que estén disponibles ambos datasets, se debe crear un ambiente virtual e instalar las dependencias.
```bash
./phase_1$ python3 -m venv venv
./phase_1$ source venv/bin/activate
./phase_1$ pip install -r requirements.txt
```
Ya instaladas las dependencias, el código se corre de la siguiente manera:
```bash
./phase_1$ python loadImages.py <cantidad-de-imagenes>
```
Una vez cargadas las imagenes, se hacen consultas de la siguiente manera:
```bash
./phase_1$ python queryImages.py <palabras-a-buscar>
```
De haber resultados, se imprimirá una lista con los URLs de las imágenes correspondientes con la consulta.

## Fase 2 - Interfaz CLI utilizando DynamoDB

En esta segunda fase también se trabaja con **Python**. Se pueden cargar datos y hacer consultas a una base de datos **DynamoDB** de AWS.

Para probar el funcionamiento se espera que exitan los datasets: `./phase_2/storage/<nombre-del-dataset>.ttl` y que estén las credenciales correctas en el archivo `~/.aws/config` en Linux o `C:\Users\<USERNAME>\.aws\config` en Windows, el cual debe verse así:

```bash
[default]
aws_access_key_id=REMPLAZAR_POR_TU_LLAVE
aws_secret_access_key=REMPLAZAR_POR_TU_LLAVE
aws_session_token=REMPLAZAR_POR_TU_LLAVE
region=REMPLAZAR_CON_LA_REGION
```

Una vez que estén disponibles ambos datasets y el archivo de configuración, se debe crear un ambiente virtual e instalar las dependencias.
```bash
./phase_2$ python3 -m venv venv
./phase_2$ source venv/bin/activate
./phase_2$ pip install -r requirements.txt
```
Ya instaladas las dependencias, el código se corre de la siguiente manera:
```bash
./phase_2$ python loadImages.py <cantidad-de-imagenes>
```
Una vez cargadas las imagenes, se hacen consultas de la siguiente manera:
```bash
./phase_2$ python queryImages.py <palabras-a-buscar>
```
De haber resultados, se imprimirá una lista con los URLs de las imágenes correspondientes con la consulta.

## Fase 3 - Interfaz CLI utilizando DynamoDB

En esta tercera fase se trabaja con **Node.js** y **jQuery**.
El objetivo es hacer consultas a la base de datos **DynamoDB** previamente cargada en la fase 2 en un ambiente web.

Para probar el funcionamiento es necesario que el archivo `./phase_3/config.json` se llene de la siguiente manera:
```json
{
    "region": "us-east-1",
    "accessKeyId": "REMPLAZAR_POR_TU_LLAVE",
    "secretAccessKey": "REMPLAZAR_POR_TU_LLAVE",
    "sessionToken": "REMPLAZAR_POR_TU_LLAVE"
}
```
Para probar la aplicación corre los siguientes comandos:
```bash
./phase_3$ npm install
./phase_3$ npm start
```
Una vez corriendo en `http://localhost:3000` se podrán hacer consultas de una varias palabras y se mostrarán las imágenes que correspondan y que existan en la base de datos de **DynamoDB**.
