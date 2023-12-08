list1=[1,2,3,4,5,6,7,8,9]

def add():
    element=input('Do you want to add a Single element or Multiple elements: ')
    if(element=='Single' or element=='single'):
        elem1=input('Enter Element: ')
        elem2=int(elem1)
        list1.append(elem2)
        print(list1)
    elif(element=="Multiple" or element=='multiple'):
        howmele=int(input('How many elements: '))
        for i in range(howmele):
            mulelement=input('Enter element: ')
            mulelement2=int(mulelement)
            list1.append(mulelement2)
        print(list1)
    else:
        print('Pick either Single or Multiple ')
            
def update():
    updatinput=input('Would you like to update values ,By Index or By Value: ')
    if(updatinput=='Index' or updatinput=='index'):
        updatindex=int(input('Enter index value: '))
        updateindexnew=int(input('Enter new value: '))
        list1.pop(updatindex)
        list1.insert(updatindex,updateindexnew)
    elif(updatinput=="Value" or updatinput=='value'):
        updatvalue=input('Enter value: ')
        updatvalue2=int(updatvalue)
        updatnewvalue=int(input('Enter new value: '))
        for i in range(0,len(list1)):
            if(i==updatvalue2):
                i=i-1
                list1.pop(i)
                list1.insert(i,updatnewvalue)
    else:
        print('Pick either Index or Value')
        
def display():
    displayorder=input('In which order would you like to display the list , In Ascending Or In Descending: ')
    if(displayorder=='Ascending' or displayorder=='ascending'):
        list1.sort()
        print(list1)
    elif(displayorder=='Descending' or displayorder=='descending'):
        list1.sort(reverse=True)
        print(list1)
    else:
        print('Pick either Ascending Or Descending')

def delete():
    deletemethod=input('How would you like to delete a value ,By Index Or By Value: ')
    if(deletemethod=='Index' or deletemethod=='index'):
        delindexvalue=int(input('Enter index value: '))
        list1.pop(delindexvalue)
        print(list1)
        
    elif(deletemethod=='Value' or deletemethod=='value'):
        delvalue=int(input('Enter the value to be deleted '))
        for i in range(0,len(list1)):
            if(i==delvalue):
                list1.pop(i-1)
                print(list1)
    else:
        print('Pick either Index Or Value')

def final():
    listmanipulation=int(input('How would you like to manipulate the given list \n1)Add  \n2)Update \n3)Display \n4)Delete  \n5)Exit \n'))
    print(list1)
    if(listmanipulation==1):
        add()
        final()
    elif(listmanipulation==2):
        update()
        final()
    elif(listmanipulation==3):
        display()
        final()
    elif(listmanipulation==4):
        delete()
        final()
    elif(listmanipulation==5):
        print( 'Final List=',list1,"\n"'Successfully exited''\n''Program complete'  )

final()









        
        
        
        
