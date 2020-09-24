# Salary Calculator
This is a program that computes the salary of employees according to specific rules

## Requirements
Make sure that you have installed python 3

## Architecture 
There are 3 main files:
1. "master.py": which is the master file that has to be executed to run the program
2. "load_data.py": which asks for the path to the data that will be computed and loads it in the right format
3. "compute_employees_salary.py": which makes the computation of the salaries

Another important file is "test_py" which contains the test cases 

## Getting started and execution
1. Download this repository and make sure that the name of the folder is: ioet_exercise
2. Open your terminal and go to ioet_exercise folder

![alt text](https://github.com/EvyW/ioet_exercise/blob/master/docs/images/Imagen%201.png)

3. Run the program using the following command:
```
python3 master.py
```
The program is going to ask you to provide the path to the data that you want to compute (make sure that the path is written inside quotation marks). You can use the exemplary data that comes in this repository. 

![alt text](https://github.com/EvyW/ioet_exercise/blob/master/docs/images/Imagen%202.png)

Ready! you are going to see the salary that has to be paid to every employee. It looks like this:

![alt text](https://github.com/EvyW/ioet_exercise/blob/master/docs/images/Imagen%203.png)

4. For running the tests, you only have to use the following command:
```
python3 test.py
```
If everything goes well, you should get an "OK" at the end of the execution

## Approach 

This problem was solved mainly based on if-then rules that enforce the constrains given by the problem:
- There are 3 shifts: 00:00-09:00, 09:00-18:00, and 18:00-00:00. Each of them have different salary rates per hour (e.g. $25, $15, and $20 respectively)
- Salary rates depend on whether this is during the weekday or weekend.
- Days are indicated by the first two letters of the day (e.g. MO for Mondays). Time comes in the format HOUR:MINUTE (e.g. 09:00)
- The input comes in the format: Name, DayHOUR:MINUTE-HOUR:MINUTE, ... (e.g. ASTRID,MO10:00-12:00,TH12:00-14:00,SU20:00-21:00)

Assumptions:
- An employee can work an undefined number of hours in one day
- An employee can start and finish at any time, any hour and minute (along with one, two, or three shifts) during the day
- The employee works continuously during the day (e.g from 10:00 to 18:00, but not from 10:00 to 14:00 and later from 15:00 to 18:00)

