import numpy as np

def read_msh(filenamne):

#Initialisation
    x = np.array([])
    y = np.array([])
    b_nodes= np.array([])
    topo= np.array([])
    nodes=np.array([])

    """ read mesh code """
    f = open(filenamne, 'r')

#Creation of the vector and matricies	
    for line in f:
        if line[0]=='$':
            print("this is useless")
        else:
            l =  map(float,line.split())
            if len(l) == 4:
                x = np.append(x,l[1])
                y = np.append(y,l[2])
            if len(l) == 7:
                #boundary
                b_nodes = np.append(b_nodes,l[6])
                b_nodes = map(int,b_nodes)
            if len(l) == 8:
                # domain
                topo = np.append(topo,l[5],l[6],l[7])
            print(line)

	
#Check the elements
    r_id = 0
    for row in topo:
        ck =      (x[row[1]]-x[row[0]])*(y[row[2]]-y[row[0]])
        ck = ck - (x[row[2]]-x[row[0]])*(y[row[1]]-y[row[0]])
        if ck < 0:
            topo[r_id,:] = np.array([[row[0],row[2],row[1]]])
        r_id+=1

    print r_id
    return topo , x , y , nodes , b_nodes


