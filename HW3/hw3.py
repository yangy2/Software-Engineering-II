#Yilin Yang
#Software Engineering Web Apps HW3

import csv
import numpy
import math

#Read external file for price data
def readfile(data, filepath):
    with open(filepath, 'rU') as f:
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
    return data

#Print statistics 
def result(data, meanval):
	sum = 0
	for i in range(0, len(data)): sum += float(data[i])
	average = sum / len(data)
	
	print('Average Price:   ', average)
	print('Predicted Price: ', meanval)
	print('Absolute Error:  ', abs(average-meanval))
	
	meanval = round(meanval, 4)
	err = numpy.fabs(((meanval - average) / average)) * 100
	
	print('Relative Error:  ', err, ' %')
	
#Bayesian curve fitting
def predict(data):
    N = len(data) #length of data
    M = 6 #order of polynomial (1.1)

    #fixed alpha and beta values
    alpha = 0.005
    beta = 11.1

    #initialize variables
    target = numpy.zeros((N,1), float) #target data
    phi = numpy.zeros((M,1), float) #phi - phi(x)i = x^i
    sig = numpy.zeros((M,1), float) #summation
    sigT = numpy.zeros((M,1), float) #summation*input

    #set variables
    for i in range(M): phi[i] = math.pow(N,i) #phi - test point x^i
    for i in range(N): target[i] = data[i] #input data
    for j in range(N):
        for i in range(M): #calculate summations
            sig[i][0] += math.pow(j+1, i)
            sigT[i][0] += target[j]*math.pow(j+1, i)

    #S^-1 = alpha*identify matrix + beta*summation of phi*transpose of phi (1.72)
    S = numpy.linalg.inv(alpha*numpy.identity(M)+beta*numpy.dot(sig, phi.T))

    mean = beta*numpy.dot(phi.T, numpy.dot(S, sigT)) #m(x) (1.70)
    var = (1/beta) + numpy.dot((phi.T), numpy.dot(S, phi)) #s^2(x) (1.71)

    meanval = mean[0][0]
        
    result(data, meanval)

    
def main():
    
    data = []
    filepath = 'data3.csv'

    readfile(data, filepath)
    
    print('Stock Price Data:')
    for i in range (0, len(data)): print(data[i])

    predict(data)

main()
