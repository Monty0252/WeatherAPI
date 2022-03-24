from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():
    try:
        city = search_box.get()

        weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
        response = requests.get(url, params=params)
        data = response.json()

        temperature = int(data['main']['temp'])
        desc = data['weather'][0]['description']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        feels_like = int(data['main']['temp'])
        pressure = data['main']['pressure']

        city_name.config(text=city.upper())
        temp_text.config(text=f"{temperature}°F")
        desc_text.config(text=desc.capitalize())
        wind_text.config(text=f"{wind} mph")
        humidity_text.config(text=f"{humidity}%")
        pressure_text.config(text=f"{pressure} hPa")
        feels_text.config(text=f"{feels_like}°F")

    except Exception as e:
        messagebox.showerror("Error", "Invalid Location. Please try again.")


# Weather GUI
Dim = "900x500"
Win = tk.Tk()
Win.title("Weather App")
Win.geometry(Dim)
Win.resizable(FALSE, FALSE)

# Search Box
search_bg = "#404040"
Search_font = "poppins,25,bold"
search_fg = "white"

search_img = PhotoImage(file="searchbar.png")
s_img = Label(image=search_img)
s_img.place(x=20, y=20)

search_box = tk.Entry(Win, width=30, font=Search_font, bg=search_bg, border=0, fg=search_fg)
search_box.place(x=50, y=40)
search_box.focus()
search_box.bind("<Return>", (lambda event: get_weather()))  # allows search with return/enter key

# Search Icon
search_icon = PhotoImage(file="searchicon.png")
icon_img = Button(image=search_icon, borderwidth=0, cursor="hand2", bg=search_bg, command=get_weather)
icon_img.place(x=338, y=30)

# Weather Logo
logo_img = PhotoImage(file="weatherlogo.png")
logo = Label(image=logo_img)
logo.place(x=180, y=100)

# Bottom box
box_img = PhotoImage(file="box.png")
box = Label(image=box_img)
box.place(x=50, y=370)

# City Name Box
city_name = Label(Win, font=("arial", 20, "bold"))
city_name.place(x=40, y=100)

# Temperature Box
temp_text = Label(font=("arial", 70, "bold"), fg="#ee666d")
temp_text.place(x=500, y=150)

# Weather Description box
desc_text = Label(font=("arial", 20, 'bold'))
desc_text.place(x=510, y=260)

# Labels
Label_font = ("Helvetica", 15, 'bold')
search_bg = "#1ab5ef"
search_fg = "white"

WindLabel = Label(Win, text="WIND", font=Label_font, fg=search_fg, bg=search_bg, anchor='n')
WindLabel.place(x=100, y=390)

HumidityLabel = Label(Win, text="HUMIDITY", font=Label_font, fg=search_fg, bg=search_bg, anchor='n')
HumidityLabel.place(x=250, y=390, )

FeelsLabel = Label(Win, text="FEELS LIKE", font=Label_font, fg=search_fg, bg=search_bg, anchor='n')
FeelsLabel.place(x=430, y=390)

PressureLabel = Label(Win, text="PRESSURE", font=Label_font, fg=search_fg, bg=search_bg, anchor='n')
PressureLabel.place(x=650, y=390)

# Labels Text Box
text_font = ("arial", 15, "bold")
text_bg = "#1ab5ef"

wind_text = Label(font=text_font, bg=text_bg)
wind_text.place(x=140, y=420, anchor='n')

humidity_text = Label(font=text_font, bg=text_bg)
humidity_text.place(x=290, y=420, anchor='n')

feels_text = Label(font=text_font, bg=text_bg)
feels_text.place(x=480, y=420, anchor="n")

pressure_text = Label(font=text_font, bg=text_bg)
pressure_text.place(x=700, y=420, anchor='n')

Win.mainloop()
