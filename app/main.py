from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import (
    create_technology,  # Import from app.crud
    delete_technology,
    get_technologies,
    update_technology,
)
from app.database import engine, get_db  # Import from app.database
from app.models import Technology  # Import from app.models

# Initialize the FastAPI app
app = FastAPI()


# Create the database tables when the app starts
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Technology.metadata.create_all)


# Endpoint to create a new technology
@app.post("/technologies/")
async def create_technology_endpoint(
    technology: dict, db: AsyncSession = Depends(get_db)
):
    return await create_technology(db, technology)


# Endpoint to get all technologies
@app.get("/technologies/")
async def read_technologies_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_technologies(db)


# Endpoint to update a technology by ID
@app.put("/technologies/{tech_id}")
async def update_technology_endpoint(
    tech_id: int, technology: dict, db: AsyncSession = Depends(get_db)
):
    updated_technology = await update_technology(db, tech_id, technology)
    if updated_technology is None:
        raise HTTPException(status_code=404, detail="Technology not found")
    return updated_technology


# Endpoint to delete a technology by ID
@app.delete("/technologies/{tech_id}")
async def delete_technology_endpoint(tech_id: int, db: AsyncSession = Depends(get_db)):
    deleted_technology = await delete_technology(db, tech_id)
    if deleted_technology is None:
        raise HTTPException(status_code=404, detail="Technology not found")
    return {"message": "Technology deleted"}
