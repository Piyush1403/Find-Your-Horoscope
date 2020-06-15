# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import bs4 as bs
import urllib.request

@app.route('/', methods=['POST', 'GET'])
    
def horoscope():
    if (request.method == 'POST'):
        sign = request.form['sign']
        sign = sign.strip()
        sign = sign.capitalize()
        possible_signs = ['Aries','Taurus','Gemini','Cancer','Leo', 
                          'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 
                          'Capricorn', 'Aquarius', 'Pisces']
        if sign not in possible_signs:
            all_reading = "'" + sign + "'" + " isn't a valid horoscope sign."
        else:
            days = ['Daily']
            date = []
            readings = []
            for day in days: 
                horoscope = ("https://www.ganeshaspeaks.com/horoscopes/" + 
                             day +  "-horoscope/" + sign + "/")
                sauce = urllib.request.urlopen(horoscope).read()
                soup = bs.BeautifulSoup(sauce, 'html.parser')
                for daily in soup.find_all(id="daily"):
                    l = []
                    for ptags in daily.find_all('p'):
                        l.append(ptags.get_text())
                    date.append(l[0])
                    readings.append(l[1])
            readings = list(map(str.strip, readings))
            all_reading = readings[0]
            all_reading = all_reading.replace('Ganesha', 'Piyush')
        return render_template('main.html', all_reading = all_reading,
                               sign=sign)
        return redirect(url_for('horoscope'))
    else:
        return render_template('main.html')
        
