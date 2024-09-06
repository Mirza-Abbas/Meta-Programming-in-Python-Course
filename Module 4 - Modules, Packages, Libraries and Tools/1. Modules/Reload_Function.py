#No matter how many times we use import statements, the module is only loaded once by the interpreter

import Test_File
import Test_File
import Test_File

#reload() function allow us to reload the module again and again by using importlib

import importlib

importlib.reload(Test_File)
importlib.reload(Test_File)