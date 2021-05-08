from fastapi import APIRouter, Depends

from .endpoints.ticket import router as ticket_router
from .endpoints.user import router as user_router
from ...core.auth import check_jwt_token

router = APIRouter()
router.include_router(ticket_router, dependencies=[Depends(check_jwt_token)])
router.include_router(user_router)
