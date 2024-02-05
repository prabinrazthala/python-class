def login_required(func):
    def inner_func(*args,**kwargs):
        password = input("enter a password")
        if(password == "12345"):
            return func(*args,**kwargs)
        else:
            return "Invalid password"
    return inner_func


@login_required
def addition(a, b):
    return a + b
print(addition(2, 3))
