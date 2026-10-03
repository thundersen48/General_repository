import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
# Обратите внимание на то, что некоторые методы и переменные тут опущены
# для того чтобы уделить основное внимание вопросам использования multiprocessing.
def run_parallel_salads():
    # Создаём многопроцессные очереди, которые
    # могут обмениваться данными через границы процессов.
    customers = mp.Queue()
    bowls = mp.Queue()
    dirty_bowls = mp.Queue()
    # Запускаем параллельное выполнение задач с использованием ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=NUM_STAFF) as executor:
        # Set all but one worker making salads
        for _ in range(NUM_STAFF - 1):
            executor.submit(make_salad, customers, bowls, dirty_bowls)
        # Поручаем ещё одному работнику мыть посуду
        executor.submit(wash_bowls, dirty_bowls, bowls)
def make_salad(customers, bowls):
    while True:
        customer = customers.get()
        order = take_order(customer)
        bowl = bowls.get()
        bowl.add(ingredients)
        bowl.add(dressing)
        bowl.mix()
        salad = fill_container(bowl)
        customer.serve(salad)
        dirty_bowls.put(bowl)
def wash_bowls(dirty_bowls, bowls):
    while True:
        bowl = dirty_bowls.get()
        wash(bowl)
        bowls.put(bowl)