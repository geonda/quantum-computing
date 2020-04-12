
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from math import pi
import sys
import kernel as kl

sys.path.append('../')
style.use("dark_background")

nshots=500

ws=kl.workspace(type = 'sim')
ws.create_circuit()
ws.create_entangled_pair()
ws.do_job(nshots = nshots)
sim_counts = ws.counts
print('sim : ', sim_counts)

ws=kl.workspace(type = 'ibmq')
ws.create_circuit()
ws.create_entangled_pair()
ws.do_job(nshots = nshots)
ibmq_counts = ws.counts
print('ibmq : ', ibmq_counts)

ax = plt.subplot(111)
plt.bar(['$|00>_{ibmq}$', '$|00>_{sim}$', '$|01>_{ibmq}$', '$|01>_{sim}$',\
            '$|10>_{ibmq}$', '$|10>_{sim}$', '$|11>_{ibmq}$','$|11>_{sim}$'],\
            [ibmq_counts['00']/nshots, 0, \
            ibmq_counts['01']/nshots, 0, \
            ibmq_counts['10']/nshots, 0, \
            ibmq_counts['11']/nshots, 0], \
                                        color = 'b', alpha = 0.5, label='ibmq')

plt.bar(['$|00>_{ibmq}$', '$|00>_{sim}$', '$|01>_{ibmq}$', '$|01>_{sim}$',\
            '$|10>_{ibmq}$', '$|10>_{sim}$', '$|11>_{ibmq}$','$|11>_{sim}$'],\
            [0, sim_counts['00']/nshots, \
            0, 0, \
            0, 0, \
            0, sim_counts['11']/nshots], \
                                        color = 'r', alpha = 0.5,  label='sim')
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
