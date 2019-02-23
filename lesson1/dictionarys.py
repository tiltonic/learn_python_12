d = {"city": "Москва", "temperature": "20"}
print(d.get("city"))
t = d.get("temperature")
print(t)
t = str(int(t) - 5)
print(t)

d["temperature"] = str(int(d.get("temperature")) - 5)

print(d)


d.get("country", "Россия")
d["date"] = "27.05.2019"

print(d)
