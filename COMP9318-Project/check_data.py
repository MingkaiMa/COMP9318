original_file = 'test_data.txt'
modified_file = 'modified_data.txt'

with open(original_file, 'r') as infile:
    data=[line.strip().split(' ') for line in infile]
Original={}
for idx in range(len(data)):
    Original[idx] = data[idx]

with open(modified_file, 'r') as infile:
    data=[line.strip().split(' ') for line in infile]
Modified={}
for idx in range(len(data)):
    Modified[idx] = data[idx]

for k in sorted(Original.keys()):
    record=set(Original[k])
    sample=set(Modified[k])
    print(k)
    print(len((set(record)-set(sample)) | (set(sample)-set(record))))
    assert len((set(record)-set(sample)) | (set(sample)-set(record)))==20

print('got here')
