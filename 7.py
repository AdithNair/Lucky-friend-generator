from tkinter import *
import random

root=Tk()

root.title("Lucky Friend Wheel")
root.geometry("500x500")


list1 = ["Akrash" , "Pranav" , "Kushal" , "JT" , "Rishit"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_luck_friend = list1[random_no]
    print("Your lucky friend is: " + random_lucky_friend)
    
btn1 = Button(root)
btn1 = Button(root, text="Who is your lucky friend?  ", command = random_number)
btn1.place(relx= 0.5,rely =0.5, anchor = CENTER )

root.mainloop()