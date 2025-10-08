# **Programación Alex**

## Contexto
Trabajo con LLM
GCP
n8n
sistema contable con prompts de usuario
generar documentos con pies de nota
descargables
DB de docs
API para habilitar comms
crear un modelo propio experto en contabilidad (números)
leyes/normativa
scrapping de plataformas informativas
aqlimentar con DBs/docs

## Pendientes
- [X] conectar con gemini
- [ ] crear webhook

- [X] manejo Sqlite
- [ ] manejo mongoDB
- [ ] tensorflow

- [X] webhook con n8n
- [ ] extraccion de actualicese.com
- [ ] entrenar un modelo (actualicese.com)

- [ ] GCP
- [ ] auth
- [X] github
- [X] crear un modelo
- [X] tortoise-orm

## **Intro a Python**
- basado en C
- interpretado (compila modulos)
- debilmente tipado
- solo con un script se puede correr
- software libre entonces tiene un montón de soporte
- hace de todo (video juegos, señal, datos, graficas, scrapping, DB, web, android, exe, ai, imagen, video, etc)

### Documentacion
https://www.python.org/downloads/

## **Modulos famosos**
### pillow

Módulo para procesamiento de imagen. Manipula imagenes cambiandoles el tamaño, obteniendo información de color, metadata, etc.
Obtiene la informacion y la organiza en estructura de matriz.
### pickle

Convierte objetos en archivos comprimidos que se pueden cargar luego. Se suele utilizar para tener en un archivo un resultado de un modelo entrenado, por ejemplo
### pygame

Libreria para desarrollo de videojuegos. Se puede utilizar tambien para crar interfaces de usuario.
### py2exe

Convierte un script o proyecto de python a un ejecutable de windows
### pyaudio

Libreria para procesamiento de audio. Similar a pillow, se obtiene y se organiza la informacion obtenida de un archivo de audio. Gestiona conexiones de entradas y salidas de audio del computador.
### csv

Libreria para leer archivos csv y tenerlos en una estructura util. Viene incluido en la instalacion de Python
### pandas

Libreria para obtener informacion de archivos csv, excel y permite realizar operaciones.
### numpy

Libreria para operacion rapida de datos (usa C). Tambien permite crear matrices y vectores en convenciones similares a Matlab y R

### numba

Libreria para compilar codigo y volverlo mas rapido
### scipy

Libreria para operaciones cientificas. Generalmente se utiliza para crear filtros, operaciones trigonometricas, etc
### matplotlib

Libreria para manipular informacion similar a matlab enfocado a graficas.
### scikit-learn

Libreria para crar modelos de deep-learn, entrenarlos y usarlos contra informacion nueva
### requests

Libreria para realizar peticiones.

### pydantic

Libreria para organizar objetos como modelos, realizar validaciones y restricciones.
### django/flask/fastapi

Frameworks para desarrollo web. Facilitan la creación de un servicio y algunos para gestionar bases de datos.
### beautiful soup

libreria para obtener informacion de paginas web
### pytorch

libreria para entrenar y analizar deferentes modelos. Tiene mayor desarrollo enfocado a procesamiento de lenguaje

## **Generales**
### Tutoriales utiles
- https://www.w3schools.com/python/

buen tutorial desde ceros
provee un ambiente para ejecucion de codigo de python

- https://www.geeksforgeeks.org/python/python-programming-language-tutorial/

suele tener soluciones a problemas comunes un poco mas especificos (por ej. "quiero reconocer un email a traves de expresiones regulares")

### vscode

Editor de codigo versatil. Permite instalar "add-ons" que facilitan programar. Entre los instalables se encuentran subrayadores propios de lenguaje (python), control de versionamientos (github), graficos de UML (diagramas de flujo, DBs, etc), formatear codigo en estilos automaticamente, entre otros.

### crear un ambiente (venv)

Python permite crear diferentes instancias de si mismo en un ambiente. Esto permite instalar dependencias especificas sin entrar en conflicto con versiones que otros ambientes o la intalacion global puedan tener

```bash
python -m venv ../ruta/a/nuevo/ambiente
```

### instalar dependencias (pip)
este instalador facilita la adicion de modulos nuevos a nuestro ambiente

```bash
pip install pandas==1.0.0
```

Nota: tambien se pueden instalar varios paquetes en serie si se tienen listados en un archivo
 
```bash
pip install -r requirements.txt
```

### Gestion de migraciones con aerich
Para ligar lo que hace tortoise en el codigo con aerich y saber en que estado esta la db
```bash
aerich init -t path.to.your.settings.TORTOISE_ORM -p your_app_name.models
```

conectar con la db
```bash
aerich init-db
```

crear un nuevo archivo de migracion (se hace cuando un modelo nuevo se crea, o cuando se borra/modifica uno existente)
```bash
aerich migrate --name your_migration_name
```

aplicar las migraciones que esten pendientes
```bash
aerich upgrade
```

## **Consumir csv/excel con pandas/csv**
- crear un archivo .py
- uso de modulo `csv` para leer archivo .csv
- se puede imprimir fila por fila
- si queremos crear un archivo de excel, necesitamos instalar `openpyxl`

### Documentacion
https://docs.python.org/3/library/csv.html


## **web scrapping**
- crear un archivo .py
- escoger una url
- convertir a BS
- mostrar informacion filtrada

## **Frameworks para servicios web**
### FastAPI
Framework reciente que permite trabajar con concurrencia facilmente, por eso se categoriza como el framework mas rápido
- requiere uvicorn

```bash
 uvicorn fastapi_example:app --port=8000
```
- funciona con pydantic


### Documentacion
https://fastapi.tiangolo.com/tutorial

## repositiorios?
## manejo de Sqlite
## manejo de mongoDB
## ORM
## conexion con AWS/GCP
## scikit learn


