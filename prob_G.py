INPUT_FILE = "prob_G.in"
OUTPUT_FILE = "prob_G.out"

DIR = {"E":(1,0),"W":(-1,0),"N":(0,1),"S":(0,-1)}

def getNextPos(curPos,direction):
   curX = curPos[0]
   curY = curPos[1]
   newX = curX + 0.5 * DIR[direction][0]
   newY = curY + 0.5 * DIR[direction][1]
   return (newX, newY)

def findTime(me, G):
   t = 0
   curPos = me[0]
   direction = me[1]
   while abs(curPos[0]) <= 100 and abs(curPos[1] <= 100):
      t += 0.5
      curPos = getNextPos(curPos, direction)
      for index in range(len(G)):
         curGhost = G[index]
         ghostPos = curGhost[0]
         ghostDir = curGhost[1]
         newPos = getNextPos(ghostPos, ghostDir)
         if newPos == curPos:
            return t
         else:
            G[index] = (newPos, ghostDir)
   return -1
   
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
      myInfo = myInput.pop(0).split(' ')
      print(myInput)
      curX = int(myInfo[0])
      curY = int(myInfo[1])
      direction = myInfo[2]
      me = ((curX, curY), direction)
      

      ghostCount = int(myInput.pop(0))
      G = []
      for index in range(ghostCount):
         ghostInfo = myInput.pop(0).split(' ')
         curX = int(ghostInfo[0])
         curY = int(ghostInfo[1])
         direction = ghostInfo[2]
         ghost = ((curX, curY), direction)
         G.append(ghost)

      
      printLine = "Case " + str(case) + ": "

      result = findTime(me, G)
      if result == -1:
         printLine += "SAFE"
      else:
         printLine += str(result)
      printLine += "\n"
      
      g.write(printLine)

   print("Done!")
   g.close()

main()
