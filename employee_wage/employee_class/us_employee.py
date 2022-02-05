from employee_class.employee import Employee


class USAEmployee(Employee):

    def emp_wage_for_the_day(self, hours_worked):
        """
        Calculate employee wage per day
        :param hours_worked: hours worked depends on the random number generated
        :return: wage per day
        """
        return self.wage_per_hr * hours_worked + 50
