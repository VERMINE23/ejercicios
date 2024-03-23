def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    return palabra == palabra[::-1]


print("anuel", es_palindromo("anuel"))
print("reconocer", es_palindromo("reconocer"))
print("amo la paloma", es_palindromo("amo la paloma"))
print("una cagoma lo paló", es_palindromo("una cagoma lo paló"))
