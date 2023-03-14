from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# Criação da tabela no banco de dados
db = sqlite3.connect('robot.db')
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS robot
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            x FLOAT,
            y FLOAT,
            z FLOAT)''')

db.commit()
db.close()
#


@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})


@app.route('/')
def robot():
    db = sqlite3.connect('robot.db')
    sql = db.cursor()
    sql.execute('SELECT * FROM robot ORDER BY id DESC LIMIT 1')
    result = sql.fetchone()
    db.close()
    if result:
        return render_template('robot.html', result=result)
    else:
        return render_template('robot.html', result='Posicao nao encontrada')


# Mostrar posição do robo
# @app.route('/robot', methods=['GET'])
# def get_robot_position():
#     db = sqlite3.connect('robot.db')
#     sql = db.cursor()
#     # pega a última posição do robo
#     sql.execute('SELECT * FROM robot ORDER BY id DESC LIMITE 1')
#     result = sql.fetchone()
#     db.close()
#     if result:
#         return render_template('robot.html', result=result)
#     else:
#         return jsonify({'error': 'Posicao do robo nao encontrada'})

# Definir a posição do robo
@app.route('/set_position', methods=['POST'])
def set_robot_position():
    x = request. form['x']
    y = request. form['y']
    z = request. form['z']

    db = sqlite3.connect('robot.db')

    sql = db.cursor()
    sql.execute(f'INSERT INTO robot (x, y, z) VALUES ({x}, {y}, {z})')

    db.commit()
    db.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
