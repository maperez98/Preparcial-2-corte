from fastapi import FastAPI, HTTPException
from models.cliente import ClienteBase, ClienteID, ClienteUpdate
from models.solicitud import SolicitudBase, SolicitudID, SolicitudUpdate
from db import SessionDep, create_all_tables
from operations.op_cliente_db import (
    crear_cliente, listar_clientes, buscar_cliente,
    actualizar_cliente, eliminar_cliente
)
from operations.op_solicitud_db import (
    crear_solicitud, listar_solicitudes, buscar_solicitud,
    actualizar_solicitud, eliminar_solicitud
)

app = FastAPI(lifespan=create_all_tables)

# --- CLIENTES ---

@app.post("/cliente", response_model=ClienteID)
def crear(cliente: ClienteBase, session: SessionDep):
    return crear_cliente(cliente, session)

@app.get("/cliente", response_model=list[ClienteID])
def listar(session: SessionDep):
    return listar_clientes(session)

@app.get("/cliente/{id}", response_model=ClienteID)
def ver_uno(id: int, session: SessionDep):
    cliente = buscar_cliente(id, session)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.patch("/cliente/{id}", response_model=ClienteID)
def modificar(id: int, datos: ClienteUpdate, session: SessionDep):
    resultado = actualizar_cliente(id, datos, session)
    if not resultado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return resultado

@app.delete("/cliente/{id}", response_model=ClienteID)
def desactivar(id: int, session: SessionDep):
    resultado = eliminar_cliente(id, session)
    if not resultado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return resultado

# --- SOLICITUDES ---

@app.post("/solicitud", response_model=SolicitudID)
def crear_sol(solicitud: SolicitudBase, session: SessionDep):
    cliente = buscar_cliente(solicitud.cliente_id, session)
    if not cliente:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    return crear_solicitud(solicitud, session)

@app.get("/solicitud", response_model=list[SolicitudID])
def listar_sol(session: SessionDep):
    return listar_solicitudes(session)

@app.get("/solicitud/{id}", response_model=SolicitudID)
def ver_sol(id: int, session: SessionDep):
    solicitud = buscar_solicitud(id, session)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud

@app.patch("/solicitud/{id}", response_model=SolicitudID)
def modificar_sol(id: int, datos: SolicitudUpdate, session: SessionDep):
    resultado = actualizar_solicitud(id, datos, session)
    if not resultado:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return resultado

@app.delete("/solicitud/{id}", response_model=SolicitudID)
def borrar_sol(id: int, session: SessionDep):
    resultado = eliminar_solicitud(id, session)
    if not resultado:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return resultado