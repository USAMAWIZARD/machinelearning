
import random
totalpopulation = 10
population = []
fitnesscore=[]
targetprase = "usama"
porobability=[]

def mixgenetics(newchild,pos):
    newchild=newchild[0:pos]+ chr(random.randint(97,122)) +newchild[pos+1:]
    return newchild
def genratepopulation(lengthofmember):
    i = 0
    member = ""
    global totalpopulation
    while i <= totalpopulation:
        for j in range(lengthofmember):
            member = member + chr(random.randint(97,122))

        population.append(member)
        member=""
        i += 1

    print("population",population)
def calculatefitness():
    for i in range(len(population)):
        fitness=0
        for letter in range(len(population[i])):
            try:
                if population[i][letter] == targetprase[letter]:
                    fitness+=1
            except:
                print(population[i])
                exit()
        fitnesscore.append(fitness)
    print("fitnesscore",fitnesscore)
def genrateprobability():
    for element in fitnesscore:
        eleloopext=element
        while eleloopext!=0:
            porobability.append(population[element])
            eleloopext-=1

    print("pobablility",porobability)
def pickparants():
    ip1=random.randint(0,len(porobability)-1)
    ip2=random.randint(0,len(porobability)-1)
    crossover(ip1,ip2)

def crossover(ip1,ip2):
    p1=porobability[ip1]
    p2=porobability[ip1]
    newchild=p1[:len(p1)//2]+p2[len(p2)//2:]
    print("newchild",newchild)
    pos=random.randint(0,len(newchild)-1)
    mutatenewchild=mixgenetics(newchild,pos)
    print("mutatedchid",mutatenewchild)
    population.append(mutatenewchild)

def cmp():
    global porobability
    global fitnesscore
    inter=set(population).intersection(set(targetprase)) #to check if requiered element is in population
    if inter==0:
        print(inter)
        exit()
    porobability = []
    fitnesscore = []
    return True
while cmp():
    genratepopulation(len(targetprase))
    calculatefitness()
    genrateprobability()
    pickparants()

