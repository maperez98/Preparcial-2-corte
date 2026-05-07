from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

class TipoAyuda(str, Enum):
    silla_ruedas = "silla_ruedas"
    silla_sanitaria = "silla_sanitaria"
    kit_visual = "kit_visual"
    kit_cognitivo = "kit_cognitivo"

class SolicitudBase(SQLModel):
    tipo_ayuda: TipoAyuda
    observaciones: Optional[str] = Field(default=None, max_length=300)
    cliente_id: int = Field(foreign_key="clienteid.id")

class SolicitudID(SolicitudBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class SolicitudUpdate(SQLModel):
    observaciones: Optional[str] = Field(default=None, max_length=300)