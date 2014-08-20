def log(*items):
    with open('lodefile', 'a') as f: 
        f.write(' '.join([str(item) for item in items]))
        f.write('\n')
    print items
