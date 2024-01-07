from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+300+200")
root.resizable(False,False)

#icon image
icon =PhotoImage(file="logo image.png")
root.iconphoto(False,icon)

def Track():
	try:
		# Clear labels
		country.config(text="")
		sim.config(text="")
		zone.config(text="")
		clock.config(text="")
		longitude.config(text="")
		latitude.config(text="")
		error_label.config(text="", fg="black")

		enter_number=entry.get()
		number=phonenumbers.parse(enter_number)

		#Get country
		locate=geocoder.description_for_number(number,'en')
		country.config(text=locate)

		#get Operator
		operator=carrier.name_for_number(number,'en')
		sim.config(text=operator)

		#Get phone timezone
		timez=timezone.time_zones_for_number(number)
		zone.config(text=timez)

		#longitude and latitude
		geolocator=Nominatim(user_agent="geoapiExercises")
		location=geolocator.geocode(locate)

		lng=location.longitude
		lat=location.latitude
		longitude.config(text=lng)
		latitude.config(text=lat)

		#phone time
		obj =TimezoneFinder()
		result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

		home = pytz.timezone(result)
		local_time = datetime.now(home)
		current_time = local_time.strftime("%I:%M %p")
		clock.config(text=current_time)

	except phonenumbers.NumberFormatError:
		# Handle the case where the phone number is invalid
		error_label.config(text="Invalid phone number. Please enter a valid one.", fg="red")
	except geopy.exc.GeocoderInsufficientPrivileges:
		# Handle the case where geocoding privileges are insufficient
		error_label.config(text="Insufficient privileges for geocoding. Provide a valid user agent.", fg="red")
	except Exception as e:
		# Handle other exceptions
		error_label.config(text=f"An error occurred: {e}", fg="red")
	else:
		# Reset error label if no exception occurred
		error_label.config(text="", fg="black")

#logo
logo =PhotoImage(file="logo image.png")
Label(root,image=logo).place(x=240,y=70)

Eback = PhotoImage(file="search png.png")
Label(root,image=Eback).place(x=20,y=190)

# Create an error label
error_label = Label(root, text="", fg="black", font=('arial', 10, 'italic'))
error_label.place(x=50, y=270)

#heading
Heading = Label(root,text="TRACK NUMBER", font=('arial',15,'bold'))
Heading.place(x=90,y=110)

#Bottom box
Box = PhotoImage(file="bottom png.png")
Label(root,image=Box).place(x=-2,y=355)

#entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=('arial',20,'bold'))
enter_number.place(x=50,y=220)

#search button
Search_image = PhotoImage(file="search.png")
search = Button(root,image=Search_image, borderwidth = 0,cursor='hand2',bd=0, command = Track).place(x=35,y=300)

#label Information
country=Label(root,text="Country:",bg="#57adff",fg="black",font=('arial',10,'bold'))
country.place(x=50,y=400)

sim=Label(root,text="SIM:",bg="#57adff",fg="black",font=('arial',10,'bold'))
sim.place(x=200,y=400)

zone=Label(root,text="Timezone:",bg="#57adff",fg="black",font=('arial',10,'bold'))
zone.place(x=50,y=450)

clock=Label(root,text="Phone Time:",bg="#57adff",fg="black",font=('arial',10,'bold'))
clock.place(x=200,y=400)

longitude=Label(root,text="Longitude:",bg="#57adff",fg="black",font=('arial',10,'bold'))
longitude.place(x=50,y=500)

latitude=Label(root,text="Latitude:",bg="#57adff",fg="black",font=('arial',10,'bold'))
latitude.place(x=200,y=500)