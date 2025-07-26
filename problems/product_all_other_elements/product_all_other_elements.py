from typing import List


def product_all_other_elements(arr: List) -> List[int]:
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
    """

    prefix_products = __get_prefix_products(arr)
    suffix_products = __get_suffix_products(arr)
    result = __get_final_result(arr, prefix_products, suffix_products)
    return result


def __get_final_result(arr, prefix_products, suffix_products):
    result = []
    for i in range(len(arr)):
        result.append(prefix_products[i] * suffix_products[i])
    return result


def __get_suffix_products(arr):
    suffix_products = []
    for i in range(len(arr) - 1, -1, -1):
        if i == len(arr) - 1:
            suffix_products.append(1)
        else:
            suffix_products.append(suffix_products[-1] * arr[i + 1])

    return suffix_products[::-1]


def __get_prefix_products(arr):
    prefix_products = []
    for i in range(len(arr)):
        if i == 0:
            prefix_products.append(1)
        else:
            prefix_products.append(prefix_products[-1] * arr[i - 1])
    return prefix_products
