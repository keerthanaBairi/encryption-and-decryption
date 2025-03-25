from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()
        if not message:
            messagebox.showerror("Encryption", "Enter text to encrypt")
            return

        encoded_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_message)
        encrypted_text = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED TEXT", font="arial", fg="white", bg="#ed3833").place(x=10, y=10)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypted_text)
        text2.config(state=DISABLED)

    elif not password:
        messagebox.showerror("Encryption", "Please enter a password")

    else:
        messagebox.showerror("Encryption", "Invalid Password")


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()
        if not message:
            messagebox.showerror("Decryption", "Enter text to decrypt")
            return

        try:
            decoded_message = base64.b64decode(message.encode("ascii"))
            decrypted_text = decoded_message.decode("ascii")

            Label(screen2, text="DECRYPTED TEXT", font="arial", fg="white", bg="#00bd56").place(x=10, y=10)
            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypted_text)
            text2.config(state=DISABLED)

        except Exception as e:
            messagebox.showerror("Decryption", "Invalid encrypted text")

    elif not password:
        messagebox.showerror("Decryption", "Please enter a password")

    else:
        messagebox.showerror("Decryption", "Invalid Password")


def reset():
    code.set("")
    text1.delete(1.0, END)


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("PctApp")

    Label(screen, text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=20)
    text1 = Text(screen, font="Roboto 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(screen, text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(screen, text="Encrypt", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(screen, text="Decrypt", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(screen, text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()
