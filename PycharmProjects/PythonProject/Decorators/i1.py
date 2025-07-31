def deco(func):
    def wrapper(*args,**kwargs):
        print("______________________")
        print(f"{func.__name__}")
        return func(*args,**kwargs)
    return wrapper

@deco
def appended_string(str1,str2):
    l=len(str1)//2
    str3=str1[0:2]+str2
    str4=str3+str1[l:]
    (print(str4))

appended_string("Sai","Teja")
@deco
def new_string(str1,str2):
    firstchar=str1[0]+str2[0]
    middlechar=str1[int(len(str1)/2):int(len(str1)/2+1)]+str2[int(len(str2)/2):int(len(str2)/2+1)]
    lastchar=str1[len(str1)-1]+str2[len(str2)-1]
    res=firstchar+middlechar+lastchar
    print(res)

new_string("saiteja","yaswanth")
@deco
def myfunc(str1):
    print("original string is ",str1)
    res=str1[0]
    l=len(str1)
    mi=int(l/2)
    res=res+str1[mi]
    res=res+str1[l-1]
    print(res)

myfunc("saiteja")

@deco
def count(str1):
    char_count = 0
    digit_count = 0
    symbols_count = 0
    for char in str1:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbols_count += 1

    print("chars=",char_count,"digits=",digit_count,"symbols=",symbols_count)
count("saiteja123456!@#$%^&")








