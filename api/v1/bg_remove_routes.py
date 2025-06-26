import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from background_remover import remove_bg

route = APIRouter()


@route.post("/upload/images")
async def bg_remove(
    images: List[UploadFile] = File(...),
    method: str = "auto"
):
    results = []

    for image in images:
        try:
            image_processed = await remove_bg(image)
            results.append({
                "processed_image": image_processed,
                "error": None,
                "success": True
            })
        except Exception as e:
            results.append({
                "processed_image": None,
                "error": str(e),
                "success": False
            })

    return {
        "message": "Processing complete",
        "results": results,
        "method_used": method
    }