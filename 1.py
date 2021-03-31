from random import randint

print("Задание-1")

def rev_Num():
    num = int(input("Введите ваше число от 100 до 1000 : "  ))
    if num > 100 and num < 1000:
        lastNum = num % 10
        secondNum = num // 10
        secondNum_2 = secondNum % 10
        firstNum = secondNum // 10
        return lastNum * 100 + secondNum_2 * 10 + firstNum    
    else:
        return "incorrect number, try again"

mynum = rev_Num()
print(mynum)

print("----------------------------------------------------------")



print("Задание-2")

num_len = int(input(" Input please length of the list : "))
lst = []
for i in range(num_len):
    r_num = randint(0, 10)
    lst.append(r_num)


new_lst = list(map(lambda x: x ** 2, lst))

if __name__ == '__main__':
    print(lst)
    print(new_lst)
