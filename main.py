from tkinter import *
from PIL import ImageTk, Image
import ctypes
import mysql.connector

database = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

db = database.cursor()

class App:
    def __init__(self):
        ctypes.windll.user32.SetProcessDPIAware()
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.title("Auth")
        self.login_entry = None
        self.password_entry = None
        self.create_widgets()

        self.window.mainloop()

    def register_account(self):
        if not self.login_entry or not self.password_entry:
            print(f"Proszę wypełnić wszystkie pola.")
            return

        login = self.login_entry.get()
        password = self.password_entry.get()

        db.execute("SELECT * FROM accounts WHERE login=%s", (login,))
        if db.fetchone() is not None:
            print(f"Konto o podanym loginie już istnieje.")
            return

        db.execute("INSERT INTO accounts (nickname, login, password) VALUES (%s, %s, %s)", ("", login, password))
        database.commit()

        print(f"Konto zostało utworzone.")

    def login_account(self):
        if not self.login_entry or not self.password_entry:
            print(f"Proszę wypełnić wszystkie pola.")
            return

        login = self.login_entry.get()
        password = self.password_entry.get()

        db.execute("SELECT * FROM accounts WHERE login=%s", (login,))
        account = db.fetchone()
        if account is None:
            print(f"Nie znaleziono konta o podanym loginie.")
            return

        if account[3] != password:
            print(f"Nieprawidłowe hasło.")
            return

        self.logged_in = True
        self.current_user_id = account[0]
        self.current_user_nickname = account[1]
        self.current_user_money = account[4]

        print(f"Zalogowano.")

    def create_widgets(self):
        image = Image.open("background.png")
        photo = ImageTk.PhotoImage(image)
        label = Label(self.window, image=photo)
        label.image = photo
        label.pack()

        self.window.geometry(f"{image.size[0]}x{image.size[1]}")
        background_image = ImageTk.PhotoImage(image)
        background_label = Label(self.window, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        login_entry_bg = Image.open("editbox.png")
        login_entry_photo = ImageTk.PhotoImage(login_entry_bg)
        login_entry_label = Label(self.window, image=login_entry_photo)
        login_entry_label.image = login_entry_photo
        login_entry_label.place(relx=0.5, rely=0.4, anchor="center")

        self.login_entry = Entry(self.window, width=20, font=("Arial", 16))
        self.login_entry.place(relx=0.5, rely=0.4, anchor="center")

        password_entry_bg = Image.open("editbox.png")
        password_entry_photo = ImageTk.PhotoImage(password_entry_bg)
        password_entry_label = Label(self.window, image=password_entry_photo)
        password_entry_label.image = password_entry_photo
        password_entry_label.place(relx=0.5, rely=0.5, anchor="center")

        self.password_entry = Entry(self.window, width=20, font=("Arial", 16), show="*")
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center")

        login_button_bg = Image.open("button.png")
        login_button_photo = ImageTk.PhotoImage(login_button_bg)
        login_button = Button(self.window, image=login_button_photo, command=self.login_account, borderwidth=0)
        login_button.image = login_button_photo
        login_button.place(relx=0.5, rely=0.6, anchor="center")
    
        register_button_bg = Image.open("button.png")
        register_button_photo = ImageTk.PhotoImage(register_button_bg)
        register_button = Button(self.window, image=register_button_photo, command=self.register_account, borderwidth=0)
        register_button.image = register_button_photo
        register_button.place(relx=0.5, rely=0.7, anchor="center")



if __name__ == "__main__":
    app = App()
