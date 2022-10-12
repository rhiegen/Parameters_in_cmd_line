import sys
import os
# get a substring after the last / symbol
# and remove the .py extension
# to get the name of the module
module_name = os.path.basename(sys.argv[0])

print(f'{sys.argv[1]}\n{module_name}\n')

print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
