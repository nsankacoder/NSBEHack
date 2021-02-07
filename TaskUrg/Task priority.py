#this is the code for the expression which will determine the task priority
'''
This expression depends upon a few variables:
1- How much time until submission (date now - submission date)
2- Task importance: (scale from 1-10)
    (A)- Professional (project, etc.)
    (B)- Personal:
        - Physical (i.e: working out ...) and mental/social state (i.e: talk to friends or family, spend time with them or meditate)
        - Personal life tasks (i.e: groceries, chores, doctor appointment)
        - Financial check-up
3- Task size (in hours)
'''
myfile = open('C:/Users/anism/OneDrive/Desktop/PL-/Learn/Hackathon/Project/TaskUrg/data.txt', 'r+')

while True:
    #Days until submission----------------------------------------------------------------------------------------------
    import datetime
    from datetime import date, datetime

    def numOfDays(today, subd):
        return (subd-today)
    try:
        now = datetime.now()
        todays = now.strftime("%Y-%m-%d, %H:%M")
        today = datetime.strptime(todays,"%Y-%m-%d, %H:%M")
        subds = input('\nPlease insert the date of the event or submission deadline in the format (yyyy-mm-dd, HH:MM):')
        subd = datetime.strptime(subds,"%Y-%m-%d, %H:%M")

        string = str(numOfDays(today, subd))
            
        days = 0
        hour = 0
        minutes = 0

        myfile.write('\n\nNew addition for: '+subds+'\n')
        myfile.write('    '+string+' left at the time of mark-up.\n')
        
        try:
            #IF more than 0 days---------------------------------------------------------------------------------------
            findd = string.index('d')
            finddi = int(findd)
            fdi = finddi - 1
            days = int(string[0:fdi])
    
            findcoma = string.index(',')
            findcomai = int(findcoma)
            findcol = string.index(':')
            findcoli = int(findcol)
            fh = findcoli - 2
            hour = int(string[fh:findcoli])

        except:
            #IF 0 days-----------------------------------------------------------------------------------------------
            test3 = string[1]
            test2 = string[2]

            if test3 or test2 in [':']:
                days = 0
                if test3 in [':']:
                    hour = int(string[0])
                    minutes = int(string[2:4])
                if test2 in [':']:
                    hour = int(string[0:2])
                    minutes = int(string[3:5])

        hours = hour + (minutes/60)
        timeLeft = (days*24) + hours


    except:
        print('Invalid input.')
        continue

    initial = input('\nWhat would you like to add? (\'Task\' or \'Event\')')
    #TASK------------------------------------------------
    if initial.lower() in ['task','t']:
        taskName = input('Please insert task name:')
        myfile.write('    Task name: '+taskName+'\n')

        class Task:
            def __init__ (self, name, timeLeft, taskImp, taskSize):
                self.name = taskName
                self.timeLeft = timeLeft
                self.taskImp = taskImp
                self.taskSize = taskSize
            def urgency(timeLeft, taskImp, taskSize):
                urgencyRating = (timeLeft/taskSize)/taskImp

                return urgencyRating
        print(numOfDays(today, subd), 'left until the deadline for', taskName)
                
        #USER RATED IMPORTANCE----------------------------------------------------------------------------------------------
        taskImps = input ('\nWhat would you rate the importance (not urgency) of this task on a scale from 0 to 10? (10 being the most important or holds the most value)')
        taskImp = int(taskImps)

        if taskImp>10 or taskImp<0:
            print('Invalid input.')
            continue
        elif taskImp>=0 and taskImp<=3: 
            print('This task is not important.')
        elif taskImp>=4 and taskImp<=8: 
            print('This task is relevent.')
        elif taskImp>=8 and taskImp<=9: 
            print('This task is very important.')
        elif taskImp==10:
            print('This task is must-do!')
        
        #TASK SIZE-----------------------------------------------------------------------------------------------------------
        taskSizes = input ('\nHow much time does this task take to complete? Please enter the number of hours expected to finish this task: ')
        taskSize = float(taskSizes)

        #Urgency and placing------------------------------------------------------------------------------------------------
        s = Task.urgency(timeLeft,taskSize,taskImp)
        print(taskName, 'has an Importance Level of: %.2f'%s, '.')


    #EVENT------------------------------------------------
    elif initial.lower() in ['event','e']:
        eventName = input('Please insert event name:')

        myfile.write('    Event name: '+eventName+'\n')

        print(numOfDays(today, subd), 'left until the time for', eventName, '.')

    else:
        print ('Invalid input.')
        continue
    last = input ('\nWould you like to add anything else? type \'yes\' or \'no\'')

    if last.lower() in ['n','no']:
        print('Goodbye! and don\'t forget to smile:)')
        myfile.close()
        print('\n The data has been saved to the file.') #saved confirmation
        break

    elif last.lower() in ['y','yes']:
        continue

    else:
       print ('Invalid input.')
       break
#END.

