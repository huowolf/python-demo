from PIL import Image,ImageFilter

img=Image.open('test.jpg')
# 应用模糊滤镜:
im2 = img.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')