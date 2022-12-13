import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from apps.todo.routers import router as todo_router
from config import settings

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(todo_router, tags=["login"], prefix="/login")
app.include_router(todo_router, tags=["workspace"], prefix="/login/workspace")
app.include_router(todo_router, tags=["deployments"], prefix="/login/workspace/deployment")
app.include_router(todo_router, tags=["install_module"], prefix="/login/workspace/install_module")
app.include_router(todo_router, tags=["devices"], prefix="/login/workspace/deployment/devices")
app.include_router(todo_router, tags=["profiles"], prefix="/login/workspace/deployment/profiles")





if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
