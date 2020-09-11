def story1():
  print("Story1 has been chosen.")
  name = input("Name: ")
  toy = input("A toy they like: ")
  color = input("Color they like: ")
  verb = input("Verb: ")
  print("%s %s on their favorite toy. Their favorite toy is a %s and its color is %s. When they %s on the %s, they tried holdng on to a chair but the chair tilted down with them. They fell down hard onto the floor that their parent came running downstairs to check on %s. %s parents called the ambulance. Then they took %s to the emergency room for an open head :p." % (name, verb, toy, color, verb, toy, name, name, name))

def story2():
  print("Story2 had been chosen.")
  manga = input("Favorite manga: ")
  character = input("Favorite character in the manga: ")
  verb = input("Verb: ")
  character2 = input("2nd favorite character: ")
  print ("My favorite manga is %s and my favorite character is %s. In %s, %s %s on %s. %s felt embarassed so they got up quick and helped %s up. After that day, they began talking and turns out they had feelings for each other <3. If %s never had %s on %s, they wouldn't have ever told their feelings for each other.~" % (manga, character, manga, character, verb, character2, character, character2, character, verb, character2))

def random():
  print("Random has been chosen!")
  name = input("Name: ")
  name2 = input("Friend: ")
  game = input("Favorite Game: ")
  adjective = input("Adjective: ")
  print("My name is %s and this is my %s friend, %s. We met through %s and started hitting it off as friends from there. %s and I planned on meeting each other face to face one day. 4 months later, %s and I had finally met and they were so %s. " % (name, adjective, name2, game, name2, name2, adjective))

def storyPicker(storyChoice):
  if storyChoice == "1":
    story1()
  elif storyChoice == "2":
    story2()
  elif (storyChoice == "r") or (storyChoice == "R"):
    random()

def main():
  print("Welcome to my Madlibz!! /n Choose your story: ")
  storyChoice = input("1 or 2 or random(r, R): ")
  storyPicker(storyChoice)

if __name__ == "__main__":
   main()
