'''

GIVEN some strings in that we need to print the strings which doesn't contain vowels in it

'''


def fn(l1):
    
    not_vowel = []
    for word in l1:
        count = 0
        for alphabet in word:
            if(alphabet in 'aeiou'):
                count = count + 1
        if(count == 0):
            not_vowel.append(word)
    
    print(*not_vowel) #Another way to print every element in list on a single line usually every element gets printed in a new line
    
    
if __name__ == '__main__':
    
    n = int(input())
    l1 = []
    for i in range(n):
        l1.append(input())
    
    print("\n")
    fn(l1)
    