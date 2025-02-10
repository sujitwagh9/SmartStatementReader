import pdf2image
import pytesseract
import cv2
import numpy as np

class PDFProcessor:
    def __init__(self):
        self.images = []
        
    def load_pdf(self, pdf_path):
        """Convert PDF to images"""
        self.images = pdf2image.convert_from_path(pdf_path)
        return self.images
    
    def preprocess_image(self, image):
        """Preprocess image for better OCR results"""
        # Convert to numpy array
        np_image = np.array(image)
        
        # Convert to grayscale
        gray = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
        
        # Apply threshold to get black and white image
        _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        return threshold