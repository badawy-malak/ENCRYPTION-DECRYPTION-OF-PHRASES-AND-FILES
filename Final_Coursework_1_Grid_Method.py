#Name:Malak Abdelrahman Ahmed samir anwar Hassan Ibrahim Badawy
#TKH ID: 20210278

import random
import string
def Generating_Random_keys (Number_of_characters_in_key): #Generating a random key
    characters_of_random_key = string.ascii_letters + string.digits + string.punctuation   #Including all characters and numbers
    Key_Random = ''.join(random.choice(characters_of_random_key) for i in range(len(Number_of_characters_in_key))) 
    print("Random Key is:", Key_Random)
    return (Key_Random)

def create_first_row(): #Creating the main rown in the grid
    characters ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .~`!@#$%^&*()_+-=\|}]{[:;?/><''\n"   #Characters available in the grid
    first_row = []
    for c in characters:
        first_row.append(c)         #Appending each character to match the original vignere cipher grid
    return first_row

def create_grid(first_row): #Creating the grid
    grid =[]                                 #Assigning the grid as a list
    for i in range (len(first_row)):
      new_row = first_row[i:] +first_row[:i] 
      grid.append(new_row)
    return grid

def create_index_dictionary(first_row): #Creating the index
    index_dict = {}
    index = 0
    for c in first_row:
        index_dict[c] = index 
        index +=1
    return index_dict

def convert_string_list(string): #Converting string (phrase) to a list
    list_of_characters =[]       #Assigning list of characters as a list
    for c in string:
        list_of_characters.append(c)
    return list_of_characters

def convert_string_list_for_file(cipher_text): #Converting string (file) to a list
    list_of_characters_for_file =[]   #Assigning list of characters for file to a list
    for c in cipher_text:
        list_of_characters_for_file.append(c)
    return list_of_characters_for_file

def encrypt_phrase (key,plain_text,grid,index_dict): #Encryption of a phrase
    key_list = convert_string_list(key)                #Converting the key into a list
    plain_text_list = convert_string_list(plain_text)  #Converting the plain text inputted into a list
    cipher_text_list=[]                                #Assigning cipher_text_list as a list
    index = 0                                          #Initializing the index with a zero
    for t in plain_text_list:           #conjunction between the letter of the original text and the key corresponding it
        row_index = index_dict[t]                      
        col_index = index_dict[key_list[index] ]        

        cipher_text_list.append(grid[row_index][col_index])  #Assembling the cipher text
        index +=1
        if index == len(key_list):
            index = 0
    return "".join(cipher_text_list)

def encrypt_file (key,grid,index_dict,name_of_file): #Encryption of a file
    key_list = convert_string_list(key)              #converting the key into a list
    file_to_encrypt = open(name_of_file, 'r')        #opening the file to read it's content
    string_in_file_list = convert_string_list(file_to_encrypt.read())   #converting the string in the file to a list
    cipher_text_list=[]                               #Assigning chiper_text_list as a list
    index = 0
    for t in string_in_file_list:         #conjunction between the letter of the original text and the key corresponding it
        row_index = index_dict[t]       
        col_index = index_dict[key_list[index] ]
        cipher_text_list.append(grid[row_index][col_index]) #Assembling the cipher text
        index +=1
        if index == len(key_list):
            index = 0
    return "".join(cipher_text_list)


def decrypt_phrase (key, cipher_text, grid, index_dict): #decryption of a phrase
    key_list = convert_string_list(key)                  #Converting key into a list
    cipher_text_list = convert_string_list(cipher_text)  #Converting the cipher text into a list
    plain_text_list = []                                 #Assigning plain_text_list as a list
    index = 0
    for c in cipher_text_list:          #conjunction between the letter of the original text and the key corresponding it
        k = key_list[index]
        k_index = index_dict[k]
        row = grid[k_index]
        plain_text_index = row.index(c)
        plain_text_character = grid[0][plain_text_index]
        plain_text_list.append(plain_text_character)    #Assembling the plain text


        index +=1
        if index == len(key_list):
            index = 0 
    return "".join(plain_text_list)
def decrypt_file(key,grid,index_dict,name_of_file_decryption): #decryption of a file
    key_list = convert_string_list(key)                        #Converting the key into a list
    file_to_decrypt = open(name_of_file_decryption,'r')        #Open the file to read cipher
    cipher_in_file_list = convert_string_list(file_to_decrypt.read())  #Reading the file
    plain_text_list = []                                        #Assigning plain_text_list as a list
    index = 0
    for c in cipher_in_file_list:        #conjunction between the letter of the original text and the key corresponding it
        k = key_list[index]
        k_index = index_dict[k]
        row = grid[k_index]
        plain_text_index = row.index(c)
        plain_text_character = grid[0][plain_text_index]
        plain_text_list.append(plain_text_character)


        index +=1
        if index == len(key_list):
            index = 0 
    return "".join(plain_text_list)

def main():  #Main function
    if __name__ == "__main__":
      first_row = create_first_row()
      grid = create_grid(first_row)
      index_dict = create_index_dictionary(first_row)
      status = input("Hello, if you want to start the program please type 'start' if not type 'stop'  ") #Initialzing the program
      while status == 'start':
          Command = input("Enter 'encrypt' if you want to encrypt and 'decrypt' if you want to decrypt    : ") #Choosing the process type
          if Command =='encrypt':
              Type_of_processing = input("Enter 'text' if you want to encrypt a phrase, and 'file' is you want to encrypt a file: ")  #Choosing what to do the process on
              if Type_of_processing =='text':
                 key_type = input("If you want to use your own key type'specific key',if you want to use a random key type'random key ")  #Choosing type of key
                 if key_type == 'random key':
                  Number_of_characters_in_key = input("Please enter an example of the key you want in the autokey:   ") #Entering an example of the key you want to generate
                  key_string = Generating_Random_keys(Number_of_characters_in_key)
                  plain_text_string = input("Enter plain text: ")  #Inputting text to encrypt
                  cipher_text = encrypt_phrase (key_string,plain_text_string,grid,index_dict)  #encrypting text
                  print("cipher text: '" , cipher_text,"'")
                  status = input("If you want to continue using the program please type 'start' if not type 'stop'  ") #Continuity of program
                 elif key_type == 'specific key':
                  key_string = input("Enter key: ")   #Inputting key
                  plain_text_string = input("Enter plain text: ")  #inputting text to encrypt
                  cipher_text = encrypt_phrase(key_string,plain_text_string,grid,index_dict)  #encrypting text
                  print("cipher text: '" , cipher_text,"'")
                  status = input("If you want to continue using the program please type 'start' if not type 'stop'  ") #Continuity of program

              elif Type_of_processing == 'file':
                  key_type = input("If you want to use your own key type'specific key',if you want to use a random key type'random key ") #Inputting the type of key
                  if key_type == 'random key':
                      Number_of_characters_in_key = input("Please enter an example of the key you want in the autokey:   ") #Entering an example of the key you want to generate
                      key_string = Generating_Random_keys(Number_of_characters_in_key)
                      name_of_file = input("Please enter the path of the file to encrypt ") #Inputting file path
                      file_to_encrypt = open  (name_of_file, 'r')   #opening file to read data
                      cipher_text = encrypt_file(key_string,grid,index_dict,name_of_file)  #encrypting text
                      print("cipher text: '" , cipher_text,"'")
                      with open('cipher2.txt','w') as f:  #opening file to write
                          f.write(str(cipher_text))  #writing in file
                      print("The cipher was saved to a file called cipher2.txt")
                      status = input("If you want to continue using the program please type 'start' if not type 'stop'  ") #Continuity of program
                  elif key_type == 'specific key':
                      key_string = input("Enter key   : ") #Inputting the key
                      name_of_file = input("Please enter the path of the file to encrypt ") #Inputting the file path
                      file_to_encrypt = open  (name_of_file, 'r')  #opening file to read
                      cipher_text = encrypt_file(key_string,grid,index_dict,name_of_file) #encrypting text
                      print("cipher text: '" , cipher_text,"'")
                      with open('cipher2.txt','w') as f: #opening file to write cipher
                          f.write(str(cipher_text))  #writing cipher  in file
                      print("The cipher was saved to a file called cipher2.txt")
                      status = input("If you want to continue using the program please type 'start' if not type 'stop'  ") #Continuity of program
          elif Command == 'decrypt':
              Type_of_processing = input("Enter 'text' if you want to decrypt a phrase, and 'file' is you want to decrypt a file: ") #Choosing what to do the process on 
              if Type_of_processing =='text':
                  key_String = input("Enter the key: ")  #Inputting the key
                  cipher_text_string = input("Enter cipher text: ") #Inputting cipher text
                  plain_text = decrypt_phrase(key_string,cipher_text_string,grid,index_dict)  #decrypting text
                  print("plaintext: '" ,plain_text,"'")
                  status = input("If you want to continue using the program please type 'start' if not type 'stop'  ") #Continuity of program
              elif Type_of_processing == 'file':
                  key_string = input("Enter the key: ") #Inputting key
                  path_of_file_decryption = input("Please enter the path of the file to decrypt ")  #Inputting filepath 
                  file_to_encrypt = open(path_of_file_decryption, 'r+') #Opening file to read cipher
                  plain_text_decryption = decrypt_file(key_string,grid,index_dict,path_of_file_decryption)  #decrypting cipher
                  print("Plain text: '" , plain_text_decryption,"'")
                  with open('Plain.txt','w') as f:      #opening file to write 
                     f.write(str(plain_text_decryption)) #writing plain text to file
                  print("The plain text was saved to a file called Plain.txt")
                  status = input("If you want to continue using the program please type 'start' if not type 'stop'  ")   #Continuity of program         
main()


                


        
