from pydantic import BaseModel
from typing import Optional
import datetime

class Ticket(BaseModel):
    id_ticket: Optional[int]
    title: str
    body: str
    urgency: str
    status: str
    published_date: Optional[datetime.date] = datetime.date.today().strftime("%Y-%m-%d")
    
class TicketCreate(BaseModel):
    title: str
    body: str
    urgency: str
    status: str
    published_date = datetime.date.today()
