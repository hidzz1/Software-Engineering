#first find out how long it took for user to complete each race 
swimming=int(input("How many minutes did it take to complete swimming?"))
cycling=int(input("How many minutes did it take to complete cycling?"))
running=int(input("How many minutes did it take to complete running?"))

#total is all of the times combined 
total = swimming + cycling + running

#now give award based on time taken 
if total <= 100: 
 print("Congratulations, you have won the Provincial Colours Award!")

if total >=101 and total <= 105:
 print("Congratulations, you have won the Provincial Half Colours Award!")


if total >=106 and total <= 110: 

 print("Congratulations, you have won the Provincial Scroll Award!")

 
elif total >=111:
  
  print("Sorry unfortunately, you have not won any Award")


