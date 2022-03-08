#!/usr/bin/env python3
message = 'Your grade is '
score = float(input( 'What is your test score? '))
if 90<=score<=100:
    message = message + 'A, excellent!'
elif 80<=score<90:
    message = message + 'B, you can do better!'
elif score >= 70:
    message = message + 'C, you need to study more!'
elif score >= 60:
    message = message + 'D,'
elif score >= 0:
    message = message + 'F, you can a least get a C if you show up more often'
else:
    message = message + 'Verify your test score'
print(message)
