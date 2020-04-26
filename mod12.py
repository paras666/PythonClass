import mod10

mod10.fun1()

print("\n")

import mod11 as m1

m1.fun5()

print("\n")

from mod10 import fun2

fun2(5,5)

print("\n")

from mod10 import *
from mod11 import *

fun2(4,5)

print("\n")

fun5()

