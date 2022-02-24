f = open("a_an_example.in.txt", "r")

class Person:
    def __init__(self, name, skills):
        self.name = name
        if skills is None:
            skills = {}
        self.skills = skills

    def __str__(self):
        return f"""{self.name} is skilled in: {self.skills}"""

class Project:
    def __init__(self, name, days ,score,bestBefore,roles):
        self.name = name
        self.days = days
        self.score = score
        self.bestBefore = bestBefore
        self.roles = roles

    def __str__(self):
        return f"""{self.name} is requires: {self.roles} in {self.days} days for {self.score} score before {self.bestBefore}"""

firstline = f.readline()
loops = firstline.split()
first = int(loops[0])
second = int(loops[1])
peoplefinal = []
projectfinal = []
people = []
for i in range(first):
    personline = f.readline().strip()
    parsedline = personline.split()
    person = parsedline[0]
    expectedskills = int(parsedline[1])
    people.append(person)
    skills = {}
    for x in range(expectedskills):
        skillsline = f.readline()
        skillage = skillsline.split()
        skills[skillage[0]] = int(skillage[1])

    peoplefinal.append(Person(person, skills))

for i in range(second):
    projectline = f.readline()
    projectline = projectline.split()
    projectname = projectline[0]
    projectduration = int(projectline[1])
    projectscore = int(projectline[2])
    projectbefore = int(projectline[3])
    projectlines = int(projectline[4])

    projectskills = {}
    projectskillslevel = []
    for i in range(projectlines):
        projectread = f.readline()
        projectskillage = projectread.split()
        projectskills[projectskillage[0]] = int(projectskillage[1])


    projectfinal.append(Project(projectname, projectduration, projectscore, projectbefore, projectskills))

    costs = []
    for i in peoplefinal:
        print(i)
    for i in projectfinal:
        cost = (i.days*i.bestBefore)/i.score
        costs.append(int(cost))
        print(i)

f.close()