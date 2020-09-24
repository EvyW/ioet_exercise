# import libraries
import sys # import current path (allow us to call our own modules/packages)
sys.path.append('../') # append current path
from ioet_exercise import compute_employees_salary, load_data # import our own modules/packages

"""
This master file executes the program  
"""

# 1. Load data (the user provides the path to the data)
raw_data = load_data.classLoadData()
data = raw_data.loadData()

# 2. Compute the salary of each employee and show it in console
compute = compute_employees_salary.classComputeEmployeesSalary()
compute.salaryPerEmployee(data)
