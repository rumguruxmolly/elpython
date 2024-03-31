from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def biverif(x):
    ch=str(x)
    s=0
    for i in range(0,len(ch)):
        if int(ch[i])==0 or int(ch[i])==1:
            s=s+1
    return s==len(ch) #done
def hexverif(x):
    s=0
    ch=str(x)
    for i in range(0,len(ch)):
        if "1"<=ch[i]<="9" or "A"<=ch[i]<="Z":
            s=+1
    return s==len(ch) #done
def decverif(x):
    if x.isdecimal():
        return True
    else:
        return False #done
def binaoct(x):
    x=binadec(x)
    x=oct(x)
    ch=str(x)
    s=""
    for i in range(len(ch)):
        if i==0 or i==1:
            pass
        else:
            s+=str(ch[i])
    return s #works
def decabin(x):
    res=""
    x = int(x)
    while x!=0:
        res=str(x % 2)+res
        x//=2
    while len(res)<4:
        res="0"+res
    return res #works

def octaltobin(x):
    som=""
    long=len(str(x))
    for i in range(long):
        som=som+str(decabin(int(str(x)[i])))
    return som #works
def binadec(x):
    ch=str(x)
    s=0
    p=len(ch)-1
    for i in range(len(ch)):
        s=s+ int(ch[i])*(2 **p)
        p-=1
    return s #works
def binahex(x):
    return decahex(binadec(x))
def hexadec(x):
    long = len(x)
    res = 0
    for i in range(long):
        if x[i].upper() == "A":
            res+=10*(16**(long-i-1))
        elif x[i].upper() == "B":
            res+=11 *(16**(long-i-1))
        elif x[i].upper() == "C":
            res+=12*(16**(long-i-1))
        elif x[i].upper() == "D":
            res+=13 * (16**(long-i-1))
        elif x[i].upper() == "E":
            res+=14 *(16**(long-i-1))
        elif x[i].upper() == "F":
            res+=15 *(16**(long-i-1))
        else:
            res+=int(x[i])*(16**(long-i-1))
    return res #works
def hexabin(x):
    return decabin(hexadec(x)) #works
def hexaoct(x):
    return decaoct(hexadec(x)) #works

def decaoct(x):
    res=""
    x=int(x)
    while x//8!=0:
        res=str(x%8)+res
        x=x//8
    res=str(x%8)+res
    return res #works
def decahex(x):
    res=""
    x=int(x)
    while x//16!=0:
        if 10<=x%16<=15:
            if x%16==10:
                res=res+"A"
            elif x%16==11:
                res=res+"B"
            elif x%16==12:
                res=res+"C"
            elif x%16==13:
                res=res+"D"
            elif x%16==14:
                res=res+"E"
            elif x%16==15:
                res=res+"F"
        else:
            res=res+str(x%16)
        x=x//16
    res=str(x%16)+res
    return res #works
def binaoct(x):
    return decaoct(binadec(x)) #works
def octadec(x):
    ch=str(x)
    s=0
    p=len(ch)-1
    for i in range(len(ch)):
        s=s+ int(ch[i])*(8 **p)
        p-=1
    return s #works
def octahex(x):
    return decahex(octadec(x))
def pushButton_click():
    global validite
    windows.res.setReadOnly(True)
    x=windows.x.text()
    index=windows.b.currentIndex()
    if index==0:
        if x.isdecimal() and biverif(x)==True:
            s="Valide"
            validite=True
        else:
            s="Invalide"
            validite=False
    elif index==1:
        if x.isdecimal():
            if 1<=int(x)<=7:
                 s="Valide"
                 validite=True
            else:
                s="Invalide"
                validite=False
    elif index==2:
        if decverif(x):
            s="Valide"
            validite=True
        else:
            s="Invalide"
            validite=False
    elif index==3:
        if hexverif(x):
            s="Valide"
            validite=True
        else:
            s="Invalide"
            validite=False
    windows.r.setText(s)

def pushButton_3_click():
    global validite
    if not validite:
        windows.res.setText("Pas valide")
    else:
        windows.res.setReadOnly(True)
        index=windows.b.currentIndex()
        index1=windows.com.currentIndex()
        if index==0 and index1==2:
            x=int(x)
            windows.res.setText(str(binadec(x)))
    #binaire
        elif index==0 and index1==0:
            windows.res.setText(str(x))
        elif index==0 and index1==1:
            windows.res.setText(str(binaoct(x)))
        elif index==0 and index1==2:
            windows.res.setText(str(binadec(x)))
        elif index==0 and index1==3:
            windows.res.setText(str(binahex(x)))
    #Octal
        elif index==1 and index1==0:
            windows.res.setText(str(octaltobin(x)))
        elif index==1 and index1==1:
            windows.res.setText(str(x))
        elif index==1 and index1==2:
            windows.res.setText(str(octadec(x)))
        elif index==1 and index1==3:
            windows.res.setText(str(octahex(x)))
    #decimal
        elif index==2 and index1==0:
            windows.res.setText(str(decabin(x)))
        elif index==2 and index1==1:
            windows.res.setText(str(decaoct(x)))
        elif index==2 and index1==2:
            windows.res.setText(str(x))
        elif index==2 and index1==3:
            windows.res.setText(str(decahex(x)))
    #hex
        elif index==3 and index1==0:
            windows.res.setText(str(hexabin(x)))
        elif index==3 and index1==1:
            windows.res.setText(str(hexaoct(x)))
        elif index==3 and index1==2:
            windows.res.setText(str(hexadec(x)))
        elif index==3 and index1==3:
            windows.res.setText(str(x))
    

app = QApplication([])
windows = loadUi ("C:/Users/mushy/OneDrive/Desktop/Algo.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )
windows.pushButton_3.clicked.connect ( pushButton_3_click )

app.exec_()