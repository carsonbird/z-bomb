import configparser

config = configparser.ConfigParser()
config.read('config')

def ports():
  return config['ServerPorts']

def audio():
  return config['Audio']

def settings():
  return config['General']