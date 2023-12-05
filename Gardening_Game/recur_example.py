"""recursion example using kitties as a function calls itself"""

class Kitty:
    def __init__(self, name):
        self.name = name

def play_with_kitties(kittens):
    if len(kittens) <= 1:
        print(f"{kittens[0].name} is having fun!")
    else:
        print("Kitties playing:")
        for kitty in kittens:
            print(f"- {kitty.name}")

        #kitty is bored and doesn't want to play anymore so they're removed from the group
        removed_kitty = kittens.pop()

        #recursion
        play_with_kitties(kittens)

        print(f"{removed_kitty.name} takes a nap.")

#making some kitties
kitty1 = Kitty("Newt")
kitty2 = Kitty("Diego")
kitty3 = Kitty("Rusty")

#initialize list
all_kitties = [kitty1, kitty2, kitty3]

#the kitties are playing
play_with_kitties(all_kitties)