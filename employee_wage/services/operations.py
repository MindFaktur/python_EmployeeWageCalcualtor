import random
import logging

from Adapter.adapter import InputToDictionary
from employee_class import employee
from employee_class.employee import Employee


class Operations:
    """
    All operations are carried out here and all objects are added to class list
    """
    logging.basicConfig(filename='log.txt', filemode='a',
                        format='%(asctime)s - %(message)s \n ', level=logging.DEBUG)

    list_of_company_objects = []
    list_of_indian_company_objects = []
    list_of_usa_company_objects = []

    def menu(self):
        """
        Shows the menu and performs accordingly
        :return: nothing
        """
        option = 0
        while option != 2:
            if option == 1:
                self.company_object_creator()
            try:
                option = int(input("Press \n1) Add company \n2) Quit \n "))
            except Exception:
                print("Error Exception")
                logging.exception("exception")

        for i in self.list_of_company_objects:
            print("Normal")
            print(i)
        for i in self.list_of_indian_company_objects:
            print("Indian")
            print(i)
        for i in self.list_of_usa_company_objects:
            print("USA")
            print(i)

    def company_object_creator(self):
        """
        Creates object of user inputs where the company specific data is created and stored
        :return: employee object
        """
        try:
            company_details = [input("Please enter company name: "),
                               int(input("Please enter the full time hours your company: ")),
                               int(input("Please enter the part time hours your company: ")),
                               int(input("Please enter the maximum number of working days in a month "
                                         "that an employee should not exceed: ")),
                               int(input("Please enter the maximum number of working hours "
                                         "in a month that an employee should not exceed: ")),
                               int(input("Please enter the wage per hour: "))
                               ]

            employee_object = InputToDictionary(company_details).return_indian_employee_object()
            indian_employee_object = InputToDictionary(company_details).return_indian_employee_object()
            usa_employee_object = InputToDictionary(company_details).return_usa_employee_object()

            self.list_of_company_objects.append(employee_object)
            self.list_of_indian_company_objects.append(indian_employee_object)
            self.list_of_usa_company_objects.append(usa_employee_object)

        except TypeError:
            print("Please enter integer value")
            logging.debug("Invalid value entered")
        except Exception:
            print("Error Exception")
            logging.exception("exception")
