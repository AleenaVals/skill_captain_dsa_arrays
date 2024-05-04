str_input = input("Enter the string : ")
str_list = list(str_input)

left = 0
right = len(str_list)-1
vowels = 'aeiouAEIOU'

while left <  right :
    if str_list[left] in vowels and str_list[right] in vowels :
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left= left+1
        right = right -1

    elif str_list[left] not in vowels:
            left =  left +1
    elif str_list[right] not in vowels:
         right = right- 1

reversed_string = "".join(str_list)
print(reversed_string)