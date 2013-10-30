from math import *
def estimate_pi():
	k = 0
	total = 0
	coeff = (2*sqrt(2))/9801
	while True:
		factor = coeff * ((factorial(4*k)*(1103+26390*k)) / (factorial(k)**(4)*369**(4*k)))
		if factor < 1e-15:
			break
		total = total + factor
		k = k + 1
		return (total)**(-1)

if __name__ == '__main__':
	print estimate_pi()