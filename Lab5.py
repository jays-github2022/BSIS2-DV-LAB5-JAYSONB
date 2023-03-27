temperature = int(input("Enter the temperature outside: "))

if temperature >= 0 and temperature <= 30: 
  print("the temperature is good today") 
  print("can go outside!") 
elif temperature < 0 or temperature > 30:
  print("the temperature is bad today!")
  print("you must stay inside!")