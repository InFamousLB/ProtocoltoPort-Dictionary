#1

def addProtocol():
    y_or_n = input('Would you like to add a protocol to the dictionary? ')
    if y_or_n == 'yes':
        added_protocol = input('What protocol are you adding? \n').upper()
        added_portnumber = input(f'What is {added_protocol} port number? \n')
        dictionary_file.write(f'\n{added_protocol} {added_portnumber}')
        dictionary_file.flush()
    else:
        print('Understood')

while True:

    ProtocolsDict = {}
    dictionary_file = open(r"C:\Users\13216\Desktop\Completed Python Projects\Protocols_dict.txt", 'r+')
    for line in dictionary_file:
        key, value = line.split()
        ProtocolsDict[key] = value

    Protocol = input('what protocol would you like to know the name of: ').upper()

    if Protocol in ProtocolsDict.keys():
        port_number = ProtocolsDict[Protocol]
        print(f'The port number for {Protocol} is {port_number}')
    elif Protocol == 'EXIT':
        print ("Program terminated")
        dictionary_file.close()
        break
    elif Protocol == 'ADD':
        addProtocol()
    else:
        print(" That protocol isn't a part of the database")
        addProtocol()