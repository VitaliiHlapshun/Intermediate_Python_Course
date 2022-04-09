class CustomerCounter:
    # Write your code below:
    def __init__(self, record):
        self.record = record

    def __iter__(self):
        self.count = 0

        return self

    def __next__(self):
        self.count += 1
        if self.count > 100:
            raise StopIteration
        return self.count


_list = ['sdf', 'dfg', 'fgh']
customer_counter = CustomerCounter(_list)
print(_list.count('dfg'))
for el in customer_counter:
    print(el)
