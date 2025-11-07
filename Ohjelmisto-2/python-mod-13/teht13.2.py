from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/kenttä/<string:ICAO>')

def kenttä(ICAO):
    yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'daniel',
        password = '3006',
        autocommit = True
        )
    
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{ICAO}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    vastaus = {
        "ICAO":ICAO,
        "Name":tulos[0],
        "Municipality":tulos[1]
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)