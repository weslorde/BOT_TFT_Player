import cv2
import numpy as np

Threshold = .80         # Accuracy of the match


Screem = cv2.imread('Data/Prints/0.png' , cv2.IMREAD_UNCHANGED)     # Load the reference img
Card = cv2.imread('Data/Cards/Ziggs.png' , cv2.IMREAD_UNCHANGED)    # Load the img to found in reference

MatchMap = cv2.matchTemplate(Screem, Card, cv2.TM_CCOEFF_NORMED)    # Result of the match

Yloc, Xloc = np.where(MatchMap >= Threshold)    # X and Y position of results upper threshold

H_Card, W_Card = Card.shape[:2]   # Dimension of the img to found

rectangles = []
for (x,y) in zip(Xloc, Yloc):
    rectangles.append( [int(x), int(y), int(W_Card), int(H_Card)] )  # Creat a list of rectangles 
    rectangles.append( [int(x), int(y), int(W_Card), int(H_Card)] )  # append duplicate line because groupRectangles function

rectangles = cv2.groupRectangles(rectangles, 1, 1)[0]   # Remove multiple results for a same match

for (x, y, w, h) in rectangles:                                         # Draw a rectangle in the img of screem
    cv2.rectangle(Screem, (x,y), (x  + w,y + h ), (0,255,255), 2)
      
cv2.imshow("test" , Screem)     # Show the img with results
cv2.waitKey()
cv2.destroyAllWindows()



