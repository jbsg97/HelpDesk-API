from fastapi import APIRouter, Body, HTTPException, status, Depends
from typing import List
from fastapi_utils.cbv import cbv
from ....models.user import UserIn, UserOut
from ....services.user import (
    fetch_user,
    retrieve_user,
    create_user,
    update_user,
    delete_user
)

router = APIRouter()
@cbv(router)
class User:

    @router.get(
        "/user", 
        response_model=List[UserOut], 
        status_code=status.HTTP_200_OK,
        tags=["User"]
    )
    async def fetch(self):
        users = await fetch_user()
        if users:
            return users
        raise HTTPException(status_code=404, detail="No se encontraron usuarios registrados.")


    @router.get(
        "/user/{id_user}", 
        response_model=UserOut, 
        status_code=status.HTTP_200_OK,
        tags=["User"]
    )
    async def retrieve(self, id_user: int):
        user = await retrieve_user(id_user)
        if user:
            return user
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")


    @router.post(
        "/user", 
        status_code=status.HTTP_201_CREATED,
        tags=["User"]
    )
    async def create(self, user: UserIn):
        user = await create_user(user)
        if user:
            return {"message": "Usuario creado con exito"}
        raise HTTPException(status_code=404, detail="Error al crear al usuario.")


    @router.put(
        "/user/{id_user}", 
        status_code=status.HTTP_200_OK,
        response_model=UserOut,
        tags=["User"]
    )
    async def update(self, id_user: int, user: UserIn):
        user = await update_user(id_user, user)
        if user:
            return user
        raise HTTPException(status_code=404, detail="Error al actualizar al usuario.")
    
    
    @router.delete(
        "/user/{id_user}", 
        response_model=UserOut, 
        status_code=status.HTTP_200_OK,
        tags=["User"]
    )
    async def delete(self, id_user: int):
        user = await delete_user(id_user)
        if user:
            return user
        raise HTTPException(status_code=404, detail="Error al eliminar al usuario.")
