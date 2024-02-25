from fastapi import APIRouter, HTTPException
from datetime import datetime
from database.database import database
from models.voucher import Voucher

router = APIRouter()

@router.post("/create_voucher")
async def create_voucher(code: str, redemption_limit: int = None, expiration_date: datetime = None, active: bool = True):
    """
    Create a new voucher with the provided details.
    """
    # Check if voucher code already exists
    existing_voucher = await database.fetch_one("SELECT * FROM vouchers WHERE code = :code", {"code": code})
    if existing_voucher:
        raise HTTPException(status_code=400, detail="Voucher code already exists")

    # Insert the voucher into the database
    query = "INSERT INTO vouchers (code, redemption_limit, expiration_date, redeemed_times, active) VALUES (:code, :redemption_limit, :expiration_date, 0, :active)"
    await database.execute(query, {"code": code, "redemption_limit": redemption_limit, "expiration_date": expiration_date, "active": active})
    return {"code": code, "redemption_limit": redemption_limit, "expiration_date": expiration_date, "redeemed_times": 0, "active": active}

@router.get("/get_voucher/{code}")
async def get_voucher(code: str):
    """
    Get voucher details by code.
    """
    # Retrieve the voucher from the database
    voucher = await database.fetch_one("SELECT * FROM vouchers WHERE code = :code", {"code": code})
    if not voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")
    return voucher

@router.put("/update_voucher/{code}")
async def update_voucher(code: str, redemption_limit: int = None, expiration_date: datetime = None, active: bool = None):
    """
    Update voucher details by code.
    """
    # Check if the voucher exists
    existing_voucher = await database.fetch_one("SELECT * FROM vouchers WHERE code = :code", {"code": code})
    if not existing_voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")

    # Update the voucher in the database
    update_fields = {}
    if redemption_limit is not None:
        update_fields["redemption_limit"] = redemption_limit
    if expiration_date is not None:
        update_fields["expiration_date"] = expiration_date
    if active is not None:
        update_fields["active"] = active
    query = "UPDATE vouchers SET " + ", ".join([f"{field} = :{field}" for field in update_fields.keys()]) + " WHERE code = :code"
    await database.execute(query, {"code": code, **update_fields})
    return {"message": "Voucher updated successfully"}

@router.delete("/delete_voucher/{code}")
async def delete_voucher(code: str):
    """
    Delete voucher by code.
    """
    # Check if the voucher exists
    existing_voucher = await database.fetch_one("SELECT * FROM vouchers WHERE code = :code", {"code": code})
    if not existing_voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")

    # Delete the voucher from the database
    query = "DELETE FROM vouchers WHERE code = :code"
    await database.execute(query, {"code": code})
    return {"message": "Voucher deleted successfully"}

@router.put("/activate_voucher/{code}")
async def activate_voucher(code: str):
    """
    Activate a voucher by its code.
    """
    # Retrieve the voucher from the database
    existing_voucher = await database.fetch_one("SELECT * FROM vouchers WHERE code = :code", {"code": code})
    if not existing_voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")
    
    # Check if the voucher is already active
    if existing_voucher["active"]:
        raise HTTPException(status_code=400, detail="Voucher is already active")

    # Update the voucher status to active
    await database.execute("UPDATE vouchers SET active = 1 WHERE code = :code", {"code": code})
    return {"message": "Voucher activated successfully"}

@router.put("/deactivate_voucher/{code}")
async def deactivate_voucher(code: str):
    """
    Deactivate a voucher by its code.
    """
    # Retrieve the voucher from the database
    existing_voucher = await database.fetch_one("SELECT * FROM vouchers WHERE code = :code", {"code": code})
    if not existing_voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")
    
    # Check if the voucher is already inactive
    if not existing_voucher["active"]:
        raise HTTPException(status_code=400, detail="Voucher is already inactive")

    # Update the voucher status to inactive
    await database.execute("UPDATE vouchers SET active = 0 WHERE code = :code", {"code": code})
    return {"message": "Voucher deactivated successfully"}

@router.get("/list_all_vouchers")
async def list_all_vouchers():
    """
    Get details of all vouchers.
    """
    vouchers = await database.fetch_all("SELECT * FROM vouchers")
    if not vouchers:
        raise HTTPException(status_code=404, detail="No vouchers found")
    return vouchers
