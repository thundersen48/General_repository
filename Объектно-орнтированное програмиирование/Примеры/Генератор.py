# Генератор - это последовательности и функции с возможностью преостановки
#Пример 1 генертора
def get_values():
    yield 'Hello'
    yield 'World'
    yield 123
    return 42


def example_get_values():
    for x in get_values():
        print(x)

    gen = get_values()
   # print(gen)
    #print(next(gen))
    #print(next(gen))
    #print(next(gen))
#print(example_get_values())

#Пример 2 генератора

class Range:
    def __init__(self,stop: int):
        self.start = 0
        self.stop = stop

    def __iter__(self):
        curr = self.start
        while curr < self.stop:
            yield curr                          # Yield - это ключевое слово, кторое работает как return,
            curr +=1                            # но возвращает генератор

    def range_example():
        for n in Range(100000000):
            print(n)
            if n == 4:
                break


#3 пример генератора
    class MyDataPoint(NamedTuple):
        x:float
        y:float
        z:float

        def mydata_reader(file):
            for row in file:
                cols = row.rstrip().split(',')
                cols = [float(c) for c in cols]
                yield MyDataPoint._make(cols)



def worker(f):
    tasks = collections.deque()
    value = None
    while True:
        batch = yield value
        value = None
    if batch is not None:
        taks.extend(batch)
    else:
        if tasks:
            args = tasks.popleft()
            value = f(*args)

    def example_worker():
        w= worker(str)
        w.send(None)
        w.send([(1,),(2),(3)])
        print(next(w))
        print(next(w))
        print(next(w))


    def another_generator():
        #yield from (x*x for x in range(5))
        for sq in (x*x for x in range(5)):
            yield sq

    def quiet_worker(f):
        while True:
            w = worker(f)
            try:
                return_of_subgen = yield from w
            except Exception as exc:
                print(f'ignoring{exc.__class__.__name__}')

w = worker(str)
print(next(w))
