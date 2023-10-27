import threading
import time

"""
Multi Threading ---> In many backend application we are using the multi threading concepts to optimize the operation
                     for example updating DB(data base) and executing third-party API call and so on.
                     
                     import threading 
                     threading.active_count()
                     threading.enumerate()
                     
                     threading.thread(target=<executable function>)
"""


def updating_db():
    print("Updating data-base...")
    time.sleep(5)
    print("updated data-base")


def greetings(name):
    print(f"welcome to the website Mr. {name}")


def print_numbers(num, args):
    for numbers in range(1, num + 1):
        print(args,numbers)


"""
Without Multi threading python will execute the code line by line some time some function take more than 5sec to 
return some data at the time other function execution also getting delayed so, this will affect the application
performance.

we come out from this issue we using the multi-threading to execute the main function and what ever the function
you need to execute in the different thread it will doesn't impact on main and other threads.

threads is literally like a separate road way for each important time taking function so it doesn't disturb the main
function execution or pause the execution.

Mian Methods:
1. thread_function = thread.Thread(target=<executable function>, args=())
2. thread_function.start()
3. threading.enumerate()
4. threading.active_count()
5. thread_function.join() --> this method was used to pause some function upto finishing this function execution.
"""
# updating_db()
# greetings("Sivaraman")

thread_db = threading.Thread(target=updating_db)
thread_db.start()

numbers_db = threading.Thread(target=print_numbers, args=(10, 'Hello'))
numbers_db.start()

greetings("Vinoth")

print(threading.active_count())
print(threading.enumerate())

thread_db.join()
print("Bye")
