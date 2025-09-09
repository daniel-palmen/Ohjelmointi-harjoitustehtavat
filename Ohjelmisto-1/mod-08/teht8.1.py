import mysql.connector

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'daniel',
        password = '3006',
        autocommit = True
        )
icao = input('Anna lentoaseman ICAO-koodi: ')
#icao = 'EFHK'
sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao}"'
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f'Lentokentän nimi on {rivi[0]} ja sijaintikunta {rivi[1]}.')