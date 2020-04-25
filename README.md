---
layout: post
title:  "Quantum Computing :  Modeling Bell's (CHSH) inequality with Qiskit"
date:   2020-04-25 06:11:00 +0300
categories: jekyll update

---
<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>
<script type="text/x-mathjax-config">
        MathJax.Hub.Config({
          TeX: { equationNumbers: { autoNumber: "AMS" } }
        });
        </script>

[source on github](https://github.com/geonda/quantum-computing)


![CHSH correlation function (S) vs relative angle between detectors ($\theta$).](/images/correlation.png)


*CHSH correlation function vs relative angle between detectors (![\theta](https://render.githubusercontent.com/render/math?math=%5Ctheta)).*

***

# Formulation


From the classical point of view, the following inequality holds for any local hidden variable theory
\begin{equation}
 \|S\|<2 \ .
\end{equation}
Here
\begin{equation}
S=E(\textbf{AB})-E(\textbf{AB'})+E(\textbf{A'B'})+E(\textbf{A'B}) \ ,
\end{equation}
and

\\(E(\textbf{AB})\\) - is a correlation function obtained from two detectors oriented along arbitrary vectors \\(\textbf{A}\\) and \\(\textbf{B}\\).

However, within the framework of quantum mechanics (QM), things are different. There are specific orientations for which ![S](https://render.githubusercontent.com/render/math?math=S) is greater than two.  

Thus ineq. 1 appears to be an important and convenient test in favor of one or another theory.  So far, the experiment (despite some challenges) confirms the prediction of the quantum mechanic and, consequently, the non-locality of nature.

---
# Detectors

 We can arbitrary constrain angles between detectors as \\(\angle(\textbf{A, B})=\angle(\textbf{B, A'})=\angle(\textbf{A',B' })=\theta\\). Then \\(S\\) becomes only a function of \\(\theta \\)

 ![Positions of detectors (A, A', B, B'). Bloch's spheres were projected onto xz plane.](/images/bloch_sphere.png)

*Projection of Bloch's sphere onto xz plane and positions of detectors (A, A', B, B') for ![\theta=0, \pi/4, \pi/2](https://render.githubusercontent.com/render/math?math=%5Ctheta%3D0%2C%20%5Cpi%2F4%2C%20%5Cpi%2F2).*

---


# QM analytical solution for spin 1/2 system

\begin{equation}
E(\textbf{AB}) = < \psi|\sigma(\textbf{A}) \sigma(\textbf{B})|\psi > =cos(\theta) \ ,
\end{equation}


here \\( \| \psi >  \\) is an entangled state of two qubits (Bell state):
\begin{equation}
\left |\psi > \right .= \frac{\[ \ |00> + |11> \]}{\sqrt{2}} \ .
\end{equation}

----
# Modeling with Qiskit

\begin{equation}
E(\textbf{AB}) = \frac{N_{11}(\textbf{AB})+N_{00}(\textbf{AB})-N_{01}(\textbf{AB})-N_{10}(\textbf{AB})}{N_{11}(\textbf{AB})+N_{00}(\textbf{AB})+N_{01}(\textbf{AB})+N_{10}(\textbf{AB})} ,
\end{equation}

and

\\(N_{ij}(\textbf{AB}) \\) is a number of counts registered in a given state \\(\|i,j>\\), where \\(i,j=\\{0,1\\}\\).

---


# QM errors

While quantum simulator gives perfect agreement with the analytical solution, quantum calculations on real devices accompanied by certain noise/errors.  For example, measurement of the  Bell state  along the *z*-axis, should not in principle, contains any contribution with mixed spin. Still, QC produces non-zero probability to obtain  \\(\|01>\\) and \\(\|10>\\) states (check */quantum_errors/*).

---
# Manual


Required packages can be installed using *pip* and are listed in *requirements.txt* file.
To get correlation ![S(\theta)](https://render.githubusercontent.com/render/math?math=S(%5Ctheta)) use

`$ python run.py`

There are two options for QM calculations using Aer qiskit simulator (`run_type='sim'`) and real quantum computer (`run_type='ibmq'`).

To use ibm quantum computer one has to register [here](https://quantum-computing.ibm.com) and specify token and name of the machine in *ibm_setting.json*.

---

# Usefull links

https://qiskit.org/textbook/ch-ex/hello-qiskit.html#Bell-test-for-classical-variables

https://pythonprogramming.net/quantum-computer-programming-tutorial/

# References
