age = int(input("Entrez l'age"))
annee_permis = int(input("Entrez le nombre d'années de permis"))
accidents = int(input("Entrez le nombre d'accidents"))
annee_assurance = int(input("Entrez le nombre d'années d'assurance:"))

if (not age >= 25 and not annee_permis >= 2):
    if (accidents == 0):
        status = "Rouge"
    else:
        status = "Refusé"
elif ((not age >= 25 and annee_permis >= 2) or (age >= 25 and not annee_permis >= 2)):
    if (accidents == 0):
        status = "Orange"
    elif (accidents == 1):
        status = "Rouge"
    else:
        status = "Refusé"
else:
    if (accidents == 0):
        status = "Vert"
    elif (accidents == 1):
        status = "Orange"
    elif (accidents == 2):
        status = "Rouge"
    else:
        status = "Refusé"

if(annee_assurance >= 5):
     if (status == "Rouge"):
         status = "Orange"
     elif (status == "Orange"):
         status = "Vert"
     elif (status == "Vert"):
         status = "Bleu"

print("Votre situation est ", status)