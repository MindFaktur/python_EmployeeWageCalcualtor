from employee_class.employee import Employee
from employee_class.indian_employee import IndianEmployee
from employee_class.us_employee import USAEmployee


class InputToDictionary:

    def __init__(self, list_of_employee_values):

        self.company_details = {"company_name": list_of_employee_values[0],
                                "full_time_hr": list_of_employee_values[1],
                                "part_time_hr": list_of_employee_values[2],
                                "max_work_days": list_of_employee_values[3],
                                "max_work_hrs": list_of_employee_values[4],
                                "wage_per_hr": list_of_employee_values[5],
                                }

    def return_employee_object(self):
        emp_object = Employee(self.company_details)
        emp_object.adds_calculated_values()
        return emp_object

    def return_indian_employee_object(self):
        ind_emp_object = IndianEmployee(self.company_details)
        ind_emp_object.adds_calculated_values()
        return ind_emp_object

    def return_usa_employee_object(self):
        usa_emp_object = USAEmployee(self.company_details)
        usa_emp_object.adds_calculated_values()
        return usa_emp_object
