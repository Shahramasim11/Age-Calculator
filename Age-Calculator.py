print("Welcome to the age calculator")
age = float(input("Enter your current age: "))
expected_age = float(input("Enter your expected age: "))
weeks_per_year = 52
days_per_year = 365
month_per_year = 12
Age_left_in_years = expected_age - age
print("Age left in years: ", Age_left_in_years)
Age_left_in_months = Age_left_in_years * month_per_year
print("Age left in months: ", Age_left_in_months)
Age_left_in_weeks = Age_left_in_years * weeks_per_year
print("Age left in weeks: ", Age_left_in_weeks)
Age_left_in_days = Age_left_in_years * days_per_year
print("Age left in days: ", Age_left_in_days)
Total_age_left = f"You have {Age_left_in_months} months, {Age_left_in_weeks} weeks, and {Age_left_in_days} days"
print(Total_age_left)