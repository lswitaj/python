import random

messages = ('It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful')

print(messages[random.randint(0, len(messages) - 1)])

#it is tuple - (), you cannot change values in it

messages.remove('It it certain')