#Objective: To change a-z's to A-Z's and A-Z's to a-z's

tex_file = open("KLSadd.tex", 'r+')       
new_tex_file = open("KLSadd_Caps_Reverse.tex",'w+')

for line in tex_file:              #increments through every line of file
    new_string = ''
    for letter in line:            #increments through every letter of line
        if (letter.isupper()):
            letter = letter.lower()
        elif (letter.islower()):
            letter = letter.upper()
        new_string += letter
    new_tex_file.write(new_string)

 
tex_file.close()
new_tex_file.close()
print ('Task Complete')


