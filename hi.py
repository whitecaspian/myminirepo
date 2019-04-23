from tkinter import*
import webbrowser
def show():
    name=text1.get()
    name1=text2.get()
    if name =="holland"and name1=="USA":
        print("country")
        webbrowser.open("http://www.yahoo.com")
    else:
           print("not a country")
      
k=Tk()
k.title("ebe")
k.geometry("6000x600")
k.configure(bg="blue")
Label(k,text="country",font=60,fg="black",bg="yellow").grid(row=1,column=1)
Label(k,text="ebe",font=200,fg="black",bg="yellow").grid(row=1,column=2)
Label(k,text="immi",font=200,fg="black",bg="green").grid(row=2,column=3)
Label(k,text="yahoo",font=200,fg="green",bg="white").grid(row=3,column=1)
text1=Entry(k,width=20,bg="white")
text1.grid(row=5,column=2)
text2=Entry(k,width=50,bg="white",fg="blue")
text2.grid(row=5,column=10)
e=Button(k,width=60,text="submit",bg="black",fg="white",font=20)
e.grid(row=3,column=12)
e=Button(k,width=70,text="ashole",bg="green",fg="red",font=50,command=show)
e.grid(row=4,column=9)


