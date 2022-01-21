import random
import logging

from emp_user_inputs import user_inputs
from emp_user_inputs.user_inputs import Employee


class Operations:
    """
    All operations are carried out here and all objects are added to class list
    """
    logging.basicConfig(filename='log.txt', filemode='a',
                        format='%(asctime)s - %(message)s \n ', level=logging.DEBUG)

    @staticmethod
    def menu():
        """
        Shows the menu and performs accordingly
        :return: nothing
        """
        list_of_company_objects = []
        option = 0
        while option != 2:
            if option == 1:
                list_of_company_objects.append(Operations.company_object_creator())
            try:
                option = int(input("Press \n1) Add company \n2) Quit \n "))
            except Exception:
                print("Error Exception")
                logging.exception("exception")

        for i in list_of_company_objects:
            print(i)

    @staticmethod
    def company_object_creator():
        """
        Creates object of user inputs where the company specific data is created and stored
        :return: employee object
        """
        try:
            company_details = {"company_name": input("Please enter company name: "),
                               "full_time_hr": int(input("Please enter the full time hours your company: ")),
                               "part_time_hr": int(input("Please enter the part time hours your company: ")),
                               "max_work_days": int(input("Please enter the maximum number of working days in a month "
                                                          "that an employee should not exceed: ")),
                               "max_work_hrs": int(input("Please enter the maximum number of working hours "
                                                         "in a month that an employee should not exceed: ")),
                               "wage_per_hr": int(input("Please enter the wage per hour: "))
                               }

            employee_object = Employee(company_details)
            employee_object.adds_calculated_values()
            return employee_object
        except TypeError:
            print("Please enter integer value")
            logging.debug("Invalid value entered")
        except Exception:
            print("Error Exception")
            logging.exception("exception")
