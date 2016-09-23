##############################################################
#Python Crawler                                              #
#An attempt at learning Python by creating a very simple game#
##############################################################
#I am borrowing heavily from years of gaming including       #
# Nethack, Pixel Dungeon, Kingdom of Loathing,               #
# Dungeons & Dragons and more                                #
##############################################################
#An empty file was created 09/23/2016                        #
#Version History                                             #
#0.01 - 09/23/2016 - notes only                              #
##############################################################
#MOBS                                                        #
#Melee                                                       #
# 1 kobold                                                   #
# 2 orc                                                      #
# 3 ogre                                                     #
# 4 golem (magical)                                          #
# 5 werewolf (magical)                                       #
#Ranged                                                      #
# 1 goblin                                                   #
# 2 lizardfolk                                               #
# 3 skeleton                                                 #
# 4 witch/warlock (magical)                                  #
# 5 elemental (magical)                                      #
##############################################################
#HEROES

#PLANNING
# 001. figure out how to draw a random dungeon of ASCII characters
# 002. figure out how to put (N)PCs in the dungeon
# 003. let player move PC
# 004. teach NPCs to move
# 005. teach NPCs to move with different motivations
# 006. let PC and NPC fight
# 06a. log hero deaths
# 007. build out different types and behaviors of NPCs
# 008. OPTIONAL allow PCs to be programmed by user
# 009. allow PC to level up
# 010. allow PC to go to different floor

print ("##############################################################")
print ("#####  Welcome to Python Crawler  ############################")
print ("##############################################################")

pcName = input("Please Name your hero\(ine\):")


print (pcName, "has died.")
print ("##############################################################")
print ("###That's it, all the code I've written#######################")
print ("##############################################################")