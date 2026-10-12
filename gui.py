import tkinter as tk
import json


def set_goal():
    goal = int(goal_entry.get())
    save_goal(goal)
    goal_confirmation.config(text =f"goal set to {goal} calories")
    
    update_goal_status()
    

def add_meal():
    food = meal_entry.get()
    food_calories = int(calories_entry.get())

    meal = {
        "name" : food,
        "calories" : food_calories   

        
    }
    meals.append(meal)
    save_meals(meals)
    meals_listbox.insert(tk.END, f"{food}: {food_calories} calories")
    
    meal_entry.delete(0, tk.END)
    calories_entry.delete(0, tk.END)

    meal_status.config(text = f"{food} was added successfully!")

    total_label.config(text = f'Total calories:{calculate_calories()}' )

    update_goal_status()







def load_meals():
    try: 
      
      with open("meals.json","r") as file:
        meals = json.load(file)
        return meals

    except(FileNotFoundError, json.JSONDecodeError):
       
       return []  


def save_meals(meals):
    with open("meals.json", "w") as file:
        json.dump(meals,file)


def show_meals():
    for meal in meals:
        meals_listbox.insert(tk.END,f'{meal["name"]}: {meal["calories"]} calories')



def remove_meal():
    try:
     selected = meals_listbox.curselection()
     index = selected[0]
     meals.pop(index)
     meals_listbox.delete(index)
        
     save_meals(meals)
     meal_status.config(text="Meal removed successfully!")
     total_label.config(text = f'Total calories:{calculate_calories()}' )
     
     update_goal_status()
    
    
    except IndexError:
       meal_status.config(text =" Please select a meal first!") 

      
       

def calculate_calories():
   total = 0
   for meal in meals:
      total += meal["calories"]
   return total
      



def update_goal_status():

   goal = int(goal_entry.get())

   total = calculate_calories()

   less = goal - total
   more = total - goal

   if goal > total:
     goal_status.config(text = f"You still have {less} calories remaining! ")
     

   elif goal < total:
       goal_status.config(text = f"You exceeded your goal by {more} calories! ")

   else:
       goal_status.config(text = "You've reached your daily calorie goal")
         
   
def save_goal(goal):
   with open ("goal.json", "w") as file:
      json.dump(goal,file)


   

def load_goal():
    try: 
      
      with open("goal.json","r") as file:
        goal = json.load(file)
        return goal

    except(FileNotFoundError, json.JSONDecodeError):
       
       return None




meals = load_meals()
saved_goal = load_goal()

root = tk.Tk()
root.title("Calorie Tracker")
root.geometry("500x600")

title_label = tk.Label(root, text="CALORIE TRACKER")
title_label.pack()

goal_label = tk.Label(root, text="Daily Goal:")
goal_label.pack()

goal_entry = tk.Entry(root)
goal_entry.pack()
if saved_goal is not None:
    goal_entry.insert(0, str(saved_goal))

goal_button = tk.Button(root, text="Set Goal", command=set_goal)
goal_button.pack()

goal_confirmation = tk.Label(root, text = "")
goal_confirmation.pack()

meal_label = tk.Label(root, text = "Meal Name: ")
meal_label.pack()
meal_entry = tk.Entry(root)
meal_entry.pack()

calories_label = tk.Label(root, text = "Calories: ")
calories_label.pack()
calories_entry = tk.Entry(root)
calories_entry.pack()

meal_button = tk.Button(root, text = "Add meal: ", command = add_meal)
meal_button.pack()

meal_status = tk.Label(root, text="")
meal_status.pack()

meals_label = tk.Label(root, text = "Today's meals: ")
meals_label.pack()


meals_listbox = tk.Listbox(root)
meals_listbox.pack()

show_meals()


remove_button = tk.Button(root, text = "REMOVE MEAL!", command = remove_meal )
remove_button.pack()



total_label = tk.Label(root, text = f"Total calories: {calculate_calories()} ")
total_label.pack()


goal_status = tk.Label(root, text="")
goal_status.pack()


root.mainloop()

