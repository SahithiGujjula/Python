def Old_MacDonald(string):
    if len(string)>3:
        print(string[:3].capitalize()+string[3:].capitalize()) 
    else:
        print('String is too short!')

Old_MacDonald('macdonald')



