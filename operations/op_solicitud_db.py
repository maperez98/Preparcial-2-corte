from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from models.solicitud import SolicitudBase, SolicitudID, SolicitudUpdate

def crear_solicitud(solicitud: SolicitudBase, session: Session):
    nueva = SolicitudID.model_validate(solicitud)
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return nueva

def listar_solicitudes(session: Session):
    return session.exec(select(SolicitudID)).all()

def buscar_solicitud(id: int, session: Session):
    try:
        return session.get_one(SolicitudID, id)
    except NoResultFound:
        return None

def actualizar_solicitud(id: int, datos: SolicitudUpdate, session: Session):
    solicitud = buscar_solicitud(id, session)
    if solicitud is None:
        return None
    cambios = datos.model_dump(exclude_unset=True)
    solicitud.sqlmodel_update(cambios)
    session.add(solicitud)
    session.commit()
    session.refresh(solicitud)
    return solicitud

def eliminar_solicitud(id: int, session: Session):
    try:
        solicitud = session.get_one(SolicitudID, id)
        session.delete(solicitud)
        session.commit()
        return solicitud
    except NoResultFound:
        return None