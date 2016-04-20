from tkinter import *
from tkinter.filedialog import askopenfilenames
from Read_Files import *
from PIL import ImageTk,Image
import os
import csv
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.image = Image.open('/Applications/Shredded Encryption/Background.jpeg')
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background_label = Label(self, image=self.background_image)
        self.background_label2 = Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=2, relheight=2)
        self.background_label2.place(x=0, y=0, relwidth=1, relheight=1)

        self.labelText = "  Welcome to\nShredded Encrpytion\n" \
                         "   Version 1.0"
        self.welcomeLabel = Label(self,text= self.labelText,)
        self.welcomeLabel.place(x=0,y=0)
        self.init_window()
        self.init_EncryptedList()
        self.init_FButton()
        self.exitButton()
        self.changeKeyButton()
    def init_window(self):
        self.master.title("Shredded Encryption")

        self.pack(fill=BOTH, expand=1)

    def init_EncryptedList(self):
        Lb = Listbox(self, width = 15,height = 12,selectmode = MULTIPLE)
        i = 1
        for x in Encrypted_List:
            Lb.insert(i,x)
            i += 1
        Lb.place(x=150, y=0)
        DecryptButton = Button(self,text = "Decrypt Files", command = lambda: self.DecryptFiles(Lb.curselection()))
        DecryptButton.place(x=170,y = 210)

    def init_FButton(self):
        fbutton = Button(self, text = "Encrypt Files", command = self.load_file)
        fbutton.place(x=20,y=60)

    def changeKeyButton(self):
        cKeyButton = Button(self, text = "Change Key", command = self.changeKeyCommand)
        cKeyButton.place(x=22,y=93)

    def load_file(self):
        fname = askopenfilenames()
        size = len(fname)
        for x in range(size):
            print(key)
            piece = splitFiles(fname[x],key)
            Encrypted_List.append((fname[x].rsplit('/', 1)[1]))
            File_List.append((fname[x],piece))
        self.init_EncryptedList()

    def exitButton(self):
        exit = Button(self,text = 'Quit', command = self.quitCommand)
        exit.place(x=45,y=130)
    def quitCommand(self):
            xpressed()

    def changeKeyCommand(self):
        global key
        global File_List
        a = []
        newKey = getKey()
        for x in File_List():
            piece_Files(x,key)
            piece = splitFiles(x[0],newKey)
            a.append(x[0],piece)
        key = newKey
        File_List = a


    def DecryptFiles(self,x):
        for y in range(0,len(x)):
            if len(x) > 1:
                piece_Files(File_List[x[y-y]],key)
                del Encrypted_List[x[y-y]]
                del File_List[x[y-y]]
            else:
                piece_Files(File_List[x[y]],key)
                del Encrypted_List[x[y]]
                del File_List[x[y]]

        self.init_EncryptedList()


Encrypted_List = []
File_List = []
key = getKey()
if os.path.exists('/Applications/Shredded Encryption/directory.csv'):
    with open('/Applications/Shredded Encryption/directory.csv', 'rb') as f:
            next(f)
            File_List= [tuple(line) for line in csv.reader(f)]

if os.path.exists('/Applications/Shredded Encryption/fjkldfemsf.txt'):
    with open('/Applications/Shredded Encryption/fjkldfemsf.txt') as f:
            key = f.readline()

key = b'\xd4h\x9a\xa9c\xc5\xb4\xc4\x00) \xb3?\xa6u\xff\xb7Y\xbe\xbd\x7fN7:\x95\x1bB`\x1bB~\r'


for x in File_List:
    Encrypted_List.append(x[0].rsplit('/', 1)[1])

def xpressed():
    with open('/Applications/Shredded Encryption/directory.csv', 'w') as csvfile:
        fieldnames = ['Filename', 'First Piece']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in File_List:
            writer.writerow({'Filename': x[0], 'First Piece': x[1]})
    with open('/Applications/Shredded Encryption/fjkldfemsf.txt', 'w') as f:
            f.write(key)
    root.destroy()

print
root = Tk()
root.geometry("300x275")
root.protocol('WM_DELETE_WINDOW', xpressed)
app = Window(root)
root.mainloop()