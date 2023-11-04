import employee_info

def test_get_employees_by_age_range():
    age_lower_limit = 20
    age_upper_limit = 30 # age cannot be either 20 or 30

    result = employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit)

    assert result == [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()

    assert result == 60166.666666666664

def test_get_employees_by_dept():
    department = 'Sales'

    result = employee_info.get_employees_by_dept(department)

    assert result == [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]