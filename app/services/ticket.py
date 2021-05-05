from ..db.db import execute, fetch
import datetime

async def fetch_tickets():
    query = """select * from tickets"""
    tickets = await fetch(query, False)
    return tickets

async def retrieve_ticket(id_ticket):
    query = """select * from tickets where id_ticket = :id_ticket"""
    values = {"id_ticket": id_ticket}
    ticket = await fetch(query, True, values)
    return ticket

async def create_ticket(ticket):
    query = """insert into tickets(title, body, urgency, status, published_date)
               values(:title, :body, :urgency, :status, :published_date)"""
    values = dict(ticket)
    try:
        await execute(query, False, values)
        return True
    except:
        return False