#question8
import copy
student_details = {101:'Judy', 102:'Victor', 103:'Sam'}
print(student_details)
replica = copy.copy(student_details)
replica.update({103:'Sally'})
print(replica)