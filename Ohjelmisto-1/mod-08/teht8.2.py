import mysql.connector

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'daniel',
        password = '3006',
        autocommit = True
        )

maakoodi = input('Anna maakoodi: ')
#maakoodi = 'FI'
sql = f'''SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = "{maakoodi}" 
        GROUP BY type'''
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f'{rivi[0]}: {rivi[1]}')