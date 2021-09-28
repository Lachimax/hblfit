import numpy as np
import numpy.linalg as la
from typing import Tuple

import hblfit.linalg as linalg


def polynomial_standard(x, y, sigma_y, order) -> Tuple[np.ndarray, np.ndarray]:
    """
    Implements the procedure for fitting a polynomial to data given in Section 1: Standard Practice (HBL2010).
    :param x: x data points
    :param y: y data points
    :param sigma_y: uncertainty in y
    :param order: order of polynomial to fit.
    :return:
    """
    a = linalg.x_values_matrix(x, order)
    a_t = a.transpose()
    # Let's set up the covariance matrix, and its inverse, according to Equation 4:
    c = linalg.covariance_matrix_from_data(sigma_y)
    c_inverse = la.inv(c)
    # Now find (b, m) according to Equation 5:
    covariance = la.inv(la.multi_dot([a_t, c_inverse, a]))
    x = np.dot(covariance, la.multi_dot([a_t, c_inverse, y]))
    return x, covariance
