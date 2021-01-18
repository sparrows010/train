tickcost = 25.00

trainuptime = [9, 11, 13, 15]
trainuptick = [480, 480, 480, 480]
trainupmoney = [0.0, 0.0, 0.0, 0.0]

traindowntime = [10, 12, 14, 16]
traindowntick = [480, 480, 480, 640]
traindownmoney = [0.0, 0.0, 0.0, 0.0]

print('Train Times \t\t Tickets \t Tickets Available')
for count in range(0, 4):
  print(trainuptime[count], '\t\t\t', trainuptick[count], '\t\t\t', trainupmoney[count])
  print(traindowntime[count], '\t\t\t', traindowntick[count], '\t\t\t', traindownmoney[count])



sellticks = 'yes'
while sellticks == 'yes':
  
  timeup = int(input('What time would you like to go up the mountain?  9,11,13,15: '))
  while timeup != 9 and timeup != 11 and timeup != 13 and timeup != 15:
    timeup = int(input('There was an error, What time would you like to go up the mountain?  9,11,13,15: '))

  for count in range(0, 4):
    if timeup == trainuptime[count]:
      IndexUp = count
      

  timedown = int(input('What time would you like to go down the mountain?  10,12,14,16: '))
  while timedown != 10 and timedown != 12 and timedown != 14 and timedown != 16:
    timedown = int(input('There was an error, What time would you like to go down the mountain?  10,12,14,16: '))
  
  for count in range(0, 4):
    if timedown == traindowntime[count]:
      IndexDown = count

  numticks = int(input('How many tickets would you like to purchase. 10th ticket is free. '))
  while numticks > trainuptick[IndexUp] or numticks > traindowntick[IndexDown]:
    numticks = int(input('There was an Error. How many tickets would you like to purchase. 10th ticket is free. '))

  trainuptick[IndexUp] = trainuptick[IndexUp] - numticks
  traindowntick[IndexDown] = traindowntick[IndexDown] - numticks

  for count in range(0, 4):
    if trainuptick[count] == 0:
      trainuptick[count] = str(trainuptick[count])
      trainuptick[count] = 'Closed'

    if traindowntick[count] == 0:
      traindowntick[count] = str(traindowntick[count])
      traindowntick[count] = 'Closed'


  tripcost = tickcost * (numticks - int(numticks / 10))

  trainupmoney[IndexUp] = tripcost
  traindownmoney[IndexDown] = tripcost

  print('your cost for the oneway trip is', tripcost)
  print('you have to pay for the return tickets too \n the total amount of your trip including the 10th ticket discount is: ' ,tripcost * 2)
 
  print('\nTrainTimes \t\t Available Tickets \n')
  for count in range(0, 4):
    print(trainuptime[count], '\t\t\t', trainuptick[count],'\t\t')
    print(traindowntime[count], '\t\t\t', traindowntick[count], '\t\t')

  sellticks = input('would u like to purchase more tickets, yes or no? : ')


for count in range(0, 4):
  if trainuptick[count] == 'Closed':
    trainuptick[count] = int('0')
    trainuptick[count] = 0

  if traindowntick[count] == 'Closed':
    traindowntick[count] = int('0')
    traindowntick[count] = 0

passup = [0] * 4
passdown = [0] * 4

totalpass = 0
for count in range(0, 3):
  
  passup[count] = 480 - trainuptick[count]
  print('Trip time:', trainuptime[count], 'had this number of passengers:', passup[count])
  totalpass = totalpass + passup[count]

  passdown[count] = 480 - traindowntick[count]
  print('Trip time:', traindowntime[count], 'had this number of passengers:', passdown[count])
  totalpass = totalpass + passdown[count]


passup[3] = 480 - trainuptick[3]
print('Trip time:', trainuptime[3], 'had this number of passengers:', passup[3])
totalpass = totalpass + passup[3]

passdown[3] = 640 - traindowntick[3]
print('Trip time:', traindowntime[3], 'had this number of passengers:', passdown[3])
totalpass = totalpass + passdown[3]

print('total passengers today:', totalpass)

totalmoney = 0

for count in range(0, 4):
  totalmoney = totalmoney + trainupmoney[count]
  toatlmoney = totalmoney + traindownmoney[count]

print('total money colected today:', totalmoney)
