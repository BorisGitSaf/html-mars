from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')

def mainPage():
    return "Миссия Колонизация Марса"

@app.route('/choice/<planet_name>')
def index(planet_name):
    if planet_name == 'Плутон':
        return 'Ну вы поняли'
    if planet_name in joj.keys():
        planet = joj[planet_name]
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet" 
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>{planet_name}</title>
                                  </head>
                                  <body>
                                    <h1><font color='{planet[0]}'>{planet_name}</font></h1>
                                    <h3>{planet[1]}</h3>
                                    <li class="uno">{planet[2][0]}</li>
                                    <li class="duo">{planet[2][1]}</li>
                                    <li class="tre">{planet[2][2]}</li>
                                  </body>
                                </html>'''
    return 'Не найдено'


joj = {
    'Меркурий': ['OrangeRed', 'Для тех, кто ищет место под солнцем', ['Самая жаркая планета',
                                                                      'НЕ родина Фредди Меркьюри',
                                                                      'Один день здесь как полгода земных']],
    'Венера': ['Sienna', 'Не самое приятное место', ['Ужасный климат',
                                                     'По соседству с землей',
                                                     'Самая яркая планета']],
    'Земля': ['SkyBlue', 'Вы находитесь здесь', ['Населена разумной жизнью (возможно)',
                                                 'Родина Фредди Меркьюри',
                                                 'Один год здесь длится примерно 365 земных дней!']],
    'Марс': ['FireBrick', 'Эта планета близка к Земле', ['Красная от ржавчины',
                                                         'Есть лёд на полюсах',
                                                         'Уже ждет колонистов']],
    'Юпитер': ['Sienna', 'Самая большая планета', ['Газовый гигант',
                                                   'Есть спутники с водой',
                                                   'Знаменит своей родинкой']],
    'Сатурн': ['Chocolate', 'Не к добру', ['Шестая планета от Солнца',
                                           'Шестиугольные облака',
                                           'Шестьдесят спутников']],
    'Уран': ['Turquoise', 'Ещё одна голубая планета', ['Ось вращения наклонена на 99 градусов',
                                                       'Не распадается',
                                                       """Рифмуется с "банан" """]],
    'Нептун': ['SteelBlue', 'Далекая планета', ['Дальше всех от нас',
                                                'Не так давно стал замыкающим в ряду планет',
                                                'Похож на Уран']],
}

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')