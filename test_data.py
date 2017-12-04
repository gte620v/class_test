"""Test"""
import numpy as np
from my_algos import my_algo


def test_run():
    """run algo"""
    data_len = 10
    np.random.seed(0)
    data_in = np.random.rand(data_len)
    output = my_algo(data_in)
    print('score is {}'.format(output))
    assert 1
