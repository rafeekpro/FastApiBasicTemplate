from fastapi import APIRouter

from .endpoints.root import router as root_router
from .endpoints.items import router as items_router


router = APIRouter()
router.include_router(root_router)
router.include_router(items_router)