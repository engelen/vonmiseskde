# Von Mises Kernel Density Estimator for Python
This repository contains a Python implementation for a weighted [Kernel Density Estimator](https://en.wikipedia.org/wiki/Kernel_density_estimation) using the [Von Mises](https://en.wikipedia.org/wiki/Von_Mises_distribution) kernel. It is intended for use in data that is inherently circular, e.g., angle data. The Von Mises distribution kernel function is

$$k_\textsc{vm}(l) = \frac{\exp\left(\kappa \cos(l)\right)}{2\pi I_0(\kappa)},$$

where $\kappa$ controls the spread of the distribution, $I_0(\kappa)$ is the zero-order modified Bessel function, and $l$ is the distance between two input points. Defining weights $(\alpha_1,\dots,\alpha_n)$ for all $n$ input samples $(x_1,\dots,x_n)$, the resulting kernel density estimate $\hat{p}(x)$ for input $x$ is defined as
$$\hat{p}(x) = \sum\limits_{i=1}^n \alpha_i k_\textsc{vm}(x - x_i).$$

## Setup
Currently, no installation scripts are provided. To use the module, simply clone the repostiroy and add the `vonmiseskde` folder to your project directory. Then, use `import vonmiseskde`.

## Usage
The KDE is automatically constructed on instantiating `VonMisesKDE`, which takes `data`, `weights` and `kappa` ($\kappa$) as its arguments. The KDE can then be evaluated at any point using its `evaluate` method, which accepts array-like input.a

## Examples
An visualized example is provided in a notebook [here](https://github.com/engelen/vonmiseskde/blob/master/examples/basic/Weighted%20Von%20Mises%20KDE.ipynb).