def standardizeInput(fileName):
   f = open(fileName, 'r')
   content = []
   for line in f:
      line = line.strip()
      line = " ".join(line.split())
      if line != '':
         content.append(line)
   return content
