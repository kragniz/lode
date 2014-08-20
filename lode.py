def log(*items, **kwargs):
    name = kwargs.get('name', 'lodefile')

    with open(name, 'a') as f: 
        f.write(' '.join([str(item) for item in items]))
        f.write('\n')
