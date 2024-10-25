from dependencies import *
check()
from reader import *
from generator import *

tax_bracket = {
    'charity': 0,
    'luxury': 18,
    'collectibles': 20,
    'fine_art': 15,
    'digital_art': 10,
    'crafts': 5,
    'commercial_art': 12,
}

menu = '''Enter required function:
1. bill a list
2. fetch all products
3. fetch details for a product
4. enter a new product
5. edit previous product details
6. delete previous product
7. fetch gst information
8. enter id to save qr
9. exit program
Your Input: '''

def f1(): #bill a list
    bill = []
    L = repeated_qr()
    print(L)
    for item in L:
        a = True
        while a:
            with open('db.txt','r') as f:
                a = f.readline()
                a = a.strip()
                a = eval(a)
                print(a)
                if str(a[0]) == item:
                    bill.append(a)
                    print('found')


def f2():
    with open('db.txt','r') as f:
        t = True
        c = 0
        while t:
            try:
                t = f.readline()
                t = t.replace('\n','')
                if not t: raise ZeroDivisionError
                if c: print(t)
                c+=1
            except:
                pass

def f3():
    p = input('Enter product name: ')
    p = p.lower()
    with open('db.txt','r') as f:
        t = True
        c = 0
        while t:
            try:
                t = f.readline()
                t = t.replace('\n','')
                if not t: raise ZeroDivisionError
                if p in t:
                    print(t)
                c+=1
            except:
                pass
def f4():
    print('Executing 4')
    with open('db.txt','r') as f:
        t = True
        while t:
            try:
                t = f.readline()
                t = t.replace('\n','')
                if not t: raise ZeroDivisionError
                print(t)
                t_old = t
            except:
                t = eval(t_old)
                l_id = t[0]
    with open('db.txt','a') as f:
        while True:
            try:
                n = int(input('Enter no. of products to be added: '))
                break
            except:
                print('Not a valid number.')
        for i in range(1,n+1):
            l_id += 1
            iden = l_id
            name = input(f'Enter name of product {i}: ').lower()
            category = None
            check = list(tax_bracket.keys())
            print('check',check)
            while category not in list(tax_bracket.keys()):
                print(f'Available categories:\n{tax_bracket}')
                category = input('Enter category of product: ').lower()
            while True:
                try:
                    price = int(input('Enter price of product: '))
                    break
                except:
                    print('Invalid.')
            comment = ''
            print('Enter Comment(Multiline,type ; and press Enter to exit):')
            while ';' not in comment:
                comment += input()
            tax = tax_bracket[category]*(price/100)
            print(tax)
            DB_list = [iden,name,category,tax,price,comment]
            f.write(DB_list)

def f7():
    print('The following is the percentages for taxes:')
    print(tax_bracket)

def f8():
    while True:
        try:
            id = int(input('Enter product ID: '))
            break
        except:
            print('Only Numbers allowed.')
    generate(id)

def f9():
    quit()


def main():
    while True:
        i = input(menu)
        eval(f'f{i}()')
        '''try:
            eval(f'f{i}()')
        except Exception as e:
            print('Debug: ',e)'''

main()