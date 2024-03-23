usuarios = [
    ["Chanchito", 4],
    ["Felipe", 3],
    ["Pulga", 5]
]

# nombres = []
# for usuarios in usuarios:
#   nombres.append(usuarios[0])
#  print(nombres)
# nombres = [usuario[0] for usuario in usuarios]

# Filtrar
nombres = [usuarios for usuarios in usuarios if usuarios[1] > 2]
print(nombres)
