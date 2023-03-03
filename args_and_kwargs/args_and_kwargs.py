# https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/

# How to use *args and **kwargs in Python

# Or, How to use variable length argument lists in Python.

# The special syntax, *args and **kwargs in function definitions is used to pass
# a variable number of arguments to a function.
# The single asterisk form (*args) is used to pass a non-keyworded,
# variable-length argument list, and the double asterisk form is used to pass a keyworded,
# variable-length argument list.

# Here is an example of how to use the non-keyworded form.
# This example passes one formal (positional) argument,
# and two more variable length arguments.

def var_args(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)


var_args(1, "two", 3)

# formal arg: 1
# another arg: two
# another arg: 3

# Here is an example of how to use the keyworded form.
# Again, one formal argument and two keyworded variable arguments are passed.

print('***')


def var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))


var_kwargs(farg=1, myarg2="two", myarg3=3)


# Using *args and **kwargs when calling a function
# This special syntax can be used, not only in function definitions, but also when calling a function.

def var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


print('///')
args = ("two", 3)
var_args_call(1, *args)


# Here is an example using the keyworded form when calling a function:

def var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


print('$$$')
kwargs = {"arg3": 3, "arg2": "two"}
var_args_call(1, **kwargs)
