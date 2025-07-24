# FastAPI PDF Extractor

This project is a FastAPI application that extracts text and images from PDF files. It utilizes `pdfplumber` for text extraction, `Pillow` or `OpenCV` for image processing, and `pytesseract` for Optical Character Recognition (OCR) on images.

## Features

- Extracts normal text from PDF documents.
- Detects and extracts images from PDF files.
- Applies OCR to images to extract text.

## Project Structure

```
fastapi-pdf-extractor
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── pdf_processing         # Module for PDF processing
│   │   ├── __init__.py        # Package initialization
│   │   ├── extract_text.py     # Text extraction from PDF
│   │   ├── extract_images.py    # Image extraction from PDF
│   │   └── ocr.py             # OCR processing on images
│   └── types                  # Custom types for the application
│       └── index.py           # Type definitions
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd fastapi-pdf-extractor
pip install -r requirements.txt
```

## Usage

To run the FastAPI application, execute the following command:

```bash
uvicorn src.main:app --reload
```

You can then access the API at `http://127.0.0.1:8000`.

## API Endpoints

- **POST /extract**: Upload a PDF file to extract text and images.
  - Request Body: Multipart form data with a file field named `file`.
  - Response: JSON object containing extracted text and images.

## Dependencies

This project requires the following Python packages:

- `fastapi`
- `pdfplumber`
- `pytesseract`
- `Pillow`
- `opencv-python` (if using OpenCV)

Make sure to have Tesseract OCR installed on your system for `pytesseract` to function properly.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.