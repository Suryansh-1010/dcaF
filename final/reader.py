import cv2


def read():
    #meant to convert qr code to product id which can be used to fetch details in python
    inp = input('Enter either path to qr image or product id: ')
    try:
        prod_id = int(inp)
        return prod_id
    except:
        print('Not a direct id, Scanning for QR.')
        img = cv2.imread(inp)
        qcd = cv2.QRCodeDetector()
        retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
        if retval:
            decoded_info = decoded_info[0]
            print(decoded_info)
            try:
                decoded_info = int(decoded_info)
            except:
                print('Not a valid product id, should be an integer.')
            return decoded_info
        else:
            print('qr not detected.')

def repeated_qr():
    check = False
    L = []
    while not check:
        i = input('''Select an option:
1. Scan a qr code or manually add product id
2. exit
Your Input: ''')
        if i == '1':
            id = read()
            L.append(id)
            while True:
                i = input('''Select an option:
1. Scan another qr code or manually add product id
2. exit
Your Input: ''')
                if i == '1':
                    id = read()
                    L.append(id)
                elif i == '2':
                    check = True
                    break
                else: print('Not a valid input.')
        elif i == 2:
            break
        else:
            print('Invalid input.')
        return L

if __name__ == '__main__':
    print('Note: Program executed indiviually for testing.')
    repeated_qr()