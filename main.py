from fastapi import FastAPI
from src.domain.models import Inscripcion
from src.infrastructure.db_repository import MySQLRepository
from src.infrastructure.mq_adapter import RabbitAdapter
from src.application.services import InscripcionService

app = FastAPI()

# Instanciamos los adaptadores e inyectamos al servicio
db = MySQLRepository()
mq = RabbitAdapter()
service = InscripcionService(db, mq)

@app.get("/Lista_inscripciones")
def listar_inscripciones():
    return service.listar_inscripciones()

@app.post("/inscripciones")
def inscribir(ins: Inscripcion):
    return service.crear_inscripcion(ins)