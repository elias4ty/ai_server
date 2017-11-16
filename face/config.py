config = {
    'mac' : '/Users/elias/Documents/python_exercise/flask_01/face/input',
    'production' : '/home/ai_demo/src/face/input/',
    'win' : 'E:/exercise/python_exercise/face/input'
}

def dic(arg = 'mac'):
    return config[arg]
