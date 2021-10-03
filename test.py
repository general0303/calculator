from equals import Equal


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
