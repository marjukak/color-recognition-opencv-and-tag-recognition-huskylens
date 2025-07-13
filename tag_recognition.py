import cv2
import numpy as np
from pupil_apriltags import Detector

# Initialize the AprilTag detector for tag36h11 family
detector = Detector(families="tag36h11")

# Load the image (make sure you have tag36h11_00000.jpg in the folder)
img = cv2.imread('tag36h11_00000.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect tags
results = detector.detect(gray, estimate_tag_pose=False)

# Draw detections
for r in results:
    # Corners come in order [ptA, ptB, ptC, ptD]
    corners = np.int0(r.corners)
    for i in range(4):
        pt1 = tuple(corners[i])
        pt2 = tuple(corners[(i+1) % 4])
        cv2.line(img, pt1, pt2, (0, 255, 0), 2)

    # Center and tag ID
    cX, cY = int(r.center[0]), int(r.center[1])
    cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
    cv2.putText(img, f"ID: {r.tag_id}", (cX - 10, cY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# Show and save results
cv2.imshow("Tag Recognition", img)
cv2.imwrite("detected_tags.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
