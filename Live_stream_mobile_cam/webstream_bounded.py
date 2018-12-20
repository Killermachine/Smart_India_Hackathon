import urllib
import cv2
import numpy as np

url='http://192.168.1.102:8080/shot.jpg?rnd=792763'

# camera specs
vertical_aov = 70
horizontal_aov = 130

frame = None
roiPts = []
inputMode = False

def select_roi(event, x, y, flags, param):
    global frame, roiPts, inputMode
    if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
        roiPts.append((x, y))
        cv2.circle(frame, (x, y), 4, (0, 0, 255), 2)
        cv2.imshow("image", frame)

cv2.namedWindow("image")
cv2.setMouseCallback("image", select_roi)

term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
roiBox = None

track_start_flag = False

while(1):
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    if roiBox is not None:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        ret, roiBox = cv2.CamShift(dst, roiBox, term_crit)

        current_center = (np.int0(ret[0][0]), np.int0(ret[0][1]))
        cv2.circle(frame, current_center, 4, (0, 255, 0), 2)
        cv2.circle(frame, original_center, 4, (255, 0, 0), 2)
        print "Vertical angle deviation", vertical_aov * (abs(current_center[1]-original_center[1]))/1080
        print "horizontal angle deviation", horizontal_aov * (abs(current_center[0]-original_center[0]))/1920

        current_distance = original_length/ret[1][1]
        if track_start_flag == False:
            distance_init =current_distance
            track_start_flag = True
        print "distance ratio",current_distance/distance_init

    cv2.imshow("image", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s") and len(roiPts) < 4:
        inputMode = True
        orig = frame.copy()
         
        while len(roiPts) < 4:
            cv2.imshow("image", frame)
            cv2.waitKey(0)
         
        roiPts = np.array(roiPts)
        s = roiPts.sum(axis = 1)
        tl = roiPts[np.argmin(s)]
        br = roiPts[np.argmax(s)]

        roi = orig[tl[1]:br[1], tl[0]:br[0]]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
         
        roi_hist = cv2.calcHist([roi], [0], None, [16], [0, 180])
        roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
        roiBox = (tl[0], tl[1], br[0], br[1])
        original_length = br[1]- tl[1]
        original_center = ( ( (tl[0]+br[0])/2 ),( (tl[1]+ br[1])/2 ) )

    if key == 27:
        break
cv2.destroyAllWindows()