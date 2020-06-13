import cv2
import pytesseract
import os


def listFiles(dir):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return (files)


def ocr_core(path):
    """
    This function will handle the core OCR processing of images.
    """
    files = listFiles(path)
    for images in files:
        img = cv2.imread(images)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

        # Specify structure shape and kernel size.
        # Kernel size increases or decreases the area
        # of the rectangle to be detected.
        # A smaller value like (10, 10) will detect
        # each word instead of a sentence.
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        # Appplying dilation on the threshold image
        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

        # Finding contours
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                         cv2.CHAIN_APPROX_NONE)

        # Creating a copy of image
        im2 = img.copy()

        # A text file is created and flushed
        ###file = open(file+txt", "w+")
        ###file.write("")
        ###file.close()
        # Looping through the identified contours
        # Then rectangular part is cropped and passed on
        # to pytesseract for extracting text from it
        # Extracted text is then written into the text file
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            # Drawing a rectangle on copied image
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Cropping the text block for giving input to OCR
            cropped = im2[y:y + h, x:x + w]

            #file = open("recognized.txt", "a")
            text = pytesseract.image_to_string(cropped)
            #file.write(text)
            #file.write("\n")
            print (text)
            #file.closeprint (text)

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    path = r"C:\\Input OCR"
    ocr_core(path)
