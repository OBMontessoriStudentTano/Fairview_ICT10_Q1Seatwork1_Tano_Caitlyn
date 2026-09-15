from pyscript import display, document
# importing document and display package

My_name = "Caitlyn Anne R. Tano"
My_age = 15
My_height = 165.1
Three_countries_I_visited = ['Singapore', 'Japan', 'Hong Kong']
Student_Type = False
Favorite_things = {'Color: Pink', 'Car_brand: Honda', 'Shoe_size: 8 feet' , 'Best Friends: My friends from my friend group'}
My_favorite_fruits = set[('Banana','Mango','Strawberry','Apple', 'Grape')]
Seven_days_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')


display(My_name, target="name")
display(My_age, target="age")
display(My_height, target="height")
display(Three_countries_I_visited, target="countries")
display(Student_Type, target="student")
display(Favorite_things, target="favorite")
display(Seven_days_of_the_week, target="weeks")

 def solving():
    document.getElementById("Answer").innerHTML = "" # clear previous output

    try:
     Number1 = float(document.getElementById("text1").value)
     Number2 = float(document.getElementById("text2").value)
     Operating = document.getElementById("Operating").value
    
    if Operating == "Addition":
       result = Number1 + Number2
       symbol = "+"
    elif Operating == "Subtraction":
       result = Number1 + Number2
       symbol = "-"
    elif Operating == "Multiplication":
       result = Number1 * Number2
       symbol = "*"
    elif Operating == "Division":
       result = Number1 / Number2
       symbol = "/"

    except ValueError:
        display("Please enter valid numbers in both boxes", target="Answer")


    