#this is the code for the expression which will determine the task priority
'''
This expression depends upon a few variables:
1- How much time until submission (date now - submission date)
2- Task importance: 
    (A)- Professional (project, )
    (B)- Personal:
        - Physical (i.e: working out ...) and mental/social state (i.e: talk to friends or family, spend time with them or meditate)
        - Personal life tasks (i.e: groceries, chores, doctor appointment)
        - Financial check-up
3- Task size (on a scale from 1 to 5)
'''


while True:
    initial = input('Welcome to Calender, what would you like to add (\'Task\' or \'Event\')?')
    #TASK------------------------------------------------
    if initial.lower() in ['task','t']:
        taskName = input('Please insert task name')

        #Days until submission----------------------------------------------------------------------------------------------
        import datetime
        from datetime import date

        def numOfDays(today, subd):
            return (subd-today)

        today = datetime.date.today()
        subds = input('Please insert the date of the last day in the format (yyyy-mm-dd):')
        subd = datetime.datetime.strptime(subds,"%Y-%m-%d").date()



        print((numOfDays(today, subd)), ' left until the submission date of ', taskName)

        '''
        #USER RATED IMPORTANCE----------------------------------------------------------------------------------------------
        taskImp = input ('What would you rate the importance of this task on a scale from 0 to 10?')

        if taskImp >
        '''

    #EVENT------------------------------------------------
    elif initial.lower() in ['event','e']:
        eventName = input('Please insert event name')
        
        #Days until submission----------------------------------------------------------------------------------------------
        import datetime
        from datetime import date

        today = datetime.date.today()
        subds = input('Please insert the date of the event in the format (yyyy-mm-dd):')
        subd = datetime.datetime.strptime(subds,"%Y-%m-%d").date()
        numOfDays = subd - today
        print(numOfDays, ' left until ', eventName)

    else:
       print ('Invalid input.')
    
    last = input ('Would you like to add anything else? type \'yes\' or \'no\'')

    if last.lower() in ['n','no']:
        print('Goodbye! and don\'t forget to smile:)')
        break

    elif last.lower() in ['y','yes']:
        continue

    else:
       print ('Invalid input.')
       break
    




#------------------------------------------------------------------------------------------------------------

