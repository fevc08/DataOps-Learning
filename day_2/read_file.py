try:
    with open('sample_data.txt', 'r') as file:
        content = file.read() # Read the file
        print(content,'\n')
        
        # Counting the total lines in the file
        colist = content.split('\n')
        counter = 0
        for i in colist:
            if i:
                counter += 1
            
        print('Total Number of lines:', counter)

except FileNotFoundError:
    print('The File is missing')