print("Lista zakupów")
lista_zakupow = ["Chleb bezglutenowy", "Bułki" ,"Rogaliki","Kokosanki","Beza","Tort"]
shopping_dict = {
    "piekarnia" : ["Chleb bezglutenowy", "Bułki" ,"Rogaliki"],
    "cukiernia" : ["Kokosanki","Beza","Tort"]
}
for key , values in shopping_dict.items():
    print(f"Idę do {key.capitalize()}, kupuję tu : {values}" )
print(f"W sumie kupuje {len(lista_zakupów)} produktów. ")