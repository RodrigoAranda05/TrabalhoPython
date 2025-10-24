import tkinter

def Interface():
    root = tkinter.Tk()
    root.title("Titulo da janela")
    root.geometry("350x200")
    root.resizable(False, False)

    label = tkinter.Label(root, text="PDF ABAIXO: ")
    label.pack()
    
    textBox = tkinter.Entry(root,width=50)
    textBox.pack();

    button = tkinter.Button(root, text="Buscar")
    #button['command'] = LigaLED
    button.pack()

    root.mainloop()

Interface();

   
