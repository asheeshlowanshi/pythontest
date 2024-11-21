#patterns 4


for i in range(1,6):
 for j in range(1,6):
  print("*",str("j",::-1))
  j-=1
 print("k")

 print()
 
''' floyd's triangle
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
''' 
'''def print_reverse_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of lines: "))
    print_reverse_number_pattern(n)'''
