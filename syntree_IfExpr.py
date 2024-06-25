#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

from operator import add, sub, mul, truediv, neg
ops = {"+": add, "-": sub, "*": mul, "/": truediv, "~": neg}

class IfExpr(Expr):
    def __init__(self, condition: Expr, then_branch: Expr, else_branch: Expr):
        self._condition = condition
        self._then_branch = then_branch
        self._else_branch = else_branch

    def prefix(self) -> str:
        cond = self._condition.prefix()
        then_expr = self._then_branch.prefix()
        else_expr = self._else_branch.prefix()
        return f"if {cond} then {then_expr} else {else_expr}"

    def infix(self) -> str:
        cond = self._condition.infix()
        then_expr = self._then_branch.infix()
        else_expr = self._else_branch.infix()
        return f"(if {cond} then {then_expr} else {else_expr})"

    def eval(self, context: dict[str, float]) -> float:
        if self._condition.eval(context) != 0:
            return self._then_branch.eval(context)
        else:
            return self._else_branch.eval(context)

class Expr:
    def prefix(self) -> str:
        raise NotImplementedError("Abstract method")

    def infix(self) -> str:
        raise NotImplementedError("Abstract method")

    def eval(self, context: dict[str, float]) -> float:
        raise NotImplementedError("Abstract method")

class BinaryOp(Expr):
    def __init__(self, op: str, x: Expr, y: Expr):
        self._op, self._x, self._y = op, x, y

    def prefix(self):
        x = self._x.prefix()
        y = self._y.prefix()
        return f"{self._op} {x} {y}"

    def infix(self):
        x = self._x.infix()
        y = self._y.infix()
        res = f"{x} {self._op} {y}"
        return f"({res})" if self._op in "+-" else res

    def eval(self, ctx):
        x = self._x.eval(ctx)
        y = self._y.eval(ctx)
        op = ops[self._op]
        return op(x, y)
    
class UnaryOp(Expr):
    def __init__(self, op, x: Expr):
        self._op, self._x = op, x

    def prefix(self):
        x = self._x.prefix()
        return f"{self._op}{x}"

    def infix(self):
        x = self._x.infix()
        return f"{self._op}({x})"

    def eval(self, ctx):
        x = self._x.eval(ctx)
        op = ops[self._op]
        return op(x)

class Var(Expr):
    def __init__(self, name: str):
        self._name = name

    def prefix(self):
        return f"{self._name}"

    def infix(self):
        return f"{self._name}"

    def eval(self, ctx):
        return ctx.get(self._name, 0)

class Num(Expr):
    def __init__(self, val: float):
        self._val = val

    def prefix(self):
        return f"{self._val}"

    def infix(self):
        return f"{self._val}"

    def eval(self, ctx):
        return self._val


def main():
    prod1 = BinaryOp("*", Num(3), Num(2))    #          *  (prod2)
    sum1 = BinaryOp("+", Num(4), prod1)      #         / \
    prod2 = BinaryOp("*", sum1, Num(5))      #        5   +  (sum1)
    print(prod2.eval({}))                    #           / \
    print(prod2.infix())                     # (prod1)  *   4
    print(prod2.prefix())                    #         / \
                                             #        3   2
if __name__ == "__main__":
    main()
