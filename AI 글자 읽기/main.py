import easyocr
import cv2
import matplotlib.pyplot as plt


def read(img_path):
    img = cv2.imread(img_path)
    '''
    plt.figure(figsize=(8, 8))
    plt.imshow(img[:, :, ::-1])
    plt.axis('off')
    plt.show()
    '''
    result = reader.readtext(img_path)
    r = []
    for bbox, text, conf in result:
        if conf > threshold:
            r.append(text)
            cv2.rectangle(img,
                          pt1=(int(bbox[0][0]), int(bbox[0][1])),
                          pt2=(int(bbox[2][0]), int(bbox[2][1])),
                          color=(0, 255, 0),
                          thickness=3)

    print(r)
    plt.figure(figsize=(8, 8))
    plt.imshow(img[:, :, ::-1])
    plt.axis('off')
    plt.show()


reader = easyocr.Reader(['ko', 'en'])

img_path = 'sample4.jpg'
threshold = 0.5
read(img_path)
