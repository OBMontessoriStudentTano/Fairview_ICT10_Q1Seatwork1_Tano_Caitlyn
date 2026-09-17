from pyscript import display, document

My_name = "Caitlyn Anne R. Tano"
My_age = 15
My_height = 165.1
Three_countries_I_visited = ['Singapore', 'Japan', 'Hong Kong']
Student_Type = False
Favorite_things = {'Color: Pink', 'Car brand: Honda', 'Shoe size: 8 feet', 'Best Friends: My friends from my friend group'}
My_favorite_fruits = ('Banana', 'Mango', 'Strawberry', 'Apple', 'Grape')
Seven_days_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

document.getElementById("name").innerHTML = My_name
document.getElementById("age").innerHTML = My_age
document.getElementById("height").innerHTML = My_height
document.getElementById("countries").innerHTML = Three_countries_I_visited
document.getElementById("student").innerHTML = Student_Type
document.getElementById("favorite").innerHTML = Favorite_things
document.getElementById("fruits").innerHTML = My_favorite_fruits
document.getElementById("weeks").innerHTML = Seven_days_of_the_week


def solving(event):
   document.getElementById("Answer").innerHTML = ""

   text1 = document.getElementById("text1").value
   text2 = document.getElementById("text2").value
   Operating = document.getElementById("Operating").value

   if text1 == "" or text2 == "":
      display("Please fill the box/es", target="Answer")
      return

   try:
      Number1 = float(text1)
      Number2 = float(text2)
   except ValueError:
      display("Please enter valid numbers", target="Answer")
      return

   if Operating == "Addition":
      result = Number1 + Number2
      symbol = "+"

   if Operating == "Subtraction":
      result = Number1 - Number2
      symbol = "-"

   if Operating == "Multiplication":
      result = Number1 * Number2
      symbol = "*" 

   if Operating == "Division":
      if Number2 == 0:
         display ("Cannot divide by zero", target="Answer")
      result = Number1 / Number2
      symbol = "/"        

   display(f"{Number1} {symbol} {Number2} = {result}", target="Answer")