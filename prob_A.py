INPUT_FILE = "prob_A.in"
OUTPUT_FILE = "prob_A.out"

def bumped(startA, startB, countA, countB, A, B):
   curA = startA     # Current positions of A & B, default = startA/B
   curB = startB
   
   moveA = False     # Boolean values to indicate whether A/B is moving/stopping
   moveB = False
   
   indexA = 0        # Index of the next change-speed time in list A and B
   indexB = 0

   t = 0             # Current time, default = 0

   while True:
      t += 1         # Increase current time by 1
      
      if (indexA < countA) and (t == A[indexA]):   # If current time matches is one of A's change-speed time
         indexA += 1
         if moveA:
            curA += 1
            moveA = False
         else:
            moveA = True
      else:
         if moveA:
            curA += 1
               
      if (indexB < countB) and (t == B[indexB]):   # If current time matches is one of A's change-speed time
         indexB += 1
         if moveB:
            curB += 1
            moveB = False
         else:
            moveB = True
      else:
         if moveB:
            curB += 1
            
      if abs(curA - curB) < 4.4:
         return True,t
      elif (indexA == countA) and (indexB == countB):
         if curA  < curB and moveA and not moveB:
            return True, (t + curB - curA - 4)
         elif curB < curA and moveB and not moveA:
            return True, (t + curA - curB - 4)
         else:
            return False, -1
            

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

   numOfCases = (len(myInput) - 1) // 3

   for case in range(numOfCases):
      startPos = myInput[case*3].split(' ')
      startA = int(startPos[0])
      startB = int(startPos[1])
      
      inputA = myInput[case*3+1].split(' ')
      countA = int(inputA[0])
      A = []
      for index in range(1, len(inputA)):
         A.append(int(inputA[index]))

      inputB = myInput[case*3+2].split(' ')
      countB = int(inputB[0])
      B = []
      for index in range(1, len(inputB)):
         B.append(int(inputB[index]))

      printLine = "Case " + str(case+1) + ": "
      result = bumped(startA, startB, countA, countB, A, B)
      if result[0]:
         printLine += "bumper tap at " + str(result[1]) + "\n"
      else:
         printLine += "safe and sound\n"

      g.write(printLine)

   print("Done!")
   g.close()

main()
