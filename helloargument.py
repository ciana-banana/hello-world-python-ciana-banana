pass  # this Python keyword is just a placeholder, stands for "don't do anything"
def get_user_name():
    name = input("What's your name?")
    return name.title()

def get_hello_message(name):
    if name == "":
        return "Hello, world!"
    else:
        return "Hello" +name + "!"

def say_hello():
    hello = get_hello_message()
    print(hello)

say_hello()