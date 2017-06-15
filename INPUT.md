# Von Mises Kernel Density Estimator for Python
This repository contains a Python implementation for a weighted [Kernel Density Estimator](https://en.wikipedia.org/wiki/Kernel_density_estimation) using the [Von Mises](https://en.wikipedia.org/wiki/Von_Mises_distribution) kernel. It is intended for use in data that is inherently circular, e.g., angle data. The Von Mises distribution kernel function is

$$k_\textsc{vm}(l) = \frac{\exp\left(\kappa \cos(l)\right)}{2\pi I_0(\kappa)},$$

where $\kappa$ controls the spread of the distribution, $I_0(\kappa)$ is the zero-order modified Bessel function, and $l$ is scaled distance between two input points. Defining weights $(\alpha_1,\dots,\alpha_n)$ for all $n$ input samples $(x_1,\dots,x_n)$, the resulting kernel density estimate $\hat{p}(x)$ for input $x$ is defined as
$$\hat{p}(x) = \sum\limits_{i=1}^n \alpha_i k_\textsc{vm}(x - x_i).$$