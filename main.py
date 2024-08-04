from PIL import Image
import pytesseract

# Path to your image file
image_path = '/Users/shanaisyuen/Downloads/payslip_jun23.png'

# Open image
img = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(img)

print("Extracted Text:")
print(text)