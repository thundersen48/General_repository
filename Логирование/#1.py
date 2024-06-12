"""
Самый низкий уровень логирования — это debug (10), а самый высокий — это critical (50)
"""
import logging
x = 3
y = 4

logging.info(f"The values of x and y are {x} and {y}.")
try:
    x/y
    logging.info(f"x/y successful with result: {x/y}.")
except ZeroDivisionError as err:
    logging.error("ZeroDivisionError",exc_info=True)
