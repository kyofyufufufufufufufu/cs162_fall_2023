import plant
import tomato
import turnip
import wiltingError

def main():
    """Initializing gardenscape"""
    my_tomato = tomato.Tomato()
    my_turnip = turnip.Turnip()
    my_plant = plant.Plant()

    print("""
              -------------------------------          
              -------------------------------
               +                           +
               +     ~*Garden Game*~       +
               +                           +
              -------------------------------
              -------------------------------
          """)
    
    print("Hello! Would you like some planting tips before we start? (Recommended)")
    user_start = (input("Y or N? "))

    if user_start.upper() == "Y":
        print(my_tomato)
        print(f"\n{my_turnip}")
    elif user_start.upper() == "N":
        pass
    else:
        print("Invalid user response.")
        raise ValueError


    
    my_plant.season_search()

    print("""        
              --------------------------
               +    *Time to Water*    +
              --------------------------
          """)
    my_turnip.add_water()

    print("Your plant must be transplanted to the garden.")
    print("""\nWhere should you place it?
    1. Full sun.
    2. Partial sun/shade.
    3. Full shade.
    """)
    
    user_input_check = input("\n1, 2, or 3? ")
    selected_option = my_turnip.check_sunlight(user_input_check)

    if selected_option is not None:
        print(f"Your plant loves where you placed it! Selected option: {selected_option}")
    else:
        raise wiltingError.WiltingError("Your plant has wilted!")



if __name__ == "__main__":
    main()