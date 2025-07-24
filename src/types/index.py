from typing import List, Dict, Any

class PDFProcessingResult:
    def __init__(self, text: str, images: List[Dict[str, Any]]):
        self.text = text
        self.images = images

    def to_dict(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "images": self.images
        }