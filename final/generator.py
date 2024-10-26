import pyqrcode
from pyzbar.pyzbar import decode

def savepng(id,path='C:\\Users\\xii\\Desktop\\ProjectTesting\\myqr.png'):
    qrcode = pyqrcode.create(id)
    qrcode.png(path,scale=8,quiet_zone=1)
    print('Saved to path:',path)
def generate(id2):
    path = input('Enter path to save image (Optional, press Enter to skip):\n')
    if path:
        savepng(path,id2)
    else:
        savepng(id=id2)
if __name__ == '__main__':
    print('Note: Program executed indiviually for testing.')
    generate('483256350149812645')