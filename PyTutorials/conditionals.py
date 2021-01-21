# Simply speaking, a conditional is a *block of code* when the program has to make a decision.
# It may also be thought of as when u come across a "True-or-False" statement and act according to the condition...

# Example:

#     /------------ Condition
#     v
if (x < 0):
    x = 0  # <------ Action taken w.r.t condition
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#  basically, conditionals help u in executing blocks of code having a structure like :: "IFTTT" or "IF This Then That"
