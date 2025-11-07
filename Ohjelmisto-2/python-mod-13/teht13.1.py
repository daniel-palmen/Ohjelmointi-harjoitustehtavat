from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')

def alkuluku(luku):
    if luku < 2:
        isPrime = False
    else:
        for i in range(2,luku):
            if luku % i == 0:
                isPrime = False
            else:
                isPrime = True
    vastaus = {
        "number" : luku,
        "isPrime" : isPrime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)