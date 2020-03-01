
def disemvowel(string):
    sesli = ["a","e","ı","i","o","u"]
    for i in range(len(sesli)):     
        if sesli[i] in string or sesli[i].upper() in string: 
            string=string.replace(sesli[i],"");string=string.replace(sesli[i].upper(),"")
    return string
print(disemvowel("This website is for losers LOL!"))




"""string = "This website is for losers LOL!"
print("string :" +str(len(string)))
sesli = ["a","e","ı","i","o","u"]
print("string :" +str(len(sesli)))
print(len(string)-1)
print(len(sesli)-1)"""




"""def disemvowel():
    string = "This website is for losers LOL!"
    sesli = ["a","e","ı","i","o","u ]
    i = len(string)-1
    while(i>-1):
        j=len(sesli)-1
        while(j>-1):      
            if sesli[i] == string[i]:
                string[i]=""
            else:
                j=j-1
    i=i-1
    return string"""

