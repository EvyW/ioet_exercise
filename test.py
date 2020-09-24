# import libraries
import unittest # testing library
import sys # import current path (allow us to call our own modules/packages)
sys.path.append('../') # append current path
from ioet_exercise import compute_employees_salary # import our own modules/packages


class testSalaryComputation(unittest.TestCase):


    def testInputDay(self):

        """
        Test that it does not accept other input DAY other than MO, TU, WE, TH, FR, SA, or SU
        """
        # example of the input
        test_data = [['MICHAELA','ZZ08:00-12:00']]
        # compute
        computation = compute_employees_salary.classComputeEmployeesSalary
        result = computation.salaryPerEmployee(test_data)
        # test
        self.assertEqual(result,'Something went wrong, format might not be correct. It must look like this MO09:00-16:00. DAY must be one of the following: MO, TU, WE, TH, FR, SA or SU in uppercase.')


    def testInputIsUppercase(self):

        """
        Test that it does not accept uppercase DAY
        """
        # example of the input
        test_data = [['FATIMA','we10:00-19:00']]
        # compute
        computation = compute_employees_salary.classComputeEmployeesSalary
        result = computation.salaryPerEmployee(test_data)
        # test
        self.assertEqual(result,'Something went wrong, format might not be correct. It must look like this MO09:00-16:00. DAY must be one of the following: MO, TU, WE, TH, FR, SA or SU in uppercase.')


    def testInputHour(self):

        """
        Test that it does not accept input HOUR out of the range 00 and 24
        """
        # example of the input
        test_data = [['DAVID','SA10:00-25:00']]
        # compute
        computation = compute_employees_salary.classComputeEmployeesSalary
        result = computation.salaryPerEmployee(test_data)
        # test
        self.assertEqual(result,'Something went wrong, format might not be correct. It must look like this MO09:00-16:00 HOUR must be between 00 and 23.')


    def testInputMinutes(self):

        """
        Test that it does not accept input MINUTE out of the range 00 and 59
        """
        # example of the input
        test_data = [['ANDRES','SA10:65-25:00']]
        # compute
        computation = compute_employees_salary.classComputeEmployeesSalary
        result = computation.salaryPerEmployee(test_data)
        # test
        self.assertEqual(result,'Something went wrong, format might not be correct. It must look like this MO09:00-16:00. MINUTES must be between 0 and 59.')


    def testWorkedInTwoShifts(self):

        """
        Test that it can compute the salary when an employee works along two shifts
        e.g.Monday from 08:00 (with a salary of $15 per hour until 9:00) to 15:00 (with a salary of $20 per hour from (9:00)
        """
        # example of the input
        test_data = [['MARIA','MO08:00-15:00']]
        # compute
        computation = compute_employees_salary.classComputeEmployeesSalary
        result = computation.salaryPerEmployee(test_data)
        # test
        self.assertEqual(result,115)

    def testWorkedInThreeShifts(self):

        """
        Test that it can compute the salary when an employee works along three shifts
        e.g.Monday from 17:00 (with a salary of $15 per hour until 18:00) to 01:00 (with a salary of $20 until 00:00 and
        $25 from 00:00 per hour)
        """
        # example of the input
        test_data = [['LENARD','FR07:00-19:00']]
        # compute
        computation = compute_employees_salary.classComputeEmployeesSalary
        result = computation.salaryPerEmployee(test_data)
        # test
        self.assertEqual(result,205)

# that the DAY input format is correct

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")


#person = TestSum()
#person.testSalaryComputation()