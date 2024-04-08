#(How to create a file in drive--) %%writefile mylib.py  #
#(Directory--) /content/drive #
!pip install qrcode
!pip install pygame

import qrcode

data='''
Yes
'''
img=qrcode.make(data)
img.save('Scan_me')
print(img)
