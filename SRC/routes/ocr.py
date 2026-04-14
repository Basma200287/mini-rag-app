from fastapi import APIRouter, UploadFile, File
import shutil
from ocr.image_to_pdf import image_to_pdf

router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.post("/ocr/image-to-pdf")
async def convert_image_to_pdf(file: UploadFile = File(...)):

    if file.filename.lower().endswith(".pdf"):
        return {"error": "This endpoint accepts only images (png/jpg)"}

    input_path = f"/tmp/{file.filename}"
    output_path = f"/tmp/output.pdf"

    # save uploaded image
    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # convert
    pdf_path = image_to_pdf(input_path, output_path)

    return {
        "message": "converted successfully",
        "pdf_path": pdf_path
    }