from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')

def mainPage():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion_image')
def promo_image():
    return f"""<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="static/img/MARS.png" height=300 width=300>
                            <p class="uno">Человечество вырастает из детства.</p>
                            <p class="duo">Человечеству мала одна планета.</p>
                            <p class="tre">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                            <p class="qrt">И начнем с Марса!</p>
                            <p class="cnq">Присоединяйся!</p>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')