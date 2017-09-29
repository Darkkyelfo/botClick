'''
Created on Sep 8, 2017

@author: raul1
'''
import time
import threading
from POINT import POINT
from ctypes import windll, byref
from MovimentoMouse import MovimentoMouse
    
class Monitorar(object):
    '''
    Classe resposavel por monitorar se o usuario esta realizando alguma acao
    '''

    def __init__(self,x,y,tempoFechar = 30,pInicialX=469,pInicialY =725,deslocamento=50):
        self.pInicialX = pInicialX
        self.pInicialY = pInicialY
        self.tempo = 0
        self.tempoFechar = tempoFechar
        self.deslocamento = deslocamento
        self.movimentoMouse = MovimentoMouse(x,y)
        self.parar = False
        
    def __worker(self):
        while(True):
            time.sleep(1)
            self.tempo = self.tempo + 1
            print(self.tempo)
            if(self.tempo == self.tempoFechar and self.parar == False):# se atingir o tempo fecha o winthor
                self.__detectarPrograma()
                self.movimentoMouse.clicar(self.movimentoMouse.x,self.movimentoMouse.y)
                self.__zerarTempo()
                self.parar = True
            #print (self.tempo)
    
    def __detectarPrograma(self):
        xd = self.pInicialX
        for i in range(3):
            self.movimentoMouse.clicar(xd,self.pInicialY)
            xd = xd + self.deslocamento
            time.sleep(5)
            
    def iniciarMonitoramento(self):
        t = threading.Thread(target=self.__worker)
        t.start()
        self.detectarEvento()
        
    def __zerarTempo(self):
        self.tempo = 0
        self.parar = False
    
    def queryMousePosition(self):
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": pt.x, "y": pt.y}
    
    def detectarEvento(self):#Fonte: https://gist.github.com/inaz2/541da967ad04d06b975e
        GetAsyncKeyState = windll.user32.GetAsyncKeyState
        special_keys = {0x08: "BS", 0x09: "Tab", 0x0d: "Enter", 0x10: "Shift", 0x11: "Ctrl", 0x12: "Alt", 0x14: "CapsLock", 0x1b: "Esc", 0x20: "Space", 0x2e: "Del"}
        # reset key states
        for i in range(256):
            GetAsyncKeyState(i)
        while True:
            posIni = self.queryMousePosition()
            for i in range(256):
                if GetAsyncKeyState(i) & 1:
                    if i in special_keys:#teclas especiais 
                        self.__zerarTempo()
                        #print ("<%s>" % special_keys[i])
                    elif 0x30 <= i <= 0x5a:#Teclas letras
                        self.__zerarTempo()
                        #print ("%c" % i)
                    else:#click do mouse
                        self.__zerarTempo()
                        #print ("[%02x]" % i)
            #sys.stdout.flush()
            posF = self.queryMousePosition() 
            if(posF["x"] != posIni["x"] or posF["y"] != posIni["y"] ):
                print(posF)
                self.__zerarTempo()
            time.sleep(0.001)
        

    
    
    