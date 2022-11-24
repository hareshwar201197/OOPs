# variables and methods uses

"""class test:
    a=10
    def __init__(self):
        test.b=20
    def m1(self):
        test.c=30
    @classmethod
    def m2(cls):
        cls.d=40
        test.e=50
    @staticmethod
    def m3():
        test.f=60

T=test()
T.m1()
test.m2()
test.m3()
test.g=70
print(test.__dict__)"""

"""class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
Test.a=888
t1.b=999
print('t2',t2.a,t2.b)"""

"""class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999
t1=Test()
t2=Test()
t1.m1()
t2.m1()
print('t1 :',t1.a,t1.b)
print('t2 :',t2.a,t2.b)
"""

"""class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):w
        self.a=888
        self.b=999
t1=Test()
t2=Test()
t1.m1()
t2.m1()
print('t1 :',t1.a,t1.b)
print('t2 :',t2.a,t2.b)
"""
class Test:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999
t1=Test()
t2=Test()
t1.m1()
print('t1 :',t1.a,t1.b)
print('t2 :',t2.a,t2.b)
print('Test :',Test.a,Test.b)
