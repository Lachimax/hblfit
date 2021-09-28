import numpy as np


def covariance_matrix_from_data(sigmas: np.ndarray) -> np.ndarray:
    """
    Creates the diagonal case of the covariance matrix C (HBL2010 equation 4).
    This ONLY handles the simple diagonal case.
    :param sigmas: Numpy array containing the sigma values.
    :return: covariance matrix
    """
    c = np.zeros((sigmas.shape[0], sigmas.shape[0]))
    for i, sigma in enumerate(sigmas):
        c[i, i] = sigma ** 2
    return c


def x_values_matrix(x: np.ndarray, order: int) -> np.ndarray:
    """
    Creates matrix A as specified by HBL2010 equation 3, generalised to higher orders.
    :param x: Numpy array containing x-values.
    :param order: Order of polynomial that is being fitted.
    :return: matrix A, containing
    """
    # We set up matrix A according to Equation 3:
    a = np.ones((x.shape[0], order + 1))
    for i in range(order + 1):
        a[:, i + 1] = x ** (i + 1)
    return a
