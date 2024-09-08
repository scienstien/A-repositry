print("\nHello, Welcome to Apollo Hospitals help index")

admitted_persons = { 
    "jackob" :['henry', 'robin'] ,
    'sarah' : ['tony', 'peter'] ,
    "jean" : ['odinson', 'ben'] ,
    "juby" : ['bruce', 'steve']
}

condition_dict = {
    'jackob' : 'Good',
    'jean' : 'critical',
    'sarah' : 'stable' ,
    'juby' : 'dead', 
}
room_dict = {
    'jackob' : '312',
    'jean' : '313',
    'jason' : '314' ,
    'juby' : '315',
}
inquiry = input("\nDo you want to know inquire about a patient: ")
if inquiry.lower() == "yes" :
    target_patient = input("Which patient do you want to know about? ")
    patient_name = target_patient.lower()# to standardize the input from users
    
    if patient_name in admitted_persons.keys() :
        print("Lemme check if this patient is registered in our database......Ahh! found it..")



        inquirer_name = input('May, I know your name? ')
        family_member = inquirer_name.lower()
        #for copying the values of a list of a key nested in dictionary you need to keep dictionary name, key name in bracket, and 
            # the usual value copy
        if family_member in admitted_persons[patient_name][:] : 

            print(f"Hey {inquirer_name}, your patient {patient_name} is in room :")
            room = room_dict[patient_name]
            print("\t" + room)
            condition = condition_dict[patient_name]
            if condition == 'dead' :
                print('Sorry we could not save him')
            else :
                print(f"His vcondition is {condition_dict[patient_name]}")
        else :
            print("Sorry you are not registered as his family member, we cannot disclose patient info to you")
    else :
         print("Lemme check if this patient is registered in our database...... sorry could not find such a patient in our data base")


 


