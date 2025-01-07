import pytest
from add import add_arrays
@pytest.mark.parametrize("a, b, expect", [
    ([1, 2, 3],    [4, 5, 6],   [5, 7, 9]),
    ([-1, -5, -3], [-4, -3, 0], [-5, -8, -3]),
])
def test_add_arrays(a, b, expect):
    output = add_arrays(a, b)
    assert output == expect

def test_add_arrays_error():
    a = [1, 2, 3]
    b = [4, 5, 'a']
    with pytest.raises(TypeError):
        output = add_arrays(a, b)

