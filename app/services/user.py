from ..db.db import execute, fetch
import datetime

async def fetch_user():
    query = """select * from users"""
    try:
        users = await fetch(query, False)
        return users
    except:
        return None


async def retrieve_user(id_user):
    query = """select * from users where id_user = :id_user"""
    values = {"id_user": id_user}
    try:
        user = await fetch(query, True, values)
        return user
    except:
        return None


async def create_user(user):
    query = """insert into users(username, password, email, name, last_name, register_date, disabled)
            values(:username, :password, :email, :name, :last_name, :register_date, :disabled)"""
    values = {
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'name': user.name,
        'last_name': user.last_name,
        'register_date': datetime.date.today(),
        'disabled': user.disabled
    }
    
    try:
        await execute(query, False, values)
        return True
    except Exception as e:
        print(e)
        return False
    

async def update_user(id_user, user):
    query = """
        update users 
        set 
        username=:username, 
        password=:password, 
        email=:email, 
        name=:name, 
        last_name=:last_name, 
        disabled=:disabled 
        where id_user=:id_user"""

    values = {
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'name': user.name,
        'last_name': user.last_name,
        'disabled': user.disabled,
        'id_user': id_user
    }
    
    try:
        await execute(query, False, values)
        user = await retrieve_user(id_user)
        return user
    except Exception as e:
        return None


async def delete_user(id_user):
    query = """delete from users where id_user = :id_user"""
    values = {"id_user": id_user}
    try:
        user = await retrieve_user(id_user)
        await execute(query, False, values)
        return user
    except:
        return None
