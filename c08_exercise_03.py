"""
3. Variable appointments refers to the list ['9:00', '10:30', '14:00', '15:00',
'15:30']. An appointment is scheduled for 16:30, so '16:30' needs to be added
to the list.
"""

# a. Using list method append, add '16:30' to the end of the list that
# appointments refers to.
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
appointments.append('16:30')
print(appointments)

# b. Instead of using append, use the + operator to add '16:30' to the end of
# the list that appointments refers to.
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
appointments += ['16:30']
print(appointments)

# c. You used two approaches to add '16:30' to the list. Which approach
# modified the list and which approach created a new list?

# answer: append modified the list and + operator created a new list.
