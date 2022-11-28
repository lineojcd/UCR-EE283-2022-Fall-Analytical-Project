import math
import numpy as np
from math import pi, cos, sin

L1 = 2
L2 = 2
L3 = 1

Twist = [[np.array([0, 0, 1]), np.array([0, 0, 0])],
         [np.array([0, 0, 0]), np.array([0, 0, 1])],
         [np.array([1, 0, 0]), np.array([0, L1, 0])],
         [np.array([1, 0, 0]), np.array([0, L1, -L2])]]


# transform the input vector to skew_symmetric matrix
def skew_matrixs(v):
    return np.matrix([[0,       -v[2],  v[1]],
                      [v[2],    0,      -v[0]],
                      [-v[1],   v[0],   0]])


# calculate SO3 from given axis and angular velocity using matrix exponential
def matrix_exponential_so3(w, theta):
    return np.asmatrix(np.identity(3)
                       + sin(theta) * skew_matrixs(w)
                       + (1 - cos(theta)) * ( np.dot(skew_matrixs(w), skew_matrixs(w))))


# calculate SE3 from given axis, linear velocity and angular velocity using matrix exponential
def matrix_exponential_se3(w, v, theta, verbose=False):
    mat = np.identity(4)
    mat[0:3, 0:3] = matrix_exponential_so3(w, theta)
    mat[0:3, 3] = np.dot( np.identity(3) * theta +
                          (1 - cos(theta)) * skew_matrixs(w) +
                         (theta - sin(theta)) * np.dot(skew_matrixs(w), skew_matrixs(w)), v.T).ravel()

    if verbose:
        print(theta)
        print(np.identity(3) * theta)
        print((1 - cos(theta)) * skew_matrixs(w) )
        print("next", theta - sin(theta))
        print((theta - sin(theta)) * np.dot(skew_matrixs(w), skew_matrixs(w)))
    return np.asmatrix(mat)

def forward_kinematics(theta):
    M = np.identity(4)
    M[0:3, 3] = [0, L2 + L3, L1 ]

    esp_S1t1 = matrix_exponential_se3(Twist[0][0], Twist[0][1], theta[0])
    esp_S1t2 = matrix_exponential_se3(Twist[1][0], Twist[1][1], theta[1])
    esp_S1t3 = matrix_exponential_se3(Twist[2][0], Twist[2][1], theta[2], False)
    esp_S1t4 = matrix_exponential_se3(Twist[3][0], Twist[3][1], theta[3])

    T = matrix_exponential_se3(Twist[0][0], Twist[0][1], theta[0]) * \
        matrix_exponential_se3(Twist[1][0], Twist[1][1], theta[1]) * \
        matrix_exponential_se3(Twist[2][0], Twist[2][1], theta[2]) * \
        matrix_exponential_se3(Twist[3][0], Twist[3][1], theta[3]) *  M
    T = esp_S1t1 * esp_S1t2* esp_S1t3* esp_S1t4 * M

    # print(esp_S1t1)
    # print(esp_S1t2)
    # print(esp_S1t3)
    # print(esp_S1t4)
    # print(M)
    # print(pi)
    return T.round(4)


# debug script
if __name__ == '__main__':
    theta = [pi/2, 0, -pi/4, 0]
    print("given theta:\n", theta,
          "\nThe result is:\n",forward_kinematics(theta))