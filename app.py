from flask import Flask
from flask import request
from flask import render_template
from flask import abort
from calc import add_two_numbers, sine_wave
import json
import helpers


app = Flask(__name__)
app.debug = True


@app.route('/')
def main():
    """
    List of the available functions
    """
    return render_template('index.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    """
    Renders template and sends result to redis on post
    """
    if request.method == 'POST':
        try:
            res = add_two_numbers(float(request.form['num1']),
                                  float(request.form['num2']))
            return json.dumps({'data': res})
        except ValueError:
            app.logger.warning('Bad add calc. Num1: %s Num2: %s' % (
                               request.form['num1'], request.form['num2']))
            return abort(400)
    else:
        return render_template('add.html', key=helpers.id_generator(size=9))


@app.route('/sine', methods=['POST', 'GET'])
def sine():
    """
    Generates a sine wave
    """
    if request.method == 'POST':
        try:
            (x, y) = sine_wave(magnitude=float(request.form['mag']),
                               period=float(request.form['period']))
            return json.dumps({'data': {'x': x, 'y': y}})
        except ValueError:
            app.logger.warning('Bad sine calc. Mag: %s Period %s' % (
                               request.form['mag'], request.form['period']))
            return abort(400)
    else:
        return render_template('sine.html')


if __name__ == '__main__':
    app.run()
