import os
import glob
from PIL import Image, ImageDraw, ImageFilter, ImageOps
#  Normal Paste
im1 = Image.open('rocket.jpg')
im2 = Image.open('lena.jpg')

# back_im = im2.copy()
# back_im.paste(im2)
# back_im.save('rocket_lane.jpg', quality= 95)

# specify the position to paste
# back_im = im1.copy()
# back_im.paste(im2, (100,50))
# back_im.save('rocket_lane_pos.jpg', quality= 95)

# use mask image
# msk_im = Image.new("L", im2.size, 0)
# draw = ImageDraw.Draw(msk_im)
# draw.ellipse((140,50,260,170), fill=255)
# msk_im.save('mask_circle.jpg', quality=95)

# back_im = im1.copy()
# back_im.paste(im2,(400,0), msk_im)
# back_im.save('rocket_lane_mask.jpg', quality= 95)
# files = glob.glob('*')

# for f in files:
#     root, ext = os.path.splitext(f)
#     if ext in ['jpg','png']:

# img_resize = back_im.resize((256,400), Image.LANCZOS)
# img_resize.save('lena_resize.png')


# im_rgba = im2.copy()
# im_rgba.putalpha(128)
# im_rgba.save("lena_putalpha.png")

# im_a = Image.new("L", im2.size, 0)
# draw = ImageDraw.Draw(im_a)
# draw.ellipse((140,50,260,170), fill=255)


# im_rgba.putalpha(im_a)
# im_rgba_crop = im_rgba.crop((140,50,260,170))
# im_rgba_crop.save('pillow.putaplha_circle.png')

im_a = Image.open('lena.jpg').resize(im2.size)
im_invert = ImageOps.invert(im_a)
im_invert.save('after1.jpg')

im_a = Image.open('shirt.jpg').convert("RGB")
im_invert = ImageOps.invert(im_a)
im_invert.save('after1.png')

# im_rgba = im2.copy()
# im_rgba.putalpha(im_a)
# im_rgba.save('pillow_putalha_invert.png')

