import requests
import tkinter
import PyPDF2
import re

#C:\\Users\\202403282046\\Downloads\\TrabalhoPython\\Lista de datas.pdf

url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

response = requests.request("GET", url, headers=headers, data=payload)
feriados = response.json()
    
def Get_pdf():
    pdf = textBox.get().strip()
    reader = PyPDF2.PdfReader(pdf)

    datas = re.findall(r"\d{4}-\d{2}-\d{2}",reader.pages[0].extract_text())

    feriadosEncontrados = []
    for data in datas:
        for feriado in feriados:
            if data == feriado["date"]:
               feriadosEncontrados.append(data)

    labelFeriado.config(text=(feriadosEncontrados))

root = tkinter.Tk()
root.title("Trabalho pyhton")
root.geometry("350x200")
root.resizable(False, False)

label = tkinter.Label(root, text="PDF ABAIXO: ")
label.pack()
    
textBox = tkinter.Entry(root,width=50)
textBox.pack();

button = tkinter.Button(root, text="Buscar")
button['command'] = Get_pdf
button.pack()

labelFeriado = tkinter.Label(root, text="")
labelFeriado.pack()

root.mainloop()








   
