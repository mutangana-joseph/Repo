

marks=[20,30,40,10,]

lenght = len(marks)

search = int(input("Enter marks you want to find: "))

for i in range(lenght):
    if marks[i] != search:
        print(f"'{search}' not found.")       
    else:
        print(f"'{marks[i]}' found at postion {i}") 
        break
        
