from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def inicio():
    return redirect(url_for('circulo'))


@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    area = None
    perimetro = None

    if request.method == 'POST':
        numero1 = float(request.form['numero1'])

        # Área del círculo
        area = 3.1416 * numero1 ** 2

        # Perímetro del círculo
        perimetro = 2 * 3.1416 * numero1

    return render_template(
        'circulo.html',
        area=area,
        perimetro=perimetro
    )

if __name__ == '__main__':
    app.run(debug=True)