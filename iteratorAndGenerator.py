# s= {10,20,50}

# siter = iter(s)
# print(next(siter))
# print(next(siter))



#generator
list = [ x for x in range(500)]
# print(list)

# to send chunks of data to a model for training
def data_loader(chunk_size, list):
    for i in range(0, len(list), chunk_size):
        yield list[i:i+chunk_size]
        
print(type(data_loader(5, list)))
z = data_loader(5, list)
print(next(z))
print(next(z))
print(next(z))