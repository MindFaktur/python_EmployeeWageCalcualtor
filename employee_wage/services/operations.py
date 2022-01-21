import random

from emp_user_inputs import user_inputs


class Operations:
    """
    All operations are carried out here and all objects are added to class list
    """

    list_of_company_objects = []

    @staticmethod
    def menu():
        """
        Shows the menu and performs accordingly
        :return: nothing
        """
        option = 0
        while option != 2:
            if option == 1:
                Operations.list_of_company_objects.append(Operations.company_object_creator())

            option = int(input("Press \n1) Add company \n2) Quit \n "))
        for i in Operations.list_of_company_objects:
            print(i)

    @staticmethod
    def returns_random_number():
        """
        Generates random number between 0, 1 & 2
        :return:
        """
        return random.randrange(0, 3)

    @staticmethod
    def company_object_creator():
        """
        Creates object of user inputs where the company specific data is created and stored
        :return: employee object
        """
        company_name = input("Please enter company name: ")
        full_time_hrs = int(input("Please enter the full time hours your company: "))
        part_time_hrs = int(input("Please enter the part time hours your company: "))
        max_work_days = int(input("Please enter the maximum number of working days in a month "
                                  "that an employee should not exceed: "))
        max_work_hours = int(input("Please enter the maximum number of working hours in a month "
                                   "that an employee should not exceed: "))
        wage_per_hour = int(input("Please enter the wage per hour: "))

        employee_object = user_inputs.UserInputs(
            part_time_hr=part_time_hrs,
            full_time_hr=full_time_hrs,
            max_work_days=max_work_days,
            max_work_hrs=max_work_hours,
            total_part_time_days=0,
            total_full_time_days=0,
            total_absent_days=0,
            wage_per_hr=wage_per_hour,
            company_name=company_name,
            total_wage=0,
            max_hrs_worked=0
        )
        Operations.all_properties(employee_object)
        return employee_object

    @staticmethod
    def emp_wage_for_the_day(wage_per_hr, hours_worked):
        """
        Calculate employee wage per day
        :param wage_per_hr: wage per hour fixe by the company
        :param hours_worked: hours worked depends on the random number generated
        :return: wage per day
        """
        return wage_per_hr * hours_worked

    @staticmethod
    def all_properties(emp_object):
        """
        Calculates all other fields of employee object and adds to it
        :param emp_object:
        :return: nothing
        """
        total_wage = 0
        max_hrs_worked = 0
        total_full_time_days = 0
        total_part_time_days = 0
        total_absent_days = 0
        max_days_worked = total_full_time_days + total_part_time_days + total_absent_days

        while (total_part_time_days + total_full_time_days) <= emp_object.max_work_days \
                and max_hrs_worked <= emp_object.max_work_hrs \
                and max_days_worked <= 31:
            type_of_day = Operations.returns_random_number()
            if type_of_day == 0:
                total_absent_days = total_absent_days + 1
            elif type_of_day == 1:
                total_wage = total_wage + Operations.emp_wage_for_the_day(emp_object.wage_per_hr,
                                                                          emp_object.part_time_hr)
                total_part_time_days = total_part_time_days + 1
                max_hrs_worked = max_hrs_worked + emp_object.part_time_hr
            else:
                total_wage = total_wage + Operations.emp_wage_for_the_day(emp_object.wage_per_hr,
                                                                          emp_object.full_time_hr)
                total_full_time_days = total_full_time_days + 1
                max_hrs_worked = max_hrs_worked + emp_object.full_time_hr

        emp_object.total_wage = total_wage
        emp_object.max_hrs_worked = max_hrs_worked
        emp_object.total_full_time_days = total_full_time_days
        emp_object.total_part_time_days = total_part_time_days
        emp_object.total_absent_days = total_absent_days


