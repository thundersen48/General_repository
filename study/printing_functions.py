#8.15. Печать моделей
from print_model import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pedant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)