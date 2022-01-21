
class UserInputs:
    """
    Creates a new employee object with all the given parameters
    """

    def __init__(self, part_time_hr, full_time_hr, max_work_days,
                 max_work_hrs, total_part_time_days, total_full_time_days,
                 total_absent_days, wage_per_hr, company_name, total_wage, max_hrs_worked):
        self.part_time_hr = part_time_hr
        self.full_time_hr = full_time_hr
        self.max_work_days = max_work_days
        self.max_work_hrs = max_work_hrs
        self.total_part_time_days = total_part_time_days
        self.total_full_time_days = total_full_time_days
        self.total_absent_days = total_absent_days
        self.wage_per_hr = wage_per_hr
        self.company_name = company_name
        self.total_wage = total_wage
        self.max_hrs_worked = max_hrs_worked

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


