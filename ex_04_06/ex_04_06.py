def computePay(hours, rate):
    # print("In computePay", hours, rate)
    if hours > 40:
        regHours = hours * rate
        overTime = (hours - 40) * (1.5 * rate)
        pay = regHours + overTime
    else:
        pay = hours * rate
    # print("Returning", pay)
    return pay

impHours = input("Enter Hours: ")
impRate = input("Enter Rate: ")
hrs = float(impHours)
rt = float(impRate)

dollars = computePay(hrs, rt)

print("Pay: ", dollars)
