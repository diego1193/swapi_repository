# Setup
1. Habilitar el ssh root de Github.
2. Crear o modificar ~/.aws/credentials utilizando la credenciales de AWS.
3. Instalar dependencias del SO:
 - Ubuntu:
```
sudo apt install libgeos-dev binutils libproj-dev gdal-bin gettext curl \
python3-dev python3-venv python3-pip \
build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev \
```
4. Crear environment: `python3 -m venv .env`
5. Pip install:
```
pip install -r requirements.txt
pip install -r requirements_dev.txt
```
6. Instalar Docker y crear los siguientes containers (solo necesario para correr localmente el proyecto):
 - PostgreSQL
 ```
 docker run --name postgis -e POSTGRES_USER=postgres -e POSTGRES_PASS=root -e POSTGRES_DBNAME=gis -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -d kartoza/postgis:9.6-2.4
 ```
 - Redis
 ```
 docker run --name redis -d redis
 ```
 - RabbitMQ. Al crear el contaianer debes crear el vhost `lqn`.
 ```
 docker run -d --hostname rabbit --name rabbit -e RABBITMQ_DEFAULT_USER=rabbit -e RABBITMQ_DEFAULT_PASS=rabs rabbitmq:3-management
 ```
 - MongoDB
 ```
 docker run --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=lqn -e MONGO_INITDB_ROOT_PASSWORD=a86HViWA mongo:5
 ```

## Crear versiones nuevas de docker-base (usadas en AWS para crear el ECR)
Generar la versión localmente. Toma en cuenta que `<version>` indica la versión generada o latest.
```
docker build . --file Dockerfile-base --tag gustav0lqn/lqn-images:<version> --tag gustav0lqn/lqn-images:latest
```

#### Hacer push al docker hub:
Primero debes estar logeado con la cuenta de LQN:
```
docker login -u gustav0lqn -p 'Zxvf^9QZUS!5'
```

Y luego hacer el push. Deben hacerlo 2 veces la primera vez con el número de versión y la segunda con `latest`.
```
docker push gustav0lqn/lqn-images:<version>
```

Para verificar si quedó bien la imagen base podemos usar el siguiente comando, que es básicamente lo que ejecuta AWS:
```
docker build . --tag lqn:1
```
