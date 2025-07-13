Task: Color Recognition Using OpenCV in Python
For this task, I was asked to create a simple project using OpenCV to detect and recognize colors based on mouse clicks on an image. I decided to build an interactive tool where I can click anywhere on a picture, and it’ll show me the name of the closest matching color along with its RGB values.

Tools, Libraries & Technologies I Used: 
1. Python 3.10.9
Main programming language I used to write and run the script.

2. Command Prompt (CMD)
I used it to check the Python version, install OpenCV with pip, navigate through directories, and execute the Python file.

3. OpenCV (opencv-python)
This was the core library I used to:
Load and display the image
Track mouse events
Read RGB pixel values from the image
Draw rectangles and overlay text on the image

4. NumPy
Although I didn’t directly import or use it, it comes bundled with OpenCV and helps process image arrays in the background.

5. Image File:
I used a test image called test_image.jpg. This was the image I clicked on to detect and recognize colors.

6. Python Script (color_recognition.py)
This file contained all my code. It handled:
Image loading
Mouse click detection
RGB color matching logic
On-screen display of results

7. Hardcoded Color Dictionary
Inside the script, I created a dictionary of common color names with their RGB values. I used this to find the closest match to the clicked color.
Key OpenCV Functions Used:
cv2.imshow() – to show the image window
cv2.setMouseCallback() – to register mouse click events
cv2.rectangle() – to draw a filled rectangle using the clicked color
cv2.putText() – to display the color name and RGB values on screen

8. How It Works (Logic):
The program loads the image and opens a window titled "Color Recognition".
When I left-click anywhere on the image, the program:
Reads the RGB value of the pixel I clicked
Compares it with predefined color values from the dictionary
Finds the closest matching color based on the sum of absolute RGB differences
Draws a rectangle with the selected color and shows its name + RGB values as text on top
I can keep clicking to detect different colors.
Pressing ‘q’ exits the program and closes the window.

Example Code Logic (Simplified):
# When I click:
b, g, r = img[y, x]  # Get RGB from clicked position
# Then:
cv2.rectangle(...)   # Show the color on screen
cv2.putText(...)     # Write the color name + RGB

What I Learned:
This project helped me understand how to:
Use OpenCV for basic image processing and UI interaction
Handle real-time events like mouse input
Match and compare RGB values to predefined color names
Build a practical and interactive mini-tool in Python
It was a simple but really fun project that gave me hands-on experience with OpenCV’s capabilities — especially around event handling and GUI overlays.




Code: 
import cv2

# Simple color dictionary (name and RGB)
colors = {
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Blue': (0, 0, 255),
    'Yellow': (255, 255, 0),
    'Cyan': (0, 255, 255),
    'Magenta': (255, 0, 255),
    'Black': (0, 0, 0),
    'White': (255, 255, 255),
    'Gray': (128, 128, 128),
    'Orange': (255, 165, 0),
    'Pink': (255, 192, 203),
    'Brown': (150, 75, 0)
}

def get_closest_color_name(r, g, b):
    min_dist = float('inf')
    closest_color = None
    for color_name, (cr, cg, cb) in colors.items():
        dist = abs(r - cr) + abs(g - cg) + abs(b - cb)
        if dist < min_dist:
            min_dist = dist
            closest_color = color_name
    return closest_color

clicked = False
r = g = b = xpos = ypos = 0

def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

img = cv2.imread('test_image.jpg')
cv2.namedWindow('Color Recognition')
cv2.setMouseCallback('Color Recognition', draw_function)

while True:
    cv2.imshow('Color Recognition', img)
    if clicked:
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)
        text = f"{get_closest_color_name(r, g, b)} R={r} G={g} B={b}"
        cv2.putText(img, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255 - r, 255 - g, 255 - b), 2)
        clicked = False
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()












Task: Tag Recognition Using HuskyLens (AprilTag)
For this task, I was asked to create a project that performs Tag Recognition using HuskyLens-style AprilTag detection. The goal was to identify and highlight visual tags from an input image, and display the tag's ID and outline using Python and computer vision libraries.

Tools I Used:
Python 3 – Main programming language for writing the script.
Command Prompt – To install required packages and run the script.
Notepad – Used for writing and editing the Python code (tag_recognition.py).
OpenCV (opencv-python) – To load and display the image, draw lines, circles, and text.
NumPy – For handling corner coordinates of detected tags.
pupil_apriltags – A pure‑Python library for detecting AprilTags.
AprilTag image (tag36h11_00000.jpg) – A sample tag image used as input.

What I Built:
 1. AprilTag Detector Setup
I started by initializing the AprilTag detector for the tag family tag36h11 using the pupil_apriltags library.

 2. Image Input and Grayscale Conversion
I loaded a sample image called tag36h11_00000.jpg and converted it to grayscale since tag detection works better in that format.

 3. Tag Detection
Using the detector, I scanned the image for any AprilTags and received a list of detected tags and their metadata (corners, center point, and tag ID).

 4. Drawing the Result
For every detected tag, I did the following:
Drew green lines connecting all four corners of the tag.
Plotted a red dot at the center of the tag.
Wrote the detected tag’s ID near its center using cv2.putText().

 5. Output
Finally, I displayed the result using cv2.imshow() and saved the image with outlines and tag IDs as detected_tags.jpg.

Reflection:
This task helped me understand how to apply computer vision for real-world tag recognition. I got hands-on experience using AprilTag detection, working with image arrays, and drawing overlays based on coordinate data. It also improved my comfort with OpenCV and how to integrate multiple libraries for a single workflow. The final output clearly highlighted the tag in the image, along with its ID, making the recognition visually understandable.

