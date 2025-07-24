from typing import List
from PIL import Image as PILImage
import pytesseract

def perform_ocr_on_images(images: List[PILImage.Image]) -> str:
    text = ""
    for image in images:
        # image is already a PIL Image, no need to open it again
        text += pytesseract.image_to_string(image) + "\n"
    return text.strip()