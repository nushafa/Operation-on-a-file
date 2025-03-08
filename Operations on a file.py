file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()



file = open('Codingal.txt', 'r')
print("Reading first line...")
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Looping through the lines...")
for line in file:
  print(line)
file.close()




file1 = open('Codingal.txt', 'r')
file2 = open('CodingalUpdated.txt', 'w')

for line in file1.readlines():
  if not (line.startswith('Coding')):
    print(line)
    file2.write(line)

file1.close()
file2.close()