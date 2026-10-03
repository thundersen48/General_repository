"""
В анализе данных или нейросетях (Data Science) срезы используются,
чтобы скармливать компьютеру информацию «кусками» (batches),
если вся база данных не влезает в оперативную память.
"""

data = list(range(1,10))
batch_size = 3

for i in range(0,len(data),batch_size):
    batch = data[i:i+batch_size]
    print(f'Processing a block of fata {batch}')
