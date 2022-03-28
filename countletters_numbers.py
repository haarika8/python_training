 
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
string = str(input("Enter a String ")) 

tot_num = 0
tot_let = 0
 
for s in string:
 
    
    if s in num:
        tot_num += 1
 
    
    elif s in let:
        tot_let += 1

print("Letters : ", tot_let)
print("Numbers : ", tot_num) 