# essa aqui é como seus scripts com argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, aquele *args é desnecessáario, podemos simplesmente fazer isso


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# essa recebe apenas um argumento


def print_one(arg1):
    print(f"arg1: {arg1}")

# essa não rebe argumento nenhum


def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "shaw")
print_one("First!")
print_none()
