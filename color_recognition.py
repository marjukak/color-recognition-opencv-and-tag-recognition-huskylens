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
