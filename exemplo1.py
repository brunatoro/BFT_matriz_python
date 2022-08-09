from email.mime import image
from turtle import width
import numpy as np
import matplotlib.pyplot as plt

#Tamaho da matriz
width = 24
height = 11

image_matrix = np.zeros([height,width])
print(image_matrix.shape)

#Letra B
#Linha vertical do B
image_matrix[:,0]=200
#Traço horizontal da barriga de cima
image_matrix[0,1:4]=200
#Traço horizontal da barriga de baixo
image_matrix[10,1:4]=200
#Traço horizontal do meio da barriga
image_matrix[5,1:4]=200
#diagonal baixo
image_matrix[9,4]=200
image_matrix[6,4]=200
image_matrix[8,5]=200
image_matrix[7,5]=200
#diagonal de cima
image_matrix[1,4]=200
image_matrix[2,5]=200
image_matrix[4,4]=200
image_matrix[3,5]=200

#Letra F
#Coluna do F
image_matrix[:,8]=200
#Linhas horizontais
image_matrix[0,9:14]=200
image_matrix[5,9:12]=200

#Letra T
#Linha horizontal do T
image_matrix[0,16:23]=200
image_matrix[:,19]=200

print(image_matrix) #print da matriz
#print gráfica da matriz
plt.imshow(image_matrix, cmap='gray')
plt.show()

