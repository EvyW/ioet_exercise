"""
This module computes the salary per employee
"""

class classComputeEmployeesSalary:

    @staticmethod
    def salaryPerEmployee(data):

        # Compute the salary of the DAY when the employee works only in one shift (e.g. shift from 9:00 to 18:00)
        def oneShift(start_time, end_time, start_minute, end_minute, wage):

            # Salary per minute
            minute_wage = wage/60

            # Compute
            if end_minute > start_minute:
                payment = (end_time - start_time)*wage + (end_minute - start_minute)*minute_wage
            elif end_minute < start_minute:
                payment = (end_time - start_time - 1)*wage + (60 - start_minute + end_minute)*minute_wage
            else: # When start_minute ==  end_minute
                payment = (end_time - start_time)*wage

            return payment


        # Compute the salary of the DAY when the employee works along two shifts (e.g. any time between shift 9:00 to 18:00 and 18:00 to 00:00)
        def twoShifts(start_time,end_time,start_minute,end_minute,limit_time1,limit_time2,hourly_wage_first_shift, hourly_wage_second_shift):

            # Salary per minute
            minute_wage_first_shift = hourly_wage_first_shift/60
            minute_wage_second_shift = hourly_wage_second_shift/60

            # Compute
            pay_first_shift = (limit_time1 - start_time - 1)*hourly_wage_first_shift + (60 - start_minute)*minute_wage_first_shift
            pay_second_shift = (end_time - limit_time2)*hourly_wage_second_shift + end_minute*minute_wage_second_shift
            total_to_pay = pay_first_shift + pay_second_shift

            return total_to_pay


        # Compute the salary of the DAY when the employee works along three shifts (e.g. any time between shift 9:00 to 18:00, shift 18:00 to 00:00, and shift 00:00 to 09:00)
        def threeShifts(start_time,end_time,start_minute,end_minute,limit_time1, limit_time2, limit_time3,limit_time4, hourly_wage_first_shift,hourly_wage_second_shift, hourly_wage_third_shift):

            # Salary per minute
            minute_wage_first_shift = hourly_wage_first_shift/60
            minute_wage_third_shift = hourly_wage_third_shift/60

            # Compute
            pay_first_shift = (limit_time1 - start_time - 1) * hourly_wage_first_shift + (60 - start_minute) * minute_wage_first_shift
            pay_second_shift = (limit_time2 - limit_time3) * hourly_wage_second_shift
            pay_third_shift = (end_time - limit_time4) * hourly_wage_third_shift + end_minute * minute_wage_third_shift
            total_to_pay = pay_first_shift + pay_second_shift + pay_third_shift

            return total_to_pay


        # Compute the salary of the DAY when the employee works along three shifts (but start_time and end_time ar both in the same shift)
        def threeShifts2(start_time, end_time, start_minute, end_minute, limit_time1, limit_time2, limit_time3, limit_time4, limit_time5, limit_time6, hourly_wage_first_shift, hourly_wage_second_shift, hourly_wage_third_shift):

            # Salary per minute
            minute_wage_first_shift = hourly_wage_first_shift / 60

            # Compute
            pay_first_shift = (limit_time1 - start_time - 1) * hourly_wage_first_shift + (60 - start_minute) * minute_wage_first_shift + (end_time-limit_time2)*hourly_wage_first_shift + end_minute*minute_wage_first_shift
            pay_second_shift = (limit_time3 - limit_time4) * hourly_wage_second_shift
            pay_third_shift = (limit_time5 - limit_time6) * hourly_wage_third_shift
            total_to_pay = pay_first_shift + pay_second_shift + pay_third_shift

            return total_to_pay


        # Defines the case (e.g. works only in one shift, or alog two shifts, etc.) and computes the salary of the DAY
        def computeSalary(start_time, end_time, start_minute, end_minute, wage_early_morning, wage_day_time, wage_night_time):

            # set as 24 hour format
            if end_time == 0:
                end_time = 24

            # CASE 1.  Works in/until the early morning shift (from 0:00 to 9:00)
            if 0 <= start_time < 9 and 0 < end_time <= 9:  # 225
                # CASE 1.1. Works only during early morning
                if start_time < end_time: # works along one shift
                    if end_time == 9 and end_minute > 0: # if surpasses the upper limit is a case of two shifts
                        None
                    else:
                        payment = oneShift(start_time, end_time, start_minute, end_minute, wage_early_morning)
                 # CASE 1.2. Works along three shifts, starts in early morning day and finishes next day also in the early morning shift
                elif start_time >= end_time: # Works along 3 shifts
                    payment = threeShifts2(start_time,end_time,start_minute,end_minute,9,0,18,9,24,18,wage_early_morning,wage_day_time,wage_night_time)
                else:
                    None

            # CASE 2.  Works in/until the day time shift (from 9:00 to 18:00)
            if 9 <= start_time < 18 and 9 < end_time <= 18:  # 135
                # CASE 2.1. Works only during day time (from 9:00 to 18:00)
                if start_time < end_time:  # Works along one shift
                    if end_time == 18 and end_minute > 0: # if surpasses the upper limit is a case of two shifts
                        None
                    else:
                        payment = oneShift(start_time,end_time,start_minute,end_minute,wage_day_time)
                # CASE 2.2. Works along three shifts, starts in shift from 9:00 to 18:00 and finishes next day also in the shift from 9:00 to 18:00
                elif start_time >= end_time: # Works along 3 shifts
                    payment = threeShifts2(start_time,end_time,start_minute,end_minute,18,9,24,18,9,0,wage_day_time,wage_night_time,wage_early_morning)
                else:
                    None

            # CASE 3.  Works in/until the night time shift (from 18:00 to 00:00)
            if 18 <= start_time < 24 and 18 < end_time <= 24:  # 120
                # CASE 3.1. Works only during night time (from 18:00 to 00:00)
                if start_time < end_time:  # Works along one shift
                    if end_time == 24 and end_minute > 0: # if surpasses the upper limit is a case of two shifts
                        None
                    else:
                        payment = oneShift(start_time,end_time,start_minute,end_minute,wage_night_time)
                # CASE 3.2. Works along three shifts, starts in shift from 18:00 to 00:00 and finishes next day also in the shift from 18:00 to 00:00
                elif start_time >= end_time: # Works along 3 shifts
                    payment = threeShifts2(start_time,end_time,start_minute,end_minute,24,18,9,0,18,9,wage_night_time,wage_early_morning,wage_day_time)
                else:
                    None

            # CASE 4.  Works along two shifts, in early morning shift (0:00 to 9:00) and day time shift (9:00 to 18:00)
            if 0 <= start_time < 9 and 9 <= end_time <= 18:  # 360
                if end_time == 18 and end_minute > 0: # if it is later than 18:00 then it is a three shifts case
                    None
                else:
                    payment = twoShifts(start_time, end_time, start_minute, end_minute, 9, 9, wage_early_morning, wage_day_time)  # 480

            # CASE 5.  Works along three shifts, in early morning shift (0:00 to 9:00), day time shift (9:00 to 18:00), and night time shift (18:00 to 00:00)
            if 0 <= start_time < 9 and 18 <= end_time <= 24:
                    payment = threeShifts(start_time, end_time, start_minute, end_minute, 9, 18, 9, 18, wage_early_morning, wage_day_time, wage_night_time)

            # CASE 6.  Works along two shifts, in early morning shift (9:00 to 18:00) and day time shift (18:00 to 00:00)
            if 9 <= start_time < 18 and 18 <= end_time <= 24:  # 255
                if end_time == 24 and end_minute > 0: # if it is later than 00:00 then it is a three shifts case
                    None
                else:
                    payment = twoShifts(start_time, end_time, start_minute, end_minute, 18, 18, wage_day_time, wage_night_time)

            # set as 00 hour format
            if end_time == 24:
                end_time = 0

            # CASE 7.  Works along three shifts, in day time shift (9:00 to 18:00), night time shift (18:00 to 00:00), and early morning shift (00:00 to 09:00)
            if 9 <= start_time < 18 and 0 <= end_time <= 9:
                payment = threeShifts(start_time, end_time, start_minute, end_minute, 18, 24, 18, 0, wage_day_time, wage_night_time,wage_early_morning)

            # CASE 8.  Works along two shifts, in early morning shift (18:00 to 00:00) and day time shift (00:00 to 09:00)
            if 18 <= start_time < 24 and 0 <= end_time <= 9:  # 345
                if end_time == 9 and end_minute > 0: # if it is later than 09:00 then it is a three shifts case
                    None
                else:
                    payment = twoShifts(start_time, end_time, start_minute, end_minute, 24, 0, wage_night_time, wage_early_morning)

            # CASE 9.  Works along three shifts, night time shift (18:00 to 00:00), early morning shift (00:00 to 09:00), and day time shift (09:00 to 18:00)
            if 18 <= start_time < 24 and 9 <= end_time <= 18:
                payment = threeShifts(start_time, end_time, start_minute, end_minute, 24, 9, 0, 9, wage_night_time, wage_early_morning,wage_day_time)

            return payment


        # Iterate over each employee, validate its information and compute its salary
        for employee in data:

                # Create an empty list to collect the payment of every day
                daily_payment = []

                # Iterate over the information of the employee
                for information in employee:

                    # Print if it is the name of the employee
                    if employee.index(information) == 0:
                        print('The amount to pay',information, 'is:')

                    # Otherwise evaluate and validate dates, and compute salary
                    else:

                        # 1. Evaluate that minutes' format is appropriate

                        # define start and end minute
                        start_minute = int(information[5:7])
                        end_minute = int(information[11:13])

                        if start_minute < 0 or start_minute > 59 or end_minute < 0 or end_minute > 59:
                            print('Something went wrong, format might not be correct. It must look like this MO09:00-16:00. '
                                  'MINUTES must be between 0 and 59. ERROR in:',information)
                            # empty the list to not to sum any value
                            daily_payment = []
                            total_payment = 'Something went wrong, format might not be correct. It must look like this MO09:00-16:00. MINUTES must be between 0 and 59.'
                            # exit loop and take next employee
                            break
                        else:
                            # everything ok, continue in the loop
                            None


                        # 2. Evaluate that hours' format is appropriate

                        # define start and end time
                        start_time = int(information[2:4]) # define as integer
                        end_time = int(information[8:10]) # define as integer

                        if start_time < 0 or start_time > 23 or end_time < 0 or end_time > 23:
                            print('Something went wrong, format might not be correct. It must look like this MO09:00-16:00, '
                                  'HOUR must be between 00 and 23. ERROR in:',information)
                            # empty the list to not to sum any value
                            daily_payment = []
                            total_payment = 'Something went wrong, format might not be correct. It must look like this MO09:00-16:00 HOUR must be between 00 and 23.'
                            # exit loop and take next employee
                            break
                        else:
                            # everything ok, continue in the loop
                            None


                        # 3. Evaluate that day's format is appropriate and compute the total salary

                        # define day
                        day = information[:2]

                        if day == 'MO' or day == 'TU' or day == 'WE' or day == 'TH' or day == 'FR':
                            # define wage for every working shift
                            wage_early_morning = 25
                            wage_day_time = 15
                            wage_night_time = 20

                            # compute payment (salary)
                            payment = computeSalary(start_time,end_time,start_minute,end_minute,wage_early_morning,wage_day_time,wage_night_time)

                            # append the total of the day
                            daily_payment.append(payment)

                        elif day == 'SA' or day == 'SU': # for saturdays and sundays
                            # define wage for every working shift
                            wage_early_morning = 30
                            wage_day_time = 20
                            wage_night_time = 25

                            # compute payment (salary)
                            payment = computeSalary(start_time,end_time,start_minute,end_minute,wage_early_morning,wage_day_time,wage_night_time)

                            # append the total of the day
                            daily_payment.append(payment)

                        else:
                            print('Something went wrong, format might not be correct. It must look like this MO09:00-16:00.'
                                  'DAY must be one of the following: MO, TU, WE, TH, FR, SA or SU in uppercase. ERROR in:',information)
                            # empty the list to not to sum any value
                            daily_payment = []
                            total_payment = 'Something went wrong, format might not be correct. It must look like this MO09:00-16:00. DAY must be one of the following: MO, TU, WE, TH, FR, SA or SU in uppercase.'
                            # exit loop and take next employee
                            break
                # If everything went well and all the right values were collected, sum them up and print it
                if daily_payment:
                    total_payment = sum(daily_payment)
                    print(total_payment)
                else: # do not print anything
                    None

        return total_payment