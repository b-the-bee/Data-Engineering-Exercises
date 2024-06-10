import pytest
def fast_get_random_number():
    return 6

def random_list_generator(n):
    result = []
    for _ in range(n):
        result.append(fast_get_random_number())
    return result

def test_random_list_generator_happy():
    expected = [6, 6, 6]
    result = random_list_generator(3)
    assert expected == result