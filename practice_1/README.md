# Práctica 1 - Cloud Storage

Aquí se encuentran las tres fases de la práctica, la cual tiene como objetivo hacer uso de un KVS y un SDK de Amazon Web Services tanto en Python como en JavaScript.

Las tres fases son las siguientes:
* Interfaz CLI utilizando SQLite
* Interfaz CLI utilizando DynamoBB
* Aplicación web para consultas

## Interfaz CLI utilizando SQLite

En esta primera fase se trabaja con Python. Se pueden cargar datos y hacer consultas a una base de datos SQLite.

Para probar el funcionamiento se espera que exitan los datasets: `./phase_1/storage/<nombre-del-dataset>.ttl`.

Una vez que estén disponibles ambos datasets, se debe crear un ambiente virtual e instalar las dependencias.

```bash
$ python3 -m venv venv
$ pip install -r requirements.txt
```

Ya instaladas las dependencias, el código se corre de la siguiente manera:

```bash
$ python loadImages.py <cantidad-de-imagenes>
```

Una vez cargadas las imagenes, se hacen consultas de la siguiente manera:

```bash
$ python queryImages.py <palabras-a-buscar>
```

De haber resultados, se imprimirá una lista con los URLs de las imágenes correspondientes con la consulta.
