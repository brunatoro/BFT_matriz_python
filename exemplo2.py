#Exemplo de leitura e plot de imagens
#Bibliotecas: Pillow => Numpy, PIL, Matplotlib

import numpy as np
from PIL import Image #pillow
import matplotlib.pyplot as plt

def main():
    #Abre a imagem
    img = Image.open('imgs/lena_gray_512.tif')
    print(img.format)
    print(img.size)
    print(img.mode)
    #img.show()
    
    #converte a imagem to numpy array
    npImg = np.array(img)
    npImg = 255 - npImg

    npImgTres = np.array(img)
    npImgTres = 127 - npImgTres

    #convert numpy array to image
    imgNew = Image.fromarray(npImg)
    imgTres = Image.fromarray(npImgTres)
    #imgNew.show()
    
    # Plot using matplotlib
    fig, ax = plt.subplots(nrows=1, ncols=3)
    ax[0].imshow(img, cmap='gray')
    ax[0].set_title("Imagem original")

    ax[1].imshow(imgNew, cmap='gray')
    ax[1].set_title("Negativo da Imagem")

    ax[2].imshow(imgTres, cmap='gray')
    ax[2].set_title("Intensidade diminuída")    
    
    plt.show()    
      
if __name__ == "__main__":
    main()