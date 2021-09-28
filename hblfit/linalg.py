import numpy as np


def covariance_matrix_from_data(sigmas):
    """
    Creates the diagonal case of the covariance matrix C (HBL2010 equation 4).
    This ONLY handles the simple diagonal case.
    :param sigmas:
    :return:
    """
    c = np.zeros((sigmas.shape[0], sigmas.shape[0]))
    c_inverse = np.zeros((sigmas.shape[0], sigmas.shape[0]))
    for i, sigma in enumerate(sigmas):
        c[i, i] = sigma ** 2
        c_inverse[i, i] = 1 / sigma ** 2
    return c, c_inverse
