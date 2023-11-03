
# generate random integer values
from random import randint

print('''
                                                ^^
      ^^      ..                                       ..
              []                                       []
            .:[]:_          ^^                       ,:[]:.
          .: :[]: :-.                             ,-: :[]: :.
        .: : :[]: : :`._                       ,.': : :[]: : :.
      .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.
  _..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._
  _:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_
  !!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!
  ^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^
              []                                       []
              []                                       []
              []                                       []
   ~~^-~^_~^~/  \~^-~^~_~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/  \~^-~_~^-~~-
  ~ _~~- ~^-^~-^~~- ^~_^-^~~_ -~^_ -~_-~~^- _~~_~-^_ ~^-^~~-_^-~ ~^
     ~ ^- _~~_-  ~~ _ ~  ^~  - ~~^ _ -  ^~-  ~ _  ~~^  - ~_   - ~^_~
       ~-  ^_  ~^ -  ^~ _ - ~^~ _   _~^~-  _ ~~^ - _ ~ - _ ~~^ -
          ~^ -_ ~^^ -_ ~ _ - _ ~^~-  _~ -_   ~- _ ~^ _ -  ~ ^-
              ~^~ - _ ^ - ~~~ _ - _ ~-^ ~ __- ~_ - ~  ~^_-
                  ~ ~- ^~ -  ~^ -  ~ ^~ - ~~  ^~ - ~
''')
print("Instructions: Type either A or B to make your selections .")
print("Welcome to Caca Bridge.")
print("You must fish up the caca before your boss learns of your mess.")
selection = input("Will you, A) [prepare your fishing rod] or B) [stare helplessly at the water]? ")

if selection == "B" :
    print("Your tears raise the river until you drown.")
    print("BAD END: Died alone")
elif selection == "A" :
    print("You reach into your backpack. OH NO! You forgot your fishing rod! You begin to panic.")
    selection = input("Will you, A) [Check your car] or B) [stare helplessly at the water]? ")
    if selection == "A":
        print("You hurry to your car.")
        print("You're not sure if you're going to make it....")
        roll = randint(1, 6)
        print("God makes a speed roll and... ")
        print("...")
        if roll > 3:
            print(f"You rolled a {roll}!")
            print("You made it to your car. But your boss is there. Staring you up and down")
            selection = input("Will you, A) [Talk to them] or B) [turn back]? ")
            if selection == "A":
                print("She is very happy to see you.")
                print("God makes a sexy roll?")
                roll = randint(1, 6)
                if roll > 3:
                    print("She is hot....")
                    print('"Why are you not working"?')
                    selection = input(
                        ' A) ["I uh..."]  B) ["Do you have a map of your chromosomes? I’m trying to find my way into your genes."] ')
                    if selection == "A":
                        print('"Lazy ass."')
                        print("Your boss kills you")
                    if selection == "B":
                        print('"Wow...." *blush* "That was a good one..." *blushes more*')
                        print("You guys smash")
                        print("GOOD END")
                else:
                    print("She is your mom.")
                    print('"Why are you not working"?')
                    selection = input(' A) ["I uh..."]  B) ["Im not feeling well."] ')
                    if selection == "A":
                        print('"Nasty ass"')
                        print("Your mom kills you")
                    if selection == "B":
                        print('"Oh no... Here, take some ibuprofen"')
                        print('You sit with your mom for hours....')
                        print('*ring* *ring*')
                        print('It is coming from your moms phone')
                        print('"Hello?"')
                        print('There is a what...')
                        print('Your mom hangs up the phone and looks at you, with fire in her eyes')
                        print('"The intern shit the bridge!"')
                        print('BAD END : Intern gets fired ')
            elif selection == "B":
                print("You to return the river only to find the intern standing on the ledge.")
                print("You try to stop him, but you were too late.")
                print("BAD END: Intern died")
        else:
            print(f"You rolled a {roll}....")
            print("You died.")
    elif selection == "B" :
        print("Your tears raise the river until you drown.")
        print("BAD END: Died alone")

