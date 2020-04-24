# quantum-computing
Modeling Bell's (CHSH) inequality with Qiskit.

![CHSH correlation function (S) vs relative angle between detectors ($\theta$).](/images/correlation.png)

*CHSH correlation function vs relative angle between detectors (![\theta](https://render.githubusercontent.com/render/math?math=%5Ctheta)).*

#### Formulation

From the classical point of view, the following inequality holds for any local hidden variable theory 


![S=E(\textbf{AB})-E(\textbf{AB^'})+E(\textbf{A^'B^'})+E(\textbf{A^'B}) \ \ \ \ \ \ \ (2).](https://render.githubusercontent.com/render/math?math=S%3DE(%5Ctextbf%7BAB%7D)-E(%5Ctextbf%7BAB%5E'%7D)%2BE(%5Ctextbf%7BA%5E'B%5E'%7D)%2BE(%5Ctextbf%7BA%5E'B%7D)%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(2).)   

![|S| \textless 2 \ \ \ \ \ \ \ (1).](https://render.githubusercontent.com/render/math?math=%7CS%7C%20%5Ctextless%202%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(1).)

Here 

![S=E(\textbf{AB})-E(\textbf{AB^'})+E(\textbf{A^'B^'})+E(\textbf{A^'B}) \ \ \ \ \ \ \ (2).](https://render.githubusercontent.com/render/math?math=S%3DE(%5Ctextbf%7BAB%7D)-E(%5Ctextbf%7BAB%5E'%7D)%2BE(%5Ctextbf%7BA%5E'B%5E'%7D)%2BE(%5Ctextbf%7BA%5E'B%7D)%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(2).)   

and 

![E(\textbf{AB})](https://render.githubusercontent.com/render/math?math=E(%5Ctextbf%7BAB%7D)) - is a correlation function obtained from two detectors oriented along arbitrary vectors ![\textbf{A}](https://render.githubusercontent.com/render/math?math=%5Ctextbf%7BA%7D) and ![\textbf{B}](https://render.githubusercontent.com/render/math?math=%5Ctextbf%7BB%7D).

However, within the framework of quantum mechanics (QM), things are different. There are specific orientations for which ![S](https://render.githubusercontent.com/render/math?math=S) is greater than two.  

Thus ineq. 1 appears to be an important and convenient test in favor of one or another theory.  So far, the experiment (despite some challenges) confirms the prediction of the quantum mechanic and, consequently, the non-locality of nature.


#### Detectors orientation

 We constrain angles between detectors as ![\angle(\textbf{A, B})=\angle(\textbf{B, A^'})=\angle(\textbf{A^',B^' })=\theta](https://render.githubusercontent.com/render/math?math=%5Cangle(%5Ctextbf%7BA%2C%20B%7D)%3D%5Cangle(%5Ctextbf%7BB%2C%20A%5E'%7D)%3D%5Cangle(%5Ctextbf%7BA%5E'%2CB%5E'%20%7D)%3D%5Ctheta). 
 
Then ![S](https://render.githubusercontent.com/render/math?math=S) becomes only a function of ![\theta](https://render.githubusercontent.com/render/math?math=\theta).  
 
 ![Positions of detectors (A, A', B, B'). Bloch's spheres were projected onto xz plane.](/images/bloch_sphere.png)

*Projection of Bloch's sphere onto xz plane and positions of detectors (A, A', B, B') for ![\theta=0, \pi/4, \pi/2](https://render.githubusercontent.com/render/math?math=%5Ctheta%3D0%2C%20%5Cpi%2F4%2C%20%5Cpi%2F2).*

#### QM analytical solution for spin 1/2 system

![E(\textbf{AB}) =\textless \psi|\sigma(\textbf{A}) \sigma(\textbf{B})|\psi \textgreater=cos(\theta) \ \ \ \ \ \ \ (3),](https://render.githubusercontent.com/render/math?math=E(%5Ctextbf%7BAB%7D)%20%3D%5Ctextless%20%5Cpsi%7C%5Csigma(%5Ctextbf%7BA%7D)%20%5Csigma(%5Ctextbf%7BB%7D)%7C%5Cpsi%20%5Ctextgreater%3Dcos(%5Ctheta)%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(3)%2C)

here ![\left |\psi \textgreater \right .](https://render.githubusercontent.com/render/math?math=%5Cleft%20%7C%5Cpsi%20%5Ctextgreater%20%5Cright%20.) is an entangled state of two qubits (Bell state):

![\left |\psi \textgreater \right .= \frac{\\[ \ |00 \textgreater + |11 \textgreater \\]}{\sqrt{2}} \ \ \ \ \ \ \ (4).](https://render.githubusercontent.com/render/math?math=%5Cleft%20%7C%5Cpsi%20%5Ctextgreater%20%5Cright%20.%3D%20%5Cfrac%7B%5C%5B%20%5C%20%7C00%20%5Ctextgreater%20%2B%20%7C11%20%5Ctextgreater%20%5C%5D%7D%7B%5Csqrt%7B2%7D%7D%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(4).)

#### Modeling with Qiskit

![E(\textbf{AB}) = \frac{N(\textbf{AB})_{11}+N(\textbf{AB})_{00}-N(\textbf{AB})_{01}-N(\textbf{AB})_{10}}{N(\textbf{AB})_{11}+N(\textbf{AB})_{00}+N(\textbf{AB})_{01}+N(\textbf{AB})_{10}} \ \ \ \ \ \ \ (5).](https://render.githubusercontent.com/render/math?math=E(%5Ctextbf%7BAB%7D)%20%3D%20%5Cfrac%7BN(%5Ctextbf%7BAB%7D)_%7B11%7D%2BN(%5Ctextbf%7BAB%7D)_%7B00%7D-N(%5Ctextbf%7BAB%7D)_%7B01%7D-N(%5Ctextbf%7BAB%7D)_%7B10%7D%7D%7BN(%5Ctextbf%7BAB%7D)_%7B11%7D%2BN(%5Ctextbf%7BAB%7D)_%7B00%7D%2BN(%5Ctextbf%7BAB%7D)_%7B01%7D%2BN(%5Ctextbf%7BAB%7D)_%7B10%7D%7D%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20(5).)


![N(\textbf{AB})_{ij} ](https://render.githubusercontent.com/render/math?math=N(%5Ctextbf%7BAB%7D)_%7Bij%7D%20) is a number of counts registered in a given state (![\left |ij \textgreater \right.](https://render.githubusercontent.com/render/math?math=%5Cleft%20%7Cij%20%5Ctextgreater%20%5Cright.)), where ![i,j=\{0,1\}  ](https://render.githubusercontent.com/render/math?math=i%2Cj%3D%5C%7B0%2C1%5C%7D%20%20).  


#### QM errors

While quantum simulator gives perfect agreement with the analytical solution, quantum calculations on real devices accompanied by certain noise/errors.  For example, measurement of the  Bell state  along the *z*-axis, should not in principle, contains any contribution with mixed spin. Still, QC produces non-zero probability to obtain  |01> and |10> states (check */quantum_errors/*).


#### Manual

Required packages can be installed using *pip* and are listed in *requirements.txt* file.
To get correlation ![S(\theta)](https://render.githubusercontent.com/render/math?math=S(%5Ctheta)) use 

`$ python run.py` 

There are two options for QM calculations using Aer qiskit simulator (`run_type='sim'`) and real quantum computer (`run_type='ibmq'`). 

To use ibm quantum computer one has to register [here](https://quantum-computing.ibm.com) and specify token and name of the machine in *ibm_setting.json*.

#### Usefull links

https://qiskit.org/textbook/ch-ex/hello-qiskit.html#Bell-test-for-classical-variables

https://pythonprogramming.net/quantum-computer-programming-tutorial/

#### References
