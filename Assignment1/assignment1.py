
def DictionaryDemo():
    n= int(input("Enter no. of values you wanted to insert into dictionary : "))
    d = {}
    for i in range(n):
        print("Enter key values seperated by space")
        text = input().split()
        d[text[0]] = text[1]
    print(d)


def ListDemo():
    
    while True:
        print("Enter your choice : \n 1. Interger List  \n 2. String List \n 3. Exit")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            list_input = input("Enter Integer List: ")
            make_list = [int(x) for x in list_input.split()]
            print(make_list)
            continue      
        elif choice == 2:
            list_input = input("Enter Mixed List: ")
            make_list = [(x) for x in list_input.split()]
            print(make_list)
            
                
        else:
            break    

def SetDemo():
    while True:
        print("Enter your choice : \n 1. Interger set  \n 2. String set \n 3. Exit")        
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            set_input = input("Enter Integer set: ")
            make_set = {int(x) for x in  set_input.split()}
            print(make_set)
            continue      
        elif choice == 2:
            set_input = input("Enter Mixed set: ")
            make_set  = {(x) for x in  set_input.split()}
            print(make_set)
            
                
        else:
            break    


def main():
    
    while True:
        print("\n -------Menu---------- \n 1. Converting user input into list \n 2. Converting user input into Dictionary \n 3. Converting user input into Set \n 4. Exit")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            ListDemo()
        elif choice == 2:
            DictionaryDemo()
        elif choice == 3:
            SetDemo()
        else:
            break


print("---------- WELCOME TO ASSIGNMENT1 -------------")
main()



# -------OUTPUT-----------
'''

---------- WELCOME TO ASSIGNMENT1 -------------

 -------Menu----------
 1. Converting user input into list
 2. Converting user input into Dictionary
 3. Converting user input into Set
 4. Exit
Enter your choice
1
Enter your choice :
 1. Interger List
 2. String List
 3. Exit
Enter your choice
1
Enter Integer List: 3 4 5 6
[3, 4, 5, 6]
Enter your choice :
 1. Interger List
 2. String List
 3. Exit
Enter your choice
2
Enter Mixed List: sonal pooja 2 3 4
['sonal', 'pooja', '2', '3', '4']
Enter your choice :
 1. Interger List
 2. String List
 3. Exit
Enter your choice
3

 -------Menu----------
 1. Converting user input into list
 2. Converting user input into Dictionary
 3. Converting user input into Set
 4. Exit
Enter your choice
2
Enter no. of values you wanted to insert into dictionary : 3
Enter key values seperated by space
sonal 45
Enter key values seperated by space
pooja 97
Enter key values seperated by space
neha 78
{'sonal': '45', 'pooja': '97', 'neha': '78'}

 -------Menu----------
 1. Converting user input into list
 2. Converting user input into Dictionary
 3. Converting user input into Set
 4. Exit
Enter your choice
3
Enter your choice :
 1. Interger set
 2. String set
 3. Exit
Enter your choice
1
Enter Integer set: 4 5 6 7
{4, 5, 6, 7}
Enter your choice :
 1. Interger set
 2. String set
 3. Exit
Enter your choice
2
Enter Mixed set: monday tue 34 56
{'56', 'tue', '34', 'monday'}
Enter your choice :
 1. Interger set
 2. String set
 3. Exit
Enter your choice
3

 -------Menu----------
 1. Converting user input into list
 2. Converting user input into Dictionary
 3. Converting user input into Set
 4. Exit
Enter your choice
4
'''
  








