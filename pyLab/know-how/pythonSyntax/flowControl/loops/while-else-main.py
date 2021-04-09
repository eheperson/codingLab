#
# 
# Using else Statement with While Loop
# Python supports to have an else statement associated with a loop statement.

# If the else statement is used with a while loop, 
# the else statement is executed when the condition becomes false.

# The following example illustrates the combination of an else statement 
# with a while statement that prints a number as long as it is less than 5, 
# otherwise else statement gets executed.
#
#
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")