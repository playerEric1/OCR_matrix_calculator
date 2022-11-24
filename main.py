import os
import numpy as np
import re
import asyncio
from PIL import Image
import pix2tex.api.app

# img_path = 'data/sample_matrix.png'
# byte = open('data/byte.txt').read().encode()
# print(byte)
# opened_img=Image.open(img_path)
# os.system('pix2tex')
# parsed_latex = os.popen('pix2tex;'+img_path).read().strip()
parsed_latex = ''
#
#
# async def parse_image(img):
#     latex = await pix2tex.api.app.predict_from_bytes(byte)
#     return latex
#
#
# parsed_latex = asyncio.run(parse_image(byte))
# parsed_latex = pix2tex.api.app.predict(img_path)
print(parsed_latex)

# remove the unnecessary format of latex
prefix = parsed_latex.find('gin{array}')
postfix = parsed_latex.find('end{array}')

parsed_latex = parsed_latex[prefix + 10:postfix - 1]

# parse latex into a raw matrix using deliminator '\' and '&'
raw_array = [col.split("&") for col in [row for row in parsed_latex.split("\\")]]

# convert string into float
numeric_array = []
for row in raw_array:
    new_row = []
    for col in row:
        new_row.append(float(re.sub(r"\D", "", col)))
    numeric_array.append(new_row)

np_array = np.matrix(numeric_array)

print(np.linalg.det(np_array))
