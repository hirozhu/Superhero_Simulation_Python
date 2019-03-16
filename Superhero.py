# Xubo Zhu
# ITP 115
# Assignment 9
# 4/9/2017
# Description: Superhero



class Superhero(object):
    def __init__(self, name, type, attack):
        self.__name = name
        self.__type = type
        self.__attack = attack
        self.__health = 100

    def getName(self):
        return self.__name

    def getAttack(self):
        return self.__attack

    def getHealth(self):
        return self.__health

    def getType(self):
        return self.__type

    def loseHealth(self, attack):
        self.__health -= attack

    def isDead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def __str__(self):
        msg = self.__name + " the " + self.__type + " has " + str(self.__attack) + " attack points and currently has " + str(self.__health) + " points of health"
        return msg

