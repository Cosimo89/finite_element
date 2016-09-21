import numpy as np

def tri_p1(x,y,eval_p):

	A=np.zeros((3,3))
	A[0]=x
	A[1]=y
	A[2]=np.array([1,1,1])
	A=np.transpose(A)
	phi=np.zeros((eval_p.shape[0],3))
	for i in range(3):
		if i == 0:
			B=np.array([1,0,0])
			phi_1=np.linalg.solve(A, B)
		if i == 1:
			B=np.array([0,1,0])
			phi_2=np.linalg.solve(A, B)
		if i == 2:	
			B=np.array([0,0,1])
			phi_3=np.linalg.solve(A,B)
	dx_phi=np.array([phi_1[0],phi_2[0],phi_3[0]])
	dy_phi=np.array([phi_1[1],phi_2[1],phi_3[1]])
	
	#surf_e=(np.abs(x[0]-x[1]))*
	#dist = np.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)
	#if y[0]<y[1]:
		#h = np.sqrt(((x[0]+float(dist)/2)-x[2])**2+((
	print phi
	for i in range(eval_p.shape[0]):
		phi[i][0]=phi_1[0]*eval_p[i][0]+phi_1[1]*eval_p[i][1]+phi_1[2]
		phi[i][1]=(phi_2[0]*eval_p[i][0]+phi_2[1]*eval_p[i][1]+phi_2[2])
		phi[i][2]=(phi_3[0]*eval_p[i][0]+phi_3[1]*eval_p[i][1]+phi_3[2])
	surf_e = 1./2. * abs(x[0]*y[2]-x[0]*y[1]+x[1]*y[0]-x[1]*y[2]+x[2]*y[1]-x[2]*y[0] )
	return dx_phi,dy_phi,phi[0],surf_e



