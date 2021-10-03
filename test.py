from equals import Equal
from matrix import Matrix


class TestEqual:
    def test_linear_equation_with_1_root(self):
        assert Equal.equal('x+1=6') == [5]

    def test_linear_equation_without_root(self):
        assert Equal.equal('0*x+1=6') == []

    def test_liner_equation_with_an_infinite_number_of_roots(self):
        assert Equal.equal('0=0') == 'any number'

    def test_quadratic_equation_with_2_roots(self):
        assert Equal.equal('x**2+x-6=0') == [-3, 2]

    def test_quadratic_equation_with_1_root(self):
        assert Equal.equal('x**2+2*x+1=0') == [-1]

    def test_quadratic_equation_without_valid_roots(self):
        assert Equal.equal('x**2+1=0') == Equal.check_result('x**2+1', '0', 'x')

    def test_exponential_equation_with_1_root(self):
        assert Equal.equal('e**x+1=2') == [0]

    def test_exponential_equation_without_valid_roots(self):
        assert Equal.equal('e**x=-1') == Equal.check_result('e**x', '-1', 'x')

    def test_logarithmic_equation_with_1_root(self):
        assert Equal.equal('ln(x)=0') == [1]

    def test_sinus(self):
        assert Equal.equal('sin(x)=1') == Equal.check_result('sin(x)', '1', 'x')

    def test_cosine(self):
        assert Equal.equal('cos(x)=1') == Equal.check_result('cos(x)', '1', 'x')

    def test_tangent(self):
        assert Equal.equal('tan(x)=1') == Equal.check_result('tan(x)', '1', 'x')

    def test_sinus_and_cosine(self):
        assert Equal.equal('sin(x)+cos(x)=1') == Equal.check_result('sin(x)+cos(x)', '1', 'x')


class TestMatrix:
    def test_addition(self):
        assert Matrix.addition([[1, 2], [3, 4]], [[4, 3], [2, 1]]) == [[5, 5], [5, 5]]

    def test_multiplication_on_number(self):
        assert Matrix.multiplication_on_number([[1, 2], [3, 4]], 2) == [[2, 4], [6, 8]]

    def test_multiplication(self):
        assert Matrix.multiplication([[1, 2], [3, 4]], [[4, 3], [2, 1]]) == [[8, 5], [20, 13]]

    def test_transposition(self):
        assert Matrix.transposition([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

    def test_determinant(self):
        assert Matrix.get_matrix_determinant([[1, 2], [3, 4]]) == -2.0

    def test_invert_matrix(self):
        assert Matrix.get_invert_matrix([[1, 2], [3, 4]]) == [[-2, 1], [1.5, -0.5]]
