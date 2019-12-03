'''
The testing file of module import
'''
# import the module example - has to be in the same directory
import module_example

# no to use it simply refer to module and then function within
module_example.do_a_thing()

'''
instead of importing a full module, there is a way to import just some with
syntax like "from <module> import <function>" - then you can use function directly
'''

# there is also a way to change name of the imported function
from module_example import do_next_thing as dnt

# try running re-named function
dnt()




'''
The ususal way of installing of python package is to use PIP library but if the
python package is custom made and hosted for example on github it has to have the
setup.py file and the simply run the command "py -version setup.py install"
'''
