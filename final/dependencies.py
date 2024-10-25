import os

def install():
    L = ['pyqrcode','opencv-python','pyzbar']
    for i in L:
        os.system(f'pip install {i}')

def check():
    try:
        import pyqrcode
        import cv2
        import pyzbar
    except:
        install()

if __name__ == '__main__':
    install()