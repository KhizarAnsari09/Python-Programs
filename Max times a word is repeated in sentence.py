'''

Create 2 functions.
Function 1 - takes a string as input and returns a dictionary containing word:occurence as key:value pairs.
Function 2 - takes a string as input and finds the word having maximum no. of occurrences. Use function 1 here.

​

​

Input 1 - Good morning Good evening
Output 1 - Good
Input 2 - Hello Bye Hi TCS Hello Xplore Hello Bye
Output 2 - Hello

​
'''

def fn1(str1):
    
    d = {}
    h = list(str1.split())
    
    for i in h:
        d.update({i:h.count(i)})
    
    return d
        
def fn2():
    
    d = {}
    d = fn1(str1)
    
    for k,v in d.items():
        if(v == max(d.values())):
            print(k)

        
if __name__ == '__main__':
    
    str1 = input("Provide the string: ")
    fn2()