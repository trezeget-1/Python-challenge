import os
import csv

employee_data = os.path.join("employee_data.csv")

emp_id=[]
name=[]
dob=[]
ssn=[]
state=[]

with open (employee_data) as pyboss_file:
    employee_file = csv.reader(pyboss_file, delimiter=",")

    next(employee_file)

    for line in employee_file:
        emp_id.append(line[0])
        name.append(line[1])
        dob.append(line[2])
        ssn.append(line[3])
        state.append(line[4])

# First Name and Last Name List

fist_name=[]
last_name=[]

for i in range(len(name)):
    name[i]=name[i].split()
    fist_name.append(name[i][0])
    last_name.append(name[i][1])

# `DOB` data

year=[]
day=[]
month=[]

for i in range(len(dob)):
    dob[i]=dob[i].split("-")
    year.append(dob[i][0])
    month.append(dob[i][1])
    day.append(dob[i][2])
    year[i]=str(year[i])
    month[i]=str(month[i])
    day[i]=str(day[i])
    dob[i]=f'{month[i]}/{day[i]}/{year[i]}'

# SSN data

ssn1=[]
ssn2=[]

for i in range(len(ssn)):
    ssn[i]=ssn[i].split("-")
    ssn1.append(ssn[i][0])
    ssn1[i]="***"
    ssn2.append(ssn[i][1])
    ssn2[i]="**"
    ssn[i]=f'{ssn1[i]}-{ssn2[i]}-{ssn[i][2]}'

#State information

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

for i in range(len(state)):
    if state[i] in us_state_abbrev:
        state[i]=us_state_abbrev[f'{state[i]}']

final_list=[]

#Presentation of results

for i in range(len(emp_id)):
    a=f'{emp_id[i]},{fist_name[i]},{last_name[i]},{dob[i]},{ssn[i]},{state[i]}'
    final_list.append(a)
    final_list[i]=final_list[i].split(",")

# Export a text file with the results

# Set variable for output file
output_file = os.path.join("final_employee_data.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(final_list)