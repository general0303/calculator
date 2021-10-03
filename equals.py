from sympy import *
from pydoc import locate


class Equal:
    @staticmethod
    def equal(valid_text):
        solution = None
        if 'x' in valid_text and '=' in valid_text:
            t = locate('sympy.sympify')
            lhs = valid_text.rsplit('=', 1)[0]
            lhs = t(lhs)
            rhs = valid_text.rsplit('=', 1)[1]
            rhs = t(rhs)
            solution = solve(Eq(lhs, rhs), 'x')
        if solution is None:
            solution = 'any number'
        return solution

    @staticmethod
    def check_result(left, right, var):
        t = locate('sympy.sympify')
        return solve(Eq(t(left), t(right)), var)


print(Equal.equal('ln(x)=0'))
