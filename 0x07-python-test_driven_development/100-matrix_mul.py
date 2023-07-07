#!/usr/bin/python3
""" This module contain a function that multiplies 2 matrices """


def matrix_mul(m_a=[[]], m_b=[[]]):
    """
    A function that multiplies 2 matrices

    Args:
        m_a (List[List[int]]): first matrix
        m_b (List[List[int]]): second matrix

    Return:
        m_c (List[List[int]]): product of m_a and m_a
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 1 and len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 1 and len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    a_row_size = len(m_a[0])
    a_col_size = len(m_a)
    b_row_size = len(m_b[0])
    b_col_size = len(m_b)

    for li in m_a:
        if len(li) != a_row_size:
            raise TypeError("each row of m_a must be of the same size")
    for li in m_b:
        if len(li) != b_row_size:
            raise TypeError("each row of m_b must be of the same size")
    if a_row_size != b_col_size:
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for li in m_a:
        if type(li) is not list:
            raise TypeError("m_a must be a list of lists")
        j = 0
        inner = []
        while j < b_row_size:
            i = 0
            s = 0
            while i < a_row_size:
                if type(m_b[i]) is not list:
                    raise TypeError("m_b must be a list of lists")
                if type(li[i]) not in [int, float]:
                    raise TypeError("m_a should contain " +
                                    "only integers or floats")
                if type(m_b[i][j]) not in [int, float]:
                    raise TypeError("m_b should contain only " +
                                    "integers or floats")
                s += (li[i] * m_b[i][j])
                i += 1
            inner.append(s)
            j += 1
        m_c.append(inner)
    return m_c
