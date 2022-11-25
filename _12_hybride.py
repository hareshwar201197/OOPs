# Hybride inhiritance
# its a combination of two or more type of inheritance

class A:
    def a(self):
        print("First step")

class B(A):
    def b(self):
        print("second step")

class C(A):
    def c(self):
        print("Second2 step")

class D(B):
    def d(self):
        print("third step")

class E(C):
    def e(self):
        print("step four")

class F(C):
    def f(self):
        print("step five")

class G(E,F):
    def g(self):
        print("Step six")

G_obj = G()
G_obj.a()
#G_obj.b()
G_obj.c()
#G_obj.d()
G_obj.e()
G_obj.f()
