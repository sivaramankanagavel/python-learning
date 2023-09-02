"""
1. The exeption handling was used to throw an error of manual, based on user entered details.
2. instead of showing the default error you want to throw your own error message as well as continue the
   execution of the program you can use the exception handling.
3. in the try block you can use to watch any error should happen or not if happened immediately jump into the
   except Exception block to execute the defined code.
4. after error happened in try block it doesn't execute the next line in the try block.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(result)

except Exception as e:
    print(e)

print("Bye")