friend=["jim","karen","kelly"]
def print_array():
    for listfriend in friend:
        print(listfriend)

def print_range():
    for index in range(len(friend)):
        print(friend[index])
        
def print_change_first():
    print("begore loop")
    print(friend)
    for index in range(len(friend)):
        if(index==1):
            print("after insert element")
            friend.insert(0,"yoon")
            print(friend)
            
def print_channge_choose_index(input_index, name_friend):
    print("begore loop")
    print(friend)
    for index in range(len(friend)):
        if(index==1):
            print("after input")
            friend.insert(input_index,name_friend)
            print(friend)
name=input("input the new name: ")
the_index_number=input("input the element number: ")
print(print_channge_choose_index(int(the_index_number),name))

    