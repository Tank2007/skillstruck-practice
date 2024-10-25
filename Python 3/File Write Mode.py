'''file = open("Doc.txt", "w")
file.write("In short, I love to code!")
file.close()
open("porcupine.txt", "w")'''

'''file = open("Email.txt", "w")
file.write("Never mind")
file.close()'''


answer = input("")
file = open ("report.txt", "w")
file.write(answer)
print(file.read())