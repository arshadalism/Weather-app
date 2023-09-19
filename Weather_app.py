from tkinter import *
import tkinter as tk
import requests
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()


root = Tk()
root.title("Weather App Youtube")
root.geometry("900x500+300+200")
root.resizable(False, False)


def bad_request_clear():
    error_label.config(text="")
    return


def bad_request_appear():
    error_label.config(text="Bad_Request", fg="red")
    return


def clear_values():
    t.config(text="")
    f_l.config(text="....")
    w_s.config(text="....")
    w_d.config(text="....")
    h.config(text="....")
    ctry.config(text="")
    clock.config(text="")
    name.config(text="")
    temp.config(text="")
    country.config(text="")
    bad_request_appear()


def all_clear_values():
    t.config(text="")
    f_l.config(text="....")
    w_s.config(text="....")
    w_d.config(text="....")
    h.config(text="....")
    ctry.config(text="")
    clock.config(text="")
    name.config(text="")
    temp.config(text="")
    country.config(text="")
    bad_request_clear()
    textfield.delete(0, tk.END)



def getWeather():
    city = textfield.get()
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json?"
    params = {"key": api_key,
              "q": city}
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        response = response.json()
        name.config(text="CURRENT WEATHER")
        if response is None:
            error_label = Label(window, text='Bad request', font=("Helvetica", 10, 'bold'))
            error_label.place(x=160, y=150)
            return

        temp_value = response.get("current").get("temp_c")
        feelslike = response.get("current").get("feelslike_c")
        wind_value = response.get("current").get("wind_kph")
        wind_dir_value = response.get("current").get("wind_dir")
        humidity_value = response.get("current").get("humidity")
        country_value = response.get("location").get("country")
        current_time = response.get("location").get('localtime')

        t.config(text=f"{temp_value}°C")
        f_l.config(text=f"{feelslike}°C")
        w_s.config(text=f"{wind_value} km/h")
        w_d.config(text=f"{wind_dir_value}")
        h.config(text=f"{humidity_value}")

        clock.config(text=f"{current_time}")
        ctry.config(text=f"{country_value}")

        temp.config(text="TEMP")
        country.config(text="COUNTRY")
        bad_request_clear()

    else:
        clear_values()
        bad_request_appear()
        # messagebox.showerror("Weather App Youtube", "Bad_Request")
        return


# search box
Search_image = PhotoImage(file="Copy of search.png")
my_search_image = Label(image=Search_image)
my_search_image.place(x=20, y=20)

textfield = tk.Entry(root, justify="left", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="Copy of search_icon.png")
my_search_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
my_search_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=200, y=140)

# Bottom box
Frame_image = PhotoImage(file="Copy of box.png")
frame_my_image = Label(image=Frame_image)
frame_my_image.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)

# Label
Label1 = Label(root, text="FEELSLIKE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label1.place(x=120, y=400)

Label2 = Label(root, text="WIND_KPH", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label2.place(x=270, y=400)

Label3 = Label(root, text="WIND_DIR", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label3.place(x=480, y=400)

Label4 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label4.place(x=650, y=400)

ctry = Label(font=("arial", 30, "bold"), fg="#ee666d")
ctry.place(x=510, y=330)

t = Label(font=("arial", 30, "bold"), fg="#ee666d")
t.place(x=510, y=180)

c = Label(font=("arial", 70, "bold"))
c.place(x=400, y=250)

f_l = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
f_l.place(x=120, y=430)

w_s = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
w_s.place(x=270, y=430)

w_d = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
w_d.place(x=500, y=430)

h = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=670, y=430)

clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

temp = Label(font=("arial", 50, "bold"), fg="black")
temp.place(x=500, y=100)

country = Label(font=("arial", 40, "bold"), fg="black")
country.place(x=500, y=250)

error_label = Label(font=("Helvetica", 12, 'bold'))
error_label.place(x=360, y=106)

clear_button = Button(root, text="CLEAR", font=("arial", 11, "bold"), fg="green", command=all_clear_values)
clear_button.place(x=800, y=50)

root.mainloop()
