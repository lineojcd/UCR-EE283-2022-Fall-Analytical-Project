import numpy as np
from math import pi, cos, sin, atan, atan2, sqrt, acos
import matplotlib.pyplot as plt
from ee283_project_FW_kinematics import forward_kinematics

L1 = 2
L2 = 2
L3 = 1

def Jocobian(theta):
    Jocobian =np.matrix([ [0, -L2*sin(theta[2]) - L3*sin(theta[2]+theta[3]), -L3*sin(theta[2] + theta[3])] ,
                           [1, L2*cos(theta[2]) + L3 * cos(theta[2]+theta[3]), L3*cos(theta[2] + theta[3])] ])
    # print("Jocobian=",Jocobian)
    return Jocobian

def EnergyGradient(theta, position):
    theta=[0] + theta
    Jcob =Jocobian(theta).transpose()
    v=np.matrix([ [ L2*cos(theta[2]) + L3*cos(theta[2] + theta[3])  - position[0] ] ,
                  [ L2*sin(theta[2]) + L3*sin(theta[2] + theta[3]) + theta[1]   - position[1]] ])
    gdEnergy = Jcob * v
    return gdEnergy

def inverse_kinematics(position):
    x,y,z = position[0],position[1],position[2]
    plane_x= sqrt(x**2 + y**2)
    mod_position = [plane_x, z-L1]

    lr_rate = 0.1
    Xk = np.matrix([[0],
                    [0],
                    [0]])
    err = np.matrix([ [ 10000000 ] ,
                      [ 10000000] ])
    err_cumulative=[]
    # while (abs(err.any()) >0.00175):
    while (sum(abs(err)) > 0.00001):
        Xk1 = Xk - lr_rate * EnergyGradient(Xk.flatten().tolist()[0],mod_position)
        err = Xk1 - Xk
        # print("error = ", sum(abs(err)))
        Xk=Xk1
        err_cumulative.append(float(sum(abs(err))))

    plt.title('Error Plot')
    plt.ylabel('Error')
    plt.xlabel('Epoch')
    plt.plot(err_cumulative)
    # plt.show()
    theta1=np.arctan2(-x,y)
    # if Xk[0][0] <0:
    #     Xk[0][0]=0
    return [theta1]+ Xk.flatten().tolist()[0]

if __name__ == '__main__':
    # given theta: [1.5707963267948966, 0, -0.7853981633974483, 0]
    # The result is:
    # [[0. - 0.7071 - 0.7071 - 2.1213]
    #  [1.      0.      0.      0.]
    # [0. - 0.7071    0.7071 - 0.1213]
    # [0.      0.      0.      1.]]

    print("Case 1")
    theta_1 = [pi/2, 0, -pi/4, 0]
    matrix = forward_kinematics(theta_1)
    print("Forward Kinematics\nGiven theta:", np.array(theta_1).round(4),
              "\nThe transform matrix is:\n",matrix)

    # Given end-point effector postion:
    position_1 = matrix[0:3,3]
    print("The end effector position is", position_1)

    print("\nInverse Kinematics\nGiven end effector position", position_1)
    inv_theta_case1 = inverse_kinematics(position_1)
    reprojected_matrix= forward_kinematics(inv_theta_case1)
    # inv_theta_case1[1] = 0
    print("The theta calculated by gradient descent is:\n", np.array(inv_theta_case1).round(4))
    reprojected_pos=reprojected_matrix[0:3,3]
    print("The reprojected end effector position is",reprojected_pos)


    # given theta: [-1.5707963267948966, 1, -0.7853981633974483, 0]
    # The result is:
    # [[0.      0.7071  0.7071  2.1213]
    #  [-1.      0.      0.      0.]
    # [0. - 0.7071        0.7071     0.8787]
    # [0.      0.      0.      1.]]

    print("\nCase 2")
    theta_2 = [-pi / 2,  1, -pi / 4, 0]
    matrix = forward_kinematics(theta_2)
    print("Forward Kinematics\nGiven theta:", np.array(theta_2).round(4),
          "\nThe transform matrix is:\n", matrix)

    # Given end-point effector postion:
    position_2 = matrix[0:3, 3]
    print("The end effector position is", position_2)

    print("\nInverse Kinematics\nGiven end effector position", position_2)
    inv_theta_case2 = inverse_kinematics(position_2)
    reprojected_matrix = forward_kinematics(inv_theta_case2)
    print("The theta calculated by gradient descent is:\n", np.array(inv_theta_case2).round(4))
    reprojected_pos = reprojected_matrix[0:3, 3]
    print("The reprojected end effector position is", reprojected_pos)
