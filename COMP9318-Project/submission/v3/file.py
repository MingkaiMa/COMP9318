
file1 = 'modified_data_1.txt'
file2 = 'modified_data.txt'


with open(file1) as f1:
    
    L1 = [line.strip().split(' ') for line in f1]

with open(file2) as f2:
    L2 = [line.strip().split(' ') for line in f2]
    
    
