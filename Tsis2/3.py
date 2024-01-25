friends ={"Tolegen","Sultanbek","Merey","Wibi"}
if "Merey" in friends:
    print("Merey is my friend!")

friends.add("Sergey")
print(set(friends))

new_friends=["Abzal","Oljaz","Amina"]
friends.update(new_friends)
friends.remove("Abzal")
friends.discard("Oljaz")
print(set(friends))

Merey = {
    "age": "17",
    "hobby": "reading",
    "live": "there"
}
print(Merey.get("age"))
Merey["hobby"]="listen music"
Merey["hair"]="curley"
Merey.pop("age")
print(Merey)
Merey.clear()
