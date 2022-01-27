pass  # this Python keyword is just a placeholder, stands for "don't do anything"


def get_hello_message():
    return 'Hello, World!'

def say_hello():
    message = get_hello_message()
    print(message)

say_hello()
