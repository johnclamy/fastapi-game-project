from fastapi import APIRouter


router = APIRouter(prefix="/explorer")


@router.get('/')
async def explorer_root():
    return {"message": "Welcome to the Explorer!"}
