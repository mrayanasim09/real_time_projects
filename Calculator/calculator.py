class Calculator:
    def __init__(self):
        print("Welcome to the Calculator!")
        self.run_calculator()

    def run_calculator(self):
        while True:
            print("\nChoose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                self.addition()
            elif choice == "2":
                self.subtraction()
            elif choice == "3":
                self.multiplication()
            elif choice == "4":
                self.division()
            elif choice == "5":
                print("Thank you for using our calculator!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def addition(self):
        expression = input("Enter the expression (e.g., num1 + num2): ")
        if "+" in expression:
            try:
                num1, num2 = map(int, expression.split("+"))
                print(f"Result: {num1 + num2}")
            except ValueError:
                print("Invalid expression format. Please enter numbers separated by +.")

    def subtraction(self):
        expression = input("Enter the expression (e.g., num1 - num2): ")
        if "-" in expression:
            try:
                num1, num2 = map(int, expression.split("-"))
                print(f"Result: {num1 - num2}")
            except ValueError:
                print("Invalid expression format. Please enter numbers separated by -.")

    def multiplication(self):
        expression = input("Enter the expression (e.g., num1 * num2): ")
        if "*" in expression:
            try:
                num1, num2 = map(int, expression.split("*"))
                print(f"Result: {num1 * num2}")
            except ValueError:
                print("Invalid expression format. Please enter numbers separated by *.")

    def division(self):
        expression = input("Enter the expression (e.g., num1 / num2): ")
        if "/" in expression:
            try:
                num1, num2 = map(int, expression.split("/"))
                if num2 == 0:
                    print("Error: Division by zero.")
                else:
                    print(f"Result: {num1 / num2}")
            except ValueError:
                print("Invalid expression format. Please enter numbers separated by /.")


# Example Usage:
if __name__ == "__main__":
    calculator = Calculator()
