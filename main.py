from fastapi import FastAPI
from database.database_init import initialize_database
from api.management import router as management_router
from api.redemption import router as redemption_router
from database.database import database


app = FastAPI()

initialize_database()

# Include routers for management and redemption
app.include_router(management_router, prefix="/management", tags=["management"])
app.include_router(redemption_router, prefix="/redemption", tags=["redemption"])

# Connect to the database when the application starts
@app.on_event("startup")
async def startup():
    await database.connect()

# Disconnect from the database when the application stops
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
