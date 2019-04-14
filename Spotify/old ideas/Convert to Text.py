import pytesseract as pyt
pyt.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
pyt.image_to_string('Test1.png')
