from PIL import Image
from PIL import ImageEnhance
import pytesseract

if __name__=='__main__':
    # 原始图像
    image = Image.open('/Users/yangchao/Desktop/乐学/img副本-1.png')
    image.show()
    # 亮度增强
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.5
    image_brightened = enh_bri.enhance(brightness)
    image_brightened.show()
    # 色度增强
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    image_colored.show()
    # 对比度增强
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()
    # 锐度增强
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()
    text = pytesseract.image_to_string(image_sharped).strip()
    print(text)