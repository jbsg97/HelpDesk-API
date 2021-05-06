from ..db.db import execute, fetch
import datetime


    
async def fetch_ticket():
    query = """select * from tickets"""
    try:
        tickets = await fetch(query, False)
        return tickets
    except:
        return None


async def retrieve_ticket(id_ticket):
    query = """select * from tickets where id_ticket = :id_ticket"""
    values = {"id_ticket": id_ticket}
    try:
        ticket = await fetch(query, True, values)
        return ticket
    except:
        return None


async def create_ticket(ticket):
    query = """insert into tickets(title, body, urgency, status, published_date)
            values(:title, :body, :urgency, :status, :published_date)"""
    values = {
        'title': ticket.title,
        'body': ticket.body,
        'urgency': ticket.urgency,
        'status': ticket.status,
        'published_date': datetime.date.today()    
    }
    try:
        await execute(query, False, values)
        return True
    except:
        return False
    

async def update_ticket(id_ticket, ticket):
    query = """update tickets set title=:title, body=:body, urgency=:urgency, status=:status where id_ticket=:id_ticket"""
    values = {
        'title': ticket.title,
        'body': ticket.body,
        'urgency': ticket.urgency,
        'status': ticket.status,
        'id_ticket': id_ticket    
    }
    
    try:
        await execute(query, False, values)
        ticket = await retrieve_ticket(id_ticket)
        return ticket
    except Exception as e:
        print(e)
        return None


async def delete_ticket(id_ticket):
    query = """delete from tickets where id_ticket = :id_ticket"""
    values = {"id_ticket": id_ticket}
    try:
        ticket = await retrieve_ticket(id_ticket)
        await execute(query, False, values)
        return ticket
    except:
        return None
