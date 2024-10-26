from dependencies import *
check()
from reader import *
from generator import *

tax_bracket = {
    'charity': 0,
    'luxury': 25,
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
        with open('db.txt','r') as f:
            a = True
            while a:
                a = f.readline()
                a = a.strip()
                if a:
                    a = eval(a)
                    print(a)
                    if int(a[0]) == item:
                        bill.append(a)
                        break
                else: break
    print('printing bill')
    print(bill)
def f2():
    with open('db.txt','r') as f:
        c = f.read()
        print(c)

def f3():
    p = input('Enter product name to search: ')
    p = p.lower()
    with open('db.txt','r') as f:
        t = True
        found = False
        while t:
            try:
                t = f.readline()
                t = t.replace('\n','')
                if not t: raise ZeroDivisionError
                if p in t.lower():
                    print(t)
                    found = True
                    break
            except:
                pass
        if not found: print(f'Could not find {p} in database.')

def f4():
    with open('db.txt','r') as f:
        c = '['
        l = True
        while l:
            l = f.readline()
            c += l
            c += ','
        c = c.removesuffix(',,')
        c += ']'
        c = c.replace('\n','')
        c = eval(c)
        lastid = c[-1][0]

    with open('db.txt','a') as f:
        while True:
            try:
                n = int(input('Enter no. of products to be added: '))
                break
            except:
                print('Not a valid number.')
        iden = int(lastid) + 1
        for i in range(1,n+1):
            name = input(f'Enter name of product {i}: ').lower()
            category = None
            check = list(tax_bracket.keys())
            print('check',check)
            while category not in list(tax_bracket.keys()):
                print(f'Available categories:\n{tax_bracket}')
                category = input('Enter category of product: ').lower()
            while True:
                try:
                    price = float(input('Enter price of product: '))
                    break
                except:
                    print('Invalid.')
            comment = ''
            print('Enter Comment(Multiline,type ; and press Enter to exit):')
            while ';' not in comment:
                comment += input()
                comment += '\n'
            comment = comment.replace('\n;','')
            comment = comment.replace(';','')
            tax = tax_bracket[category]*(price/100)
            DB_list = f"['{iden}','{name}','{category}','{tax}','{price}','{comment}']"
            f.write('\n'+DB_list)
            print(f'{DB_list} added with ID.')
            iden += 1

def f6():
    p = input('Enter product name to remove: ')
    p = p.lower()
    with open('db.txt','r') as f:
        t = True
        found = False
        while t:
            try:
                t = f.readline()
                if not t: raise ZeroDivisionError
                if p in t.lower():
                    with open('db.txt','r') as f:
                        c = f.read()
                        c = c.replace(t,'')
                    with open('db.txt','w') as f:    #PROCEED WITH CAUTION
                        f.write(c)
                    t = t.replace('\n','')
                    print(t,'was removed.')
                    found = True
                    break
            except:
                pass
        if not found: print(f'Could not find {p} in database.')
    #print(f'Product \n{} with details\n{}\ndeleted.')

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