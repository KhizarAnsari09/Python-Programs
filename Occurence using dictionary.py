def func1(n):
    lst1 = n.split()
    for i in lst1:
        u = lst1.count(i)
        dict1.update({i:u})
        print(dict1)

def func2(dict1):
    v = 0
    s = ""
    for item,value in dict1.items():
        if(v<int(value)):
            v = value
            s = item
    print(f"'{s}' occured {v} times.")
    
    
if __name__ == "__main__":
    dict1 = {}
    n = input("Provide the string: ")
    func1(n)
    func2(dict1)

#the .fromkeys() is like .split() or .list() function for making dictionary
#.fromkeys(key,value)
#refer link "https://www.programiz.com/python-programming/methods/dictionary/fromkeys"
#.get() isme key dalke value nikal sakta hai not vice versa