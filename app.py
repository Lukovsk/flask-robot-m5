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
            z FLOAT,
            rotation FLOAT)''')

db.commit()
db.close()
#


@app.route('/')
def robot():
    try:
        db = sqlite3.connect('robot.db')
        sql = db.cursor()
        # sql.execute('SELECT * FROM robot ORDER BY id DESC LIMIT 1')
        sql.execute('SELECT * FROM robot ORDER BY id DESC')
        result = sql.fetchall()
        for position in result:
            print(position)
        db.close()
        return render_template('robot.html', result=result)
    except Exception as e:
        return render_template('robot.html', result=str(e))

# Definir a posição do robo
@app.post('/set_position')
def set_robot_position():
    try:
        x = request. form['x']
        y = request. form['y']
        z = request. form['z']
        rot = request.form['rotation']

        db = sqlite3.connect('robot.db')

        sql = db.cursor()
        sql.execute(
            f'INSERT INTO robot (x, y, z, rotation) VALUES ({x}, {y}, {z}, {rot})')

        db.commit()
        db.close()

        return redirect('/')
    except Exception as err:
        print("Erro:" + str(err))
        return "<h1> Alguma coisa deu errado na inserção de uma nova posição :( </h1>"

# Mostrar posição do robo
@app.get('/get_position')
def get_robot_position():
    try:
        db = sqlite3.connect('robot.db')
        sql = db.cursor()
        sql.execute('SELECT * FROM robot ORDER BY id DESC LIMIT 1')
        result = sql.fetchone()
        db.close()
        return jsonify([result])
    except Exception as err:
        print("Erro:" + str(err))
        return jsonify({'error': str(err)})

# Faz o robô passar por todas as posições
@app.get('/get_all_positions')
def get_all_positions():
    try:
        db = sqlite3.connect('robot.db')
        sql = db.cursor()
        sql.execute('SELECT * FROM robot ORDER BY id DESC')
        result = sql.fetchall()
        db.close()
        print(result)
        return jsonify(result)

    except Exception as err:
        print("Erro:" + str(err))
        return jsonify({'error': str(err)})

if __name__ == '__main__':
    app.run(debug=True)
