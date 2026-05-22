# EMPLOYEE OVERTIME CALCULATOR

#Get employee details
employee_name = input("Enter employee name: ")

try:
    hourly_rate = float(input("Enter hourly rate (UGX): "))
    hours_worked = float(input("Enter total hours worked: "))

    if hourly_rate <= 0 or hours_worked <= 0:
        print("Error: Values must be greater than zero.")

    else:
        standard_hours = 40

        if hours_worked <= standard_hours:
            regular_pay = hourly_rate * hours_worked
            overtime_pay = 0
            gross_pay = regular_pay

            print(
                f"Employee: {employee_name} | "
                f"Rate: {hourly_rate:.2f} UGX/hr | "
                f"Hours: {hours_worked:.0f} | "
                f"Regular: {regular_pay:.2f} | "
                f"Overtime: {overtime_pay:.2f} | "
                f"Gross: {gross_pay:.2f} UGX | "
                f"No overtime accrued."
            )

        #Overtime calculation
        else:
            overtime_hours = hours_worked - standard_hours

            regular_pay = hourly_rate * standard_hours
            overtime_pay = overtime_hours * (hourly_rate * 1.5)

            gross_pay = regular_pay + overtime_pay

            print(
                f"Employee: {employee_name} | "
                f"Rate: {hourly_rate:.2f} UGX/hr | "
                f"Hours: {hours_worked:.0f} | "
                f"Regular: {regular_pay:.2f} | "
                f"Overtime: {overtime_pay:.2f} | "
                f"Gross: {gross_pay:.2f} UGX | "
            )

except ValueError:
    print("Error: Please enter valid numeric values.")
    