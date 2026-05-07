from sqlmodel import SQLModel, Field
from typing import Optional

class ClienteBase(SQLModel):
    nombre: str = Field(min_length=3, max_length=100)
    telefono: str = Field(min_length=7, max_length=15)
    localidad: str = Field(default="Bosa")
    activo: bool = Field(default=True)

class ClienteID(ClienteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ClienteUpdate(SQLModel):
    telefono: Optional[str] = Field(default=None, min_length=7, max_length=15)
    activo: Optional[bool] = Field(default=None)