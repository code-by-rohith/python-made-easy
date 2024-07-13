import requests

def arithmetic_operation(num1, num2, operation, iterations):
    for i in range(iterations):
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'undefined'
        else:
            result = 'invalid operation'
        print(f"Result after iteration {i + 1}: {result}")


url = "https://api.restful-api.dev/objects/ff80818190a5a11e0190ab7cdfda11d6"

while True:
    user_name = input("Enter the name to check: ").strip()
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()

            if isinstance(data, dict):
                if data.get('name') == user_name:
                    # Get user input for arithmetic operation and numbers
                    operation = input(
                        "Enter the arithmetic operation (add, subtract, multiply, divide): ").strip().lower()
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    iterations = int(input("Enter the number of iterations: "))

                    # Validate the arithmetic operation
                    if operation not in ['add', 'subtract', 'multiply', 'divide']:
                        print("Invalid arithmetic operation.")
                    else:
                        # Perform the user-specified arithmetic operation
                        arithmetic_operation(num1, num2, operation, iterations)
                    break
                else:
                    print(f"The name is not '{user_name}'.")
            else:
                print("No data found or data is not a dictionary.")
        except ValueError:
            print("Failed to decode JSON.")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)


