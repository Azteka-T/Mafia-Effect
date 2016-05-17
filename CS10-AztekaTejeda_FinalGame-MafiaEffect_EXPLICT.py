# -*- coding: utf-8 -*-
import sys


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

Associate_start = story_line('Into_building', None, None, None, None,\
'The back of the van didn\'t automatically make the most comfortable seat in the world, nor did the occasional bump in the road make it any better. You tried to avoid looking the other man who sat in the back with you, instead choosing to focus on why you were here in the first place. You were a Jack of most trade, dipping your fingers into various jobs as you tried to make a living in the world. A recent friend of yours had mentioned your name to the Don of the local criminal group, and the next thing you realise you\'re here and sure that you were about to do something you hadn\'t before. Before you could begin the dream of what your possible future would look like, the van slows down to stop. The gruff man sitting across from you stands and clambers out of the vehicle, as the driver and front seat passenger do the same', "OPTIONS: " + "\nA: Get out of van", 'You follow after the three men, nervousness chewing away at your insides. You didn\'t know what reason you were here for, just the brief statement from when you were first picked up, \'Don wants us to test you.\' Great. Just the attention you needed.', \
None, None, None, None)

Into_building = story_line('accept_gun', 'refuse_gun', None, None, None, \
'You follow the three men, doing your best not to stray too far behind. The building they entered is and old apartment building which seems to be decaying under their feet. Up the stairs they went until they eventually reached an apartment numbered "3D”, and the tallest man, whom you assume is the leader of this operations motions for the other two to kick down the door. It falls to their strength quickly, and in they go. You follow quickly, only to see they two men who kicked down the door holding a third, new man down who struggled, pleading with the leader. The leader scoffs before motioning you over. You walk over and he points to the man. "This man owns Vargas some money, and is late to paying him back. Vargas is not a patient man, and this свинья\'s time has run out.” He offers you a small pistol, looking at you expectantly.',\
"OPTIONS: " + "\nA: Shoot the man " + "\nB: Refuse" , \
'You accept the gun, cocking it and walking towards the now blabbering man. He screams something about his family, saying he couldn\'t help his addiction, and please to spare him, allow him to live, he\'ll have the money soon if just given more time', 'You shake your head, staring at the leader as if he had gone mad. To kill a man for his debt, what had your friend gotten you into?', None, None, None)

accept_gun = story_line('kill_him', 'refuse_kill', None, None, None, 'You stare down at the man, aiming the pistol directly at his forehead. His pleas and cries become louder, and you can see the tears and snot running down his face. You momentarily pause: are you able to take away another human\'s life?', "OPTIONS: " + "\nA: Kill Him " + "\nB: Suggest another option", 'You realise, yes, that you can take another human\'s life, and give the man a small smile. You see the hope spark breifly before pull the trigger, and the loud bang echoes in the small, dirty apartment.', 'You lower the gun, looking back the leader. "Instead of wasting a bullet in this scum, what about we break his legs or something? Give him some time try and gather some fund, with some preview of what will happen if he doesn\'t?', None, None, None)

refuse_gun = story_line('kill_him', None, None, None, None, 'The leader sneers at you, before smacking you with the butt of the gun. "Don\'t give me any of that fucking shit, you damn wuss. Take the gun and shoot his ass, or else I\'ll shoot you instead, you got that?', "OPTIONS: " + "\nA: Take gun and kill the man", 'Fearful, you take the gun and cock it,walking over and aiming it at the man. Unable to look him in the eye, you glnce away and pull the trigger. The resulting bang hit you like a ton og bricks.', None, None, None, None)

kill_him = story_line('meet_don_first', None, None, None, None, 'The man now lies dead on the floor, peices of brain matter, skull fragments, and blood splatters lightly coat part f the surroundings as his brain pours out from the back of his head. His eys are wide and unseeing, making you look away before you do something like throw up. Your hand shakes lightly with the realisations of what you have just done.', "OPTIONS: " + "\nA: To Don's ", 'You are patted on the back before the gun is removed from your grip, and you travle with the group of three down to the van. You had heard your first kill would be hard, but you didn\'t imagine you would evr have to commit it.', None, None, None, None)

refuse_kill = story_line('to_van', None, None, None, None, 'The leader sneers breifly befre just conceedinging to your idea. "Alright boys, break his left leg and a few fingers on both hands. Meet me back at the van when you\'re done. You-" He stated, pointing at you, "-With me." With that, he turned and left the room.', "OPTIONS: " + "\nA: Follow After", 'You take one last look behind you and leave, ignoring the sound of a snap and loud painful screams that follow after it. It\'s best if you didn\'t stick around anymore than needed.', None, None, None, None)

to_van = story_line('meet_don_first', None, None, None, None, 'The leader of the operation climbs into the passnger side of the car, and you into the backseat of the car. You\'re breifly startled when he speaks up, "Kid, I\'m not sure what type of life you used to live, but out here it\'s dog eats dog, and you\'lll need to understand that if you want to surviv, understand? Dont go around and try to pull that type of shit again, or you\'ll be the one with the barrel in between your eyes. Sutton told us some good things about you, don\'t prove him wrong now.”', "OPTIONS: " + "\nA: Nod", 'You nod in response, staring down at the floor n silence as you both wait for the other two men to finish.', None, None, None, None)

#meet_don_first = story_line('proposition', 'flattery', None, None, None, 'Eventually, the van starts up once again, and you and the three men are driving again. Nothing is mentioned about the incident in the apartment complex. You notice you are in the north side of tow when the van comes to a stop and everyone clambers out again execpt for the driver. The leader motions for you to follow and you do. "The Don wants to see you," He said flatly, as he led you through the halls and towards what you assumed was the office door. "Don\'t fuck up or your head will be on a silver platter in less than ten."  Withthat simple warning, you were pushed inside the now open door. Stumbling slightly, you quickly corrected yourself as you noticed the other presence in the room. You turn your eyes to the floor. "Don\'t be modest," Come the calm, collected voice of the Don. "My good friend has told me alot about you, Winston Russel, ad I can say that I\'m slightly impressed with your skill set, though I have seen better.", None, None, None, None, None)

meet_don_first = story_line('proposition', 'flattery', None, None, None, 'Eventually, the van starts up once again, and you and the three men are driving again. Nothing is mentioned about the incident in the apartment complex. You notice you are in the north side of tow when the van comes to a stop and everyone clambers out again execpt for the driver. The leader motions for you to follow and you do. "The Don wants to see you," He said flatly, as he led you through the halls and towards what you assumed was the office door. "Don\'t fuck up or your head will be on a silver platter in less than ten."  Withthat simple warning, you were pushed inside the now open door. Stumbling slightly, you quickly corrected yourself as you noticed the other presence in the room. You turn your eyes to the floor. "Don\'t be modest," Come the calm, collected voice of the Don. "My good friend has told me alot about you, Winston Russel, ad I can say that I\'m slightly impressed with your skill set, though I have seen better."',"OPTIONS: " + "\nA: Ask about proposition" + "\nB: Flatter", 'You frown a bit, trying not to let your nervousness known. "I heard you have a proposition for me?" You bite out awkardly.', 'You smile, and respond to the Don\'s statement, "And I\'ve heard a few things about you, yourself, Mr, Vargas. Horrow stories about your and your knives seem to be the most popular ones however.', None, None, None)

proposition = story_line('choice_capo', None, None, None, None, 'The Don tilts his head, and lean forward in his seat, eyes gleaming with various emotions as he studies you. "Mm, indeed I do. You see Winston, I hope you don\'t mind if I call you that, right? I figured, hearing such stunning reviews from Sinclair, I\'d graciously allow you to join my fine business here, what do you say? All previous prefomances aside."', "OPTIONS: " + "\nA: Continue ", 'You nod, waiting for him to continue.', None,None, None, None)

flattery = story_line('choice_capo', None, None, None, None, 'Mr. Vargas waves his hand with a small chuckle, "Trying to flatter me are you? Yes, yes, I know all about those stories. I\'ve heard them all along with various variations. My brother is fond of telling me them as soon as he hears a new one." He shakes his head as he thinks of brother. "Nevermind all that, however. I do have a choice for you to make."', "OPTIONS: " + "\nA: Continue", 'You fall silent and wait for the Don to contiune.', None, None, None, None)

choice_capo = story_line('extermination_capo', 'prostituion_capo', 'torture_capo', 'weapon_capo', None, '"You see, I have four divisins within my group here, and I figured you\'d like to at least choose which one of my Caporegime you will work under." Saying no to choosing one simply wasn\'t an options you realize, and wait for him to explain what options there were. "I have four Capos, Vladimir in charge of extermination, Luther with weapon management and shipment, Marelda leading the torture ring, and finally Racchka with our spy network and prostitution ring. So, Winston, care to pick one of my fine sub-leaders to wokr for? Hurry up, I\'m not a patient man."', "OPTIONS: " + "\nA: Join Extermination Squad" + "\nB: Join Weapon Management" + "\nC: Join Torture Corp" + "\nD: Join Prostitution Network", 'You rub your hands together nervously as you think it over. You think back to the apartment complex earlier, and what had transpired there. "Extermination," You say with only the smallest sense of hesitation.', '"Weapon managemnet," You say with a small shrug of your shouders. It seemed like the easiest out of all of them, and you hope that your assumption was correct.', '"Torture," You state, firmly. You felt like you had the stomach to handle that type of job, and you only could hope that you weren\'t wong with that thought.', '"Prostitution?" You say, almost as if it was a question. He had said it was a porstitution ring along with a spy network of sorts, right?', None)

extermination_capo = story_line('meet_exter', None, None, None, None, 'The Don\'s eyebrow arches. "Enjoyed your time with Vlad, I\'m guessing?" He grinned, before making a shooing motion. "I\'ll be sure to make a note of this and do the proper work for it later. Go down to Warehouse 3, that\'ll be the main base of operations. Good luck. I expect to hear great things about you Mr. Russel. Don\'t disappoint me now."', "OPTIONS: " + "\nA: To Warehouse", 'You nod, and leave the room, leaving the mansion style building to go hail a taxi. You soon reach your destination and give a knock to what you assumed were the entrance doors to the old building.', None, None, None, None)

weapon_capo = story_line('meet_weap', None, None, None, None, 'The Don shrugged. "Not what I was expecting for you to choose in all honesty, however it somewhat suites you I suppose basing off what I know of you and a what a few background checks have told me. And lucky for you, there\'s a recent opening. Lutz only likes to work with around ten people, and if you had asked to join three hours ago, coldn\'t have letcha. Now go on, you\'ll be needing to head towards the storage units south of the shopping mall. There, you\'ll be taken to Lutz." The Doon nodded, flashing you a grin before dismissing you with a flick of the hand.', "OPTIONS: " + "\nA: Head to Storage Buildings", 'You stare for a moment more, then turn and leave the room. You would have thought something more would have occured, but you were wrong. You sighed, exiting the building and hailing a cab for the short ride over.', None, None, None, None)

torture_capo = story_line('meet_tort', None, None, None, None, 'The Don let out a small laugh. "No beating around the bush for you, huh Mr. Russel? You\'d need practice no doubt, but Marelda is always willing to take a new person under wing. Hopefully you last longer than the last one. Lucky for you, Marelda\'s in the building already, so I\'ll have someone to escort you to her in the kitchen, or rather.. I\'ll just take you there myself. I need to see what\'s taking so long on my damn coffee anyway." He stands, walking around his desk and towards the door.', "OPTIONS: " + "\nA: Follow Don", 'You quickly fall in line and trail after the Don, absently wondering why Marelda, whom you inferred was the leader of the torture corps was doing here, and in the kitchen no less.', None, None, None, None)

prostitution_capo = story_line('meet_prost', None, None, None, None, 'The Don chuckles at your answer, staring at you with mirth dancing in his eyes. "I\'ll admit, you caught me a tad off guard there. Not many are willing to play the part of a cheap fuck and open their legs for just anyone to slip in between. Though, looking at your build, you might be working as a guard instead for her workers," He tilted his head, still staring intensley. "Head to the apartments toward the south of town, the ones on Lincon Street. Racchka should be in today, in the one with two burly men stadning on the front porch. Go now, and tell Racchka I said to expect Sinclair later tonight."', "OPTIONS: " + "\nA: Head to Apartment complex", 'You give a small nod, ears burning with some embarrassment. You left the room with the dismisal, finding your way outside and looking to hail a taxi since you had your car at home and no firends to drive you.', None, None, None, None)

meet_exter = story_line('find_abitur', None, None, None, None, 'Eventually, you arrive at your destination, and stare impassively at the warehouse. You walk up toward the building, and a hand lands on your shoulder. You jump a little, and turn to see the leader from earlier. "You decided to work with us, then?" He asked, amusement coloring his tone. "I want you to know however-" His hand on your shoulder tightened, "-"We don\'t tolerate any weak links in the chain. If you step one toe out of line, well.." He gave a gruff laugh, loosing his grip and hitting you on the back, hard. You had to stop yourself from stumbling. "You\'ll find out, won\'t you? Now, go inside, find a small perky blonde named Abitur. He\'ll introduce you to whomever is around and tell you the ropes."', "OPTIONS: " + "\nA: Find Abitur", 'You gve the man a small, fright filled look as your imagination ran ramped with what exactly could ahppen if you failed to follow orders. Giving a nervous smile, you walked inside, and attempted to find Abitur.', None, None, None, None)

find_abitur = story_line('nervous_greet', 'bad_abi_greet', None, None, None, 'You didn\'t have to even attempt to search as a short man quickly bounded over, and stopped in front of you. "Helllo~!" He chirped, giving a small wave. "Who\'re you?"', "OPTIONS: " + "\nA: Introduce yourself" + "\nB: Respond Sarcastically", '"Oh, I\'m Winston Russel. I was told to look for an Abitur?"', 'You snort, staring down at the man who reigned a few inches shorter than you. "What\'s it to ya\' Short Stuff? I\'m supposed to be looking for someone named Abitur." You glance away and look around the warehouse space.', None, None, None)

nervous_greet = story_line('pleased_meet_squad', None, None, None, None, 'The shorter man beams, and grabs your arm in a firm grip. "Well, you\'re looking at \'im! Second in Command for the Executioners for one Allesandro and Flavio Vargas!" He dragged you along with him. "I\'m assuming you\'re a new recruit? Vladdy wouldn\'t send someone to find me, at least that\'s whom I think sent you, yeah? He\'ll probably want me to show you the ropes, so don\'t worry I got that covered. I\'ll show you around, and introduce you to who\'sever around and then we\'ll be off to the storage lockers on the other side of town for your weapon!"', "OPTIONS: " + "\nA: Stare incredeously", 'You stare at the man who seems to defy what exactly you would have imagined a man in this profession would act, and let him continue on his mad ramble as he forced iformation after information at you. At this point, it was easier to let him drag you away than to put up much of a fight. Plus, Abitur had a strong grip for someone so short.', None, None, None, None)

bad_abi_greet = story_line('ignore_squad_greet', None, None, None, None, 'Suddenly, you\'re grabbed by the front of your shirt and roughly pulled down to Abitur\'s eye level, where you stare into the eyes as anger burns behind the like pools of lava. "Listen here, you little brat. Don\'t you dare start making assumptions about me because of my height and the way I choose to act or trust me, a bullt will end up in the back of your head sooner or later, I can guarentee it." He let go of your shirt, and went back to his seemingly bubbly self. "As long as you remember your place on the pecking order, we won\'t have any problems! I\'m assuming you\'re a new recruit so let\'s meet the crew will quick and then I need you get some form of weapon to do your job with, hm?"', "OPTIONS: " + "\nA: Nod Dumbly" , 'You blink, and stare as the blonde happily moves away from you, heading towards the other side of the warehouse where some people were loitering, cleary staring. "Come along!" Abitur shouts, and you move to catch up.', None, None, None, None)

pleased_meet_squad = story_line('storage_weapon_visit', None, None, None, None, 'Suddenly, you\'re pushed in front of a group of four people. They stare at you, some giving looks of sympaty, others merely looking on with amusement. "Squad! Meet Winston, Winston, Squad." Abitur said, gesturing with grand hand motions. They each gave a half-hearted greeting. "Mmkay, that\'s done so let\'s go get your guns huh?"', "OPTIONS: " + "\nA: Nod", 'He beams again. "I have my car parked out back, let\'s go then!" And once again, you\'re dragged off to another door opposite from the one you entered fron.', None, None, None, None)

ignore_squad_greet = story_line('storage_weapon_visit', None, None, None, None, 'You make it towards the crowd of four people eventually, whom Abitur is already chatting pleasantly to. They glance at you, one of them even sniggering. They don\'t greet you, eyes glancing towards you before falling away, dismissing you immediatly.', "OPTIONS: " + "\nA: Stand awkwardly", 'You stand there for awhile as they chat, only catchig bits and pieces of of what they were talking about. You did hear Sinclair thrown around a few times however. Eventually, you are lead away towards Abitur\' car.', None, None, None, None)

storage_weapon_visit = story_line('meet_lutz_visit', None, None, None, None, 'as you both sit in the car, on the drive over to get your weapons, Abitur speaks up. "Now, a few things to know abut our squad. Vlads may have choosen not to give you the talk, however, we don\'t appreciate disresepct, and as our newbie of the group, if you show  any disrespect, you\'ll be kicked back under the porch with the rest of those who think they can play in the big league, understand? ano talking back, and just do as you\'re told." Abitur looked at you from the corner of his eye as the car pulled up to the storage and waited until the gates opened before driving inside. "Come on, let\'s get this done and then you can go home for the day. Tomorrow will be your first job most likely."', "OPTIONS: " + "\nA: Nod and Follow", 'You merely nod, elicting to remain silent and getting out of the vehicle, trialing after the short man as he headed down the rows of different storage units towards what seemed like an office towards the back.', None, None, None, None)

meet_lutz_visit = story_line('gain_first_weapon', None, None, None, None, '"Abitur? Vhat are you doing here?You\'re not do for anozer upgrad until your mission next month," A thickly present German accent floats through the air as a blond male steps out from the office, looking a tad confused, unti he spots you trailing behind the shorter male. "OH, are you here for a neue recruit?" He hums as Abitur nods. "Vell, I wasn\'t expecting to have to hold back any new guns from the recent shipment, but I suppose ve can part with a few standard. Maybe two small, and a few knives if ve have any extra ones laying around. Come along, we are going to 7C." He said, pointing off towards a certain row of units. "I already have something in mind."', "OPTIONS: " + "\nA: Follow to storage unit", 'You duitfully follwo the two men, making sure to tag alon behind them at a distance of five feet.', None, None, None, None)

gain_first_weapon = story_line('home_night_one', None, None, None, None, 'when they arrived in front of the unit, Lutz pulled out a set of keys, quickly finding the right one and unlocking the door, lifting it open. Inside was a variety of guns an ammo neatly lining the walls along with a knife or two stikcing out oddly among the ranged weapons. "I zhink a Kimber and perhaps a Beretta for you." The German stated, walking to a case and retriving two guns from it and placing them aside as he searched around for a knife and some ammunition. "Ah, here we are. One neck knife and zero tolerence, and you should be set. Just need a holster or two-" He removed the items he needed, before setting them all into a seperate box. "Zhat should do for now. Upgrads norally come when you get promoted or you require somzhing for a mission. Then perhaps you choose." Abitur took this time to speak up. "Go home now, and take your equipment with you. You\'ll need at least one gun on you at all times along with a knfe."', "OPTIONS: " + "\nA: Head Home", 'You nod, staring at the box you were given before hesitiating a moment. Box in hand, you sighed and left, planning on just falling alseep and figuring out the rest in the morning.', None, None, None, None)

home_night_one = story_line('mission_choice_next', None, None, None, None, 'You placed the box on your dresser as you walked into your room, yawning, tired from the events and scares of the day. Not even choosing to change out of your clothes, you fell asleep as soon as you fell onto your bed.',"OPTIONS: " + "\nA: To Next Day", 'You do not wake until the next day comes.', None, None, None, None)

mission_choice_next = story_line('rid_bdy_docks', 'pick_up_rat', None, None, None, 'The next day you drive dow to the same warehouse as yesterday, the morning sun being as unfriendly as ever. You had the Kimber at your waist, Beretta in the glov compartment, and your neck knive hidden under your shirt. You parked around back, making sure you locked the doors, and then headed into the building, which as surprising open. Glancing around the space, only two people were currently present: Abitur who was on a stuhl snoozing and Vladimir who was in the process of walking to the other side of the building. He stopped upon noticing you, and motioned you over. "I Have something for you to do today. They are simple enough, and I\'ll even let you choose your first mission. We have a dsposal that needs to be take care of before noon and there appears to have been a rat dsicovered last night that needs to be delivered to the Torture head. So, which will it be?"', "OPTIONS: " + "\nA: Accept Disposal Job" + "\nB: Accept Pickup/Delivery", 'The dispossal seemed simple enough, right? "I\'ll help with the disposal."', 'You hum. Delivering a person would just be like delivering any old thing, like a dresser or something. Execpt dressers probably don\'t scream while you do. "I\'ll do the delivery."', None, None, None)

rid_bdy_docks = story_line('to_docks_rid', None, None, None, None, 'Vladimir nodded, before looking down at his watch. "I\'ll be sure to let Drago know that you\'re on your way. You shall meet him by the docks and do everything he says am I understood?" You nod. "Good, then get going. I want you two back before three at the latest."', "OPTIONS: " + "\nA: Head to the docks", 'You nod, and start heading back towards your car. Barely arriving and you\'re already eing sent away on something. You idly hoped it wasn\'t going to be like this all the time during your time working here. With a sigh, you merely climb into your car and do your best to driver over towards the docks as quickly as possible.', None, None, None, None)

pick_up_rat = story_line('rat_pickup_prost', None, None, None, None, 'You\'re new boss nods in acceptance. He motioned towards the sleeping man. "Take Abitur with you for this. You\'ll need someone to sit in the back to make sure he doesn\'t try and stupid or reckless. Abitur will know where to go."', "OPTIONS: " + "\nA: Wake up Abitur", 'You nod, heading over to the dosing male and tapping him lightly on the shoulder. He stirs, and you merely explain the situation to him. He sighs, but follows you to your car anyway, and merely tells you where to go.', None, None, None, None)

to_docks_rid = story_line('ask_about_drago', None, None, None, None, 'Arriving at te docsk, you notice there\'s another car parked further away, this one closer towards the docksfor what you assumed was easy load onto the boat. Climbing out of yourcar, you head over and a man, about an nch taller steps out of the car and greet you with a hand shake. "Hello, you are Winston, yes? Good? Alright. Help me carry the chum to the boat, and then we are off." "Chum?"You ask, confused. What happened to a body? "Body is in chum," Drago quickly explains. "Much qucker to just feet the fishes, instead of doing something stupid likem getting hyenas. Just help load them. The quicker this is done, the faster I can go grab a drink."', "OPTIONS: " + "\nA: Load Body onto Boat", 'You don\'t say anything more after that, helping Drago with the two coolers of chum to load them onto the boat. You cast a weary gaze around before climbing onto the boat as well.', None, None, None, None)

ask_about_drago = story_line('throw_chum_over', 'friendly_joke', None, None,None, 'You assit Drago with loading the two coolers. as you clamber onto the boat, both coolers load, you glance over at Drago, "So, how long have you been working with Vladimir and Vargas?" You ask, attempting to start some type of conversation. Drago snorts,unhooking the boat and heading towards the steering wheel. He motioned you to follow, and you did as he started up the boat and drove off further into the waters. "I\'ve been working for Vargas for four years now, and Vladimir for only one. Though, Vladimir is better than the last Capo, I don\'t like the way he talks back to VArgas sometimes. Won\'t bode well when Vargas finally finds someone who can replace him, could replace him." You two drew into silence for awhile, before the Drago eventually slowed the boat down to a stop.', "OPTIONS: " + "\nA: Throw Chum Over" + "\nB: Make a Joke", None, None, None, None, None)







    
    












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

    


