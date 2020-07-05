#### COLLEGE ADMISSIONS ASSIGNMENT ####
# Below are student's applications for Monsters University 
# Each list corresponds to a single student and we can find information about the student by doing:
#        list_name[0] = First Name
#        list_name[1] = Last Name
#        list_name[2] = Cumulative GPA  
#        list_name[3] = City Located
#        list_name[4] = Major
mike = ['miKe', 'wAzOwSki', 3.4, 'MoNsTroPolIs', 'scareology']
print(mike)
randall = ['RaNdAlL', 'BoGgs', 3.2, 'MoNStroVille', 'laughter science']
james = ['JaMeS','sUlLiVan', 2.9, 'bOo JoSe', 'nC', 'scareology']

mike_classes = {'AP Scare', 'Bed Scare', 'English'}
randall_classes = {'Closet Scare', 'Scare Academy', 'Creative Writing'}
james_classes = {'Scare 101', 'Scare Academy', 'Forest Scare'}

#### DO NOT CHANGE CODE ABOVE ####

#### PART 1 ####
# Add all three students to a list called all_students
# Tip: Look at the Python Cheat Sheet for a function to do this!

##### YOUR CODE HERE #####


















#### PART 2 ####
# Now the Monsters University wants to process all of the students locations. Edit each student's city from their own list (for ex. Mikes's list is mike) & save them to their own variable (for example: Mikes's city can be in the variable mike_city). 
# To process all of the student's locations, we want to for example, print 'Monstropolis' with 'M' and being capitalized for Mike's location. Essentially for the city, we want the first letter capitalized and the rest would be lowercase.  
# Note we can get the upper case version of a string using the function string.upper() and lower case using string.lower(). See the example below:

''' Uncomment this code (the 3-chained quotations) & run it!
mike_city = mike[3]
mike_city = str(mike_city[0].upper() + mike_city[1:].lower())    
# capitalized should be 'M' & lower_case should be 'onstropolis'
print('reformatted : ' + mike_city)
'''

##### YOUR CODE HERE #####
















 


#### PART 3 ####
# The University is complaining that the system that they used to retrieve information was broken and even the students' names are unformatted. They want to clean the data, and they are asking for your help. Reformat each list to have the first letter in the name & city capitalized (everything else lowercase), both letters in the state to be upper case.
# You can use your previous city & state variables to make this part easier!
# Ex: 
# Before modifying list mike = ['miKe', 'wAzOwSki', 3.4, 'MoNsTroPolIs', 'scareology']
# After modifying list student1 = ['Mike', 'Wazowski', 3.4, 'Monstropolis', 'scareology']

##### YOUR CODE HERE #####
''' Example for Mike is done for you :)
mike_fname = mike[0] # miKe
mike_lname = mike[1] # miKe
mike_fname = mike_fname[0].upper() + mike_fname[1:].lower() # Mike
mike_lname = mike_lname[0].upper() + mike_lname[1:].lower() # Mike
mike[0] = mike_fname # Set new variable in list at that index 0
mike[1] = mike_lname # Set new variable in list at that position 1
mike[3] = mike_city # Set new variable in list at that position 2
print(mike) # Prints the originally list modified: ['Mike', 'Wazowski', 3.4, 'Monstropolis', 'scareology']
'''



















#### PART 4 ####
# Let's try modifying the classes of each student's schedules contained in sets:
# 1) Add 'AP Scare', 'Movie Scare', & 'Geopolis' to Mike's classes
# 2) Remove 'Creative Writing' from Randalls's classes & add 'Scare Academy' to Randalls's classes
# 3) Remove 'Scare 101' from Jame's classes & add 'Forest Scare'

# For 1)-3), predict the length of each set after making these changes. Then, print out these sets along with their lengths with (for Mike's example): print(mike_classes, len(mike_classes))
# Was the elements in the set & their lengths what you expected to be printed after modifying them? Explain why your elements & length was printed this way. How is a set different from a list? (Write your answer as a comment below)

##### YOUR CODE HERE #####

















#### PART 5 ####
# Now that we have cleaned up our lists, we can print the output for the University. But Monsters University is strictly not admitting students who are interested in pursuing (majoring) laughter science, because they have limited capacity, and also students with lower than a 2.8 GPA. Therefore use conditions to filter out students who don't meet the requirements. The report will be a series of print statements that state:
# Accepted: StudentName from City is interested in studying MajorName with a GPA of higher than or equal to a 2.8, so he is admitted to Monsters University.
#
# OR 
#
# Rejected: StudentName from City is interested in studying MajorName, with a GPA of lower than or equal to a 2.8, so he does not meet the qualifications.
#
# For example, if we looked at the list student1, we would print:
# Accepted: Emma from San Jose, CA is interested in studying biology with a GPA of higher than or equal to a 3.0, so she is admitted to the University.

##### YOUR CODE HERE #####

''' Example for Mike is done for you :)
mike_major = mike[4]
mike_gpa = mike[2]
if (mike_major != 'laughter science' and mike_gpa >= 3.0):
  print("Accepted: " + mike_fname + " " + mike_lname + " from " + mike_city + ", " + " is interested in studying " + mike_major + " with a GPA of higher than or equal to a 2.8, so he is admitted to Monsters University.")
else: 
  print("Rejected: " + mike_fname + " " + mike_lname + " from " + mike_city + ", " + "is interested in studying" + mike_major + " with a GPA of lower than or equal to a 3.0, so he does not meet the qualifications.")
'''
