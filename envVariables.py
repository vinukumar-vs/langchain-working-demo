from dotenv import load_dotenv, dotenv_values, get_key
load_dotenv()
config = dotenv_values()

print("dotenv values..\n", config)

def getEnv(key):
    return config[key]

def printEnv(key): 
    print(key, ":", config[key])