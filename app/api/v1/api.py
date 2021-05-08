from fastapi import APIRouter

from .endpoints.ticket import router as ticket_router
from .endpoints.user import router as user_router

router = APIRouter()
router.include_router(ticket_router)
router.include_router(user_router)
