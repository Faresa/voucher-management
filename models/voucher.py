from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from database.database import database

router = APIRouter()

class Voucher(BaseModel):
    id: Optional[int]
    code: str
    redemption_limit: Optional[int]
    expiration_date: Optional[datetime]
    redeemed_times: Optional[int]
    active: bool

@router.post("/create_voucher", response_model=Voucher)
async def create_voucher(voucher: Voucher):
    """
    Create a new voucher with the provided details.
    """
    with database as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO vouchers (code, redemption_limit, expiration_date)
            VALUES (?, ?, ?)
            """,
            (voucher.code, voucher.redemption_limit, voucher.expiration_date)
        )
        voucher_id = cursor.lastrowid
        conn.commit()
        return Voucher(**voucher.dict(), id=voucher_id, redeemed_times=0)

@router.get("/get_voucher/{voucher_id}", response_model=Voucher)
async def get_voucher(voucher_id: int):
    """
    Get voucher details by ID.
    """
    with database as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM vouchers WHERE id=?
            """,
            (voucher_id,)
        )
        voucher_data = cursor.fetchone()
        if voucher_data:
            return Voucher(**dict(voucher_data))
        else:
            raise HTTPException(status_code=404, detail="Voucher not found")

@router.get("/get_all_vouchers", response_model=List[Voucher])
async def get_all_vouchers():
    """
    Get details of all vouchers.
    """
    with database as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM vouchers
            """
        )
        vouchers_data = cursor.fetchall()
        return [Voucher(**dict(voucher_data)) for voucher_data in vouchers_data]
