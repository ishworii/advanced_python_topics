class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B):
    pass


class E(B, C):
    pass


class F(D, E, C):
    pass


if __name__ == "__main__":
    print(F.mro())
