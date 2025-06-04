contacts = {}
 
while True:
    print('1: Save Contact')
    print('2: exit')
    print('3: View contact')
    print('4: Update')
    print('5: Count contact')
    print('6: Delete contact')
    
    start = int(input('Enter a number: '))
    
    
    
    
    
    if start == 1:
        name = input('Enter a contact name: ')
        if name in contacts:
            print('User is already exit')
        else:
            age = int(input('Enter a age of user = '))
            phone_number = int(input('Enter the user phone number = '))
            contacts[name] = {age,phone_number}
            print('User is save successuflly')
            
            
    if start == 2:
        break         
            
            
    if start == 3:
        name = input('Enter contact name: ')        
        if name in contacts:
            contact = contacts[name]
            print(f' Name = {name} \n Age = {age} \n Phone number = {phone_number}')
        else:
            print('Contact is not found!')    
            
            
            
    elif start == 4:
        name = input('Enter contact name: ')
        if name in contacts:
            age = int(input('Enter a age of user = '))
            phone_number = int(input('Enter the user phone number = '))
            contacts[name] = {age,phone_number}
            print('Contact is updated')
        else:
            print('Contact is found')    
            
                
            
            
    elif start == 5:       
        print('Total contacts is: ') 
        print(len(contacts[name]))
        
        
       
    elif start == 6:
        name = input('Enter contact name: ')
        if name in contacts:
            del contacts[name]          
            print('Contact is deleted successuflly!')
        else:
            print('Contact is not found!')    
            
            
            
            
            
           