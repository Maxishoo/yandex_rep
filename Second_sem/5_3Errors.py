def func():
    x = int("Helo wofg!")


try:
    func()
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")
else:
    print("No Exceptions")
