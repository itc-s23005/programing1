import pickle
withm open('test1.pk1', 'rb') as f:
    result = pickle.load(f)
    print(result)
