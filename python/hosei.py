DATAFILE = "dataset.txt"

if __name__ == "__main__":
    with open(DATAFILE, 'r') as f:
        '''
        for s in f:
            data = list(s.strip('\n').split(':')[1])
            print(type(data))
        '''
        data = [s.strip('\n').split(':')[1] for s in f]
        data = [list(dt) for dt in data]
        
    print(data)