import os

def install():
    L = ['pyqrcode','opencv-python','pyzbar','pypng']
    for i in L:
        os.system(f'pip install {i}')

def check():
    try:
        import pyqrcode
        import cv2
        import pyzbar
        #import pypng
    except:
        install()

if __name__ == '__main__':
    install()