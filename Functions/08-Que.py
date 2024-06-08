# Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value

def kwargs_arg(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


kwargs_arg(name="Victor", power="Magic", weakness="Nothing")
kwargs_arg(name="Sara", power="Beauty", weakness="Victor")
kwargs_arg(name="Carlo", enemy="Victor")
kwargs_arg(name="Anddy", enemy="Victor")