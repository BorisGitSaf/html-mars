from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Домашняя страница')

@app.route('/training/<prof>')
def training(prof):
    img = 'NS'
    room = 'Научные симуляторы'
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        img = 'IT'
        room = 'Инженерные тренажёры'
    print(img)
    return render_template('Тренировка в полёте.html', title='Тренировка в полёте', imag=img, room=room)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')