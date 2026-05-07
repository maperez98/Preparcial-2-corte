from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from models.cliente import ClienteBase, ClienteID, ClienteUpdate

def crear_cliente(cliente: ClienteBase, session: Session):
    nuevo = ClienteID.model_validate(cliente)
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo

def listar_clientes(session: Session):
    return session.exec(select(ClienteID)).all()

def buscar_cliente(id: int, session: Session):
    try:
        return session.get_one(ClienteID, id)
    except NoResultFound:
        return None

def actualizar_cliente(id: int, datos: ClienteUpdate, session: Session):
    cliente = buscar_cliente(id, session)
    if cliente is None:
        return None
    cambios = datos.model_dump(exclude_unset=True)
    cliente.sqlmodel_update(cambios)
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

def eliminar_cliente(id: int, session: Session):
    cliente = buscar_cliente(id, session)
    if cliente is None:
        return None
    cliente.activo = False
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente