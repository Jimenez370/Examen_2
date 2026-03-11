from pydantic import BaseModel
from typing import Optional

class Inscripcion(BaseModel):
    id: Optional[int] = None
    idioma: str
    nivel: str
    horario: str