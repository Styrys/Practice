class HelloWorld:
    def __init__(self):
        self.message = "Hello, World!"

    def greet(self):
        return self.message

# Example usage
if __name__ == "__main__":
    hello = HelloWorld()
    print(hello.greet())