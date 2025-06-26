import rembg
import numpy as np
from PIL import Image
import uuid
import asyncio
import os
import io

async def remove_bg(upload_file):
    # Read the uploaded file into memory
    contents = await upload_file.read()
    
    # Convert bytes to a PIL Image
    input_image = Image.open(io.BytesIO(contents))
    input_array = np.array(input_image)
    
    # Remove background
    output_array = rembg.remove(input_array)
    output_image = Image.fromarray(output_array)
    
    # Save to static folder (ensure it exists)
    os.makedirs("static", exist_ok=True)
    filename = f"static/{uuid.uuid4().hex}.png"
    output_image.save(filename)
    
    return filename 

