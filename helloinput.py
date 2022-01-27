pass  # this Python keyword is just a placeholder, stands for "don't do anything"


def get_hello_message():
    name = input("What's your name? ")
    if name == "":
        return 'Hello, World!'
    else:
        return 'Hello, ' + name + '!'

def say_hello():
   hello = get_hello_message()
   print(hello) 

say_hello()