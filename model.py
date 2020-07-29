import numpy as np


def sigmoid(z):
	"""
	Compute the sigmoid of z 

	Arguments:
	z -- A scalar or numpy array

	Return:
	s -- sigmoid(z)
	"""
	return 1 / (1 + np.exp(-z))

def predict(x0, x1, x2, x3, x4, x5):
	"""
	Predict whether the label is 0 o 1 (married or divorce) using w and b

	Arguments:
	x0 -- A numpy array with the results of 1st question
	x1 -- A numpy array with the results of 2nd question
	x2 -- A numpy array with the results of 3th question
	x3 -- A numpy array with the results of 4th question
	x4 -- A numpy array with the results of 5th question
	x5 -- A numpy array with the results of 6th question


	Return:
	a -- A scalar that is the probability of be divorcied in 5 years 
	y -- A scalar with the prediction (0/1) for the example X
	"""
	w = np.array([[0.65904116],
       				[0.70190606],
       				[0.652069  ],
       				[0.69367283],
       				[0.67032735],
       				[0.63724911]])

	b = -1.0041191584869766

	X = np.array([	[x0/4.],
					[x1/4.],
					[x2/4.],
					[x3/4.],
					[x4/4.],
					[x5/4.]	])

	z = np.dot(w.T, X) + b
	a = np.squeeze(sigmoid(z))
	if a <= 0.5:
		y = 0
	else:
		y = 1
	return a, y

# a2, y2 = predict(1, 1, 1, 0, 0, 0)
# if int(y2) == 0:
# 	output = "Permanecerás casado con una probabilidad de " + str(int(a2*100)) + " % de divorciarte."
# else:
# 	output = "Tienes probabilidad del " + str(int(a2*100)) + " % de divorciarte en los próximos 5 años."

# print(output)