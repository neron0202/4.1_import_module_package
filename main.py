from datetime import datetime
from application import salary
from db import people

if __name__ == '__main__':
    print(datetime.strftime(datetime.now(), "%Y%m%d"))
    salary.calculate_salary()
    people.get_employees()