def main():
      calories1 = int(input( "How many calories are in the first food? "))
      calories2 = int(input( "How many calories are in the first food? "))
      showCalories(calories1, calories2)

def showCalories(first_food, second_food):   
   print(f"The total calories you ate today {first_food + second_food}")

if __name__=="__main__":
    main()
