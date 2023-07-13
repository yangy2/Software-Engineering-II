# Yilin Yang
# Software Engineering Web Apps
# HW 5

import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
	if(deriv==True): return x*(1-x)
	else: return 1/(1+np.exp(-x))

# input
# 3rd column has no correlation with output
# output should be 1 if 1st and 2nd column differ
# else output should be 0
X = np.array([
        [0,0,1],
        [0,1,1],
        [1,0,1],
        [1,1,1]])

# output (XOR)
y = np.array([[0],[1],[1],[0]])

learn_rate = float(input("Enter learning rate: "))
target_error = float(input("Enter target error: "))

# seed random numbers for consistency
np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
print ("Initial Weight (Input Layer):  \n", syn0)
print ("Initial Weight (Hidden Layer): \n", syn1)

# batches of iteration
for iter in range(60000):

        # Feed forward through layers 0, 1, and 2
        l0 = X # layer 0 is input
        l1 = nonlin(np.dot(l0,syn0)) # layer 1 is hidden
        l2 = nonlin(np.dot(l1,syn1)) # layer 2 is output

        # Error is difference between expected output and actual output
        l2_error = y - l2
        current_error = np.mean(np.abs(l2_error))

        # Print error
        if (iter == 0): print ("Initial Error:", current_error)
        if ((iter%500 == 0) & (iter != 0)): print ("Error:", current_error)
        if (current_error < target_error):
                print ("Error:", current_error)
                print (" <<< Target Error Reached >>> ")
                print (" <<< " + str(iter+1) + " Iteration(s) >>> ")
                break

        if (iter == 60000-1): print (" <<< " + str(iter+1) + " Iteration(s) >>> ")
        
        # Backpropagate error
        l2_delta = l2_error*nonlin(l2,deriv=True)*learn_rate
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = l1_error * nonlin(l1,deriv=True)*learn_rate

        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)

print ("Final Weight (Input Layer):  \n", syn0)
print ("Final Weight (Hidden Layer): \n", syn1)
print ("Final Error: \n", l2_error)
print ("Final Result: \n", l2)
