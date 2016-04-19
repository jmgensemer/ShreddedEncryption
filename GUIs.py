from tkinter import *
from tkinter.filedialog import askopenfilenames
from Read_Files import *
import os
import csv
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.init_EncryptedList()
        self.init_FButton()
        self.exitButton()
    def init_window(self):
        self.master.title("Shredded Encryption")
        self.pack(fill=BOTH, expand=1)

    def init_EncryptedList(self):
        Lb = Listbox(self, width = 15,height = 12,selectmode = MULTIPLE)
        i = 1
        for x in Encrypted_List:
            Lb.insert(i,x)
            i += 1
        Lb.place(x=400, y=100)
        DecryptButton = Button(self,text = "Decrypt Files", command = lambda: self.DecryptFiles(Lb.curselection()))
        DecryptButton.place(x=420,y = 310)

    def init_FButton(self):
        fbutton = Button(self, text = "Encrypt a File", command = self.load_file)
        fbutton.place(x=200,y=150)

    def load_file(self):
        fname = askopenfilenames()
        size = len(fname)
        for x in range(size):
            piece = splitFiles(fname[x])
            Encrypted_List.append((fname[x].rsplit('/', 1)[1]))
            File_List.append((fname[x],piece))
        self.init_EncryptedList()

    def exitButton(self):
        exit = Button(self,text = 'quit', command = self.quitCommand)
        exit.place(x=300,y=350)
    def quitCommand(self):
        with open('/Applications/Shredded Encryption/directory.csv', 'w') as csvfile:
            fieldnames = ['Filename', 'First Piece']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for x in File_List:
                writer.writerow({'Filename': x[0], 'First Piece': x[1]})
            self.quit()


    def DecryptFiles(self,x):
        for y in range(0,len(x)):
            if len(x) > 1:
                piece_Files(File_List[x[y-y]])
                del Encrypted_List[x[y-y]]
                del File_List[x[y-y]]
            else:
                piece_Files(File_List[x[y]])
                del Encrypted_List[x[y]]
                del File_List[x[y]]

        self.init_EncryptedList()


Encrypted_List = []
File_List = []
if os.path.exists('/Applications/Shredded Encryption/directory.csv'):
    with open('/Applications/Shredded Encryption/directory.csv') as f:
            next(f)
            File_List= [tuple(line) for line in csv.reader(f)]

for x in File_List:
    Encrypted_List.append(x[0].rsplit('/', 1)[1])

root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop()