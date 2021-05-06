from fastapi import APIRouter, Body, HTTPException, status, Depends
from typing import List
from fastapi_utils.cbv import cbv
from ....models.ticket import TicketOut, TicketIn
from ....services.ticket import (
    fetch_ticket,
    retrieve_ticket,
    create_ticket,
    update_ticket,
    delete_ticket
)

router = APIRouter()
@cbv(router)
class Ticket:
    hola = "fdf"
    @router.get(
        "/ticket", 
        response_model=List[TicketIn], 
        status_code=status.HTTP_200_OK,
        tags=["Ticket"]
    )
    async def fetch(self):
        tickets = await fetch_ticket()
        if tickets:
            return tickets
        raise HTTPException(status_code=404, detail="No se encontraron tickets.")


    @router.get(
        "/ticket/{id_ticket}", 
        response_model=TicketIn, 
        status_code=status.HTTP_200_OK,
        tags=["Ticket"]
    )
    async def retrieve(self, id_ticket: int):
        ticket = await retrieve_ticket(id_ticket)
        if ticket:
            return ticket
        raise HTTPException(status_code=404, detail="Ticket no encontrado.")


    @router.post(
        "/ticket", 
        status_code=status.HTTP_201_CREATED,
        tags=["Ticket"]
    )
    async def create(self, ticket: TicketIn):
        ticket = await create_ticket(ticket)
        if ticket:
            return {"message": "Ticket creado con exito"}
        raise HTTPException(status_code=404, detail="Error al crear ticket.")


    @router.put(
        "/ticket/{id_ticket}", 
        status_code=status.HTTP_200_OK,
        response_model=TicketIn,
        tags=["Ticket"]
    )
    async def update(self, id_ticket: int, ticket: TicketOut):
        ticket = await update_ticket(id_ticket, ticket)
        if ticket:
            return ticket
        raise HTTPException(status_code=404, detail="Error al actualizar ticket.")
    
    
    @router.delete(
        "/ticket/{id_ticket}", 
        response_model=TicketOut, 
        status_code=status.HTTP_200_OK,
        tags=["Ticket"]
    )
    async def delete(self, id_ticket: int):
        ticket = await delete_ticket(id_ticket)
        if ticket:
            return ticket
        raise HTTPException(status_code=404, detail="Error al eliminar ticket.")
