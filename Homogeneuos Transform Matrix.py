import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("IMAGE").convert("L")
img = np.array(img)

rad = 52 * np.pi/180

#np.zeros로 생성할 행과 열의 크기계산
new_height  = round(img.shape[0]*np.cos(rad)+img.shape[1]*np.sin(rad)) 
new_width  = round(img.shape[1]*np.cos(rad)+img.shape[0]*np.sin(rad))

print(new_height)
print(new_width)

#Homogeneous Transform Matrix
mat = np.array([[np.cos(rad), -np.sin(rad)],
              	             [np.sin(rad), np.cos(rad)]])   

x = np.linspace(0,799,800)
y = np.linspace(0,599,600)

X,Y = np.meshgrid(x,y)

X = X.flatten()
Y = Y.flatten()

b = np.concatenate(([X],[Y]),axis=0) 

c = mat.dot(b).round().astype(int)

# 회전된 이미지의 새로운 array 크기 
#-> new_height, new_width : 높이의 -값만큼 빈 행렬크기 증가
out = np.zeros((new_height+472,new_width))  

out[c[0]+472, c[1]] = img[X.astype(int), Y.astype(int)]

out= np.delete(out, np.s_[965:], axis=0)

plt.imshow(out,'gray')
plt.show()
