def formula(job1, job2, money_wanted, taxes):
    denominator = 40 * job1 + 40 * job2
    denominator *= 1 - taxes
    weeks = money_wanted / denominator
    months = weeks / 4
    return str(months)

taxes = .2
money_wanted = 10000
print("Job 1 pay rate: ", end='')
job_one = float(input())
print("Job 2 pay rate: ", end='')
job_two = float(input())
print("Amount of months: ")
print(formula(job_one, job_two, money_wanted, taxes))

# Copy this to the other website