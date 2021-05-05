from fastapi import APIRouter, Body
from typing import List
from ....models.ticket import Ticket, TicketCreate
from ....services.ticket import fetch_tickets, retrieve_ticket, create_ticket

router = APIRouter()

@router.get("/ticket", response_model=List[Ticket])
async def fetch_ticket():
    tickets = await fetch_tickets()
    return tickets

@router.get("/ticket/{id_ticket}", response_model=Ticket)
async def retrieve_tickets(id_ticket: int):
    ticket = await retrieve_ticket(id_ticket)
    return ticket

@router.post("/ticket")
async def create_tickets(ticket: TicketCreate):
    ticket = await create_ticket(ticket)
    if ticket:
        return {"message": "Ticket creado con exito"}
    return {"message": "Error al crear ticket"}