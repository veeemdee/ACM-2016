INPUT_FILE = "prob_E.in"
OUTPUT_FILE = "prob_E.out"

def encode(i, x, y):
   if i % x == 0:
      if i % y == 0:
         return "FizzBuzz"
      else:
         return "Fizz"
   else:
      if i % y == 0:
         return "Buzz"
      else:
         return str(i)

def fizzBuzz(x, y, n):
   result = ""
   for i in range(1, n+1):
      result += encode(i, x, y) + "\n"
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

   numOfCases = len(myInput) - 1

   for case in range(numOfCases):
      parameters = myInput[case].split(' ')
      x = int(parameters[0])
      y = int(parameters[1])
      n = int(parameters[2])
      
      printLine = "Case " + str(case+1) + ":\n" + fizzBuzz(x,y,n)
      
      g.write(printLine)

   print("Done!")
   g.close()

main()
