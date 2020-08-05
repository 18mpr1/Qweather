# This app was self-made by 18mpr1
# Finished August 5, 2020 after staying up late
# The background and icon change based on the weather at Queen's University in Kingston, ON


from tkinter import *
import datetime
import pytz
import requests

# root
root = Tk()
root.title('Qweather')
root.iconbitmap(r'C:\Users\matth\PycharmProjects\QueensWeather\icons')
root.geometry("450x400")
root.configure(bg="#2886C9")

# Label
queensLabel = Label(root,text="🆀🆄🅴🅴🅽'🆂 🆄🅽🅸🆅🅴🆁🆂🅸🆃🆈",font=("Arial",28,'underline'),width="20",height="1",fg="#F0B40A",bg="#A21616")
queensLabel.pack(side=TOP,fill=X)
cityLabel = Label(root,text="𝓚𝓲𝓷𝓰𝓼𝓽𝓸𝓷, 𝓞𝓝",font=("Arial",22),width="20",height="1",fg="#F0B40A",bg="#103652")
cityLabel.pack(side=TOP,fill=X)
#mainframe = Frame(root,bg="#8128FF")
#mainframe.pack(fill="both",expand=True)
timeLabel = Label(root,text="",font=("Arial",10,'bold'),fg="#F0B40A",bg='#42085C')
timeLabel.pack(side=BOTTOM,fill=X)
dateLabel = Label(root,text="",font=("Denmark",10,'bold'),fg="#F0B40A",bg="#900C3F")
dateLabel.pack(side=BOTTOM,fill=X)
#canvas = Canvas(root,bg="#2886C9")
#canvas.pack()
#img = PhotoImage(file="campus.ppm")
#canvas.create_image(1,1,anchor=NW, image=img)


# Definitions
def clock():
    x = datetime.datetime.now(pytz.timezone('US/Eastern'))
    wday = x.strftime("%A")
    day = x.strftime("%d")
    month = x.strftime("%B")
    year = x.strftime("%Y")
    hour = x.strftime("%H")
    minutes = x.strftime("%M")
    seconds = x.strftime("%S")
    z = "Local Time: " + hour + ":" + minutes + ":" + seconds
    fd = wday + ", " + month + " " + day + ", " + year
    #print(fd)
    #print(z)
    dateLabel.config(text=fd)
    dateLabel.after(100000,clock)
    timeLabel.config(text=z)
    timeLabel.after(500,clock)


# Kingston City ID: 5992495
cId = 5992495
url = 'http://api.openweathermap.org/data/2.5/weather?id=5992495&appid=4489e5b388fec0529f5f088637031035&units=metric'

res = requests.get(url)
data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longtitude = data['coord']['lon']
description = data['weather'][0]['description']
id = data['weather'][0]['id']
icon = data['weather'][0]['icon']
print(id)
print("icon: " + icon)
print('Temperature : {} degrees celsius'.format(temp))
print('Windspeed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longtitude))
print('Description : {}'.format(description))
print(icon)


wLabel1 = Label(root,text=temp,font=("Arial",15,'bold'),fg="#ECE5E0",bg="#095244",height='4',width='35')
wLabel1.pack(side=RIGHT)


#photo1 = PhotoImage(file="campus.ppm")
#wLabel2 = Label(root,image = photo1)
#wLabel2.pack(side=LEFT)
#photo2 = PhotoImage(file='')
#wLabel3 = Label(root,image = photo2)
#wLabel3.pack(side=LEFT)

def showWeather():

    a = 'Temperature: {} °C\n'.format(temp) + 'Windspeed: {} m/s\n'.format(wind_speed) + 'Description: {}'.format(description)
    wLabel1.config(text=a)

    if icon:
        if icon == '01d':
            root.configure(bg="#56BEFF")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#56BEFF", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '01n':
            root.configure(bg="#031A29")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#031A29", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '02d':
            root.configure(bg="#9BD5F9")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#9BD5F9", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '02n':
            root.configure(bg="#535A5E")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#535A5E", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '03d':
            root.configure(bg="#D6ECFA")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#D6ECFA", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '03n':
            root.configure(bg="#2D3D47")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#2D3D47", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '04d':
            root.configure(bg="#879DAB")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#879DAB", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '04n':
            root.configure(bg="#292B3A")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root,image=photo,bg="#292B3A",width='300',height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial",8,'bold'),width='32',fg="white",bg="green")

        elif icon == '09d':
            root.configure(bg="#7D8E98")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#7D8E98", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), width='32', fg="white", bg="green")

        elif icon == '09n':
            root.configure(bg="#343F46")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#343F46", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), fg="white", bg="green")

        elif icon == '10d':
            root.configure(bg="#6D7981")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#6D7981", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), fg="white", bg="green")

        elif icon == '10n':
            root.configure(bg="#2D3C45")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#2D3C45", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), fg="white", bg="green")

        elif icon == '11d':
            root.configure(bg="#404A4F")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#404A4F", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(text=a + ("\nSevere weather alert!"), font=("Arial", 8,'bold'), fg="black", bg="red")


        elif icon == '11n':
            root.configure(bg="#08151D")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#08151D", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(text=a + ("\nSevere weather alert!"), font=("Arial", 8,'bold'), fg="black", bg="red")

        elif icon == '13d':
            root.configure(bg="#CDDCE5")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#CDDCE5", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), fg="white", bg="green")

        elif icon == '13n':
            root.configure(bg="#394247")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#394247", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), fg="white", bg="green")

        elif icon == '50d':
            root.configure(bg="#B7B8B8")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#B7B8B8", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8), fg="white", bg="green")
            if id == 762:
                wLabel1.config(text=a + ("\nVolcanic ash alert!"), font=("Arial", 8, 'bold'), fg="black", bg="red")
            elif id == 781:
                wLabel1.config(text=a + ("\nTornado alert!"), font=("Arial", 8, 'bold'), fg="black", bg="red")
            else:
                pass

        elif icon == '50n':
            root.configure(bg="#414A50")
            photo = PhotoImage(file=r"icons\04n@2x.png")
            display = Label(root, image=photo, bg="#414A50", width='300', height='300')
            display.image = photo
            display.pack(side=LEFT)
            wLabel1.config(font=("Arial", 8,'bold'), fg="white", bg="green")
        else:
            return None






clock()
showWeather()
root.mainloop()