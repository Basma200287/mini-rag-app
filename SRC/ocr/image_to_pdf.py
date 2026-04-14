from PIL import Image
import os

def image_to_pdf(image_path: str, output_pdf_path: str):
    image = Image.open(image_path)

    # convert image to RGB (important for PNG)
    if image.mode != "RGB":
        image = image.convert("RGB")

    image.save(output_pdf_path, "PDF", resolution=100.0)

    return output_pdf_path