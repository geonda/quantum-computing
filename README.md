# quantum-computing
Belle's (CHSH) inequality modeling with Qiskit.

## Formulation:

From the classical point of view, the following inequality holds for any local hidden variable theory |S|<2 (1).
Here S=E(AB)-E(AB1)+E(A1B)+E(A1B1) and E(AB) is a correlation function obtained from two detectors oriented along arbitrary vectors A and B.

However, within the framework of quantum mechanics (QM), things are different. There are specific orientations for which S is greater than two.  

Thus inequality 2 appears to be an important and convenient test in favor of one or another theory.  So far, the experiment (despite some challenges) confirms the prediction of the quantum mechanic and, consequently, the non-locality of nature.

- Detectors orientation:

 We constrain angles between detectors as (A, B)=(B, A)=(A1, B1)=\theta, and S becomes only a function of theta.  

- QM analytical solution for spin 1/2 system:

E(AB) =<\psi_B|sigma_A sigma_B|\psi_B>=cos(AB)

- Modeling with Qiskit:

E(AB) = \frac{N_{11}+N_{00}-N_{01}-N_{10}}{N_{11}+N_{00}+N_{01}+N_{10}}

- QM errors:

While quantum simulator gives perfect agreement with the analytical solution, quantum calculations on real devices accompanied by certain noise/errors.  For example, measurement of the  Belle state (\frac{|00>+|11>}{\sqrt{2}}) along the z-axis, should not in principle, contains any contribution with mixed spin. Still, QC produces non-zero probability to obtain  |01> and |10> states (check /quantum_errors/).

![CHSH correlation function vs relative angle between detectors ($\theta$).](/images/correlation.png)

![Positions of detectors (A, A1, B, B1). Bloch's spheres were projected onto xz plane.](/images/bloch_sphere.png)

- Manual:

Required packages can be installed using 'pip' and are listed in the 'requirements.txt' file.
Use `python run.py` to get correlation S vs \theta. There are two options for QM calculations using Aer qiskit simulator (run_type='sim') and real quantum computer (run_type='ibmq'). To use ibm quantum computer one has to register here (https://quantum-computing.ibm.com) and specify token and name of the machine in the 'ibm_setting.json'.

- Usefull links:

https://qiskit.org/textbook/ch-ex/hello-qiskit.html#Bell-test-for-classical-variables

https://pythonprogramming.net/quantum-computer-programming-tutorial/
