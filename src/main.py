import utils

filename = 'operations.json'

load = utils.load_options(filename)
five_last = utils.last_five_operations(load)
print_operation = utils.prin_operations(five_last)

for operation in print_operation:
    print(operation)