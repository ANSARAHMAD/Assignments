#Excersises
# print("Ch # 3")

# Q:1
#print("Q: 1")
# try:
#     hours = int(input("Enter Hours: "))
# except:
#     hours = -1
# if hours>0:
#     if hours <= 40:
#         pay = hours * 10
#     else:
#         x = hours - 40
#         pay = 40 * 10 + x * 15
#     print(pay)
# else:
#     print("Invalid Format")

# Q:2
#print("Q: 2")
# score = float(input("Enter Score: "))
# if score>=0.9:
#     print("A")
# elif score>=0.8:
#     print("B")
# elif score>=0.7:
#     print("C")
# elif score>=0.6:
#     print("D")
# elif score>=0.5:
#     print("E")
# elif score<0.4:
#     print("F")
# else:
#     print("Something went Wrong")

# Q:3
# # print("Q: 3")
# x = int(input("Enter a Digit: "))
# if x<10:
#     print("SMALLER")
# else:
#     print("Greater")

# Q:4
# print("Q: 4")
# x = 5
# if x==5:
#     print("Equals 5")
# if x>4:
#     print("Greater than 4")
# if x>=5:
#     print("Greater than or Equals 5")
# if x<=5:
#     print("Less than or Equals 5")
# if x!=6:
#     print("Not 6")


# Q:5
#print("Q: 5")
# x = 5
# if x>2:
#     print("Bigger than 2")
#     print("Still Bigger")
# print("Done with 2")
# for i in range(5):
#     print(i)
#     if i>2:
#         print("Bigger than 2")
#     print("Done with i")
# print("All Done")

# Q:6

# print("Q:6")

# astr = ("Hello Bob")
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print("First ",istr)
# astr = "123"
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print("Second ",istr)

# Q:7

# print("Q:7")
# x = int(input("Enter Value: "))
# if x<2:
#     print("Tiny")
# elif x<4:
#     print("Small")
# elif x<6:
#     print("Medium")
# elif x<8:
#     print("Big")
# elif x>=10:
#     print("Huge")

print("Ch # 4")

# print("Q:1")
# def thing():
#     print("Hello")
#     print("Fun")

# thing()
# print("2nd")
# thing()    

# print("Q:2")
# x = 5
# print("Hello")
# def lyrics():
#     print("I am Lumber Jack")
#     print("I sleep all Night and walk all day")
# print("40")
# lyrics()
# x= x+2
# print(x)

print("Q:3")

def add_two(a,b):
    added = a+b
    return added
x = add_two(4,7)
print(x)