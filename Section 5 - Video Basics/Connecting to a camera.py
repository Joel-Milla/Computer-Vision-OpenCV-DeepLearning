import cv2

def main(args=None):
    cap = cv2.VideoCapture(0) # series of image

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # floating point number
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    width = int(width)
    height = int(height)
    
    print("Press 'q' for exiting the program")
    while True:
    
        ret, frame = cap.read()
    
        # gray = cv2.cvtColor(frame)
        cv2.imshow('frame', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()