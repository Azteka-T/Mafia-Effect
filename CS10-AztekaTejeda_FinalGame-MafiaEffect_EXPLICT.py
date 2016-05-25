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

game_start - story_line('deny_prost', 'accept_prost', None, None, None, 'You often pondered where in your life you had gone of the righteous path and stumbled of the side, crashing straight into hell. Standing alone within the entrance hall of a rich Don\'s house (clearly, he made no attempt the hide this as how lavish the room, and no doubt the rest of the house was decorated), you mused as you took another chance to glance around, staring at all the different art pieces scattered about, trying to do anything from keeping you from becoming even more bored thena you already were. You didn\'t want to move and start touching anything, nor did you want to go and piss off anyone anytime soon. So you stood, as you have done, waiting for that pink haired man who had left you here in the first place to return, and mke do on his promise to come and retreive you so you could meet the don of this place. Not as if you had a choice, of course. You weren\'t looking forward to it. As you began to imagine how much profit you could possibly make by selling only two peices of art from the entrance hall alone, a sharp voice cuts through your train of thought. You flinch at the sound at the unexpected noise. Looking for the source, you see a female in her early twenties sauntering over, a purposeful sway to her hips. Her deep red curls bounced with each step, framing her face, blue eyes standing out on the beige skin tone, and as she was finally a few feet away she made her move, grabbing your arm and looking up into your eyes, batting her eyelashes. Trying to ignore her very obvious assests pressing on your arm, you try and retain only eye contact with her. "So, what a good lookin\' guy like yaself doin\' all by yah lonsome, huh, han\'some?" She asked, one of her hands trailing across your chest. "\'Cause I wouldn\' mind showin\' ya around myself, ya know? So how about it han\'some?"', "OPTIONS: " + "\nA: Reject Her Offer" + "\nB: Accept Her Offer", 'You give her a sheepish grin. "Sorry, but I\'m going to have to reject that... tour." You turned your gaze upward when you felt her grip on your arm tighten. "I\'m here to see someone."', 'Staring down at her, and maybe a little lower than that to where she gripped your arm, you gave her a grin. "Why, of course I would love to have a beautiful doll such as yourself show me around." All previous arrangements forgotten, you were more than willing to trail after her where ever she wanted to go if you got a peice of tail.', None, None, NOne)

deny_prost = story_line('flavio_pos', None, None, None, None, 'She pouts, ready to try again, only to cut off as another voice interrupts. "I would prefer if you didn\'t try and seduce our new recruit, you damn cagna. Go back to that Succubus of yours, and tell her that she should try and keep track of her demone least one looses a finger or two." The female stiffened, and she shot a glare towards the pink haired male who had retunred to the scene. "Jealous, are we Flavio?" She crowned, "Or you too pissed about not being able to fuck that Capo of yours?" She sneered, releasing you from her grip and flipping him off. Flavio merely glared as she stormed off in a huff, simply avoiding continuing the confrontation.. He turned his attention to you as soon as she was gone from sight. "You, come along. The boss doesn\'t like the be kept wainting.", And he too, walked swiftly down the hall he came from.', "OPTIONS: " + "\nA: Follow", 'You looked at the scene with amusement, and when given the order, you followed without hesitation. Obviously, ther\'s a story to that and you wouldn\'t mind finding out more about it..', None, None, None, None)

accept_prost = story_line('flavio_neg', None, None, None, None, 'Her eyes light with victory, and she begins to tug you towards the staircase, where you assume the bedrooms are, or in the very lleast, some type of empty room. "One step further, and I will place a bullet in either of you." A voice interrupts your  no doubt perverted thoughts, and you both tense at the third party. The lady releases you, and turns around to face the owner of the voice, and you quickly do the same. The man with the pick hair has returned, and you can clearly feel his anger boil off him in waves. "Puttanella, go return to the Succubus before either of you find another poison finding its way into your food." She turned a tad green at that, probably in remembrance of an incident in which that occurred. She merely sneered, wanting to say anything in retaliation but she decided against it. Turning to you, she batted her eyelashes once more, and with a purr of \'Call me sometime han\'some\', she left you alone with the pink haired male. He turned his disgusted expression on you, moving to grab your arm roughly and dragging you away from the stairs to a hallway.', "OPTIONS: " + "\nA: Follow", 'You stumble at this action, but quickly correct yourself and easily keep pace with the angry man. Whoops. You almost forgot why you weere here in the first place', None, None, None, None)

flavio_pos = story_line('prop_a', None, None, None, None, 'He lead you to a room with one guard posted outside. The burly man nodded in  greeting and opened the door. Favio enters first, and you enter soon after. "Ah! Fratello!" A voice calls, a smooth baritone that sounds odd with the cheerful tone. "Back so soon? Oh, and that must be Mr. Jones! Do come in, I\'ve simly been waiting all day to see you! Flavio, carissimo Fratello, go.. do something." Flavio huffed, shot the Don an irritated look, before leaving the room and shutting the door behind him without an arguement. Now you sat alone with the Don, Allessandro Vargas of the Romulus Familiga, known for their ruthlessness and brutal methods to get their way in any situation. You gulped. "Now, Mr. Jones, there\'s no need to be so tense. I\'ve only heard quite good things about you and your preformance abilities, of course. The reason your here, actually."', "OPTIONS: " + "\nA: Wait for him to continue", 'You shift where you stand, not saying a word and your gaze low. What could this man know about you?.', None, None, None, None)

flavio_neg = story_line('prop_b', None, None, None, None, 'The door that appears to be the designation has a guard in front of it, who stares at you two with barely hidden amusement. Opening the door for you two, he steps to the side as the pink haired man shoves you through before following himself, slamming the door closed. As soon as it does, he begins a ranting in what you assumed was Italian, but you were never really well-versed in languages. When the small rant ends, and the pink man has run out of steam, you have notied the man sitting behind the desk is terribly amused at his display. "And is that all, mio fratello, Flavio?" Flavio crosses his arms, grabbing you and forcing you into the chair across from the Don before leaving the room, again slamming the door with a huff. "Ah~ mio fratello maggiore always with the temper," He sighed, before giving a small laugh. Then, his eyes flashed toward you. "Now, Mr. Jones. It\'s wonderful to finally see you face to face, wouldn\'t you agree?" No, you wouldn\'t because now that you actually looked, across from you sat Allessandro Vargas, one of the most ruthless bastards to ever enter the underground.', "OPTIONS: " + "\nA: Wait Until he Continues", 'You shrink down into the seat of the chair, avoiding the gaze of the Mob boss. Always the one to find trouble, weren\'t you?', None, None, None, None)

prop_a = story_line('extermination', 'prostitution', None, None, None, 'You didn\'t mean to say  it but - "Why is it that I\'m here, Mr. Vargas?" The Don blinked, before smiling a tad too brightly. "Why, because you owe me of course! Why, you didn\'t think that lawyer and bribe money simply appeared out of thin air, did you? Why, of course not! So, in exchange for helping you escape your prison sentance, I\'ll be asking you give me say.. what was your supposed sentence, ah yes." His eyes gleamed eerily. "It was a life sentence, wasn\'t it? So I will merely require the same of you. Until you either die, or become worthless to me, you will work under me and my regime or you would sooner find a bullet through your heart. Understoood, yes? And now that we have that out of the way, I\'ll be generous enough to offer you two positions you could possibly choose from. Would you prefer to work in extermination, or prostitution? So how about it cagnolino? Which will it be?"', "OPTIONS: " + "\nA: Extermination" + "\nB: Prostitiution", '"Extermination," You answer, clearly irritated at having this man hold your leash, and your life as such. At least this way, you could take out some frustrations through other, unfortunate souls.', 'After a brief moment of hesitation, you simply sigh and present him your answer. "Prostitution." It hopefully wouldn\'t be too bad of a thing to do for the apparent rest of your life.', None, None, None)

prop_b = story_line('extermination', None, None, None, None, '"Winston Jones, born to common street whore and some business man away on trip who decided to cheat on his wife. Previous leader of the Rising Kings, fell when a rat sold you out to the police. Known for his prefered killing method, a gunshot to the lung, allowing the victim to drown in their own blood, before you carved in your insignia. Simple, but workable. Now, mio Fratello, singing his curses, told me about your little encounter with one of my girls, and because of that, I\'m afraid you don\'t get a choice of being able to work in the prostitution branch since you can\'t seem to handle yourself around women, much less ones who whore themselves out for cash and information. So you\'ll put those killing skills to work, huh? Don\'t worry, you\'ll know it\'s all for the benefit of me, myself, and maybe Flavio and Sinclair if I feel generous enough."', "OPTIONS: " + "\nA: Join Extermination", 'You knew that you didn\'t have a choice, and that was glaringly obvious to you. It was either this or lose your life. You sighed.', None, None, None, None)

extermination = story_line('first_day_ext', None, None, None, None, '"See? That wasn\'t too hard, now was it? It should be such an easy thing for you to do so don\'t go around and complain to much, do you hear me? Now, I\'m sure you can see yourself out. I have a few calls to make. Expect a black volga to be outside at 7 in the morning. You\'ll need to get into it with no questions. You\'ll meet Vladdie then. Now shoo with you, cognolino." He waved you away with his hand, grabbing his flip phone from his desk and quickly dialing a number, placing it to his ear. "Vladdie, baby, light of my day! Come stai oggi? No? Non va bene... My, you guess it, clever aren\'t you? Oi, I am not you bastardo russo." ', "OPTIONS: " + "\nA: Leave for Home", 'Seeing as you clearly weren\'t needed anymore, you left the room as quickly as you could, trrying to not to seem as if you were fleeing. Stressful days were ahead, no doubt about it.', None, None, None, None)

prostitution = story_line('first_day_prost', None, None, None, None, '"Allessandro rose an eyebrow at this. "Honestly, I feel as if you\'re somewhat going to waste there, since all my ladies do is gather information and sell themselves to the highest bidder but Racchka will give you the full rundown of that division tomorrow and find somewhere to place you. Now, leave and I\'ll have a car to pick you up in the morning. Be ready by 7 or the driver will drag you out of bed, dressed or not. Get it? Yes? Good. Now I have a call or two to make." The Don hummed, whipping out his phone and making a call. "Racchka, amore, dolcezza. Tutto bene? Yup. You\'ve seen his picture, do what you feel is best."', "OPTIONS: " + "\nA: Leave for Home", 'Seeing as you were completely ignored, you merely left the room without another word, planning on just going home and collapsing into bed, and trying to process what the hell you life was coming to.', None, None, None, None)

first_day_ext = story_line('demo', 'demo', None, None, None, 'The next morning brings a ringing head ache, as the events from the previous day came rushing back, causing you to groan and roll out of bed. Knowing that if you werenn\'t on time, it yould be your ass on a silver platter, you hurried through your routines in your new apartment, stumbling aroud half awake. When that time came you walked down the stairs of your apartment to see the black volga where he said it would be. You enter the said car and only manage to sit down nd close the door before it drives away. You are thrown back against the seat at the sudden start. Blinking, you notice another person is sitting next to you, at the other window. He is a broad shouldered man dressed in dark colors, a solider cut hairstyle, and is taring straight at you.', "OPTIONS: " + "\nA: Introduce ourelf" + "\nB: Say nothing",  'Unsure what the proper protacol would be, you give him a nod of the head and grant him your name to try and rid the car of the strange tension you find yourself experiencing. "Winston Jones," You state, only falling silent when he continues to stare.', 'Licking your lips, you stare back for a minute, letting the silence in the air become thicker. You wait for the other man to do so first, and make no attempt yourself.', None, None, None)

first_day_prost = story_line('demo', None, None, None, None, 'As the next morning came, you found yourself dressed and ready to leave far too early. Sitting down at the table in your small kitchen, you sigh, and stare at the wall. Eventually, you stand when the time comes, and leave the apartment for the black car sitting almost innocently at the curb, door already open. You sigh, and enter te vehicle, closing the door just in time as the car pulls away from the curb. Aside from you and the driver in the car, there is an envelope on the chair of the seat next to yours, where yuur name is written in a fancy cursive font. Loooking at the driver breifly, you reach for the letter.', "OPTIONS: " + "\nA: Open Letter", 'Staring at your name on the letter, you do eventually tunr it over and use your thumb to tear it open. Pulling out the sheet of paper, you begin the read.', None, None, None, None) 

demo = story_line(None, None, None, None, None, 'Congradulations on reaching the end of the DEMO version of the game. We at CiFy hope you enjoyed your gaming experience and would be delighted at any feedback you have for the development of this game. Have a Nice Day!', "OPTIONS: " + "\nA: End DEMO", 'Good Bye.', None, None, None, None)







node = Intro_game_start

while True:
    if node == demo:
        sys.exit()
        
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

    


