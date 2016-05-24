# -*- coding: utf-8 -*-
import sys
#Insert Code

class story_line():
    def __init__(self, A, B, C, D, E, scene, options, response1, response2, response3, response4, response5):
	self.A = A
	self.B = B
	self.C = C
	self.D = D
	self.E = E
	self.scene = scene
	self.options = options
	self.response1 = response1
	self.response2 = response2
	self.response3 = response3
	self.response4 = response4
	self.response5 = response5
	
    def scene_change(self, choice):
        global node
        if choice == 'A':
            print node.response1
        if choice == 'B':
            print node.response2
        if choice == 'C':
            print node.response3
        if choice == 'D':
            print node.response4
        if choice == 'E':
            print node.response5
          
        node = globals()[getattr(self, choice)]
        
#"OPTIONS: " + "\nA: " + "\nB: " + "\nC: " + "\nD: " + "\nE: "

    def change_options(self, scene):
        global node
        if scene == accept_gun:
           node.C = 'find_abitur' 
           node.response3 = 'Woah, what just happened? Weren\'t you just somewhere else?'
           node.options = node.options + "\nC: IT BLOODY WORKS"
           #node.options = "\nA: Kill him"
                  
    def relations_NPC(self, scene):
        global Abitur_Heart
        global node
        if scene == Into_building:
            Abitur_Heart += 1
            

Intro_game_start = story_line('intro_game_instructions', None, None, None, None, \
'Welcome to Mafia Effect, the choose your own adventure style game. A warning to all those who are willing to play the game: This is an EXPLICIT game, meaning it will feature Harsh Language, suggestive scenes, and situations which the gamer may find disturbing. Discretion is advised.',\
"OPTIONS: " + "\nA: Continue", " " , None, None, None, None)

intro_game_instructions = story_line('Associate_start', None, None, None, None,\
'TO PLAY MAFIA EFFECT: The user will be presented with a scene, in which a variety of options will be displayed. In order to choose an options, input the letter in front of the option and press enter. You will be presented with your character\'s response and the scene resulting afterwards.' + '\nTO EXIT GAME: In order to leave the game, enter with q, quit, or exit and then press enter.' + '\nWe hope you enjoy the game, and now it\'s time to get started! Be careful which path you choose and whom you associate yourself with! Enjoy!', \
"OPTIONS: " + "\nA: Start Game", 'Here we go.', None, None, None, None)

game_start - story_line('deny_prost', 'accept_prost', None, None, None, 'You often pondered where in your life you had gone of thhe good path and stumbled and crshed stright ino hell. Standing alone withing the entrance hall of a rcih don\'s house, you wondered as you glanced around, staring at all the different art pieces scattered about, trying to do anything from keeping you from being bored. You didn\'t want to move and start toching anything, nor did you want to piss off anyoneanytime sooon. So you stood, waiting for that pink haired man t come and retreive you so you could meet the don of this place. You weren\'t looking forward to it. As you you begn t imagine all the ways you could possibly be killed by the man or one of his subordinates, a sharp voice cuts through your thoughts and causes you flinch at the sound. Looking for the source, you see a female in her early twenties sauntering over, a purposeful sway to her hips. Her deep red urls bounced with each step, and as she was finaly within reach, she grabbed your arm and look up into your eyes, battering her eyelashes. Trying to ignore her very obvious assests gripping onto your arm, you try and retin only eye contact with her. "So, what a goodloookin\' guy lke yaself doin\' all by yah lonsome, huh, han\'some?" She asked, one of her hands trailing across your chest. "\'Cause I wouldn\' mind showin\' ya around myself, ya know? So how about it han\'some?"', "OPTIONS: " + "\nA: Reject Her Offer" + "\nB: Accept Her Offer", 'You give her a sheepish grin. "Sorry, but I\'m going to have to deny that... tour." You turned your gaze upward when you felt her grip on your arm tighten. "I\'m here to see someone."', 'Staring down at her, and maybe a little loweer than that, you gave her a grin. "wy, of course I would love to have a beautiful doll such as yourself sho me around." All previous arrangements forgotten, you were more than wiling to trail after her whhere ever she wanted to go.', None, None, NOne)

deny_prost = story_line('flavio_pos', None, None, None, None, 'She pouts, ready to try and beg, only to cut off as another voice interrupts. "I would prefer if you didn\'t try and seduce ur new recruit, you damn cagna. Go back to that Succusbus of yours, and tell her that she should try and keep track of her demone least one looses a finger or two." The female stiffened, and she shot a glare towards the pink haired male. "Jealous, are we Flavio?" She sneered, "Or you too pissed about not being able to fuck that Capo of yours?" She hissed, releasing you and flipping him off. Flavio merely glared as she stormed off in a huff. He turned his attention to you. "You, come along. The boss doesn\'t like the be kept wainting.", And he too, walked swiftly down a hall in a huff.', "OPTIONS: " + "\nA: Follow", 'You looked at the scene with amusement, and when given the order, you followed without hesitation. Obviously, ther\'s a story to that.', None, None, None, None)

accept_prost = story_line('flavio_neg', None, None, None, None, 'Her eyes light with victory, and she begins to tug you towards the staircase, where you assume the bedrooms are. "One step further, and I will place a bullet in either of you." A voice interrupts your perverted thoughts, and you both tene at the third party. The lady releases you, and turns around to face the voice, and you quickly do the same. he man with the pick hair has returned, and you can clearly read he emtions of disgust and anger. "Puttanella, go return to the Succusbuss before either of you find something unplesant in your food again." She turned a tad green at that. She merely sneered, wanting o say more but decided against it. Turning to you. she batted her eyelashes again, and with a purr of \'Call me sometime han\'some\', she left you alone with the pink haired male. HE turned his ferious expression on you, grabbing your arm roughly and dragging you away from the stairs o a hallway.', "OPTIONS: " + "\nA: Follow", 'You stumble, but quickly correct yourself and easily keep pace with the angry man. Whoops.', None, None, None, None)

flavio_pos = story_line(None, None, None, None, None, 'He lead you to a room with one guard posted outside. The burly man nods in greeting and opens the door. Favio enters first, and you enter soon after. "Ah! Fratello!" A voice calls, a smooth baritone that sounds odd with the cheerful tone. "Back so soon? Oh, and that must be Mr. Jones! Do come in, I\'ve simly been waiting all day to see you! Flavio, carissimo Fratello, go.. do something." Flavio huffed, shot the Don a look, before leaving the room and shutting the door behidd him. Now you sat alone with the don, Allessandro Vargas of the Romulus Familiga, known for their ruthlessness and uderhand methods to get their way. You gulped. "Now, Mr. Jones, ther\'s no need to be so tense. I\'ve only heard quite good things about you and your preformance abilities."', "OPTIONS: " + "\nA: Wait for him to continue", 'You shift where you stand, not syaing a word and your gaze low.', None, None, None, None)

flavio_neg = story_line(None, None, None, None, None, 'The door that appears to be the designation has a guard i front of it, who stares at you two with ausement. Opening the door for you two, he steps to the side as Flavio shoves you through before follwoing himself, slamming the door close. As soon as it does, he beins a small rant in what you feel is Italian, buut you\'re not really sure because you were never really well-versed in languages. When the small ran ends, you have notied the man sitting behnd thedesk is teribly amused at this. "And is that all, mio fratello, Flavio?" Flavio crosses his arms, grabbing yu and forcing you into the chaiir before leaving the room, again slamming the door. "Ah~ mio fratello maggiore always with the temper," He sighed, before giving a small laugh. Thn, his eyes  zeroed onto you. "Now, Mr. Jones. It\'s wonderful t finally see you face too face, wuldn\'t you agree?" No, you wouldn\'t cause across from you sat Allessandro Vargas, one of the most ruthless bastards to ever enter the underground.', "OPTIONS: " + "\nA: Wait Until he Continues", 'You srink down into the seat of the chair, avoiding the gaze of the Mob boss. Always the one to find trouble, weren\'t you?', None, None, None, None)









Abitur_Heart = 0

node = Intro_game_start

while True:
    if node == Into_building:
        node.relations_NPC(node)
        
    if Abitur_Heart == 1:
        node.change_options(node)
    
    
    print node.scene
    print node.options
            
    command = raw_input('>').strip().upper()
    

     
    if command in ['Q', 'EXIT', 'QUIT']:
        print "REALITYSANILLUSIONTHEUNIVERSEISAHOLOGRAMBYEGOLDBYE"
        sys.exit(0)
         
    

            
                    
    elif command in ['A', 'B', 'C', 'D', 'E']:
             
        try:
            node.scene_change(command) 
        except:
            print 'Invalid input. Input a valid option.'  

    


