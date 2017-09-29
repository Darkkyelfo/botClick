'''
Created on Sep 8, 2017

@author: raul1
'''
import cv2
import numpy as np
import pyscreenshot as ImageGrab

class Visao(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def contarCores(self,img):
        frame = img
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([70,35,35])
        upper_blue = np.array([130,255,255])
        # range de vermelho
        lower_red = np.array([0,90,60]) #example value
        upper_red = np.array([10,255,255]) #example value
        #range verde
        lower_green = np.array([46,100,100]) #example value
        upper_green = np.array([86,255,255]) #example value
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        maskRed = cv2.inRange(hsv,lower_red,upper_red)
        maskGreen =  cv2.inRange(hsv,lower_green,upper_green)
        #conta quantos pixels azuis existem
        nBlue = cv2.countNonZero(mask)
        nRed = cv2.countNonZero(maskRed)
        nGreen = cv2.countNonZero(maskGreen)
        #print('The number of blue pixels is: ' + str(nBlue))
        #print('The number of red pixels is: ' + str(nRed))
        #print('The number of green pixels is: ' + str(nGreen))
        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(frame,frame, mask= maskRed)
        #cv2.imshow('frame',frame)
        #cv2.imshow('mask',maskGreen)
       # cv2.imshow('res',res)
        #cv2.waitKey(0)
        return nBlue,nGreen,nRed
    
    #determina se a imagem é a tela desejada
    def ehTela(self,img,blueMin,blueMax,greenMin,greenMax,redMin,redMax):
        qtPixels = self.contarCores(img)
        blueR = list(range(blueMin,blueMax))
        greenR = list(range(greenMin,greenMax))
        redR = list(range(redMin,redMax))
        if(qtPixels[0] in blueR and qtPixels[1] in greenR and qtPixels[2] in redR):
            return True
        return False
    
    def acharComponente(self):
         print("ainda vai ser implementada")
        
    #realiza uma captura da tela atual
    def printTela(self):
        imagem = ImageGrab.grab()
        imagem.save('tela.jpg', 'jpeg')
        imagem.show()
        
    '''
    def detectarLowerUpper(self):
        blue = 87
        green = 181
        red = 66 
         
        color = np.uint8([[[blue, green, red]]])
        hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
         
        hue = hsv_color[0][0][0]
         
        print("Lower bound is :"),
        print("[" + str(hue-10) + ", 100, 100]\n")
         
        print("Upper bound is :"),
        print("[" + str(hue + 10) + ", 255, 255]")
    '''
        
    def detectarSeFechou(self):
        print("fechou")

if __name__ == "__main__":
    # fullscreen
    v = Visao()
    img = img = cv2.imread("teste.jpg")
    '''
    cv2.imshow('teste2',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    print(v.contarCores(img))
    #v.printTela()
    #v.contarAzul()
        