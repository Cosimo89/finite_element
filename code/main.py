import numpy as np

from mesh import *
from basis_func import *
from assemble import *

from viewer import *

def clear_rows(A,b_nodes,f):
    """ code to clera rows """

    d=np.diag(A)
    B=np.diag(d)
    A=A-B
    A[b_nodes,:]=0
    A=A+B
    f[b_nodes]=0
    return A,f

if __name__ == "__main__":
    read_msh(/mesh/square.msh)
