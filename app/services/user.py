from ..db.db import execute, fetch
import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password):
    return pwd_context.hash(password)

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
    hashed_password = get_password_hash(user.password)
    values = {
        'username': user.username,
        'password': hashed_password,
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
    

async def verify_user(username, password):
    query = """select * from users where username = :username"""
    values = {"username": username}
    try:
        user = await fetch(query, True, values)
        if not user:
            print('No existe user')
            return False
        if not verify_password(password, user['password']):
            print('Contraseña no es igual')
            return False
        print('todo es correcto')
        return user
    except Exception as e:
        print(e)
        return None
    

async def verify_username(username):
    query = """select * from users where username = :username"""
    values = {"username": username}
    try:
        user = await fetch(query, True, values)
        if user:
            return True
    except:
        return False
