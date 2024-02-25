from fastapi import APIRouter, HTTPException
from datetime import datetime
from database.database import database
from models import voucher

router = APIRouter()

@router.post("/redeem_voucher/{code}")
async def redeem_voucher(code: str):
    """
    Redeem a voucher by its code.
    """
    # Retrieve the voucher from the database
    voucher = await database.fetch_one("SELECT * FROM vouchers WHERE code = :code", {"code": code})
    if not voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")

    # Check if the voucher is active
    if not voucher["active"]:
        raise HTTPException(status_code=400, detail="Voucher is not active")

    # Check if redemption limit has been reached
    redemption_limit = voucher["redemption_limit"]
    if redemption_limit is not None and voucher["redeemed_times"] >= redemption_limit:
        raise HTTPException(status_code=400, detail="Redemption limit exceeded")

    # Check if voucher has expired
    expiration_date = voucher["expiration_date"]
    if expiration_date is not None:
        expiration_date = datetime.fromisoformat(expiration_date)  # Convert to datetime object
        if datetime.now() > expiration_date:
            raise HTTPException(status_code=400, detail="Voucher has expired")

    # Increment redeemed times and update the voucher in the database
    await database.execute("UPDATE vouchers SET redeemed_times = redeemed_times + 1 WHERE code = :code", {"code": code})
    return {"message": "Voucher redeemed successfully"}
