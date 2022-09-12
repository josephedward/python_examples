import subprocess

COMMANDS = {
    "Java": "javac",
    "C": "gcc",
    "C++": "g++",
    "C#": "mcs",
    "Python": "pylint",
    "Ruby": "ruby-lint",
    "Golang": ["go", "run"]
}

def linter(text, lang, tempfileName):
    f = open(tempfileName, "w")
    f.write(text)
    f.close()
    runcommand = [COMMANDS[lang],tempfileName]
    if isinstance(COMMANDS[lang], list):
        runcommand = [COMMANDS[lang][0], COMMANDS[lang][1], tempfileName]
    process = subprocess.run(runcommand,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True)
    if (lang == "Ruby" or lang == "Python") and process.stdout:
        return { 'status': 'err', 'message': process.stdout }
    if process.stderr:
        return { 'status': 'err', 'message': process.stderr }
    return { 'status': 'ok' }