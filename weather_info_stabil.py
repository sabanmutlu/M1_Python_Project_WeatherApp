import tkinter as tk
from tkinter import StringVar, ttk
import requests, json, locale
from datetime import datetime
import tkinter.font as font


class Wetterinformationen:
    __stadt: StringVar
    __land: StringVar
    __json_var: StringVar
    __erg_data: StringVar

    def main(self):
        # Create main fenster
        fenster = tk.Tk()
        fenster.title('Wetterinformationen')
        fenster.geometry('1000x400+100+100')

        self.__stadt = StringVar()
        self.__land = StringVar()
        self.__json_var = StringVar()
        self.__erg_data = StringVar()

        # Create labels, input boxes and result area
        e_frame = tk.Frame(fenster)
        e_frame.pack()
        lbl1 = tk.Label(e_frame, text='Stadt : ', font=('Arial', 15))
        lbl1.pack(anchor="w", side="left", padx=5, pady=5)
        ent_stadt = tk.Entry(e_frame, textvariable=self.__stadt, font=('Arial', 14))
        ent_stadt.pack(anchor="w", side="left", padx=5, pady=5)
        lbl2 = tk.Label(e_frame, text='Land : ', font=('Arial', 15))
        lbl2.pack(anchor="w", side="left", padx=5, pady=5)
        land = tk.Entry(e_frame, textvariable=self.__land, font=('Arial', 14))
        land.pack(anchor="w", side="left", padx=5, pady=5)

        z_frame = tk.Frame(fenster)
        z_frame.pack()
        bt_font = font.Font(size=12)

        btn_wetter = tk.Button(z_frame, text=' Aktuelle Wetterinformationen ', command=self.__button_info_klick)
        btn_wetter["font"] = bt_font
        btn_wetter.pack(anchor="w", side="left", padx=5, pady=5)

        d_frame = ttk.Frame(fenster)
        d_frame.pack()
        erg_titel = f'Wetterinformationen:'
        lbl_erg = ttk.Label(d_frame, text=erg_titel, font=('Arial', 15))
        lbl_erg.pack()
        v_frame = ttk.Frame(fenster)
        v_frame.pack()
        erg_data = ttk.Label(v_frame, textvariable=self.__erg_data, font=('Arial', 14), background="white")
        erg_data.pack(anchor="w")

        fenster.mainloop()

    def __button_info_klick(self):
        # When latest weather information button pushed
        stadt = self.__stadt.get().strip()
        land = self.__land.get().strip()

        # Validate the inputs
        fehlermeldung = ''
        meldung = ''
        if stadt is None or stadt == '':
            fehlermeldung = 'Stadt Feld kann nicht leer sein!'
        elif land is None or land == '':
            fehlermeldung = f'Land Feld kann nicht leer sein!'
        if fehlermeldung == '':
            # Connect to API and get the data as JSON
            api_key = '1f376d57a9f8db239af30093b382b340'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={stadt},{land}&appid={api_key}&units=metric' \
                  f'&lang=de'
            response = requests.get(url)

            # Convert the result to dictionary
            data = json.loads(response.text)

            # When there is no response, warn the user for possible syntax or no data
            if str(response)[1:-1] == 'Response [404]':
                meldung_mode = 1
                meldung = f'Keine Antwort auf die gesuchten Wörter.\n ' \
                          f'Bitte überprüfen Sie die Werte auf Korrektheit, \n' \
                          'oder es gibt keine solche Stadt in der Datenbank.'
            else:
                self.__json_var.set(data)
                meldung_mode = 2
        else:
            meldung_mode = 0
            meldung = fehlermeldung
        self.ergebnis_data(meldung_mode, meldung)

    def ergebnis_data(self, meldung_mode, meldung):
        # Prepare the result data (Can be also error message)
        ergebnis_data_built = ''
        if meldung_mode == 0:
            ergebnis_data_built = meldung
        elif meldung_mode == 1:
            ergebnis_data_built = meldung
        elif meldung_mode == 2:
            # Make titles and data for result area
            locale.setlocale(locale.LC_ALL, 'de_DE')
            b_datum = datetime.now().strftime('%A, %B %d %H:%M')
            json_var = self.__json_var.get()
            jvr = json_var.replace("\'", "\"")
            jvl = json.loads(jvr)
            info_labels = ["Berichtszeit", "Stadt", "Position", "Hauptwetter", "Regen & Wind", "Sonstiges"]
            info_datas = [b_datum, f'{jvl["name"]}, {jvl["sys"]["country"]}',
                          f'{jvl["coord"]["lon"]}, {jvl["coord"]["lat"]}',
                          f'Temperatur: {jvl["main"]["temp"]}°C, Gefühlte Temperatur: {jvl["main"]["feels_like"]}°C,' 
                          f' {jvl["weather"][0]["description"]}',
                          f'Windgeschwindigkeit: {jvl["wind"]["speed"]} m/s, Windrichtung: {jvl["wind"]["deg"]} Grad, '
                          f'Regen: {"Kein info" if "rain" not in jvl else str(jvl["rain"]["1h"]) + " mm letzte Stunde"}',
                          f'Druck: {jvl["main"]["pressure"]} hPA, Feuchtigkeit: {jvl["main"]["humidity"]}']
            edb = ''
            for il in range(len(info_labels)):
                edb += info_labels[il] + ' : ' + info_datas[il] + '\n'
            ergebnis_data_built = edb
        self.__erg_data.set(ergebnis_data_built)


if __name__ == '__main__':
    r = Wetterinformationen()
    r.main()

