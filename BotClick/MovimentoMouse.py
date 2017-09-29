'''
Created on Sep 8, 2017

@author: raul1
'''
import win32api, win32con
    
class MovimentoMouse(object):
    '''
    Classe resposavel por clicar em um lugar especificado da tela apos um tempo
    '''

    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def clicar(self,x,y):
        '''     MOUSEEVENTF_MOVE = 0x0001 # mouse move
        MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
        MOUSEEVENTF_MOVEABS = MOUSEEVENTF_MOVE + MOUSEEVENTF_ABSOLUTE
        
        MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down 
        MOUSEEVENTF_LEFTUP = 0x0004 # left button up 
        MOUSEEVENTF_CLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP
        
        x = 65536 * self.x / windll.user32.GetSystemMetrics(0) + 1
        y = 65536 * self.y / windll.user32.GetSystemMetrics(1) + 1
        windll.user32.mouse_event(MOUSEEVENTF_MOVEABS, x, y, 0, 0)

        #then click
        windll.user32.mouse_event(MOUSEEVENTF_CLICK, 0, 0, 0, 0)
        '''
        self.moverMouse(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
    def moverMouse(self,x,y):
        win32api.SetCursorPos((x,y))
        

    
    
    