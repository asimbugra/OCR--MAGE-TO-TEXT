from PIL import Image
import pytesseract
#resim yolu
image_path = '/path/to/image.png'

#resmi aç
image = Image.open(image_path)

#resimdeki yazıyı stringe çevir
result = pytesseract.image_to_string(image)

print("OCR'den elde edilen metin:")
print(result)
