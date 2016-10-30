INPUT_FILE = "prob_C.in"
OUTPUT_FILE = "prob_C.out"

def deduce(names, rules):
   size = len(names)
   relationship = {}
   for name in names:
      relationship[name] = ([],[])
   for rule in rules:
      (rType, rNames) = rule
      
      if rType == 'f':
         for i in range(len(rNames)-1):
            for j in range(i+1, len(rNames)):
               personA = rNames[i]
               personB = rNames[j]
               relationship[personA][0].append(personB)
               relationship[personB][0].append(personA)

      if rType == 'e':
         personA = rNames[0]
         personB = rNames[1]
         
         relationship[personA][1].append(personB)
         for name in relationship[personB][1]:
            if name != personA:
               relationship[personA][0].append(name)
               relationship[name][0].append(personA)

         relationship[personB][1].append(personA)
         for name in relationship[personA][1]:
            if name != personB:
               relationship[personB][0].append(name)
               relationship[name][0].append(personB)
   return relationship

def areFriends(names, relationship):
   for i in range(len(names)-1):
      for j in range(i+1, len(names)):
         personA = names[i]
         personB = names[j]
         if not personB in relationship[personA][0]:
            return False
   return True

def standardizeInput(fileName):
   f = open(fileName, 'r')
   content = []
   for line in f:
      line = line.strip()
      line = " ".join(line.split())
      if line != '':
         content.append(line)
   f.close()
   return content

def main():
   myInput = standardizeInput(INPUT_FILE)

   g = open(OUTPUT_FILE, 'w')
   case = 0
   while len(myInput) > 1:
      case += 1
      rAndP = myInput.pop(0).split(' ')
      r = int(rAndP[0])
      p = int(rAndP[1])
      
      rules = []
      names = []

      for i in range(r):
         rInfo = myInput.pop(0).split(' ')
         rType = rInfo[0]
         rNames = rInfo[2:]
         for name in rNames:
            if not name in names:
               names.append(name)
         rules.append((rType,rNames))

      printLine = "Case " + str(case) + ":"         

      relationship = deduce(names, rules)
      
      for i in range(p):
         pInfo = myInput.pop(0).split(' ')
         pNum = int(pInfo[0])
         pNames = pInfo[1:]
         if areFriends(pNames, relationship):
            printLine += " yes"
         else:
            printLine += " no"

      printLine += "\n"
      
      g.write(printLine)

   print("Done!")
   g.close()

main()
