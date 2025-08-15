from flask import Flask, render_template

app = Flask(__name__)
'''
@app.route('/')
def principal():
    return "Bienvenido/a a mi sitio web con python."

@app.route('/contacto')
def contacto():
    return "Esta es la página de contacto."
'''

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/lenguajes')
def mostrarlenguajes():
    mislenguajes=("PHP", "JavaScript", "Python", "Java", "C++", 
               "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html', lenguajes=mislenguajes)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)