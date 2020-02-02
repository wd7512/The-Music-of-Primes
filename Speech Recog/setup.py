from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Speech.py", base=base)]

packages = ["idna",'speech_recognition','sounddevice',
            'scipy.io','numpy','time','googletrans']
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
