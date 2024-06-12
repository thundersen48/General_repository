from concurrent.futures import ThreadPoolExecutor
import queues
# Обратите внимание на то, что некоторые методы и переменные тут опущены
# для того чтобы уделить основное внимание вопросам многопоточности.
def run_concurrent_burgers():
    # Создание блокирующих очередей
    customers = queue.Queue()
    orders = queue.Queue(maxsize=5)  # Возможна одновременная обработка до 5 заказов
    cooked_patties = queue.Queue()
    # Гриль совершенно независим от работника,
    # он превращает сырые котлеты в котлеты жареные.
    # Это напоминает чтение данных с диска или выполнение сетевого запроса.
    grill = Grill()
    # Выполнить три задачи, используя пул потоков
    with ThreadPoolExecutor() as executor:
        executor.submit(take_orders, customers, orders)
        executor.submit(cook_patties, grill, cooked_patties)
        executor.submit(make_burgers, orders, cooked_patties)
def take_orders(customers, orders):
    while True:
        customer = customers.get()
        order = take_order(customer)
        orders.put(order)
def cook_patties(grill, cook_patties):
    for position in range(len(grill)):
        grill[position] = raw_patties.pop()
    while True:
        for position, patty in enumerate(grill):
            if patty.cooked:
                cooked_patties.put(patty)
                grill[position] = raw_patties.pop()
        # Не проверять снова в течение минуты
        threading.sleep(60)
def make_burgers(orders, cooked_patties):
    while True:
        patty = cooked_patties.get()
        order = orders.get()
        burger = order.make_burger(patty)
        customer = order.shout_for_customer()
        customer.serve(burger)

