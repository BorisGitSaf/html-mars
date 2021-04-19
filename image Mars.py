from flask import Flask

app = Flask(__name__)


@app.route('/')

def mainPage():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promo():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <title>Рекламная кампания</title>
                          </head>
                          <body>
                            <p>Человечество вырастает из детства.</p>
                            <p>Человечеству мала одна планета.</p>
                            <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                            <p>И начнем с Марса!</p>
                            <p>Присоединяйся!</p>
                          </body>
                        </html>"""

@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="static/img/MARS.png" height=400 width=400>
                            <div>Мы сделаем обитаемыми безжизненные пока планеты.</div>
                          </body>
                        </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')