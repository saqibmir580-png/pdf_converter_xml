from typing import List
import pdfplumber
from PIL import Image
import io

def extract_images_from_pdf(pdf_path: str) -> List[Image.Image]:
    images = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for img in page.images:
                # Extract the raw image bytes
                try:
                    x0, top, x1, bottom = img['x0'], img['top'], img['x1'], img['bottom']
                    # Crop the image region from the page as a PIL image
                    page_image = page.to_image(resolution=300)
                    cropped = page_image.original.crop((x0, top, x1, bottom))
                    images.append(cropped)
                except Exception as e:
                    print(f"Failed to extract image: {e}")
    return images