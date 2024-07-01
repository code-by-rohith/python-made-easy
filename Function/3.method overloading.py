class Printer:
    def print(self, value):
        if isinstance(value, int):
            self.print_int(value)
        elif isinstance(value, float):
            self.print_float(value)
        elif isinstance(value, str):
            self.print_string(value)
        else:
            raise TypeError("Unsupported type")

    def print_int(self, value):
        print(f"Integer: {value}")

    def print_float(self, value):
        print(f"Float: {value}")

    def print_string(self, value):
        print(f"String: {value}")

printer = Printer()
printer.print(10)          
printer.print(10.5)        
printer.print("Hello")     
