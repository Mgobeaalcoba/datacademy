def palindrome(string):
    string = string.lower().replace(" ","")
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False 

def run():
    text = input("Ingrese la palabra o frase que desea comprobar si es palindromo: ")
    is_palindrome = palindrome(text)
    if is_palindrome == True:
        print("Su palabra o frase es un palindromo. Felicitaciones!!!")
    else:
        print("Su palabra o frase no es un palindromo. Vuelva a intentarlo.")

if __name__ == "__main__":
    run()