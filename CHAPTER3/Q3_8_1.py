import pickle

with open("test1.pk1", "wb") as f:
    my_list = list(range(1.111))
    pickle.dump(my_list, f)
