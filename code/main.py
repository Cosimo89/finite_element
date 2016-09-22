import numpy as np

from mesh import *
from basis_func import *
from assemble import *

from viewer import *

def clear_rows(A,b_nodes,F):
    """ code to clera rows """

    d=np.diag(A)
    B=np.diag(d)
    A=A-B
    A[b_nodes,:]=0
    A=A+B
    f[b_nodes]=0
    return A,F

if __name__ == "__main__":
    read_msh(/mesh/square.msh)
    gradu_gradv(topo,x,y)
    f_v(topo,x,y)
    clear_rows(A,F)
    sol=np.linalgsolve(A,F)
    plot_sol_p1(x,y,sol,topo)
   
