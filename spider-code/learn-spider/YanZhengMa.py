# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image
image=Image.open('图片路径')
code=pytesseract.image_to_string(image)
print(code)























