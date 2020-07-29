from flask import Flask, render_template, request, redirect, url_for, flash
import model

app = Flask(__name__)

app.secret_key = 'la_llave_secreta_mia'

@app.route('/')
def Index():
	return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
	q0 = request.form.get('question0')
	q1 = request.form.get('question1')
	q2 = request.form.get('question2')
	q3 = request.form.get('question3')
	q4 = request.form.get('question4')
	q5 = request.form.get('question5')

	if (q0==None or q1==None or q2==None  or q3==None or q4==None or q5==None):
		flash(u'Favor de seleccinar una opción para todas las preguntas.', 'error')
	else:

		if request.method == 'POST':
			print("Pregunta 1 = " + str(q0))
			print("Pregunta 2 = " + str(q1))
			print("Pregunta 3 = " + str(q2))
			print("Pregunta 4 = " + str(q3))
			print("Pregunta 5 = " + str(q4))
			print("Pregunta 6 = " + str(q5))

			a, y = model.predict(int(q0), 
						   int(q1), 
						   int(q2), 
						   int(q3), 
						   int(q4), 
						   int(q5)	)
			if int(y) == 0:
				 	output = "Permanecerás casado con una probabilidad de " + str(int(a*100)) + " % de divorciarte en los próximos 5 años."
			else:
					output = "Tienes probabilidad del " + str(int(a*100)) + " % de divorciarte en los próximos 5 años."
		flash(output, 'success')
	return redirect(url_for('Index'))

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)