from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image


root = Tk()
root.title("날씨 알리미")
root.geometry("450x600")
root['background'] = "white"

# 현재 시간 받아오기
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime(' %a- %d'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%b'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# 시간 생성
hour = Label(root, text=dt.strftime(' %H : %M   %p'),
             bg='white', font=("bold", 15))
hour.place(x=10, y=160)

# 18~6시 사이에는 밤(이미지: 달) 출력, 아니면 낮(이미지: 해) 출력
if int((dt.strftime('%H'))) >= 18 or int((dt.strftime('%H'))) <= 6:
    img = ImageTk.PhotoImage(Image.open('moon.png'))
    panel = Label(root, image=img)
    panel.place(x=180, y=150)
else:
    img = ImageTk.PhotoImage(Image.open('sun.png'))
    panel = Label(root, image=img)
    panel.place(x=150, y=150)

# 도시 검색
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W + E + N + S)

def city_name():
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&units=metric&appid=9cb3559e8ebc8eebd428e94fb3c63610")
    api = json.loads(api_request.content)

    # 온도
    y = api['main']
    current_temprature = y['temp']
    humidity = y['humidity']
    tempmin = y['temp_min']
    tempmax = y['temp_max']

    z = api['sys']
    country = z['country']
    city = api['name']

    lable_temp.configure(text=current_temprature)
    lable_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    lable_country.configure(text=country)
    lable_city.configure(text=city)

city_nameButton = Button(root, text="검색", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W + E + N + S)

lable_city = Label(root, text="...", width=0, bg='white', font=("Verdana", 25))
lable_city.place(x=10, y=63)

lable_country = Label(root, text="...", width=0, bg='white', font=("Verdana", 18))
lable_country.place(x=135, y=63)

lable_temp = Label(root, text="...", width=0, bg='white',font=("Helvetica", 40), fg='black')
lable_temp.place(x=18, y=220)

humi = Label(root, text="습도: ", width=0, bg='white', font=("나눔고딕", 15))
humi.place(x=3, y=400)
lable_humidity = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_humidity.place(x=107, y=400)

maxi = Label(root, text="최고 기온: ", width=0, bg='white', font=("나눔고딕", 15))
maxi.place(x=3, y=430)
max_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

mini = Label(root, text="최저 기온: ", width=0, bg='white', font=("나눔고딕", 15))
mini.place(x=3, y=460)
min_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

note = Label(root, text="기온 단위: ℃,   습도 단위: %", bg='white', font=("나눔고딕", 13))
note.place(x=130, y=530)

root.mainloop()