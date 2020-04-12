import numpy as np
from math import pi
from tqdm import *

import kernel as kl
import graphics as gs

# array of angles between detectors :
theta_arr = np.linspace(0,pi*2,20)

type of calcualtions ('sim' - using qiskit similator, 'ibmq' - using ibm quantum computer):
run_type = 'ibmq'

ws=kl.workspace(type=run_type)

# names of 4 correlation fucntions :
cor_name_list = ['ab','a1b','ab1','a1b1']

# CHSH correlaiton^* function  :
S_theta = []

# main loop :
for theta in tqdm(theta_arr):
    E = {}
    # body of the exepriment
    for cor_name in cor_name_list:
        ws.create_circuit()
        # key ingradient - entaglement :
        ws.create_entangled_pair()
        # set of different probes (orientations) :
        if cor_name == 'ab':
            ws.rotate_detector_B(theta)
        elif cor_name =='a1b':
            ws.rotate_detector_A(2*theta)
            ws.rotate_detector_B(theta)
        elif cor_name == 'ab1':
            ws.rotate_detector_B(3*theta)
        elif cor_name == 'a1b1':
            ws.rotate_detector_A(2*theta)
            ws.rotate_detector_B(3*theta)
        # actual calculations (see details in kernel.py):
        ws.do_job(nshots=1000)
        E[cor_name]=ws.calculate_correlation()

    S_theta.append(E['ab'] + E['a1b1'] + E['a1b'] - E['ab1'])

np.savetxt('data_' + run_type, np.column_stack((theta_arr/pi, S_theta)))
#plotting routine
p=gs.plot()
# to plot bounderes of the classsical limit :
p.classical_limit()
# to plot analytical solution of S(\theta) :
p.analytical_model()
# to plot simulation of S(\theta) using qiskit (if run_type=='sim') :
theta_from_file,S_theta_from_file = np.loadtxt('./reference/ref_data_sim').T
p.qiskit_simulation(theta_from_file,S_theta_from_file)
# to plot results from quantum computer (ibmq) (if run_type=='ibmq') :
theta_from_file,S_theta_from_file = np.loadtxt('data_ibmq').T
p.qiskit_quantum_computer(theta_from_file,S_theta_from_file)
# to show labels and curves :
p.show()
