from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    A=np.zeros((x.shape[0],x.shape[0]))
    for element in topo:
        x_l = x[element]
        y_l = y[element]
        (dx_phi,dy_phi,phi,surf_e) = tri_p1(x_l,y_l,np.zeros((1,2)))
        local_x = np.einsum('i,j->ij', dx_phi, dx_phi)
        
        local_y = np.einsum('i,j->ij', dy_phi, dy_phi)
             
        local_matrix=surf_e*(local_x+local_y)
        
        for i in range(3):
            for j in range(3):
                A[element[i],element[j]] +=local_matrix[i,j]
    return A

def f_v(topo,x,y):
    F=np.zeros(x.shape[0])
    k=0
    for element in topo:
        x_l = x[element]
        y_l = y[element]
        (dx_phi,dy_phi,phi,surf_e)=tri_p1(x_l,y_l,np.zeros((1,2)))
        loc_f=(surf_e/3.)*np.array([1,1,1])
        for j in range(3):
                F[element[j]] += loc_f[j]
        
    return F
