import tkinter as tk
from tkinter import StringVar, ttk
import requests
import json


class WeatherInfo:
    __city: StringVar()
    __country: StringVar()
    __json_var: StringVar()

    def create_top_frame(self):
        frame = ttk.Frame()
        frame['padding'] = 5
        frame['borderwidth'] = 2
        frame['relief'] = 'solid'

        lbl1 = ttk.Label(frame, text='City : ', font=('Arial', 15))
        lbl1.grid(row=1, column=0, sticky='w', padx=5, pady=5, ipadx=5, ipady=5)
        city = ttk.Entry(frame, textvariable=self.__city, font=('Arial', 12))
        city.grid(row=1, column=1, sticky='w', padx=10, pady=5, ipadx=5, ipady=5)
        lbl2 = ttk.Label(frame, text='Country : ', font=('Arial', 15))
        lbl2.grid(row=2, column=0, sticky='w', padx=5, pady=5, ipadx=5, ipady=5)
        country = ttk.Entry(frame, textvariable=self.__country, font=('Arial', 12))
        country.grid(row=2, column=1, sticky='w', padx=10, pady=5, ipadx=5, ipady=5)
        btn = ttk.Button(frame, text='     Current Weather Info     ', command=self.__button_info_klick)
        btn.grid(row=4, column=1, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)

        return frame

    def create_bottom_frame(self):
        frame = ttk.Frame()
        frame['padding'] = 5
        lbl3 = ttk.Label(frame, textvariable=self.__json_var, font=('Arial', 12))
        lbl3.grid(row=0, column=0, padx=10, pady=5, ipadx=5, ipady=5)

        return frame

    def __button_info_klick(self):
        city = self.__city.get()
        country = self.__country.get()
        api_key = '1f376d57a9f8db239af30093b382b340'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = json.loads(response.text)
        self.__json_var.set(data)
        coord = data['coord']
        print(f'01 {coord}')

    def main(self):
        fenster = tk.Tk()
        fenster.title('Weather Info')
        fenster.geometry('800x600+100+100')
        fenster['padx'] = 5

        self.__city = StringVar()
        self.__country = StringVar()
        self.__json_var = StringVar()

        top_frame = self.create_top_frame()
        top_frame.grid(column=0, row=0, pady=5, sticky='n')

        bottom_frame = self.create_bottom_frame()
        bottom_frame.grid(column=0, row=1, pady=5, ipadx=5, ipady=5, sticky='s')

        fenster.mainloop()

    """
    self.__info.set(data['weather'])
    coord = data['coord']
    lng = coord['lon']
    w = data['weather']
    print(coord)
    print(w)
    print(lng)
    """


if __name__ == '__main__':
    r = WeatherInfo()
    r.main()
