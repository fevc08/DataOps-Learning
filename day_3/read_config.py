import yaml

try:
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        
        database = config.get('database', {})
        print('Database Host:', database.get('host', 'Not specified'))
        print('Database Port:', database.get('port', 'Not specified'))
        print('Database Username:', database.get('username', 'Not specified'))
        print('Database Password:', database.get('password', 'Not specified'))
except FileNotFoundError:
    print("File doesn't exist")