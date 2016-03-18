# -*- coding: UTF-8 -*-

#Importar bibliotecas:
import pylab as py
import numpy as np

"""
INTERPOLACIÓN:
MÉTODOS DE LAGRANGE Y NEWTON
"""

#Puntos iniciales:
n = 0
"""
while n < 2:
	n = int(input('¿Cuántos puntos conocidos tiene?'))
	if n < 2:
		print 'Se necesitan más de dos puntos para poder interpolar, por favor pruebe con más puntos'
points = np.arange(n*2,dtype=float)
points.shape = (2,n)
"""

"""
for i in range(0,n):
	print 'n\Introduzca los puntos a interpolar\n'
	print '(Cuando haya terminado introduzca el valor 9999'
	print "x",i,",y",i
	x = float(input("Ingrese 'x' > "))
	y = float(input("Ingrese 'y' > "))
	points[0,i] = x
	points[1,i] = y
"""

points = np.array([[5.0,4.0,1.0,7.0],[8.0,3.0,2.0,6.0]])
p_gr = np.arange(0,10,0.01)

deterPoint = float(input('Ingrese la coordenada "x" del punto que desea conocer'))

n = len(points[0])
lPol = np.arange((n)**2,dtype = float)
lPol.shape = (n,n)

#PRODUCTORIO
def prod(dat):
	a=1
	for i in range(len(dat)):
		a=a*dat[i]
	return a
		
#INTERPOLACIÓN LAGRANGE
def lagrange(points,lPol,deterPoint):
	
	Pol = []
	
	for i in range(len(points[0])):
		for j in range(len(points[0])):
			if j==i:
				lPol[i,j] = 1.0
			else:
				lPol[i,j] = (deterPoint - points[0,j])/(points[0,i]-points[0,j])
				
	for i in range(len(points[1])):
		Pol.append(prod(lPol[i])*points[1,i])
		
	result = sum(Pol)
		
	return result

n = len(points[0])
lPol = np.arange((n)**2,dtype = float)
lPol.shape = (n,n)


#MÉTODO DE INTERPOLACIÓN DE NEWTON

#Definimos las diferencias divididas
polN = np.arange((n)**2,dtype = float)
polN.shape = (n,n)

def difference(x,y,n):
	polN = []
	
	for i in range(n):
		polN.append(y[i])
	
	for j in range(1,n): #el 0 se queda como está
		for i in range(n-1, j-1, -1):
			polN[i] = (polN[i] - polN[i-1])/(x[i] - x[i-j])
	return polN

def Newton(polN,x,deterPoint):
	result = 0
	partResult=1
	for i in range(0,n):
		for j in range(0,i,1):
			polN[i] = polN[i]*(deterPoint - x[j])
		result = result + polN[i]
	return result

Lgr = []
Ngr = []
for i in range(len(p_gr)):
	Lgr.append(lagrange(points,lPol,p_gr[i]))
for i in range(len(p_gr)):
	Ngr.append(Newton(difference(points[0],points[1],n),points[0],p_gr[i]))

print lagrange(points,lPol,deterPoint)
print Newton(difference(points[0],points[1],n),points[0],deterPoint)   


#REPRESENTACIONES RESULTADOS
py.plot(points[0],points[1],'.r',label='Puntos iniciales')
py.plot(p_gr,Lgr,'-g',label='Interpolacion de Lagrange')
py.plot(p_gr,Ngr,'-b',label='Interpolacion de Newton')
py.plot(deterPoint,lagrange(points,lPol,deterPoint),'*y',label='Punto determinado')
py.legend(loc='best')
py.show()

