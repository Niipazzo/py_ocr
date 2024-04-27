import pytesseract
from PIL import ImageGrab, Image
import pygetwindow as gw
import pyautogui

# Configure tesseract executable path if not in PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def highlight_items():
    # Get the bounding box of the first window titled 'Notepad' or similar
    win = gw.getWindowsWithTitle('The Grand Mafia')[0]  # Change the title for your target window
    win.activate()
    
    # Take a screenshot of the whole screen or a specific window
    img = ImageGrab.grab(bbox=(win.left, win.top, win.right, win.bottom))
    
    # Use pytesseract to detect text and their bounding boxes
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    
    # Loop through detected text instances
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:  # Confidence level greater than 60%
            # Extract coordinates
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            # Highlight text
            pyautogui.rectangle(win.left + x, win.top + y, w, h, color='red')

if __name__ == "__main__":
    highlight_items()
