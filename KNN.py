import matplotlib.pyplot as plt
import math

dataset=   [[5.0,2.0,"AB"],
            [4.0,2.5,"AB"],
            [1.8,5.3,"AB"],
            [6.0,3.5,"AB"],
            [8.0,4.5,"AB"],
            [1.5,3.5,"AB"],
            [6.0,4.0, "A"],
            [9.0,2.5, "A"],
            [1.0,6.0, "A"],
            [1.25,3.7,"A"],
            [2.25,4.7,"A"]]

xi = input("Enter X-Axis value: ")
yi = input("Enter Y-Axis value: ")

xi = float(xi)
yi = float(yi)

len_dataset=len(dataset)
#print(len_dataset)

dist_list=[]
i=0

#Euclidean distance
while(i<=len_dataset):
    d1=[ind for ind in dataset]
    #print(d1[0][0])
    dist=math.pow((d1[i][0]-xi),2)+math.pow((d1[i][1]-yi),2)
    dist_final=int(math.sqrt(dist))

    dist_list.append([dist_final,d1[i][2]])
    i=i+1

    if(i==len_dataset):
        break

#print(dist_list)
dist_list.sort()
print(dist_list)

i=1

for x in dist_list:
    x.append(i)
    i=i+1

print("\nDistance with Order and given Category values: \n")
print (dist_list)

k=3

print("\n3 Nearest Neighbours: \n")
print(dist_list[0:k])
print("\n")
i=0
count_ab=0
count_a=0

while(i<=k):
    print(dist_list[i][1])
    if(dist_list[i][1]=="AB"):
        count_ab +=1
    else:
        count_a +=1
        
    i=i+1
    if(i==k):
        break

print("\nFinal Output: ")

if(count_ab > count_a):
    print("For", xi, yi,"","Output is", "AB\n")
else:
    print("For", xi, yi,"","Output is", "A\n")

x1 = [5.0, 4.0, 1.8, 6.0, 8.0, 1.5,]
x2 = [6.0, 9.0, 1.0, 1.25, 2.25]
x3 = [xi]

y1 = [2.0, 2.5, 5.3, 3.5, 4.5, 3.5]
y2 = [4.0, 2.5, 6.0, 3.7, 4.7]
y3 = [yi]

plt.scatter(x1, y1, label="AB", color="green", marker= ".", s=50)
plt.scatter(x2, y2, label="A", color="blue", marker= ".", s=50)
plt.scatter(x3, y3, label="INPUT", color="red", marker= "*", s=50)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('KNN Graph!')
plt.show()