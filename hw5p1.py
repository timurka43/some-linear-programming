"""
Title: Homework 5, part 1. Using Simplex
Author: Timur Kasimov (Grinnell, 2025)
Data Created: April 20, 2024
Date Updated: April 29th, 2024

Purpose: Model an optimization problem using matrices and use Simplex
         to solve it.

This is a homework assignment for my Computational Methods Class
"""

import math
import scipy
import numpy as np

# define and fill in the cost vector
cost = np.zeros((72,1))
coefficients = [2000, 0, 180, 320, 400, 8]
coef = 0
while (coef <6):
    i = 0
    while (i < 12):
        cost[12*coef+ i] = coefficients[coef]
        i +=1
    coef += 1


#define identity matrix 12x12
I12 = np.identity(12)

# define a 12x12 matrix of zeros
O12 = np.zeros((12,12))

# define matrix 'steve' that has ones
# along the main diagonal and negative ones
# on the diagonal below the main one
steve = np.identity(12)
for rowcol in range(11):
    steve[rowcol+1, rowcol] = -1


############################
# define A equality matrix #
############################
Aeq = np.zeros((36,72))

#first 12 rows
Aeq[0:12, 0:12] = -20 * I12
Aeq[0:12, 12:24] = I12
Aeq[0:12, 24:36] = -I12
Aeq[0:12, 36:48] = O12
Aeq[0:12, 48:60] = O12
Aeq[0:12, 60:72] = O12

#second 12 rows
Aeq[12:24, 0:12] = steve
Aeq[12:24, 12:24] = O12
Aeq[12:24, 24:36] = O12
Aeq[12:24, 36:48] = -I12
Aeq[12:24, 48:60] = I12
Aeq[12:24, 60:72] = O12

#third 12 rows
Aeq[24:36, 0:12] = O12
Aeq[24:36, 12:24] = -I12
Aeq[24:36, 24:36] = O12
Aeq[24:36, 36:48] = O12
Aeq[24:36, 48:60] = O12
Aeq[24:36, 60:72] = steve


# define b equality vecotr
beq = np.zeros((36,1))
beq[12,0] = 30 # w_0 = 30
demand = np.array([600, 440, 920, 710, 920, 600, 500, 450, 700, 680, 440, 500])
beq[24:,0] = -demand



###############################
# define A upper bound matrix #
###############################
Aub = np.zeros((12,72))

Aub[0:12, 0:12] = -6 * I12
Aub[0:12, 12:24] = O12
Aub[0:12, 24:36] = I12
Aub[0:12, 36:48] = O12
Aub[0:12, 48:60] = O12
Aub[0:12, 60:72] = O12


# define b upper bound vector
bub = np.zeros((12,1))



# throw everything into simplex
results = scipy.optimize.linprog(cost, Aub, bub, Aeq, beq)



'''
CREDITS: print_res function slightly modified from the original version
kindly provided my Almond Heil. I have been long trying to figure
out a way to print nicely formatted strings in python and Almond 
helped me figure it out. 
'''
def print_res(res_vec):
    months = 12
    print(" i | w_i      | x_i      | o_i      | h_i      | f_i      | s_i      ")
    print("---+----------+----------+----------+----------+----------+----------")
    for i in range(months):
        print("%2d | %8.2f | %8.2f | %8.2f | %8.2f | %8.2f | %8.2f" %
            (i+1, res_vec[(0 * months) + i],
              res_vec[(1 * months) + i],
              res_vec[(2 * months) + i],
              res_vec[(3 * months) + i],
              res_vec[(4 * months) + i],
              res_vec[(5 * months) + i]))
        

print_res(results.x)

# My results are consistent with Almond's results shared on Teams
# for example, we have the following sequence of workers:
#   30.00, 30.00, 39.83, 39.83, 39.83, 30.00, 
#   29.13, 29.13, 29.13, 29.13, 23.50, 23.50

# then number of sprockets, overtime, hires, fires, and stored.

#like in Almond's example, no usage of overtime here.


'''
Of course, we have non-integer values for a most of our 'optimal' values. 
This is not a good solution for this kind of problem, since ideally we 
would restrict all our values to be integers, since we can't produce partial 
sprockets or have a part of the worker working. This would be a much more 
challenging problem to solve though.
'''


