import cv2
import numpy as np
import matplotlib.pyplot as plt

frame = np.zeros((800, 800, 3), np.uint8)
last_mes = current_mes = np.array((2,1),np.float32)
last_pre = current_pre = np.array((2,1),np.float32)

## structure kalman filter
kalman = cv2.KalmanFilter(6,2)  # state_size, meas_size

"""
 x y vx vy ax ay
[1,0,0, 0, 0, 0]  x  ( meas = measureMatrix * state )
[0,1,0, 0, 0, 0]  y
"""
kalman.measurementMatrix = np.array([
    [1,0,0,0,0,0],
    [0,1,0,0,0,0]
], np.float32)


""" default t=1
 x y vx vy ax ay
[1,0, 1, 0, 1/2, 0]  x
[0,1, 0, 1, 0, 1/2]  y   (transition Matrix represent mathmatics model)
[0,0, 1, 0, 1, 0]        vx  (this is a constant acceleration motion )
[0,0, 0, 1, 0, 1]        vy
[0,0, 0, 0, 1, 0]        ax
[0,0, 0, 0, 0, 1]        ay
"""
kalman.transitionMatrix = np.array([
    [1,0,1,0,1/2,0],
    [0,1,0,1,0,1/2],
    [0,0,1,0,1,0],
    [0,0,0,1,0,1],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1]
], np.float32)


# discribe the correction of mathmatic model
kalman.processNoiseCov = np.eye(6, dtype=np.float32)*0.003

# discribe the correction of measurement
kalman.measurementNoiseCov = np.eye(2, dtype=np.float32)


def mousemove(event, x, y, s, p):
    # if event != cv2.EVENT_LBUTTONDOWN:
    #     return
    global frame, current_mes, last_mes, current_pre, last_pre
    last_pre = current_pre
    last_mes = current_mes
    current_mes = np.array([
        [np.float32(x)],
        [np.float32(y)]])
    
    kalman.correct(current_mes)
    current_pre = kalman.predict()

    lmx, lmy = int(last_mes[0]), int(last_mes[1])
    lpx, lpy = int(last_pre[0]), int(last_pre[1])
    cmx, cmy = int(current_mes[0]), int(current_mes[1])
    cpx, cpy = int(current_pre[0]), int(current_pre[1])

    cv2.line(frame, (lmx, lmy), (cmx, cmy), (0,200,0))
    cv2.line(frame, (lpx, lpy), (cpx, cpy), (0,0,200))

cv2.namedWindow("Kalman")
cv2.setMouseCallback("Kalman", mousemove)

while(True):
    cv2.imshow('Kalman', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()


# print('successful')