import cv2
import numpy as np
import pyautogui
import os
import keyboard
import time

def ProxNome():
   try: 
       NamesF = os.listdir('Data/Cards/')
       NumbersF = []
       for name in NamesF:
           NumbersF.append( int(name[:-4]) )
    
       return(max(NumbersF)+1)
   except:
       return(0)
 

while(1):

    # keyboard.wait('space')
    
    # check = []
    # while(len(check) < 1):
    #     check = os.listdir(os.path.abspath('W:/Jogos Oficial/Riot Games/League of Legends/Screenshots/'))

        
    # Screem = cv2.imread(os.path.abspath('W:/Jogos Oficial/Riot Games/League of Legends/Screenshots/' + check[0]) , cv2.IMREAD_UNCHANGED)
         
    Threshold = .80         # Accuracy of the match
    
    time.sleep(10)
    ScreemShot = pyautogui.screenshot()
    Screem = cv2.cvtColor(np.array(ScreemShot), cv2.COLOR_RGB2BGR)
    
    Screem = Screem[870:1080, 260:1490]
    
    CardFiles = os.listdir('Data/Cards/')
    
    result = [0,0,0,0,0]
    
    for files in CardFiles:
        
        Card = cv2.imread('Data/Cards/' + files , cv2.IMREAD_UNCHANGED)    # Load the img to found in reference
        
        MatchMap = cv2.matchTemplate(Screem, Card, cv2.TM_CCOEFF_NORMED)    # Result of the match
    
        Yloc, Xloc = np.where(MatchMap >= Threshold)    # X and Y position of results upper threshold
        
        H_Card, W_Card = Card.shape[:2]   # Dimension of the img to found
        
        rectangles = []
        for (x,y) in zip(Xloc, Yloc):
            rectangles.append( [int(x), int(y), int(W_Card), int(H_Card)] )  # Creat a list of rectangles 
            rectangles.append( [int(x), int(y), int(W_Card), int(H_Card)] )  # append duplicate line because groupRectangles function
        
        rectangles = cv2.groupRectangles(rectangles, 1, 1)[0]   # Remove multiple results for a same match
        
        for (x, y, w, h) in rectangles:                                         # Check any valid rectangles
            # cv2.rectangle(Screem, (x,y), (x  + w,y + h ), (0,255,255), 2)
            
            if (x>475 and x<675):
                result[0] = files[:-4]
            
            if (x>675 and x<875):
                result[1] = files[:-4]
                
            if (x>875 and x<1075):
                result[2] = files[:-4]
                
            if (x>1075 and x<1275):
                result[3] = files[:-4]
            
            if (x>1275 and x<1475):
                result[4] = files[:-4]
    
     
    for n in range(5):
        if result[n] == 0:
            NewCard = Screem[0:160, 215+n*200:415+n*200]
            cv2.imwrite('Data/Cards/' + str(ProxNome()) + '.png', NewCard) 
    
    print(result)     
    
    # os.remove(os.path.abspath('W:/Jogos Oficial/Riot Games/League of Legends/Screenshots/' + check[0]))
          
        
    # cv2.imshow("test" , Screem)     # Show the img with results
    # cv2.waitKey()
    # cv2.destroyAllWindows()  
    
     
    
               

      

