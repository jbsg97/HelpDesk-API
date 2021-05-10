from pydantic import BaseModel
from typing import Optional
import datetime

class UserOut(BaseModel):
    id_user: int
    username: str
    password: str
    email: str
    name: str
    last_name: str
    register_date: Optional[datetime.date] = datetime.date.today().strftime("%Y-%m-%d")
    disabled: Optional[bool] = False
    

class UserIn(BaseModel):
    username: str
    password: str
    email: str
    name: str
    last_name: str
    disabled: Optional[bool] = False
    

class Token(BaseModel):
    access_token: str
    token_type: str
