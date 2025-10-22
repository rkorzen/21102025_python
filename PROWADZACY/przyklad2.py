a = 1

def foo():
    global a
    a = 10
    b = 20  # z punkt widzenia bar to jest b z przestrzeni nielokalne. - mowimy tez, ze jest to przestrzen domykajaca
            # ale z punktu widzenia foo to jest przestrzen lokalna

    def bar():
        nonlocal b
        b = 30
        
    print("b przed bar=", b)
    bar()
    print("b po bar=", b)
    print("\nw funkcji foo  - przestrzen lokalna:")
    # print(dir())
    # print("locals", locals())
    print("globals", globals())


print("globalnie")
print(dir())
# print("locals", locals())
print("globals", globals())

foo()

print("Po wywolaniu funkcji")
print("globals", globals())
