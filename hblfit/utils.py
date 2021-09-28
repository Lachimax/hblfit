import numpy as np


def display_as_matrix(arr: np.ndarray):
    for row in arr[, :]:
        print(row)


def count_sig_figs(digits: str) -> int:
    """
    Return the number of significant figures of the input digit string.
    Taken from https://codereview.stackexchange.com/questions/122284/counting-significant-figures-in-a-number
    :param digits:
    :return:
    """

    integral, _, fractional = digits.partition(".")

    if fractional:
        return len((integral + fractional).lstrip('0'))
    else:
        return len(integral.strip('0'))


def round_to_sig_fig(x: float, n: int) -> float:
    """
    https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
    :param x: Number to round.
    :param n: Number of significant figures to round to.
    :return: Rounded number
    """

    return round(x, (n - 1) - int(np.floor(np.log10(abs(x)))))


def build_equation_string(coefficients: np.ndarray, covariance: np.ndarray) -> str:
    """
    Constructs a polynomial equation as a Latex-formatted string, given the coefficients and covariance matrix.
    :param coefficients:
    :param covariance:
    :return:
    """
    string = "$"
    for i, coeff in enumerate(coefficients):
        sigma = np.sqrt(covariance[i, i])
        if i == 1:
            string = f"\ x" + string
        elif i > 1:
            string = f"\ x^{i}" + string
        string = f"({round_to_sig_fig(coeff, 2)} \pm {round_to_sig_fig(sigma, 2)})" + string
        if i < len(coefficients):
            string = "+" + string
    string = "$y =" + string
    return string
