import pygame
import info as Info
import homework
from helpers import*
import teacher
import gameinfo
import character

# Initialize Pygame
pygame.init()

#teachers
teacher1 = teacher.Teacher("Monica", "English")
teacher2 = teacher.Teacher("Manuel", "Math")
teacher3 = teacher.Teacher("Marzano", "Biology")
teacher4 = teacher.Teacher("Mack", "Comp. Sci")
teacher5 = teacher.Teacher("Mcdougal", "History")

teacher3.transition("feeling the rage")

#homework
testhwk1 = homework.Homework("major", "English", 240, "Bibliography", teacher1)
testhwk2 = homework.Homework("minor", "Biology", 1050, "Mitochondria MCQ", teacher2)
testhwk3 = homework.Homework("minor", "English", 50, "Freewrite", teacher3)
testhwk4 = homework.Homework("minor", "Math", 550, "Online Quiz", teacher5)

#Game tracker variables
homeworkQ = [testhwk1, testhwk2, testhwk3, testhwk4]
teachers = [teacher1, teacher2, teacher3, teacher4, teacher5]

#Desk graphics object

#Mouse event handler

#make character
player = character.Character("Miguel")
#Gameinfo Object
game = gameinfo.Game(homeworkQ, teachers)
game.activehwk = testhwk1
game.activehwk.active = True
# Main game loop
game.run()