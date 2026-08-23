#9.11. Импортирование класса Admin.
from admin import Admin

adrian = Admin('adrian', 'szymanski', 'zeus', 'adrian88szymanski@gmail.com', 'adrian88szymanski', 'sport', 'poland')
adrian.describe_user()

adrian.privileges.show_privileges()

print("\nAdding privileges...")
adrian_privileges = [
    'can add posts',
    'can remove posts',
    'can suspend accounts',
    ]
adrian.privileges.privileges = adrian_privileges
adrian.privileges.show_privileges()