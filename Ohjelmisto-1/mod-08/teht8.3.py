import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'daniel',
        password = '3006',
        autocommit = True
        )

#icao = 'EFHK'
icao = input('Anna ensimmäisen kentän ICAO-koodi: ')
sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"'
kursori = yhteys.cursor()
kursori.execute(sql)
kenttaA = kursori.fetchall()

#icao = 'EFNU'
icao = input('Anna toisen kentän ICAO-koodi: ')
sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"'
kursori = yhteys.cursor()
kursori.execute(sql)
kenttaB = kursori.fetchall()

etaisyys = geodesic(kenttaA, kenttaB).kilometers

print(f'Lentokenttien etäisyys on {etaisyys:.0f}km')