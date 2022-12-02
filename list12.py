"""tech_companies = ['Qualcomm','Google','Apple',['Nvidia','Cisco','Samsung']]

tech_companies.pop()
print(tech_companies.pop())
tech_companies.extend(['Nvidia','Cisco','Samsung'])
print(tech_companie)"""


"""if the date lies between 1st Jan, 2020 - 31st March, 2020, you need to extract the corresponding quarter as '2020-Q1'

if the date lies between 1st April, 2020 - 30th June, 2020, the extracted quarter will be '2020-Q2'

if the date lies between 1st July, 2020 - 30th September, 2020, the extracted quarter will be '2020-Q3'

if the date lies between 1st October, 2020 - 31st Decemeber, 2020 then the extracted quarter will be '2020-Q4'

"""

# Take a proper date input from the user in the format YYYY-MM-DD. Consider this date as a string
user_date = "2020-09-09"
# Write your code using if else statements to extract the quarter
date_year=user_date[:5]
date_month=user_date[5:7]

print(date_year)
print(date_month)
# Store the quarter value in a string variable named quarter
if date_month>'09':
    print('fourth_quarter')
if date_month>'07':
    if date_month<'10':
        print('third_quarter')

if date_month<'04':
    print('first quater')
if date_month>'03':
    if date_month<'07':

        print('second_quater')
