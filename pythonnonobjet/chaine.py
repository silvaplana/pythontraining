
################################################
# exo : chaine
################################################
print("============== exo : chaine ================")



# remplacer tiret par diese:
print("\nremplacer tiret par diese:")
str2="IL-etait-une-fois"
print("str de depart", str2)
liste = str2.split("-")
str2 = "#".join(liste)


print("str de fin", str2)

    

# 5.6544444444  -> 5,65
# attention avant: convertir le float en str
#

fl = 5.65283665
frStr = str(fl)
print(frStr)
liste2 = frStr.split(".")
goalStr=f"{liste2[0]},{liste2[1][:2]}"
print(goalStr)

