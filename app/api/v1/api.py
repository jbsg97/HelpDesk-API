from fastapi import APIRouter

from .endpoints.ticket import router as ticket_router

router = APIRouter()
router.include_router(ticket_router)
