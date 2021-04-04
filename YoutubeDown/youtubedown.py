from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


Folder_Name = ""


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Por favor mude a pasta", fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url) > 1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(
                progressive=True, file_extension='mp4').last()

        elif (choice == choices[2]):
            select = yt.streams.filter(
                only_audio=True).first()

        else:
            ytdError.config(text="Cole o link, agora", fg="red")

    select.download(Folder_Name)
    ytdError.config(text="Download completo!")


root = Tk()
root.title("J.Download")
root.geometry("350x400")
root.columnconfigure(0, weight=1)

ytdLabel = Label(root, text="Insira o link do vídeo", font=("Arial,15"))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError = Label(root, text="Aguarde...",
                 fg="red", font=("Arial", 10))
ytdError.grid()

saveLabel = Label(root, text="Salve o arquivo", font=("Arial", 15, "bold"))
saveLabel.grid()


saveEntry = Button(root, width=10, bg="red",
                   fg="white", text="Selecione a Pasta", command=openLocation)
saveEntry.grid()

locationError = Label(root, text="Pasta não localizada",
                      fg="red", font=("Arial", 10))
locationError.grid()

ytdQuality = Label(
    root, text="Selecione a qualidade do Download", font=("Arial", 15))
ytdQuality.grid()

choices = ["720p", "144p", "Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()

downloadbtn = Button(root, text="Download", width=10,
                     bg="red", fg="white", command=DownloadVideo)
downloadbtn.grid()

devLabel = Label(root, text="Jailson App", font=("Arial", 15))
devLabel.grid()


root.mainloop()
