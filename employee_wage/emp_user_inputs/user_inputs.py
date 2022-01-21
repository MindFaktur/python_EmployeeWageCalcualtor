import random


class Employee:
    """
    Creates a new employee object with all the given parameters
    """

    def __init__(self, part_time_hr, full_time_hr, max_work_days,
                 max_work_hrs, wage_per_hr, company_name):
        self.part_time_hr = part_time_hr
        self.full_time_hr = full_time_hr
        self.max_work_days = max_work_days
        self.max_work_hrs = max_work_hrs
        self.total_part_time_days = 0
        self.total_full_time_days = 0
        self.total_absent_days = 0
        self.wage_per_hr = wage_per_hr
        self.company_name = company_name
        self.total_wage = 0
        self.max_hrs_worked = 0

    def __str__(self):
        """
        Prints the object in below format when printed
        :return:
        """
        return "{ company_name: " + str(self.company_name) + \
               ", full_time_hr: " + str(self.full_time_hr) + \
               ", part_time_hr: " + str(self.part_time_hr) + \
               ", max_work_days: " + str(self.max_work_days) + \
               ", max_work_hrs: " + str(self.max_work_hrs) + \
               ", wage_per_hr: " + str(self.wage_per_hr) + \
               ", total_part_time_days: " + str(self.total_part_time_days) + \
               ", total_full_time_days: " + str(self.total_full_time_days) + \
               ", total_absent_days: " + str(self.total_absent_days) + \
               ", total_wage: " + str(self.total_wage) + \
               ", max_hrs_worked: " + str(self.max_hrs_worked) + \
               " }"

    @staticmethod
    def returns_random_number():
        """
        Generates random number between 0, 1 & 2
        :return:
        """
        return random.randrange(0, 3)

    def emp_wage_for_the_day(self, hours_worked):
        """
        Calculate employee wage per day
        :param hours_worked: hours worked depends on the random number generated
        :return: wage per day
        """
        return self.wage_per_hr * hours_worked

    def adds_calculated_values(self):
        """
        Calculates all other fields of employee object and adds to it
        :param self:
        :return: nothing
        """
        total_wage = 0
        max_hrs_worked = 0
        total_full_time_days = 0
        total_part_time_days = 0
        total_absent_days = 0
        max_days_worked = total_full_time_days + total_part_time_days + total_absent_days

        while (total_part_time_days + total_full_time_days) <= self.max_work_days \
                and max_hrs_worked <= self.max_work_hrs \
                and max_days_worked <= 31:
            type_of_day = self.returns_random_number()
            if type_of_day == 0:
                total_absent_days = total_absent_days + 1
            elif type_of_day == 1:
                total_wage = total_wage + self.emp_wage_for_the_day(self.part_time_hr)
                total_part_time_days = total_part_time_days + 1
                max_hrs_worked = max_hrs_worked + self.part_time_hr
            else:
                total_wage = total_wage + self.emp_wage_for_the_day(self.full_time_hr)
                total_full_time_days = total_full_time_days + 1
                max_hrs_worked = max_hrs_worked + self.full_time_hr

        self.total_wage = total_wage
        self.max_hrs_worked = max_hrs_worked
        self.total_full_time_days = total_full_time_days
        self.total_part_time_days = total_part_time_days
        self.total_absent_days = total_absent_days


