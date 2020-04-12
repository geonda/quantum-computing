# quantum-computing
Modeling Belle's (CHSH) inequality with Qiskit.

![CHSH correlation function (S) vs relative angle between detectors ($\theta$).](/images/correlation.png)

*CHSH correlation function vs relative angle between detectors (![\theta](https://render.githubusercontent.com/render/math?math=%5Ctheta)).*

#### Formulation:

From the classical point of view, the following inequality holds for any local hidden variable theory 

![|S| \textless 2 \ \ \ \ \ \ \ (1).](https://render.githubusercontent.com/render/math?math=%7CS%7C%20%5Ctextless%202%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(1).)

Here 

![S=E(\textbf{AB})-E(\textbf{AB^'})+E(\textbf{A^'B^'})+E(\textbf{A^'B}) \ \ \ \ \ \ \ (2).](https://render.githubusercontent.com/render/math?math=S%3DE(%5Ctextbf%7BAB%7D)-E(%5Ctextbf%7BAB%5E'%7D)%2BE(%5Ctextbf%7BA%5E'B%5E'%7D)%2BE(%5Ctextbf%7BA%5E'B%7D)%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(2).)   

and 

![E(\textbf{AB})](https://render.githubusercontent.com/render/math?math=E(%5Ctextbf%7BAB%7D)) - is a correlation function obtained from two detectors oriented along arbitrary vectors ![\textbf{A}](https://render.githubusercontent.com/render/math?math=%5Ctextbf%7BA%7D) and ![\textbf{B}](https://render.githubusercontent.com/render/math?math=%5Ctextbf%7BB%7D).

However, within the framework of quantum mechanics (QM), things are different. There are specific orientations for which ![S](https://render.githubusercontent.com/render/math?math=S) is greater than two.  

Thus ineq. 1 appears to be an important and convenient test in favor of one or another theory.  So far, the experiment (despite some challenges) confirms the prediction of the quantum mechanic and, consequently, the non-locality of nature.


#### Detectors orientation:

 We constrain angles between detectors as ![\angle(\textbf{A, B})=\angle(\textbf{B, A^'})=\angle(\textbf{A^',B^' })=\theta](https://render.githubusercontent.com/render/math?math=%5Cangle(%5Ctextbf%7BA%2C%20B%7D)%3D%5Cangle(%5Ctextbf%7BB%2C%20A%5E'%7D)%3D%5Cangle(%5Ctextbf%7BA%5E'%2CB%5E'%20%7D)%3D%5Ctheta), and ![S](https://render.githubusercontent.com/render/math?math=S) becomes only a function of theta.  
 
 ![Positions of detectors (A, A', B, B'). Bloch's spheres were projected onto xz plane.](/images/bloch_sphere.png)

*Projection of Bloch's sphere onto xz plane and positions of detectors (A, A', B, B') for ![\theta=0, \frac{\pi}{4}, \frac{\pi}{2}](https://render.githubusercontent.com/render/math?math=%5Ctheta%3D0%2C%20%5Cfrac%7B%5Cpi%7D%7B4%7D%2C%20%5Cfrac%7B%5Cpi%7D%7B2%7D). *

#### QM analytical solution for spin 1/2 system:

![E(AB) =<\psi_B|sigma_A sigma_B|\psi_B>=cos(AB)](https://render.githubusercontent.com/render/math?math=E(AB)%20%3D%3C%5Cpsi_B%7Csigma_A%20sigma_B%7C%5Cpsi_B%3E%3Dcos(AB))

- Modeling with Qiskit:

![E(AB) = \frac{N_{11}+N_{00}-N_{01}-N_{10}}{N_{11}+N_{00}+N_{01}+N_{10}}](https://render.githubusercontent.com/render/math?math=E(AB)%20%3D%20%5Cfrac%7BN_%7B11%7D%2BN_%7B00%7D-N_%7B01%7D-N_%7B10%7D%7D%7BN_%7B11%7D%2BN_%7B00%7D%2BN_%7B01%7D%2BN_%7B10%7D%7D)

#### QM errors:

While quantum simulator gives perfect agreement with the analytical solution, quantum calculations on real devices accompanied by certain noise/errors.  For example, measurement of the  Belle state (\frac{|00>+|11>}{\sqrt{2}}) along the z-axis, should not in principle, contains any contribution with mixed spin. Still, QC produces non-zero probability to obtain  |01> and |10> states (check /quantum_errors/).


#### Manual:

Required packages can be installed using 'pip' and are listed in the *requirements.txt* file.
Use `python run.py` to get correlation S vs \theta. There are two options for QM calculations using Aer qiskit simulator (`run_type='sim'`) and real quantum computer (`run_type='ibmq'`). To use ibm quantum computer one has to register [here](https://quantum-computing.ibm.com) and specify token and name of the machine in the *ibm_setting.json*.

#### Usefull links:

https://qiskit.org/textbook/ch-ex/hello-qiskit.html#Bell-test-for-classical-variables

https://pythonprogramming.net/quantum-computer-programming-tutorial/
