#numbers = [1,2,3,4,5,6,6,7,8,9,10]
#print(numbers)
#for k in  numbers:
#    print(k)



#friends = ["makarand","uday","shreyash","om sawant","pratham"]
#print(friends)
#for f in enumerate(friends):
#    print(f)

#for f in range(1,20,7):
#    print(f)



dict1 = {"name":"gajodhar","age":500,"adress":"dubai phata","marks":90,"education":"ITUS"}
#for j in dict1:
 #   print(j)

# for j in dict1.values():
#     print(j)
for j in dict1:
    #print(j)
    if j == "age" or j=="education":
       print(dict1[j])
    if j == "adress" or j=="name":
        print(dict1[j])   
else:
    print("completed")    
          