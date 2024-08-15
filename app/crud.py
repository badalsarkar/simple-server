from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Technology  # Import from app.models


async def create_technology(db: AsyncSession, tech_data: dict):
    technology = Technology(**tech_data)
    db.add(technology)
    await db.commit()
    await db.refresh(technology)
    return technology


async def get_technologies(db: AsyncSession):
    result = await db.execute(select(Technology))
    return result.scalars().all()


async def update_technology(db: AsyncSession, tech_id: int, tech_data: dict):
    technology = await db.get(Technology, tech_id)
    if not technology:
        return None
    for key, value in tech_data.items():
        setattr(technology, key, value)
    await db.commit()
    await db.refresh(technology)
    return technology


async def delete_technology(db: AsyncSession, tech_id: int):
    technology = await db.get(Technology, tech_id)
    if not technology:
        return None
    await db.delete(technology)
    await db.commit()
    return technology
