from fastadmin import fastapi_app as admin_app
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.api import authentication_router, client_router, news_router
from src.utils.exceptions import ResultNotFound

app = FastAPI(
    title="hackaton backend",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/admin", admin_app, "admin panel")

main_app_router = APIRouter(prefix="/api")

main_app_router.include_router(authentication_router, tags=["Authentication"])
main_app_router.include_router(client_router, tags=["Clients"])
main_app_router.include_router(news_router, tags=["News"])

app.include_router(main_app_router)


@app.exception_handler(ResultNotFound)
async def not_found_exception_handler(request: Request, exc: ResultNotFound):
    return JSONResponse(
        status_code=404,
        content={"detail": "Result not found"},
    )
