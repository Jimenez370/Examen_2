Levantar la Infraestructura
Desde la terminal en la raíz del proyecto, levanta los contenedores:

docker compose up -d


Iniciar la API

uvicorn main:app --reload

Base de Datos (MySQL)
La base de datos se configura automáticamente al primer arranque. Para visualizar las tablas manualmente:


docker exec -it mysql_examen mysql -u root -e "USE examen_db; SELECT * FROM insc