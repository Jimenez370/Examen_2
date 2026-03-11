class InscripcionService:
    def __init__(self, db, mq):
        self.db = db
        self.mq = mq

    def crear_inscripcion(self, datos):
        # Guardar en DB
        self.db.save(datos)
        # Enviar a RabbitMQ para generar el recibo
        mensaje = f"RECIBO GENERADO: {datos.idioma} - Nivel {datos.nivel} - {datos.horario}"
        self.mq.send(mensaje)
        return {"mensaje": "Inscripción exitosa y recibo enviado a cola"}

    def listar_inscripciones(self):
        return self.db.get_all()