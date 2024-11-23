try:
    with open('sample_data.txt', 'r') as file:
        content = file.read() # Read the file
        print(content,'\n')
        
        # Splitting file content into lines and counting non-empty lines
        colist = content.split('\n')
        counter = sum(1 for line in colist if line.strip())  # Count non-empty lines
        
        print('Total Number of lines:', counter)

        # Handling empty file case
        if counter == 0:
            print("The file is empty.")

except FileNotFoundError:
    print('The File is missing')