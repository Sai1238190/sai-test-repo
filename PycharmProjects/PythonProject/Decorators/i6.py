#decorator function
# def deco(func):
#     def wrapper(*args,**kwargs):
#         print(f"calling function...{func.__name__}")
#         print("_____________________________________")
#
#         return func(*args,**kwargs)
#     return wrapper
#
# @deco
# def even_num(num):
#     for num in range(1,num+1):
#         if num%2==0:
#          print(f"{num} is a even number")
#     else:
#         print(f"{num} is not a even number")
# even_num(7)



# def deco(func):
#     def wrapper(num):
#         num=num*2
#         return func(num)
#     return wrapper
#
# @deco
# def even(nums):
#     for num in range(2,nums+1):
#         if num%2==0:
#             print(f"{num} is a even number")
#
# even(10)
#
