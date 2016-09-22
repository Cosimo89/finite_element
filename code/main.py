from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

from mesh import *
from basis_func import *
from assemble import *



def clear_rows(A,b_nodes,F):
    """ code to clera rows """

    d=np.diag(A)
    B=np.diag(d)
    A=A-B
    A[b_nodes,:]=0
    A=A+B
    F[b_nodes]=0
    return A,F

def plot_sol_p1(x,y,z,topo):

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(x, y, z, cmap=cm.jet,vmin=min(z), vmax=max(z), linewidth=0.2)

    plt.show()
    return


if __name__ == "__main__":
    
    topo, x,y,b_nodes=read_msh("./mesh/square.msh")
    A=gradu_gradv(topo,x,y)
    F=f_v(topo,x,y)
    A,F=clear_rows(A,b_nodes,F)
    sol=np.linalg.solve(A,F)
    plot_sol_p1(x,y,sol,topo)

print "ciao" 
   
