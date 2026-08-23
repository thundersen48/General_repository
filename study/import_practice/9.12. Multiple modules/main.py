#9.12. Множественные модули.
from admin import Admin

dicersmaks = Admin('Maksim', 'Puzankov', 'P@sswOrd', 'dicersmaks@mail.ru', 
                   'thundersen48', 'robotics', 'Moskow')

dicersmaks_privileges = [
    'can add posts',
    'can remove posts',
    'can suspend accounts',
    ]

dicersmaks.privileges.privileges = dicersmaks_privileges
dicersmaks.privileges.show_privileges()