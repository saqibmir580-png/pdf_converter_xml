from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pdf_processing.extract_text import extract_text_from_pdf
from pdf_processing.extract_images import extract_images_from_pdf
from pdf_processing.ocr import perform_ocr_on_images
import os
from pdf2image import convert_from_path

app = FastAPI()


@app.post("/extract/")
async def extract_from_pdf(file: UploadFile = File(...)):
    # Save uploaded PDF to disk
    pdf_path = os.path.join(os.getcwd(), file.filename)
    with open(pdf_path, "wb") as buffer:
        buffer.write(await file.read())

    # 1. Extract selectable text
    text = extract_text_from_pdf(pdf_path)

    # 2. Extract embedded images and OCR them
    images = extract_images_from_pdf(pdf_path)
    ocr_text_images = perform_ocr_on_images(images)

    # 3. Render each page as an image and OCR the whole page
    page_images = convert_from_path(pdf_path)
    ocr_text_pages = perform_ocr_on_images(page_images)

    # 4. Combine all text sources, removing duplicate lines
    all_text = "\n".join([text, ocr_text_images, ocr_text_pages])
    all_text = "\n".join(dict.fromkeys(all_text.splitlines()))

    return JSONResponse(content={"extracted_text": all_text})

