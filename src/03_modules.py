"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
#----------------------------------------------------------------------
# Print out the command line arguments in sys.argv, one per line:
for args in sys.argv:
    print(args)

#----------------------------------------------------------------------
# Print out the OS platform you're using:

print(sys.platform)
# darwin

#----------------------------------------------------------------------
# Print out the version of Python you're using:
# YOUR CODE HERE

#----------------------------------------------------------------------

print(sys.version)

#3.7.3 (default, Jun 19 2019, 07:38:49) 
#[Clang 10.0.1 (clang-1001.0.46.4)]

#----------------------------------------------------------------------
#----------------------------------------------------------------------


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

#----------------------------------------------------------------------
# Print the current process ID

print(os.getpid())
#36372

#----------------------------------------------------------------------
# Print the current working directory (cwd):
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())
