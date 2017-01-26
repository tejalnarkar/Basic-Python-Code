@@ -0,0 +1,29 @@
#Display odd numbers between 0 to 9

for x in range(10):
    if (x%2==0):
        print x,
        

# Create list of numbers and display sum of all items
y=[1,2,3]
sum=0
for i in y:
    sum=sum+i
print "Sum of all elements in the list is "+str(sum)    
print y          
                        
# Create data dictionary with student name and student score 
studentScore={}
studentScore["StudentA"]=56
studentScore["StudentB"]=39
studentScore["StudentC"]=98

print studentScore["StudentA"]  


# Create a function
def CalSum(a,b):
    return a+b

print CalSum(2,3)
\ No newline at end of file
