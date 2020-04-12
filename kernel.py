import numpy as np
from math import pi
from matplotlib import pyplot as plt
from matplotlib import style
import json

import qiskit as q
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ


class workspace(object):
    """docstring for workspace."""

    def __init__(self, nqubits=2,type='sim'):
        super(workspace, self).__init__()
        self.nqubits = nqubits
        self.run_type=type
        if self.run_type=='ibmq':
            with open('ibm_setting.json') as f:
                self.ibm_set=json.load(f)
            self.load_ibm_account()

    def load_ibm_account(self):
        IBMQ.save_account(self.ibm_set['token'])
        IBMQ.load_account()
        self.provider = IBMQ.get_provider("ibm-q")


    def create_circuit(self):
        self.circuit = q.QuantumCircuit(2, 2)

    def create_entangled_pair(self):
        self.circuit.h(0)
        self.circuit.cx(0,1)

    def rotate_detector_A(self, theta):
        self.circuit.ry(-theta,0)

    def rotate_detector_B(self, theta):
        self.circuit.ry(-theta,1)

    def do_job(self, nshots=1000):
        self.nshots=nshots

        if self.run_type=='sim':
            backend = q.Aer.get_backend('qasm_simulator')
        elif self.run_type=='ibmq':
            backend = self.provider.get_backend(self.ibm_set['backend'])
        else:
            print('run_type error')

        self.circuit.measure([0,1],[0,1])
        job = q.execute(self.circuit, backend=backend, shots=nshots)

        # if self.run_type=='ibmq':
        #     job_monitor(job)

        result = job.result()
        self.counts = result.get_counts()

        return self.counts

    def check(self, name):
        try:
            return self.counts[name]
        except:
            return 0

    def calculate_correlation(self):
        E = self.check('11')/self.nshots\
        + self.check('00')/self.nshots\
        - self.check('01')/self.nshots\
        - self.check('10')/self.nshots

        return E

    def clear(self):
        self.circuit=[]
        self.counts=[]
