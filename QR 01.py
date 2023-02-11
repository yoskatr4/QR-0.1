import tkinter as tk
import qrcode
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import cv2
import numpy as np
from pyzbar import pyzbar
from datetime import datetime

root = tk.Tk()
root.title(" QR 0.1")

def change_bg_color1():
    color = "black" if bg_color.get() == "white" else "white"
    bg_color.set(color)
    root.config(bg=color)


def open1():

    def generate_qr_code():
        url = entry.get()
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr_code.png")
        image = Image.open("qr_code.png")
        image = image.resize((250, 250), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label.config(image=image)
        label.image = image


    def save_qr_code():
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            image = Image.open("qr_code.png")
            image.save(file_path)

    root1 = tk.Tk()
    root1.title("QR Code Generator")
    root1.geometry("500x500")

    frame = tk.Frame(root1)
    frame.pack(pady=20)

    label = tk.Label(frame)
    label.pack()

    entry = tk.Entry(frame, width=50)
    entry.pack(pady=10)

    generate_button = tk.Button(frame, text="Generate QR Code", command=generate_qr_code)
    generate_button.pack(pady=10)

    save_button = tk.Button(frame, text="Save QR Code", command=save_qr_code)
    save_button.pack()

    root1.mainloop()


def open2():
    def decode_qr_codes():
    # QR kodunun okunması için kamera açılır
        cap = cv2.VideoCapture(0)

        while True:
        # Kameradan görüntü alınır
            _, frame2 = cap.read()

        # Görüntüde QR kodları aranır
            decoded_objects = pyzbar.decode(frame2)
        
        # QR kodlar bulunursa, kodlar ekrana yazdırılır
            for obj in decoded_objects:
                label_text.set(obj.data.decode("utf-8"))
                break
            else:
                label_text.set("QR Kod Bulunamadı")
        
            cv2.imshow("QR Kod Tarama", frame2)
        
        # Esc tuşuna basılırsa döngüden çıkılır
            key = cv2.waitKey(1)
            if key == 27:
                break
    
        cap.release()
        cv2.destroyAllWindows()

    # Tkinter penceresi oluşturulur
    root2 = tk.Tk()
    root2.title("QR Kod Tarama")
    root2.geometry("200x120")

# Labe oluşturulur
    label_text = tk.StringVar()
    label = tk.Label(root2, textvariable=label_text)
    label.pack()

# Buton oluşturulur
    button = tk.Button(root2, text="QR Kodu Oku", command=decode_qr_codes)
    button.pack()

    label_2 = tk.Label(root2, text="Çıkmak İçin ESC Tuşuna Basın")
    label_2.pack()









    root2.mainloop()


def hakkimda():
    root3 =tk.Tk()
    root3.title("HAKKIMDA")
    root3.geometry("650x200")

    label= tk.Label(root3, text="Öncelikle Hoşgeldiniz\nBu uygulamanın yapılış amacı çevrim dışı bir şekilde qr kod oluşturmaktır\nPiyasada kendisini geliştirmiş fakat reklam yapan uygulamalar yerini bu uygulamayı tercih ettiğiniz için teşekkürler\nBu uygulamayı kullanıp paylaşarak bana çok büyük destekte bulunursunuz\nBu uygulama 212 satır kod ile yazılmıştır\nYakında QR 0.2 çıkacaktır bizi takip etmeyi unutmayın ;)")
    label.grid(row=0,column=0)

    label= tk.Label(root3, text="Yapımcı : Enes Aksoy")
    label.grid(row=2,column=0)

    label= tk.Label(root3, text="Yapım Tarihi : 10.02.2023")
    label.grid(row=4,column=0)

    label= tk.Label(root3, text="Yapım Saati : 21:50")
    label.grid(row=5,column=0)

    label= tk.Label(root3, text="Yapım Yeri : Türkiye/Isparta/Yalvaç")
    label.grid(row=6,column=0)

    label= tk.Label(root3, text="Yapıncı e-posta : ensaks46@gmail.com")
    label.grid(row=3,column=0)




    root3.mainloop()








welcome = tk.Label(root, text= "QR 0.1'e Hoşgeldiniz",font="Times 20" )
welcome.grid(row=0, column=0, padx=10, pady=10)

welcome = tk.Label(root, text= "Birini Seç  : ",font="Times 13" )
welcome.grid(row=1, column=0, padx=10, pady=10)


bg_color = tk.StringVar(value="white")
toggle_button = tk.Button(root,text= " Karanık Mod", command=change_bg_color1)
toggle_button.grid(row=5, column=0, padx=10, pady=10)



buton=tk.Button(root,text="Qr Kod Oluştur",command=open1)
buton.grid(row=2, column=0, padx=10, pady=10)

hbuton=tk.Button(root,text="Hakkımda",command=hakkimda)
hbuton.grid(row=4, column=0, padx=10, pady=10)


ex_buton1=tk.Button(root,text="Çıkış",command=quit) 
ex_buton1.grid(row=5,column=1, padx=10, pady=10)


buton1=tk.Button(root,text="Qr Kod Okut",command=open2)
buton1.grid(row=3, column=0, padx=10, pady=10)




def update_time():
    # Şu anki zaman
    current_time = datetime.now().strftime("%H:%M:%S")
    # Label'a zaman yazdırılır
    label_text.set(current_time)
    # 1 saniyede bir fonksiyon tekrar çağırılır
    root.after(1000, update_time)

# Label oluşturulur
label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text, font=("Helvetica", 24))
label.grid(row=3,column=1)

label2 = tk.Label(root, text="SAAT : ", font="Times 20")
label2.grid(row=2,column=1)

# Zamanı güncelleme fonksiyonu çağırılır
update_time()



root.mainloop()