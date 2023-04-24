import tkinter
from tkinter import *
from  tkinter import ttk
import time
import sqlite3
from tkinter import messagebox




def YolcuTablo():
    #Burada veri tabanına bağlanıp verileri kaydediyoruz.
    vt=sqlite3.connect("Yolcular.db")
    imlec=vt.cursor()
    table=imlec.execute("CREATE TABLE IF NOT EXISTS Yolcular (Ad NOT NULL,Soyad NOT NULL,Durum,Biniş Havalimanı NOT NULL,İniş Havalimanı NOT NULL,Saat INTEGER)")
    imlec.execute("""INSERT INTO Yolcular (Ad,Soyad,Durum,Biniş,İniş ,Saat) VALUES(?,?,?,?,?,?)""",(Ad.get(),Soyad.get(),var.get(),Sehirler.get(),Sehirler1.get(),Sefer_Saatleri.get()))
    #Burada veri tabanındaki bütün verileri konsola yazdırıyoruz.
    imlec.execute("SELECT *FROM Yolcular")
    yolcular = imlec.fetchall()
    print(yolcular)


    vt.commit()
    vt.close()





def Yazdır():
    #Burada ilk pencerede girdiğimiz bilgileri kontrol edip onaylıyoruz.
    pencere1=tkinter.Tk()
    pencere1.title("Bi Bilet")
    pencere1.geometry("400x400")
    Label(pencere1, text="Jetgiller Havayolu", bg="blue").pack(fill=X, pady=10)
    YolcuAdı=Label(pencere1,text="Adınız Soyadınız:",bg="red").place(x=40,y=50)
    YolcuAdı1 = Label(pencere1, text=Ad.get(), bg="grey").place(x=150, y=50)

    YolcuSoyad=Label(pencere1,text="Soyadınız:",bg="red").place(x=40,y=70)
    YolcuSoyad1 = Label(pencere1, text=Soyad.get(), bg="grey").place(x=150, y=70)

    BinilenSehir=Label(pencere1,text="Binilen Şehir:",bg="red").place(x=40,y=90)
    BinilenSehir1 = Label(pencere1, text=Sehirler.get(), bg="grey").place(x=150, y=90)

    İnilenSehir = Label(pencere1, text="İnilen Şehir:", bg="red").place(x=40, y=110)
    İnilenSehir1 = Label(pencere1, text=Sehirler1.get(), bg="grey").place(x=150, y=110)

    Durum = Label(pencere1, text="Kişi Durumu:", bg="red").place(x=40, y=130)
    Durum1 = Label(pencere1, text=var.get(), bg="grey").place(x=150, y=130)

    HareketSaatı = Label(pencere1, text="Sefer Saati:", bg="red").place(x=40, y=150)
    HareketSaatı1= Label(pencere1, text=Sefer_Saatleri.get(), bg="grey").place(x=150, y=150)
    #Tamam'a bastığımız takdirde bilgileri veri tabanına ekliyoruz.
    b2=Button(pencere1,text="Tamam",command=YolcuTablo).place(x=180,y=180)

    t1 = Label(pencere1, text=time.asctime(), bg="blue").place(x=260, y=30)


    pencere1.mainloop()


#Arayüz penceremizi oluşturuyoruz
pencere=tkinter.Tk()
pencere.title("Bi Bilet")
pencere.geometry("500x500")
Label(pencere,text="Jetgiller Havayolu",bg="blue").pack(fill=X,pady=10)
#Projemizde bulunan şehirlerimizi değere atayıp Combobox ile kullanıcıya sunuyoruz.
deger=StringVar()
Label(pencere,text="Biniş Havalimani",bg="green").place(x=40,y=40)
Sehirler=ttk.Combobox(pencere,width=20,textvariable= deger)
A=Sehirler['values']=('İstanbul',
                    'Ankara',
                    'İzmir',
                    'Kayseri',
                    'Konya',
                    'Antalya',
                    'Gaziantep',
                    'Rize',
                    'Malatya',
                    'Trabzon',
                    'Samsun',
                    'Ağrı'
                    )
Sehirler.pack()
deger1=StringVar()
Sehirler1=ttk.Combobox(pencere,width=20,textvariable=deger1)
Label(pencere,text="İniş Havalimani",bg="green").place(x=45,y=63)
B=Sehirler1['values']=('İstanbul',
                    'Ankara',
                    'İzmir',
                    'Kayseri',
                    'Konya',
                    'Antalya',
                    'Gaziantep',
                    'Rize',
                    'Malatya',
                    'Trabzon',
                    'Samsun',
                    'Ağrı'
                    )
Sehirler1.pack()
deger2=StringVar()
Label(pencere,text="Sefer Saatleri",bg="green").place(x=55,y=85)
Sefer_Saatleri=ttk.Combobox(pencere,width=20,textvariable=deger2)
Sefer_Saatleri['values']=('06.00',
                          '06.50',
                          '07.30',
                          '08.15',
                          '09.00',
                          '10.00',
                          '10.45',
                          '11.20',
                          '12.10',
                          '13.00',
                          '13.40',
                          '14.15',
                          '14.50',
                          '15.20',
                          '16.00',
                          '16.40',
                          '17.10',
                          '18.05',
                          '19.10',
                          '19.30',
                          '20.40',
                          '21.20',
                          '22.00',
                          '22.45',
                          '23.30',
                          '00.00',
                          '01.30'
                          )
Sefer_Saatleri.pack()
#Kullanıcı adını alıyoruz.
Ad=Label(pencere,text="Adınız: ",bg='green').place(x=50,y=150)
Ad=Entry(pencere)
Ad.place(x=180,y=150)
Ad.get()


#Kullanıcı adını alıyoruz.
Soyad=Label(pencere,text="Soyadınız: ",bg='green').place(x=50,y=175)
Soyad=Entry(pencere)
Soyad.place(x=180,y=175)
Soyad.get()


#Kullanıcı öğrenci mi değil mi onu belirliyoruz.
var=StringVar()
r1=Radiobutton(pencere,text="Yetişkin",variable=var,value="Yetişkin").place(x=180,y=220)
r2=Radiobutton(pencere,text="Öğrenci",variable=var,value="Öğrenci").place(x=180,y=200)
#Butona basınca bizi ikinci sayfaya yönlendiriyor.
b1=Button(pencere,text="Tamam",command=Yazdır,borderwidth=10).place(x=200,y=250)
#Güncel tarih ve saat bilgisini alıyoruz.
t=Label(pencere,text=time.asctime(),bg="blue").place(x=350,y=30)

#penceremizi  kapatıyoruz
pencere.mainloop()
