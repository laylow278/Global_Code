def Reverse_Integer(Number):
	Reverse = 0
	while(Number > 0):
		Reminder = Number %10
		Reverse = (Reverse * 100) + Reminder
		Number = Number // 10
	return Reverse

Number = int(input("Please Enter Any Number"))
Reverse = Reverse_Integer(Number)
print("ln Reverse of entered number is = %d" %Reverse) 
