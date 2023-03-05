from datetime import datetime
import easypass
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now().date())
    password = easypass.Password()
    print('Вам сгенерирован новый пароль:)', end=' ')
    password.print()
