string1 = "I love scp:sl!"
'''print(string1[3:])'''
#spilt 
'''print(string1.spilt())'''
#Length
'''print(len(string1))'''
#find
'''print(string1.find("l"))'''

'''string1 = "I love sp sl"
result = string1.split()
print(result)'''
#Challenge
'''input_string = input("Enter a string ")
words = input_string.split()
word_count = len(words)
print(word_count)'''
#Challenge 2
user_input = input("Enter a string: ")
first_g_index = user_input.find('g')
second_g_index = user_input.find('g', first_g_index + 1)
print(second_g_index)