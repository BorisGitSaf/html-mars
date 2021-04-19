from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')

def mainPage():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
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
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 align="center"><font color="black">Анкета претендента</font></h1>
                                <h2 align="center">На участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="firstname" placeholder="Введите имя" name="firstname">
                                        <input type="text" class="form-control" id="lastname" placeholder="Введите фамилию" name="lastname">
                                        <p></p>
                                        <p></p>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Общее</option>
                                              <option>Высшее</option>
                                              <option>Наивысшее</option>
                                            </select>
                                         </div>
                                        <p></p>
                                        <p></p>
                                        <div class="form-group">
                                            <label for="form-check">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="инженер-исследователь" value="инженер-исследователь" checked>
                                              <label class="form-check-label" for="инженер-исследователь">
                                                Инженер-исследователь
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="Инженер-строитель" value="Инженер-строитель">
                                              <label class="form-check-label" for="Инженер-строитель">
                                                Инженер-строитель
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="Пилот" value="Пилот">
                                              <label class="form-check-label" for="Пилот">
                                                Пилот
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="Метеоролог" value="Метеоролог">
                                              <label class="form-check-label" for="Метеоролог">
                                                Метеоролог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="Инженер по жизнеобеспечению" value="Инженер по жизнеобеспечению">
                                              <label class="form-check-label" for="Инженер по жизнеобеспечению">
                                                Инженер по жизнеобеспечению
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="Инженер по радиационной защите" value="Инженер по радиационной защите">
                                              <label class="form-check-label" for="Инженер по радиационной защите">
                                                Инженер по радиационной защите
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="Врач" value="Врач">
                                              <label class="form-check-label" for="Врач">
                                                Врач
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="Экзобиолог" value="Экзобиолог">
                                              <label class="form-check-label" for="Экзобиолог">
                                                Экзобиолог
                                              </label>
                                            </div>
                                        </div>
                                        <p></p>
                                        <p></p>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <p></p>
                                        <p></p>
                                        <form method="post" enctype="multipart/form-data">
                                       <div class="form-group">
                                            <label for="photo">Выберите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <p></p>
                                        <p></p>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы осться на Марсе?</label>
                                        </div>
                                        <p></p>
                                        <p></p>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        return 'Спасибо!'



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')