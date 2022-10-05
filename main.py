# program : Calorie counter -- week 2
# programmer: Karim Boutine
# date : 10/04/2022
# purpose: the purpose of this program is to count calories


#input 
g_carbs = 16
g_fats = 3.5
g_proteins = 1
name = "Kind Bar"

#Process

total_cals = (g_carbs * 4) + (g_fats * 9) + (g_proteins * 4)



#output 
print("The total calories in a ", name ,"are", total_cals)

print("Total cals for {} are {}".format(name, total_cals))