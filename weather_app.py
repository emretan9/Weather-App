from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
     city=textfield.get()

     geolocator=Nominatim(user_agent="geoapiExercises") #imports the Nominatim geocoder class from the geopy library and creates a geolocator object that uses the geoapiExercises user agent.
     location=geolocator.geocode(city) #uses the geolocator object to geocode the given city string and retrieve a Location object that contains information about the city's latitude, longitude, address, and other details.
     obj=TimezoneFinder() #creates a TimezoneFinder object from the timezonefinder library.
     result=obj.timezone_at(lng=location.longitude,lat=location.latitude) #uses the TimezoneFinder object to determine the timezone at the coordinates of the city, which are retrieved from the location object using its longitude and latitude attributes. The resulting timezone string is stored in the result variable.
    
     home=pytz.timezone(result) #creates a timezone object from the pytz library using the result timezone string. This timezone object can be used to convert datetimes between UTC and the local time of the specified timezone.
     local_time=datetime.now(home)
     current_time=local_time.strftime("%I:%M %p") #The strftime() method is a method of the datetime class that converts a datetime object to a string according to a specified format. In this case, the format string "%I:%M %p" is used, which stands for: %I - hours in 12-hour format, %M - minutes, %p - AM/PM designation.
     clock.config(text=current_time)
     name.config(text="CURRENT WEATHER")

     #Weather
     api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=76538a427d4dfeca2b9efa12a3835144"

     json_data=requests.get(api).json()
     condition=json_data['weather'][0]['main']
     description=json_data['weather'][0]['description']
     temp=int(json_data['main']['temp']-273.15)
     pressure=json_data['main']['pressure']
     humidity=json_data['main']['humidity']
     wind=json_data['wind']['speed']

     t.config(text=(temp,"°"))
     c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

     w.config(text=wind)
     h.config(text=humidity)
     d.config(text=description)
     p.config(text=pressure)
    
    except Exception as e:
       messagebox.showerror("Weather App","INVALID CITY!")

#Search box
Search_image=PhotoImage(file="Weather App\search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,
                   justify="center",
                   width=17,
                   font=("poppins",25,"bold"),
                   bg="#404040",
                   border=0,
                   fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="Weather App\search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)


#Logo
logo_image=PhotoImage(file="Weather App\logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#Bottom box
frame_image=PhotoImage(file="Weather App\kutu.png")
frame_myImage=Label(image=frame_image)
frame_myImage.pack(padx=5,pady=5,side=BOTTOM)

#Time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",15))
clock.place(x=30,y=130)



#Label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d") #Temperature
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold")) #Condition
c.place(x=400,y=250)

w=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef") #Wind
w.place(x=120,y=430)
h=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef") #Humidity
h.place(x=280,y=430)
d=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef") #Description
d.place(x=450,y=430)
p=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef") #Pressure
p.place(x=670,y=430)




root.mainloop()

################################################
#     ⒸCopyrighted by Emre TanrıkuluⒸ        #
#                                              #
#                                              #
################################################