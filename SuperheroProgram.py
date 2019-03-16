# Xubo Zhu
# ITP 115
# Assignment 9
# 4/9/2017
# Description: Superhero



from Superhero import Superhero

def main():

    again = "y"

    while again == "y":
        name1 = input("Enter fighter #1's name: ")
        type1 = input("Is fighter #1 a hero or villain? ")
        attack1 = int(input("Enter fighter #1's attack points: "))

        name2 = input("Enter fighter #2's name: ")
        type2 = input("Is fighter #2 a hero or villain? ")
        attack2 = int(input("Enter fighter #2's attack points: "))

        player1 = Superhero(name1, type1, attack1)
        player2 = Superhero(name2, type2, attack2)

        print("\nFIGHTERS\n")

        print(player1)
        print(player2)

        print("\nBEGINNING BATTLE!\n")

        n = 0

        while Superhero.isDead(player1) == False and Superhero.isDead(player2) == False:
            n +=1
            print("\n=======Round",n,"========")

            Superhero.loseHealth(player1, attack2)
            Superhero.loseHealth(player2, attack1)

            print(player1)
            print(player2)

        if Superhero.isDead(player1) == True and Superhero.isDead(player2) == False:
            print("\n" + Superhero.getName(player2) + " won!")
        elif Superhero.isDead(player2) ==True and Superhero.isDead(player1) == False:
            print("\n" + Superhero.getName(player1) + " won! ")
        elif Superhero.isDead(player1) ==True and Superhero.isDead(player2) ==True:
            print("\nNobody won. It's a tie!")

        again = input("\nWould you like to play again? (y/n): ")


    print("\nGoodbye!")


main()