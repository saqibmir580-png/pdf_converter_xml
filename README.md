
# PDF Converter FastAPI Backend

# This project extracts all text from a PDF, including:
# - Selectable (normal) text
# - Text inside embedded images (via OCR)
# - Text visible on the page (via OCR on rendered pages)

# ---

# ## Features

# - **FastAPI** backend for PDF text extraction
# - Uses `pdfplumber` for selectable text
# - Uses `pytesseract` for OCR on images and full pages
# - Uses `pdf2image` to render pages as images for OCR
# - Removes duplicate lines in the final output

# ---

# ## Requirements

# - Python 3.8+
# - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (must be installed and in PATH)
# - [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/) (must be installed and in PATH)

# ### Python dependencies

# Install all dependencies with:
# ```
# pip install -r requirements.txt
# ```

# Example `requirements.txt`:
# ```
# fastapi
# uvicorn
# pdfplumber
# pillow
# pytesseract
# pdf2image
# python-multipart
# ```

# ---

# ## Windows: Poppler & Tesseract Setup

# 1. **Poppler**
#    - Download from [Poppler Releases](https://github.com/oschwartz10612/poppler-windows/releases/)
#    - Extract, add the `bin` folder to your system PATH (e.g. `C:\poppler\Library\bin` or `C:\poppler\bin`)

# 2. **Tesseract**
#    - Download from [Tesseract Releases](https://github.com/tesseract-ocr/tesseract)
#    - Install, add the install folder (e.g. `C:\Program Files\Tesseract-OCR`) to your PATH

# 3. **Restart your terminal or VS Code** after changing PATH.

# ---

# ## How to Run the Project

# 1. **Install dependencies**  
#    ```
#    pip install -r requirements.txt
#    ```

# 2. **(Windows only) Make sure Poppler and Tesseract are installed and in your PATH.**

# 3. **Start the FastAPI server**

#    - From the `src` directory:
#      ```
#      cd src
#      uvicorn main:app --reload
#      ```
#    - Or from the project root:
#      ```
#      uvicorn src.main:app --reload
#      ```

# 4. **Open your browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  
#    Use the `/extract/` endpoint to upload a PDF and get all extracted text.

# ---

# ## Project Structure

# ```
# fastapi-pdf-extractor/
# ├── src/
# │   ├── main.py
# │   └── pdf_processing/
# │       ├── extract_text.py
# │       ├── extract_images.py
# │       └── ocr.py
# ├── requirements.txt
# └── README.md
# ```

# ---

# ## Troubleshooting

# - **Poppler not found:** Make sure Poppler's `bin` folder is in your PATH or pass `poppler_path` to `convert_from_path`.
# - **Tesseract not found:** Make sure Tesseract is installed and in your PATH.
# - **OCR accuracy:** Try increasing DPI in `convert_from_path`, and/or preprocess images (grayscale, thresholding).

# ---
