# Standard imports
import math
import numpy as np
from scipy.special import iv
from scipy.interpolate import interp1d

class VonMisesKDE():
    def __init__(self, data, weights=[], kappa=1.0):
        """ Constructor. Define KDE options and input data
        
        @param List[float] Input data points in radians. Normalized by method to range [0, 2*pi]
        @param List[float] Optional. Weights for input samples
        @param float kappa Optional. Kappa parameter of Von Mises pdf
        """
        
        # Input data
        self.data = self.normalizeAngles(np.asarray(data))
        
        # Input data weights
        self.weights = np.asarray(weights)
        self.weights = self.weights / np.sum(weights)
        
        # Model parameter
        self.kappa = kappa
        
        # Generate KDE
        self.kde()
    
    def normalizeAngles(self, data):
        """ Normalize a list of angles (in radians) to the range [-pi, pi]
        
        @param List[float] Input angles (in radians)
        @return List[float] Normalized angles (in radians)
        """
        # Change range to 0 to 2 pi
        data = np.array(data % (np.pi * 2))

        # Change range to -1 pi to 1 pi
        data[data > np.pi] = data[data > np.pi] - np.pi * 2
        
        return data
        
    def vonMisesPDF(self, alpha, mu=0.0):
        """ Probability density function of Von Mises pdf for input points
        
        @param List[float] alpha List-like or single value of input values
        @return List[float] List of probabilities for input points
        """
        
        num = np.exp(self.kappa * np.cos(alpha - mu))
        den = 2 * np.pi * iv(0, self.kappa)

        return num / den

    def kde(self):
        """ Calculate kernel density estimator distribution function """
        
        plot = True
        
        # Input data
        x_data = np.linspace(-math.pi, math.pi, 1000)

        # Kernels, centered at input data points
        kernels = []

        for datapoint in self.data:
            # Make the basis function as a von mises PDF
            kernel = self.vonMisesPDF(x_data, mu=datapoint)
            kernels.append(kernel)
    
        # Handle weights
        if len(self.weights) > 0:
            kernels = np.asarray(kernels)
            weighted_kernels = np.multiply(kernels, self.weights[:, None])
        else:
            weighted_kernels = kernels
        
        # Normalize pdf
        vmkde = np.sum(weighted_kernels, axis=0)
        vmkde = vmkde / np.trapz(vmkde, x=x_data)

        self.fn = interp1d(x_data, vmkde)
    
    def evaluate(self, input_x):
        """ Evaluate the KDE at some inputs points
        
        @param List[float] input_x Input points
        @param List[float] Probability densities at input points
        """
        
        # Normalize inputs
        input_x = self.normalizeAngles(input_x)

        return self.fn(input_x)
