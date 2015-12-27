#Objective: To change all M's to m's and m's to M's

tex_file = open("in.txt", 'r+')       
new_tex_file = open("out.txt",'w+')

for line in tex_file:                     #increments through every line of file
 
    line = line.replace("M" , "!@#$")     #sets M as !@#$
    line = line.replace("m" , "M")        #changes m to M
    line = line.replace("!@#$" , "m")     #changes !@#$ to m 
    new_tex_file.write(line)

tex_file.close()
new_tex_file.close()
print ('Task Complete')
