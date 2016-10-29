INPUT_FILE = "prob_F.in"
OUTPUT_FILE = "prob_F.out"

def findTimes(n, m, T):
   A = []

   firstRow = [T[0][0]]
   for i in range(m-1):
      firstRow.append(firstRow[i]+T[0][i+1])
   A.append(firstRow)

   for j in range(1, n):
      rowJ = [A[j-1][0]+T[j][0]] + [None]*(m-1)
      A.append(rowJ)

   for j in range(1, n):
      for i in range(1, m):
         A[j][i] = max(A[j-1][i], A[j][i-1]) + T[j][i]

   result = []
   for j in range(n):
      result.append(A[j][m-1])

   return result

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
      nAndM = myInput.pop(0).split(' ')
      n = int(nAndM[0])
      m = int(nAndM[1])

      T = []
      for i in range(n):
         data = myInput.pop(0).split(' ')
         swatherTime = list(int(i) for i in data)
         T.append(swatherTime)

      printLine = "Case " + str(case) + ":"

      result = findTimes(n, m, T)
      for swatherTime in result:
         printLine += " " + str(swatherTime)

      printLine += "\n"
      
      g.write(printLine)

   print("Done!")
   g.close()

main()
