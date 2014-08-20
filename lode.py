def log(*args):
    with open('lodefile', 'a') as f: 
        f.write(str(args) + '\n')
    print args
