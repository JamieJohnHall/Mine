# Print page header
def page_topper(header):
    print("\n" * 80)
    print("\t\t      GIVE YOURSELF GOOSEBUMPS")         
    print("\n\t\tESCAPE FROM THE CARNIVAL OF HORRORS")
    print("\t\t-----------------------------------")


# To get Wheel of Chance result on PAGE 9
import random

def spin(wheel_of_chance):
    wheel_of_chance = (random.randint(1, 8))
    if (wheel_of_chance ==  1) or (wheel_of_chance == 5):
        wheel_of_chance = 'PAGE 38'
        return wheel_of_chance
    
    elif (wheel_of_chance == 2) or (wheel_of_chance == 4):
        wheel_of_chance = 'DOUBLE OR NOTHING - PAGE 19'
        return wheel_of_chance

    elif (wheel_of_chance == 3) or (wheel_of_chance == 6):
        wheel_of_chance = 'SPIN AGAIN - PAGE 9'
        return wheel_of_chance

    elif wheel_of_chance == 7:
        wheel_of_chance = 'FREE SPIN - PAGE 49'
        return wheel_of_chance

    elif wheel_of_chance == 8:
        wheel_of_chance = 'NO CHANCE - PAGE 15'
        return wheel_of_chance

wheel_result = spin('wheel')


# Reader still reading?
def reading_still(answer):
	still_reading = input("\n\tAre you reading on? YES(y) NO(n)...")
	return still_reading


# Choose a page
def choose_page(answer):
    new_page = (pages[input("\n\tChoose Page ... ")])
    return new_page


# Readers name
page_topper('top')
reader = input("\n\tWhat is your name? ... ").lower()


# PAGES

pages = {

# INTRODUCTION - PAGE 0
    '0': (f"""\n\tBEWARE! {reader.upper()}
\tDO NOT READ THIS
\tBOOK FROM
\tBEGINNING TO END!

\tWelcome to the carnival of horrors. This is no
\tordinary carnival. Here you'll find awesome
\trides. Exciting games of chance. And the weird-
\test Freak Show ever.
\t  Do you enter?
\t  Are you brave enough to risk the Supersonic
\tSpace Coaster? Will you know whom to trust-
\tthe Snake Lady or the Three Headed man? Can
\tyou make it though the House of Horrors alive?
\t  This scary adventure is all about YOU. You're
\tin control. You decide what will happen. And
\tyou decide how terriying the scares will be.
\t  Start on page 1. Then follow the instructions
\tat the bottom of each page. You make the choices.
\t  If you make the right choices, you'll escape
\tfrom the spine-tingling Carnival of Horrors in
\ttime. If you make the wrong choices ...
\tBEWARE!
\t  So take a long, deep breath, cross your fingers,
\tand turn to PAGE 1 to GIVE YOURSELF GOOSEBUMPS!"""),

# PAGE 1
    '1': ("""\n\t1\n\n\t  "What do you want to do?"
\t  "I don't know, Patty. What do you want to
\tdo?"
\t  "Not fair, Brad. I asked you first."
\t  Patty and Brad. Your two best friends. Argu-
\ting. As usual.
\t  It's the last week of August. And Patty and
\tBrad haven't stopped fighting since your sum-
\tmer holiday started.
\t  Patty likes being bossy. You don't mind
\tthough. It's no big deal.
\t  It's hard to win a fight with her anyway. You
\tdon't know why Brad even tries. You guess it's
\tbecause he doesn't want to look like a whimp in
\tfront of a girl.
\t  "There's nothing to do. I guess I'll just go
\thome," Brad says. He shoves his hands in his
\tpockets. Then his shoulders slump and he sort
\tof shrivels up. You guess Brad is a bit of a
\twimp-even if he is your best friend.
\t "You're so boring, Brad," Patty complains.
\tWhenever Patty complains, her freckles really
\tpop out. Now there are a million of them
\tspread across her face.
\t  "Hey! I know what we should do!" Patty sud-
\tdenly bursts out.

\t Go to PAGE 2."""),

# PAGE 2
    '2': ("""\n\t2\n\n\t  "Lets bike over to Bennet's Field and watch
\tthem set up the carnival!"
\t  "I don't know," you answer. "It's getting dark
\tand mum said I have to be in by nine."
\t  "It's only a quick bike ride," Brad says. "Are
\tyou some kind of wimp?"
\t  Brad calling you a wimp? You can't believe it!
\t  "Okay. Okay," you agree. "But if it's as bad
\tas last year, there won't be much to see. Don't
\tyou remember the main attraction?" you remind
\tthem. "The ride they called Terror Track? It
\tturned out to be a baby choo-choo train that
\tcircled round and round and round."
\t  It doesn't matter what you say. Patty's made
\tup her mind. You're going to ride over to the
\tcarnival.
\t  A hot, humid breeze blows in your face as you
\tpedal along. Patty's in the lead. No surprise.
\tAnd Brad's puffing behind you.
\t  It's dark by the time you reach Bennet's Field.
\t  You and your friends drop your bikes in the
\tgrass and race across the moonlit field, towards
\tthe hugh wooden fence that surrounds the
\tcarnival.

\tTo take a closer look, turn to PAGE 3."""),

#PAGE 3
    '3': ("""\n\t3\n\n\t  As you reach the carnival entrance, you hear
\tmusic coming from inside. Not the usual corny
\torgan stuff they always play. But some really
\tstrange music. It sounds familiar and totally
\tnew at the same time.
\t  Brad stretches his neck to try and peer over
\tthe fence. But no luck. The fence is far too high.
\t  Patty jiggles the padlock on the door. It's
\tsealed shut.
\t  "I guess we'll have to wait until tomorrow
\tnight when the carnival opens," Brad says.
\t  "No way," Patty says. "Let's climb the fence.
\tNow!"
\t  "Are you crazy?" Brad says. "We'll get
\tcaught!"
\t  "come on. There's probably no one in there,"
\tPatty replies.
\t  Your friends turn to you to cast the deciding
\tvote. You glare at your watch. It's almost
\t9:00 pm. If you're going to get home in time,
\tyou should start back now.
\t  What are you going to do?

\t  If you decide to go home, turn to PAGE 10.
\t  If you climb the fence to get inside, turn to
\t PAGE 6."""),

# PAGE 4
    '4': ("""\n\t4\n\n\t  "Wh-what do you mean?" Brad asks, trem-
\tbling all over.
\t  "I've just had an idea. A great idea," the man
\trelies. "I want you kids to stay and try out the
\trides before the grand opening tomorrow."
\t  Patty's eyes open wide. "Cool!" she says.
\t  "Are you sure it's all right with the owner?"
\tyou ask.
\t  "I'm Big Al, the manager. And what I say
\taround here goes."
\t  Big Al digs around in his checked jacket and
\tpulls out three maps. He hands one to each of
\tyou.
\t  "Study them carefully", he says. "If you have
\tany questions, ask them now."
\t  Your eyes fall upon the map. You have a ques-
\ttion. But when you gaze up, Big Al is gone. He's
\tvanished!
\t  "A whole carnival to ourselves!" Patty
\texclaims. "Where should we start?"
\t  You stare down at your map once again. You
\tnotice that the carnival is split in half. On one
\tside are rides. Tons of them. On the other
\tside are the sidestalls, packed with games of
\tchance and the Freak Show.
\t  What will you try first?

\t  To go on the rides, turn to PAGE 34.
\t  To check out the side stalls, turn to PAGE 77."""),

# PAGE 5
    '5': ("""\n\t5\n\n\t  "Come on, run!" you yell to Patty and Brad as
\tyou spin around. "There's got to be another way
\tout!"
\t  Big Al blows a whistle. It's shrill blast hurts
\tyour ears. He blows it again and, suddenly,
\tdozens and dozens of carnival people appear out
\tof nowhere. But they don't look the way they
\tdid before.
\t  Some have green flesh. Some are deathly
\twhite. Their rotting skin hangs from their
\tbones. Above their sunken cheeck-bones, their
\teyes glow an eerie yellow.
\t  You watch in horror as more and more of them
\tappear.
\t  What should you do? Your legs won't budge.
\tYou can't think clearly. You're terrified! You
\tstand there-frozen-in a trance.
\t  But Brad breaks the spell when he screams
\tout, "They're ghosts! That's why they're wearing
\tthose old-fashioned clothes. They're dead!"
\t  "Watch out! Over there!" Patty yells. "That-
\tthat ghost ... it's coming right at us. Run!"

\t  Run to PAGE 127."""),

# PAGE 6
    '6': ("""\n\t6\n\n\t  "Let's do it!" you say to your friends. "Let's
\tclimb the fence!"
\t  Patty is halfway up before you finish speak-
\ting. You let Brad go next. Your're last.
\t  It's a hard climb up. There's really no place
\ton the fence to get a good grip. But you make it
\tto the top, swing your legs over, and tumble
\tdown. You land on the grass. You're inside!
\t  You and your friends gaze around. It's pretty
\tdark-the only light comes from torches. At first
\tthe carnival looks the same as it always does.
\tDinky rides. Hot dog wagons. Then the lights
\tstart to flicker on in every corner of the field-
\tthe rides start to move. It's as if the whole place
\tis magically coming to life.
\t  "Hey! Look at that giant roller coaster!" you
\texclaim, pointing up ahead. "They never had a
\troller coaster before!"
\t  "Yeah," Brad agrees. "And the whole place is
\ta lot bigger than last year!"
\t  "This is awesome!" Patty says as she sprints
\ttowards the rides.

\t  Race over to PAGE 7."""),

# PAGE 7
    '7': ("""\n\t7\n\n\t  You and Brad take off after Patty. You all stop
\tin front of the roller coaster.
\t  "Wow!" Patty say as she gazes up at it. "It's
\tlike a rocket to outer space!"
\t  Beyond the roller coaster, you spy a castle
\tsurrounded by a moat. And a spooky-looking
\thaunted house sitting high atop a hill.
\t  "These are the coolest rides I've ever seen!"
\tyou say. "They still have that stupid choo-choo
\ttrain over there," you point out, "but we could
\tride this stuff all night and never go near it!"
\t  Patty grabs your arm and tugs you over to
\tthe other side of the carnival-to the sidestalls.
\tBrad races after you.
\t  "Hey! Where are all those dinky wooden
\tbooths from last year?" you ask as you gawk at
\tthe amazing games of chance.
\t  They're gone. And in their place are giant
\tvideo games and huge spinning wheels studded
\twith hundreds of blinking coloured lights!
\t  "Get a load of that!" Brad suddenly cries out.
\t  You and Patty spin around.
\t  You can't believe what you see!

\t  Be more amazed on PAGE 87."""),

# PAGE 8
    '8': ("""\n\t8\n\n\t  You wander over to the Wheel of Chance and
\timmediately notice two strange things.
\t  First, you read the sign on the booth. It says
\tWheel of No Chance. Then you hear the barker's
\tvoice calling, "step right up!" But there's no one
\tthere.
\t  No one but a green-and-yellow parrot.
\t  "Excuse me," you say, hoping someone will
\tanswer. "Is the game open?"
\t  "No, I'm standing by this wheel for my
\thealth," the parrot cracks. "Now do you want to
\tspin or what?"
\t  The parrot is obviously annoyed. "Mammals,1
\the mutters. "Can't live with them, can't live
\twithout them."
\t  you steal a glance around. Maybe you should
\tskip this game. But Big Al sneaks up behind
\tyou.
\t  "Spin," he says. "You must earn enough points
\tto win."
\t  "But how will I know if I have enough point?"
\tyou ask.
\t  "Spin!" It's his final word.

\t  Go to PAGE 9."""),

# PAGE 9
    '9': f"""\n\t9\n\n\t  The wheel spins and lands on ... 
\t  {wheel_result}.

\t  Quick! Go to the page you landed on!""",

# PAGE 10
    '10': ("""\n\t10\n\n\t  You've decided not to sneak into the carnival?
\tYou're going home instead? Well, it's a good
\tthing Patty usually makes all the decisions.
\tOtherwise, you'd never have any fun! And this
\tbook would be over before it began!
\t  Go ahead. Take a deep breath. Then go and
\tclimb the fence. You're not scared-are you?

\t  Turn back to PAGE 6."""),

# PAGE 11
    '11': ("""\n\t11\n\n\t  You've decided to help the freaks. As you race
\talong, you spot Brad and Patty.
\t"Listen, guys," you tell them, lowering your
\tvoice. "We've got a problem. A big problem."
\t  You take a deep breath and tell them all about
\tMadame Zeno and the blue card.
\t  "So," you finish saying, "somebody might need
\tour help in the back of the Freak Show."
\t  "What's a freak?" Brad asks nervously.
\t  "Remember the poster we saw when we came
\tin? The one with the three-head man and the
\tlady with the snake body?" you remind him.
\t  Brad bites down on his lip. "Are they really
\treal?"
\t  "Sure they're real," Patty chimes in. "I once
\tsaw a bearded lady at the circus."
\t  "I don't know," Brad says. "It sounds kind of
\tcreepy."
\t  "Well, Madame Zeno said this was my fate.
\tI'm going to help them-whatever they are. Are
\tyou guys in?"
\t  "You bet," Patty answers, hers eyes shining
\twith excitement.
\t  "Okay, okay. I'll go," Brad mumbles.
\t  "Then let's hurry!" you exclaim.

\t  Race to the back of the Freak Show on PAGE
\t 35."""),

# PAGE 12
    '12': ("""\n\t12\n\n\t  You run to the right. "Follow me!" you cry out
\tto Patty and Brad.
\t  You run faster than you've ever run in your
\tlife. Your sides ache, but you keep on going.
\t  When your chest feels as if it's about to burst,
\tyou finally stop. And hear a crash behind you.
\tThen at both sides of you. Then in front of you.
\tTrapping you.
\t  "Welcome to the Reptile's Petting Zoo", a deep
\tvoice echoes through the darkness.
\t  Reptile's Petting Zoo? You thought the sign
\tsaid Reptile Petting Zoo.
\t  "Our alligator has been so lonely," the deep
\tvoice continues. "Waiting and waiting-for his
\tnew pets to arrive. And here you are-finally."

\t\t\tTHE END"""),

# PAGE 13
    '13': ("""\n\t13\n\n\t  The room is dark, but all around you, you hear
\thushed moans. "Help us! Help us!"
\t  "We're in a prison," Patty says. "And look at
\tthe prisoners! They're weird!"
\t  Patty is right. As your eyes grow accustomed
\tto the darkness, you see cell after cell. Each
\tone holds a strange-looking prisoner. There's an
\tenormous fat lady who's nearly bursting out of
\tthe bars. A giant. A dwarf. A young lady with
\tboa constrictors wrapped around her waist. And
\ta woman with a long black beard!
\t  "We're the freakssss," the snake lady says.
\t"Every night when the show ends, the master
\tlocks us up."
\t  "The master? You mean Big Al is-" you start
\tto say.
\t  "You must help us!" the giant interrupts.
\t  "Sssssssh," the Snake Lady says. "The
\tmaster'sssss coming-you mustn't be here! Go!
\tThat way!" She points to a door down the hall.

\t  Escape through the door down the hall, go to
\t PAGE 48.
\t  Stay and talk to Big Al, go to PAGE 62."""),  

# PAGE 14
    '14': ("""\n\t14\n\n\t  You reach out slowly and touch the red card.
\t  To your amazement a 3-D heart magically
\tappears and rises from the flat surface. Then it
\tstarts to beat! Tha-dump, tha-dump. It must be
\tsome fancy optical illusion. You lean closer to
\tfigure out the trick.
\t  "Yowwwww!" you screech and jerk back to
\tavoid the warm red liquid that nearly squirts
\tin your eye. Is it blood? It looks like blood. 
\t"Wow! Cool effect," you say. "How did you do it?"
\t  "Turn over the card," Madame Zeno orders.
\t"Do it now!"
\t  Madame Zeno really gets into her act. Doesn't
\tshe know this is just a game? you think. But
\tyou do as you're told.
\t  Big deal. No weird pictues. No hidden for-
\ttunes. All you see are the numbers 1, 3, 2 shim-
\tmering in gold script against a midnight
\tbackground. "What does it mean?" you ask.
\t  "You will know when the time is right," the
\tfortune-teller whispers. Her voice is so low, you
\tcan barely hear her. "It could save your life!"

\t  What does she mean? Turn to PAGE 41 to find
\t out."""),

# PAGE 15
    '15': ("""\n\t15\n\n\t  Round and round the wheel spins. It finally
\tlands on number 15. NO CHANCE.
\t  No chance. Does that mean what you think it
\tmeans?
\t  No chance at all.
\t  Zip.
\t  Zero.
\t  Nothing.
\t  Nada.
\t  Negative.
\t  Yes. That's exactly what it means. You have
\tmet...

\t\t\tTHE END"""),

# PAGE 16
    '16': ("""\n\t16\n\n\t  "Hi!" you say to Big Al. "Who are all those
\tpeople?"
\t  He doesn't really answer your question.
\t  "Welcome to the Carnival of Horrors," he says.
\t"You must play or pay. We have many games
\there. You must play two." He practically spits
\tthe word must out. "If you succeed, you can win
\tprizes. But if you lose, you pay with your life!"
\t  Boy, he's really laying it on thick, you think.
\tBut it's a pretty cool gimmick. "Okay, I'll play
\ta game. Then I've got to go home."
\t  "No one goes home," Big Al says, "until they
\tplay. You must play two games. And survive."
\t  "Okay. Okay," you mutter to yourself.
\t  You glance around at the two closest games.
\tGuess Your Weight on Mars and the wheel of
\tChance. You have to pick one to start, or you'll
\tnever get out of here.

\t  For Guess Your Weight on Mars, go to PAGE
\t 72.
\t  To play Wheel of Chance, go to PAGE 8."""),

# PAGE 17
    '17': ("""\n\t17\n\n\t  You take a few steps along the way hoping
\tyou've won enough prizes and points. You notice
\tthe crowd of people surrounding Big Al. They're
\tstill chanting, "PAY OR PLAY. PAY OR
\tPLAY."
\t  You break through the crowd and grab Big
\tAl's arm. "Hey! Do you know where my friends
\tare?"
\t  "Certainly," Big Al says, pointing up ahead.
\t"They're right over there!"
\t  "Patty! Brad!" you shout as you rush up to
\tthem. "Come on! We've got to go! This carnival
\tis evil!"
\t  But before they can say a word, Big Al's voice
\tbooms from behind you. "Not before The Final
\tChallenge!

\t  The Final Challenge begins on PAGE 84."""),

# PAGE 18
    '18': ("""\n\t18\n\n\t  The space lady slowly circles you as she sizes
\tyou up from head to toe. "Hmmmm, I think you
\tweigh thirty-eight pounds."
\t  "Thirty-eight pounds! Boy are you wrong!"
\t  "I'm never wrong," she says, smirking. She
\tsnaps her fingers and two enormous guards
\tappear. They each take one of your arms and
\tdrag you out of the courtyard.
\t  "I don't weigh thirty-eight pounds!" you yell.
\tBut then you remember. It isn't your weight on
\tEarth that matters. It's your weight on Mars.
\t  Do you weigh thirty-eight pounds on Mars?
\tYou'd better find out quickly, because something
\ttells you that what Big Al said about having to
\tsurvive might be true.

\t  Weigh in on PAGE 134."""),

# PAGE 19
    '19': ("""\n\t19\n\n\t  You land on number 19.
\t  "Double of nothing. Double or nothing," two
\tvoices behind you echo.
\t  You whirl around-and gasp! It's a man with
\ttwo heads.
\t  "Congratulations. You win 10 points," one
\t head says to you. "Quit while you're ahead!"
\t  "Ahead, get it? A head!" the other head adds,
\tlaughing hysterically.
\t  "Shut up," head number one says.
\t  "You shut up," head number two shoots back.
\t"Ten points is nothing. You'd better spin again.
\tAnd this time it's double or nothing. You get
\tdouble the points wherever you land."
\t  Which head should you listen to?

\t  If you think you don't have enough points, go
\tback to PAGE 9 and spin again.
\t  If you think you have enough points and you
\thaven't played Guess Your Weight, go to PAGE
\t72.
\t  If you have played Guess Your Weight, go to
\tPAGE 17."""), 

# PAGE 20
	'20': ("""\n\t20\n\n\t  It seems as if hours have passed. Or maybe
\tit's only minutes.
\t  You try to unclasp your hands. But they won't
\tbudge. It's as if your arms are glued around your
\tknees.
\t  You try to move something. Anything.
\t  But you can't blink an eyelid. You body is
\tparalysed. You can't even scream.
\t  A door opens and two men dressed in overalls
\tand wearing gas masks amble in. Finally.
\tThey're here to rescue you!
\t  "Looks like the perfume worked," you hear
\tone of them say.
\t  "Yeah. And just in time. We needed a new
\tdummy for the Real-Life Space Display," the
\tother adds.
\t  They pick up your rigid body and carry you
\tout. No wonder those astronauts in the silver
\ttunnel looked so real!
\t  Sorry. You can't screm. You can't escape.
\t  Next time, you promise yourself, you'll stick
\twith the baby rides. But then you remember-
\tthere isn't going to be a next time ... because
\tthis is...

\t\t\tTHE END"""),

# PAGE 21
	'21': ("""\n\t21\n\n\t  You're outside-standing in Bennet's field-
\tgazing at the fence that surrounds the carnival.
\t  "I guess we'll have to wait until tomorrow
\tnight when the carnival opens," Brad says.
\t  "No way," Patty says. "Let's climb the fence."
\t  What's going on here?
\t  You guessed it. The silver locker was a time
\tmachine. You've gone back in time to the first
\tmoment you spotted the carnival. Now it
\tappears as if you have to start all over again-
\tfighting horror after horror, right up to...

\t\t\tTHE END"""),

# PAGE 22
	'22': ("""\n\t22\n\n\t  You're pretty sure that the space lady guessed
\twrong! Now all you have to do is step on the
\tscales to prove it.
\t  The two goons shove you inside the planet
\tsimulation chamber. It's a long narrow tube,
\tand it's really stuffy inside. You can barely
\tbreathe.
\t  You step up on the scales. You check the read-
\tout. Boy, oh, boy! The space lady is wrong!
\t  You jump up and down. "I won! I won!"
\t  Back outside you collect your prize. It's a huge
\tchocolate bar. You take a big bite out of it and
\tstuff the rest in your pocket.
\t  You gaze around. The coast is clear. Maybe
\tyou can find Patty and Brad and get out of here.
\t  You walk a few steps forward. But a heavy
\thand clamps down on your shoulder from
\tbehind.
\t  It's Big Al.
\t  "It's time to play another game," he says,
\tgrinning.

\t  If you have not tried the Wheel of Chance, go
\t to PAGE 8.
\t  If you've already played the Wheel of Chance,
\t go to PAGE 17."""),

# PAGE 23
    '23': ("""\n\t23\n\n\t  You yank on the reins. But your horse ploughs
\tahead, pulling you forward-closer and closer to
\tthe chopping, chopping, chopping blades. Brad
\tsqueezes into the cart and buries his head in
\this lap.
\t  Patty jumps into the front seat with you.
\tTogether you pull on the reins and scream,
\t"Whoa, fellow! Whoa!"
\t  But your horse trots onward. "It's no use," you
\tcry. "We'd better jump!"
\t  You stare over the side. You're riding along a 
\tnarrow ridge and there's a deep drop that makes
\tyour blood run cold! If you jump, you'll plunge
\tto your death!
\t  Then you glance up ahead-and spot a safer
\tplace to leap. Great!
\t  You are about to show it to your friends when
\tBrad cries out, "Look at the elves! They chop at
\tset times. If we can get the horses to move faster,
\twe can miss the axes!"
\t  "That's stupid, we should jump!" argues Patty.
\t  What do you think you should do?

\t  If you decide to jump out, go to PAGE 103.
\t  If you urge the horse to gallop, go to PAGE 119."""),

 # PAGE 24
 	'24': ("""\n\t24\n\n\t  Carnival workers. The carnival workers who
 \tset up the same rinky-dinky carnival you go to
 \tevery summer.
 \t  You can't believe your eyes. You must be see-
 \ting things!
 \t  Patty tries to say something smart, but the
 \tonly thing she manages is "Huh?"
 \t  "Hey, kids!" a worker yells at you. "Get away
 \tfrom that ride. The carnival doesn't start till
 \ttomorrow night."
 \t  You gaze around in wonder at the faded
 \tgames, the baby rides, the tacky food stands.
 \tFor the first time in your life, it all looks great!
 \t  "We'll be there!" you shout as you head for
 \tyour bikes. "This is the greatest carnival I've
 \tever seen!"

 \t\t\tTHE END"""),

# PAGE 25
	'25': ("""\n\t25\n\n\t  Seconds later your head and the back of your
\tfeet slam into the wall. You're hanging upside
\tdown-in the middle of a gigantic magnetic
\twheel!
\t  "Are you ready for The Final Challenge?" Big
\tAl asks.
\t  "Of course not!" you say. "LET ME DOWN!"
\t  "We'll let you down-but not until you face
\tThe Final Challenge. One spin will decide your
\tfate. If you win, you go. If you lose, you stay
\there for ever."
\t  Will that be your fate?
\t  Big Al approaches the wheel.
\t  Brad and Patty are holding on to each other.
\t  Your heart is pounding.
\t  Your hands are sweating.
\t  This is it. One spin.
\t  He gives the wheel-with you on it-a hard
\tturn. Where will it stop? Guess!

\t  On PAGE 44?
\t  On PAGE 74?
\t  On PAGE 124?"""),

# Page 26
    '26': ("""\n\t26\n\n\t  "Hey, wait up!" you yell to Brad and Patty as
\tyou sprint through the Space Coaster gate.
\t  They both ignore you and charge straight
\tahead. You follow them into a narrow tunnel
\tthat leads to the boarding area.
\t  You gaze down at the floor. Black rubber. It
\tmakes you walk with a strange bounce.
\t  Every few feet there is a round porthole
\twindow. When you glance out of one, you see
\tastronauts planting flags on the moon. You peer
\tout of another. Now they're seated in their
\tcapsule. This is amazing, you think. The figures
\tlook real. Totally real.
\t  After a long climb, you and Patty and Brad
\tfinally arrive at the loading area.
\t  A sleek bullet-shaped capsule whooshes up
\tand stops right beside you. It has three sections.
\tBrad climbs defiantly into the last section. You
\tleap into the front. Patty's left with the middle
\tsection.
\t  And suddenly you're trapped!

\t  Go on to PAGE 58."""),

# PAGE 27
    '27': ("""\n\t27\n\n\t  The crowd is closing in. Your pockets are
\tempty-you have nothing to defend yourself
\twith. So you run!
\t  You spot a crack in the wall, next to the wheel.
\tIt's small-too small for an adult to squeeze
\tthrough-but you can probably make it.
\t  "Follow me!" you yell out to Patty and Brad
\tas you squeeze through the opening. It leads to a
\tbackstage area-and then to the flap of another
\ttent.
\t  You can hear the crowd behind you, trying to
\tfollow you through the crack.
\t  "Come on! We can slip under this tent," you
\tsay. For once, no one argues with you.
\t  The three of you duck in and find yourself
\tsurrounded by another crowd. They are all
\tseated in chairs. And they don't move. They just
\tstare at you with glassy eyes.

\t  Turn to PAGE 55."""),

# PAGE 28
    '28': ("""\n\t28\n\n\t  What's the big idea? You're going to embar-
\trass the giant into helping you.
\t  "Hey, you. You know, you're a real wimp," you
\tsay to the giant.
\t  He looks at you as if he can't believe what he
\thears.
\t  Patty and Brad look at you as if you're crazy.
\t  Maybe you are.
\t  "You wimp," you continue. "You sit here all
\tday, taking orders from that creep, Big Al. And
\tyou live in these horrible conditions. Why?
\tBecause you're a wimp and refuse to fight
\tback. You could bend those bars and escape-
\tbut you won't. Because you are a wimp-
\tW-I-M-P--wimp."
\t  The giant stands. You gaze up. He's over fif-
\tteen feet tall. He lumbers over to you. He isn't
\tsmiling.
\t  Is your plan going to work? Is he going to bend
\tthe bars to prove you wrong? Or is he going to
\tbend you?
\t  It's out of your control now.
\t  Look out of the window.

\t  If it's sunny out, turn to PAGE 45.
\t  If it's raining or if it's night-time, turn to
\t PAGE 85."""), 

# PAGE 29
    '29': ("""\n\t29\n\n\t  You stumble down the corridor to your right.
\tAs you peer from side to side, you are met with
\thundreds of images of-you! And you look
\tpretty baffled. And scared.
\t  "Hey, I could use some help," you call out.
\t  Silence.
\t  You pound your fist against the wall.
\t  The wall starts to move.
\t  Just a couple of centimeters-a couple of
\tcentimetres closer to you!
\t  You take a step back-but the wall behind
\tyou is moving, too.
\t  The walls are moving together. They're clos-
\ting in on you.
\t  You're going to be crushed!

\t  Squeeze over to PAGE 65."""),

# PAGE 30
    '30': ("""\n\t30\n\n\t  You're falling ... falling ... You can't think
\tof anthing else to do, so you start flapping your
\tarms like a bird.
\t  At that moment a huge gust of air shoots up
\tfrom under you and blows you back on to the
\tbridge.
\t  Breathing hard, you run the rest of the way
\tacross the rickety span. When you reach the
\tsafety of the other side, you glance back. And
\tgasp! The bridge and the sidestalls beyond it
\thave vanished! Only a black void remains!
\t  "Wow! Awesome special effects!" you cry out
\tloud. But was your fall part of the special effects,
\ttoo? It didn't feel like it.
\t  You spin around to face the House of Horrors.
\tUp close it appears really, really creepy. Cob-
\twebs drip down from it's roof and an eerie yellow
\tlight glows inside. Cool! Next to the house you
\tspot a sign that reads BOAT TRIP TO NOWHERE.
\tThere are amazing speedboats that you can
\tdrive yourself.
\t  Which should you try first?

\t  Want to try the Boat Trip to Nowhere? Go to
\t PAGE 88.
\t  Ready for the House of Horrors? Go to PAGE
\t 66."""),

# PAGE 31
    '31': ("""\n\t31\n\n\t  You snap your head around to the right-
\twhere you hear footsteps coming towards you.
\t  You are facing a short man with wrinkly skin
\tand bloodshot eyes. His bushy, black hair
\tresembles a scouring pad-and from the looks
\tof it, it probably feels like one, too. His evil
\texpression makes you cringe.
\t  But he's nothing compared to the "things"
\tbehind him-two seven-foot-tall monsters. One
\thas blue horns and bulging red eyes. The other
\thas scaly skin and an alligator snout that snaps
\topen and closed as he eyes you.
\t  The trio all wear lab coats. And from the eager
\tway they're looking at you, you realize that you
\tare the lab rat.
\t  You struggle to escape from the net. But
\tyou're trapped in the webbing. Like a fly in a
\tspider's web.
\t  "Welcome to my humble laboratory," the short
\tman says. "I am Dr Frank N. Stone, the
\tmastermind who created the Carnival of
\tHorrors."
\t  The Carnival of Horrors! You don't like the
\tsound of that!

\t  Go to PAGE 89."""),

# PAGE 32
    '32': ("""\n\t32\n\n\t  Your boat glides through the channel at high
\tspeed to Booger Bog. Water sprays up into your
\tface. But soon you have to slow down. Trees
\thave suddenly sprung up all around you. You're
\tcompletely surrounded now by their towering
\ttrunks.
\t  In the dark light, their limbs take on the
\tshape of gnarled arms with blackened, bony
\tfingers at the end. You stare hard at the tree
\ttrunks. Could it be? Are they reaching out for
\tyou?
\t  You slowly weave the boat through the
\ttwisted trunks and branches. They've grown so
\tthick here that you can barely pilot your boat
\tthrough them.
\t  The trees rustle as if they're whispering to
\teach other. Their limbs begin to sway. As you
\tglide carefully through the water, the leaves
\tslap against your face. Slap. Slap. Slap.
\t  Your heart starts hammering away in your
\tchest. This is really scary. Just how far is
\tnowhere? you begin to wonder. Something
\tswipes at your hair! What was that?

\t  Turn to PAGE 105."""),

# PAGE 33
    '33': ("""\n\t33\n\n\t  You glance once more at the dwarf. He lets
\tout an evil cackle. That's it-there's no way you
\tcan trust him. Besides, you can hear music up
\tahead. You're sure you must be near an exit.
\t  "No, thanks. I don't need any help," you
\tmumble.
\t  He shrugs. "Oh, yes, you do," he says. But
\tthen he sprints off.
\t  You walk in the direction of the music. But
\tafter five minutes, you realize that you're not
\tgetting anywhere.
\t  Maybe you should have followed the dwarf.
\tYou start to think about Patty and Brad. Are
\tthey okay? you wonder.
\t  Just when you think you'll be wandering
\tthese tunnels for the rest of your life, the pass-
\tageway ends! Now you're facing two doors-one
\tred and one blue. Which one should you try?
\tYou might as well flip a coin!
\t  Get a coin. Flip it and check whether it comes
\tup heads or tails.

\t  If it comes up heads, take the blue door to
\t PAGE 57.
\t  If it comes up tails, take the red door to PAGE
\t 104."""),

# PAGE 34
    '34': ("""\n\t34\n\n\t  "Let's go on the rides first!" you say. "That
\troller coaster looks awesome!"
\t  "Okay," Patty agrees. "Over this way!" she
\tyells as she charges over to it.
\t  When you reach the rides, you can only stare
\tin amazement. These are the most fantastic
\trides you've ever seen. The towering roller coas-
\tter ... the soaring speedboats...the twisty
\tslides! Every one is in motion. Whizzing, whirl-
\ting, doing loop-the-loops. And they're all empty!
\tNo riders. No people in line!
\t  "Cool!" Patty exclaims. "We have the whole
\tplace to outselves."
\t  Brad's face turns a little green as his gaze
\tswings from the Supersonic Space Coaster to
\tthe Doom Slide. "Do you think they have rides
\tthat don't go upside down?" he asks.
\t  "Come on! Let's check out the coaster!" Patty
\tcalls to you and Brad. Then they run off to its
\tstarting gate.
\t  You stop and crane your neck to gaze up at
\tthe coaster's first hill. And you gasp!

\t  Quick! Go to PAGE 47."""),

# Page 35
    '35': ("""\n\t35\n\n\t  Five minutes later, the three of you are sneak-
\ting down a dark alley. Brad is so frightened,
\the's practically walking on top of you.
\t  The alley is littered with large cardboard
\tboxes and overflowing rubbish bins. And it
\tsmells like dead fish.
\t  "Hey! Quit stepping on my shoes," you say to
\tBrad.
\t  "I'm not stepping on your shoes," he shoots
\tback. "I'm not anywhere near your stupid shoe."
\t  You glance down. And nearly scream.
\t  Brad's right. He's not stepping on you. But
\tabout a dozen rats are.
\t  You shake your foot wildly. The rats scurry
\toff.
\t  Brad catches sight of the rats and tries to bolt.
\t  You and Patty quickly pull him back.
\t  "Hey! Look!" Patty says, pointing up ahead.
\t"A door!"
\t  On the door you see a big sign that reads KEEP
\tOUT, so ... you go in.

\t  Go to PAGE 13."""),

# PAGE 36
    '36': ("""\n\t36\n\n\t  You turn back and head in the other direction.
\tYour reflections bounce off the walls at crazy
\tangles. Are you walking straight, or have you
\trounded a corner? There's no way to tell. Yet
\tthis time you're sure you're going the right way!
\t  "Over here!" a voice calls. "Turn left again!"
\t  Turn left again? Now you are really confused.
\t  If you turn left again, will you finally escape?

\t  Turn to PAGE 118.
\t  HELP!"""),

# PAGE 37
    '37': ("""\n\t37\n\n\t  You cover your head with your hands and try
\tto run into a thick grove of trees. But the bat
\tcircles in front of you and dives again.
\t  "Stop it! Stop it!" you scream.
\t  As you turn and race towards some low
\tbushes, you remember the stories-the horrible
\tstories about bats making nests in people's hair.
\tAnd the only way to get them out was to shave
\tyour head...
\t  Those stories weren't true-were they?
\t  You spot a big stick in the wet dirt and scoop
\tit up.
\t  The bat swoops down at you once more and-
\tFWAP! You hit it.
\t  The bat falls to the ground.
\t  And you see it's on a wire.
\t  It's a mechanical bat.
\t  All part of the ride, you think. You think about
\tthe boat ride. Boy, they really make things seem
\treal at this carnival, you think. You feel much
\tbetter when you gaze up ahead. There's a
\tclearing.
\t  But when you see what's there-you scream!

\t  Turn to PAGE 93."""),

# PAGE 38
    '38': ("""\n\t38\n\n\t  "Got a winner, got a winner," the parrot
\tsquawks. "You've won twenty-five points, plus
\tanything you want in the prize room. Step this
\tway."
\t  Eagerly you follow the bird into a storeroom
\tbehind the booth. It's packd with the weirdest
\tassortment of junk you've ever seen. Dusty old
\tcatalogues, stuffed rats, a collection of axes, and
\tportraits of headless people holding their own
\theads!
\t  "So pick something. It's getting late," the par-
\trot says.
\t  Not this garbage, you think. Then you spot a 
\tshelf of small cans with bright labels: PLAY AND
\tGLOW, CLAY SLIME, and MONSTER BLOOD. Mon-
\tster Blood? Hey, isn't that the magic stuff you
\tread about in GOOSEBUMPS?
\t  "I'll take the Monster Blood," you decide.
\t  "Excellent choice," the parrot remarks.
\t  As you quickly leave the room with your prize,
\tyou wonder, is twenty-five points enough? What
\tdo you do next?

\t  If you want to spin again for more points, go
\t to PAGE 9.
\t  If you haven't played Guess Your Weight on
\t Mars yet, go to PAGE 72.
\t  If you have played Guess Your Weight on
\t Mars, go to PAGE 17."""), 

# PAGE 39
    '39': ("""\n\t39\n\n\t  You close your eyes. When you open them,
\tyour car lunges forward with a burst of speed-
\tand you loop-the-loop. Your mouth drops open
\tto scream, but no sound comes out.
\t  Now your car starts to plunge downward-
\tlike a lift out of control. Your heart pounds in
\tyour chest. This is the fastest and best roller
\tcoaster you've ever been on! As you near the
\tbottom, you slow down. You begin to catch your
\tbreath. And then you see what's up ahead. A
\thuge black hole-a tunnel!
\t  As you shoot towards the open mouth of the
\ttunnel, you begin to scream again. The door of
\tthe tunnel is about to close!
\t  Snap! The door comes crashing down-
\tbehind your car. You breathe out a long sigh.
\tBut now you're in a tunnel so dark that you
\tcan't see a thing.
\t  Scary! But not nearly as scary as what hap-
\tpens next.

\t  What happens? Turn to PAGE 94 to find out!"""),

# PAGE 40
    '40': ("""\n\t40\n\n\t  "Five, four, three, two, one. We have lift-off,"
\ta mechanical voice announces.
\t  To your horror, the rocket blasts off! You're
\tslammed against the side of the capsule with
\thurricane force. Seconds later, you've left
\tEarth's atmosphere.
\t  A recorded message comes on: "Congratu-
\tlations. You are the perfect weight for our Mars
\texplorer. We'll be monitoring your trip and will
\tbring you back in approximately twenty years-
\twith a plus or minus ten-years margin of error
\tin case something goes wrong. But do not worry.
\tNothing can go wrong ... go wrong ... go
\twrong."

\t\t\tTHE END"""),


# PAGE 41
    '41': ("""\n\t41\n\n\t  "What do you mean the magic number could
\tsave my life?" you ask Madame Zeno. But the
\tfortune-teller doesn't answer. She stares off into
\tspace. She seems to have fallen into a deep
\ttrance.
\t  You don't really believe her-these fortune-
\tellers are all fakes, but you memorize the
\tnumber anyway. 1-3-2, 1-3-2. I picked red
\tinstead of blue, you chant to help you remember.
\t  Madame Zeno puts the card back in the deck.
\tShe closes her eyes and waves away with
\ther jewelled hand.
\t  You guess the fortune-telling is over, so you
\tleave the tent to search for Patty and Brad.
\t  You squint under the bright lights of the side-
\tstalls, scanning all the game booths. But you
\tcan't find them.
\t  You're trying to figure out which way to go
\twhen you spot Big Al coming towards you. He's
\tnot alone. He's leading a large group of people.
\tAs they come closer, you hear that they are
\tchanting something. What is it?
\t  "Play or pay. Play or pay."
\t  What does that mean?

\t  Turn to PAGE 16 to find out."""),

# PAGE 42
    '42': ("""\n\t42\n\n\t  A wave of panic washes over you as the walls
\tcrumble around you. You throw your arms over
\tyour head and close your eyes.
\t  Then silence. The shaking stops.
\t  When you open your eyes, the room and all
\tthe costumed people have vanished. And you
\tare outside-in the rides area! But the biggest
\tsurprise of all is that you spot Patty and Brad!
\t  "Boy, am I glad to see you," you say, racing
\tover to them. "Where have you guys been?"
\t Brad shakes his head. "You wouldn't believe
\tthe rides we went on!"
\t  "We've got to get out of here before midnight,"
\tyou say. Quickly you tell your friends about the
\twarning from the lady with the red parasol.
\t  "No problem," Patty says. "Look. I'm sure the
\texit is right over there past that ride called the
\tHall of the Mountain King."
\t  "No, it's that way-near the sign that says
\tHALLOWE'EN EXPRESS," Brad insists.

\t  Which way do you think is the right way?
\t  Hallowe'en Express? Then turn to PAGE 108.
\t  Mountain King? Then turn to PAGE 107."""), 

# PAGE 43
    '43': ("""\n\t43\n\n\t  You are about to scream. It seems like the
\tonly sensible thing to do.
\t  And then you remember the sign.
\t  Reptile Petting Zoo.
\t  You have an idea. It's a crazy idea, you know.
\tBut everything in this carnival is crazy.
\t  You can feel the alligator's hot breath on your
\tarm. But instead of pulling your arm back, you
\tstretch it out!
\t  "What are you doing?" Patty screams.
\t  Your fingers reach out. Out over the alli-
\tgator's open snout to the top of his head.
\t  And you pet him.
\t  "Nice alligator," you purr as you stroke his
\tscaly head.
\t  Your arm trembles, but you don't stop. And
\tslowly-very slowly-the creature's mouth
\tbegins to shut.
\t  Then he rolls over and falls asleep!
\t  You slip quietly off the log, charge for the
\tshore-and plough right into Big Al!
\tAl sings out. "Come with me. It's time for The
\tFinal Challenge."

\t  You have no choice. Follow Big Al to PAGE
\t 84."""),

# PAGE 44
    '44': ("""\n\t44\n\n\t  You're spinning round and round. Everything
\tis a blur. You can't see, but you hear the crowd
\tchanting, "FI-NAL! FI-NAL! FI-NAL!"
\t  And then the wheel stops.
\t  A huge gasp escapes from the audience.
\t  Did you win or lose?
\t  Neither. You stopped on SPIN AGAIN.

\t  Go back to PAGE 25 and spin again."""),

# PAGE 45
    '45': ("""\n\t45\n\n\t  The giant looms over you. He's as tall as the
\ttree outside your house-and a lot meaner. His
\thuge lips part and he says, "You hurt my
\tfeelings."
\t  Then he begins to cry.
\t  "I am not a wimp. I am not," he says between
\thuge sobs.
\t  He certainly looks like a wimp.

\t  Turn to PAGE 98."""),

# PAGE 46
    '46': ("""\n\t46\n\n\t  You're falling ... falling ...everything passes
\tas if you're dropping in slow motion. Is this...

\t\t\tTHE END?

\t\t\t  Yes."""),

# PAGE 47
    '47': ("""\n\t47\n\n\t  The tracks stretch up so high that they seem
\tto touch the clouds. Your gaze follows one of the
\tcars speeding around a sharp curve. It looks like
\tthe space shuttle. You notice that it has a safety
\tharness that locks over your body-you've seen
\tthose before. They keep you in when the ride
\tturns upside down. You didn't want to admit it
\tbefore, but, like Brad, riding upside down is not
\tyour favourite thing.
\t  Still, the coaster does look amazing-one part
\tenters a tunnel-and you can see that the cars
\tgo fast. Really fast!
\t  You're just about to walk through the Space
\tCoaster gate when you hear spooky organ music
\tcoming from behind you. You turn around.
\tLooming in the distance is a dark and creepy
\thaunted house.
\t  You gaze down at your map. It's called the
\tLittle House of Horrors. Hmmm. You love
\thaunted houses. And this one really looks scary.
\t  Now you're not sure what to do. You won't
\thave time for everything. The coaster or the
\thaunted house? Decide now.

\t  If you decide to join Patty and Brad on the
\t Space Coaster, get on board on PAGE 26.
\t  If you want to go to the House of Horrors alone,
\t go to PAGE 64."""),

# PAGE 48
    '48': ("""\n\t48\n\n\t  "Come on!" Patty cries. "Come on!"
\t  Then, without another word, she races off.
\tYou and Brad dash after her.
\t  I hope Patty knows what she's doing, you
\tthink as you try to catch up. Because right now,
\tit doesn't look that way.
\t  Patty leads you through a maze of under-
\tground passageways. Then, just as you're about
\tto yell, "Stop!"-she does. And you find yourself
\tstanding outside, in front of a barbed-wire fence!
\t  Up ahead, you spot an opening.
\t  "let's go in!" Patty says.
\t  The three of you creep through the fence and
\ttrudge through some tall, wet grass. You gaze
\taround. It's far too dark to see.
\t  But you can hear perfectly. And the sounds
\tthat reach your ears make your skin crawl.
\t  Slithering. You definitely hear slithering.
\t  And hissing.
\t  You want to leave. You spin around, but you
\tcan't find the opening in the fence!  You do see
\tsomething else. A sign!

\t  Hurry to PAGE 60."""),

# PAGE 49
    '49': ("""\n\t49\n\n\t  The wheel stops on FREE SPIN. You are ready
\tto try again. But the stupid parrot flies over and
\tlatches on to your shoulder.
\t  "Ouch! That hurts," you cry.
\t  "Free spin, free spin, you're going on a free
\tspin."
\t  "Turn me loose," you command. When you
\tswivel your head to glare at the bird, a scream
\tfreezes in your throat. The parrot has ballooned
\tinto an enormous vulture. His black, beady eyes
\tpierce right through you. He digs his razor-
\tsharp claws deeper into your shoulder.
\t  Run!-your every survival instinct shouts.
\tBut the bird of prey has other ideas. One of them
\tis dinner-with you as the main course.
\t  The big bird snatches you by the back of your
\tshirt as if you were a rag doll. Kicking and
\tscreaming and using every defensive move you
\tlearned in karate class, you struggle for your
\tlife. But it's no use. With a jerk he lifts you off
\tthe ground.
\t  And suddenly you have a frightening view of
\tthe carnival from ten metres ... twenty metres
\t... thiry metres up.

\t  Fly on to PAGE 50."""),

# PAGE 50
    '50': ("""\n\t50\n\n\t  Thummp, thump, thump. Your heart bangs
\tloudly inside your chest. What kind of carnival
\tis this, you wonder, where free spin in more
\tlike a death sentence?
\t  You circle a green clump of treetops? You're
\treally dizzy now. You want to close your eyes.
\tBut you know it's not a good idea-since you're
\tflying thirty metres high without a plane or a 
\tparachute.
\t  As you circle closer to the treetops, you are
\tmet with a horrifying view. Five baby vultures
\tin a nest, five hungry babies, with mouths
\tgaping wide open.
\t  The end is near. You are going to wind up as
\ta take-home dinner. Unless you can somehow
\tforce the vulture to let you go. Frantically, you
\treach into your pockets!

\t  If you've won a chocolate bar at one of the
\t Games of Chance, go to PAGE 76.
\t  If you haven't, go to PAGE 115."""),

# PAGE 51
    '51': ("""\n\t51\n\n\t  You can't take on both monsters, so you decide
\tto wait until one of them leaves the room.
\t  You grab hold of Dr Stone's hand. He's a lot
\tstronger than he looks. With one small tug, he
\tpulls you free of the web.
\t  Then he turns to the monsters. "Okay," he
\tbarks. "Adjust the net. It's time to practice
\tspiking."
\t  Spiking? What does he mean by that?
\t  The monsters leap up. They rub their hands
\ttogether in evil delight. Then they untie the net
\tand head to the back of the room, where two
\thuge poles rest on the floor.
\t  You close your eyes-and hope that when you
\topen them, you'll see that this was all a dream.
\tA really bad dream.
\t  But when you open your eyes, you know it's
\tnot a dream. No-it's a volleyball game. The
\tnet has been tied to the poles-and guess what
\tposition you play? That's right. You're the ball!
\tWatch out for those two-handed spikes! They
\tcan be painful!

\t\t\tTHE END"""),

# PAGE 52
    '52': ("""\n\t52\n\n\t  Just as the clock strikes twelve, the train
\tenters a tunnel.
\t  You hold your breath, wondering what you'll
\tsee when you reach the other end.
\t  Chug. Chug. Chug.
\t  The choo-choo slowly pulls out of the tunnel-
\tand you are surrounded by carnival workers-
\teverywhere!

\t  Chug to PAGE 24."""),

# PAGE 53
    '53': ("""\n\t53\n\n\t  Oh, no! You think the space lady guessed
\tright! Now what's going to happen?
\t  The two guards shove you into the space
\tchamber.
\t  It's a clear, narrow tube that rises farther up
\tthan you can see.
\t  As the door slams shut behind you, one of the
\tguards barks, "Get on the scales!"
\t  You step up on the scales-and it shows just
\thow right the space lady's guess was.
\t  You press the chamber-door release, but it's
\tstuck.
\t  You try again. It doesn't budge.
\t  Maybe it's locked from the outside.
\t  "Hey! I can't get out!" you yell to the guards.
\tBut they simply wave.
\t  "Hey, let me out!" Now you're angry. "Let me
\tout!"
\t  All at once the room starts to shake and rattle.
\tRRRRRRRR. The thrust of powerful rocket
\tengines echoes in your ears. It sounds as if
\tyou're being launched into space, but that's
\timpossible, isn't it?

\t  Go to PAGE 40."""),

# PAGE 54
    '54': ("""\n\t54\n\n\t  Your Hallowe'en Express car pulls up in front
\tof a cottage and the cottage door opens with a
\tcreak. You all jerk your heads up to peer at the
\tdoor. You see a skeleton wearing an evil smile.
\tAnd he lunges right at you!
\t  "Trick or treat!" he screeches. Then he
\tstretches out his bony hands to snatch you!
\t  You pound on the accelerator, and the car
\tshoots forward-out of the skeleton's grasp!
\t  Your heart begins to race as the car speeds
\tout of control. You tear through an eerie forest,
\tspeed past more cottages-but still you don't
\tsee a way out.
\t  And then it comes into view-a service exit!
\t  All you have to do is stop the car, jump out
\tand scramble through the fence, and you'll be
\tfree.
\t  You check your watch-five minutes to
\tmidnight!
\t  "Oh, no!" Patty screams. "Quick, turn left!
\tDon't stop!"

\t  Turn left! And go to PAGE 83."""),

# PAGE 55
    '55': ("""\n\t55\n\n\t  They're dummies. That's why they don't
\tmove!
\t  "They've got to be here somewhere," you hear
\tBig Al's voice boom outside the tent.
\t  "Hey! This dummy looks just like the one in
\tthat GOOSEBUMPS book," Patty says.
\t  "You mean Night of the Living Dummy?" Brad
\tasks.
\t  Great! you think. Your friends are chatting
\tabout books minutes before you're about to be
\tattacked by a mob. Then you get an idea.
\t  "Remember those magic words that brought
\tthe dummy to life in that book?" you ask your
\tfriends. "Maybe we can bring this guy to life and
\the'll help us-he was pretty tough."
\t  Your friends agree-it's worth a try.

\t  If you think the words are karru marri odonna
\t loma molonu karrano, go to PAGE 69.
\t  If you think the words are oooopah lupah
\t dummie dupah, go to PAGE 82."""),

# PAGE 56
    '56': ("""\n\t56\n\n\t  You leap out of the boat. The putrid brown
\twater splashes into your mouth. Gross!
\t  You swim a few strokes and suddenly find
\tyour knees scraping the bottom of the bog. The
\twater here is less than a foot deep. Unbeliev-
\table! You were practically inches away from
\tsafety the whole time!
\t Slogging through the brown foam, you wade
\tto shore. You clothes are dripping wet and
\tsmell like a sewer. Well, look on the bright side,
\tyou remind yourself. At least you didn't go down
\twith your boat.
\t  But your troubles aren't over yet. You're
\tstanding in a dank, eerie forest that surrounds
\tthe lake. Creepy screeches echo through the
\tnight mist. And you're totally lost.
\t  The wind starts to blow. Shivering, you wrap
\tyour arms around your shoulders and wonder
\twhere your friends are and what they are doing.
\t  Then-POW!  Something black and furry
\tswoops down at you! You duck your head, but
\tit comes at you again and again.
\t  A huge bat!

\t  Turn to PAGE 37."""),

# PAGE 57
    '57': ("""\n\t57\n\n\t  You open the blue door and peer through.
\tYou're staring down a long dark passageway.
\tAt least you think it's long. It's difficult to tell.
\tIt's pitch-black. You don't know what to do.
\t  "Maybe I should have picked the other door,"
\tyou say to yourself. "I'm getting out of here!"
\t  But the blue door has locked behind you! Now
\tyou're sure you made the wrong choice. But
\tthere's nowhere to go but forward.
\t  Your knees begin to tremble as you inch your
\tway down the dark hallway.
\t  The passage end in a bright burst of light.
\tAnd in front of you, a tall purple mountain rises
\thundreds of feet into the air.
\t  You breathe out a long sigh of relief. You're
\tout of the dark!
\t  You study the mountain. It looks so real! But
\tcut into its side, you spot a doorway. Above it a
\tbrightly painted sign reads: DOOM SLIDE. WILL
\tYOU BE THE ONE TO SLIDE FOR EVER?

\t  Turn to PAGE 135."""),

# PAGE 58
    '58': ("""\n\t58\n\n\t  Steel bars plunge down from above and drop
\tacross your lap and chest, pinning you in place.
\tYou can't move at all. Even your head is held by
\tsuper-strong headphones that clamp over your
\tears. A voice comes through them announcing:
\t"Five, four, three, two, one, BLAST OFF!"
\t  You hear a huge bang. Smoke and fireworks
\tfill the air as your car starts up the first big hill.
\tYour head presses back against the seat as you
\tclimb higher and higher. That first hill is end-
\tless, but the view in awesome. From the top, you
\tcan see the sidestalls, the haunted house, and
\ta shadowy swamp. You can't believe how big the
\tcarnival is!
\t  "Neat!" Patty yells. "There's AHHHH-"
\t  Whatever she was going to say turns into a
\twild scream as the rocket plunges down the
\tother side of the hill. The wind whips at your
\tface. You are pressed back so hard, you feel like
\ta pancake. Everything passes in a fantastic
\tblur.
\t  As your car shoots up to the top of the next
\thill, you're laughing and screaming at the same
\ttime. This is great, you think! But then you
\tmake a big mistake.

\t  Turn to PAGE 39."""),

# PAGE 59
    '59': ("""\n\t59\n\n\t  Blue is your favourite colour. You turn the
\tblue card over.
\t  There is a message: Help us! You are our only
\thope. Hurry to the back door of the freak show.
\tSigned, The Freaks.
\t  "What does this mean?" you ask Madame
\tZeno. She stares deep into your eyes. Her lips
\ttremble. She leans forward. She's about to
\tspeak.
\t  And then the lights go out-and a blood-
\tcurdling scream rips through the dark!
\t  You start to bolt for the door when a dim light
\tsuddenly flickers. You stare across the table.
\tMadame Zeno is gone!
\t  You reach out to take the card. And it bursts
\tinto red-hot flames! In seconds, the entire tent
\tfills with thick smoke. Flames shoot across the
\tfloor. You run for the door.
\t  Outside you gulp the fresh air. Whew! You
\tmade it.
\t  You glance back. No smoke. No fire. No tent!
\tEverything has disappeared! What should you
\tdo now?

\t  If you decide to help the freaks, go to PAGE
\t 11.
\t  If you don't want to help the freaks, go to PAGE
\t 113."""),

# PAGE 60
    '60': ("""\n\t60\n\n\t  "There's a sign!" you call out to Patty and
\tBrad. "Let's see what it says."
\t  The three of you race through the wet grass.
\tYour socks are drenched. And your trainers
\tsqueak as you run. But that's not the sound
\tthat's sending chills down your spine.
\t  It's the hissing. It's growing louder.
\t  "I'm not sure I want to read that sign," you
\tcall out to Patty and Brad.
\t"I know what you mean!" Patty shouts back.
\t"I have a feeling we're not going to like what it
\tsays".
\t  And you don't. You reach the sign and read it
\taloud. "Reptile Petting Zoo! Whoever heard of a
\tReptile Petting Zoo! What kind of carnival is
\tthis anyway?"
\t  "This carnival is e-evil," Brad stammers.
\t  You're about to agree when you notice the
\tgrass in front of you is swaying. Something is
\tslithering through it. Something big. And then
\tit comes into view.
\t  "Snake!" Brad cries.
\t  You know you have to run-but which way?
\tLeft or right?

\t  If you run to the left, turn to PAGE 125.
\t  If you run to the right, turn to PAGE 12."""),

# PAGE 61
    '61': ("""\n\t61\n\n\t  You're too scared to turn around. And too
\tscared not to. Risking a glance over your shoul-
\tder, you see a large, dark shape behind you. It's
\ta big man. No. You squint hard. It's dark and
\thairy with muddy leaves and green vines trail-
\ting from its body. It's some sort of swamp
\tmonster!
\t  You run as fast as you can. Your chest is on
\tfire. The swamp monster is gaining on you.
\t  You know you should keep running, but your
\theart feels as if it's about to explode. You have
\tto stop.
\t  You turn and stare right into the swamp mon-
\tster's bloody eyes. "Neat costume," you say
\thopefully.
\t  Good try-but the swamp monster isn't wear-
\ting a costume. He's real and this, unfortunately,
\tis really...

\t\t\tTHE END"""),

# PAGE 62
    '62': ("""\n\t62\n\n\t  You decide to wait for Big Al.
\t  "Big Al has to free the freaks," you say to
\tPatty and Brad. "If he doesn't, we'll tell him
\twe're calling the police!"
\t  "Free the freaks?" Big Al says, bursting into
\tthe room. "The freaks are free to go any time.
\tThis prison is just part of the show. Did you
\tpull that 'free us' joke on him?" Big Al laughs
\theartily.
\t  "He'ssss lying," the Snake Lady says. "We're
\tprisonersssss."
\t  "Oh, come now," Big Al says. "You're not pris-
\toners." And with that he unlocks all the cell
\tdoors. Then he turns to you and your friends.
\t  "As you can see, the freaks are free. Now,
\tcome with me. You haven't even tried one game
\there."
\t  "Don't go with him. It's a trick!" the Snake
\tLady cries.
\t  Should you go with Big Al?
\t  Who's telling the truth? Big Al or the Snake
\tLady?

\t  If you want to go with Big Al, turn to PAGE
\t 84.
\t  If you trust the Snake Lady, turn to PAGE
\t 102."""),

# PAGE 63
    '63': ("""\n\t63\n\n\t  Bump.
\t  A chute opens up. You land head first on soft
\tgrass.
\t  You blink several times. A long sigh escapes
\tfrom your lips. It wasn't the Doom Slide after
\tall.
\t  As you climb to your feet you hear someone
\tcall your name.
\t  You glance up and shout for joy. It's Brad!
\tAnd Patty's there, too!
\t  You tell them about your scary ride on the
\tslide-about how you thought you'd slide for
\tever.
\t  "Cool!" Patty exclaims. "Let's all ride it this
\ttime!"
\t  "No!" you tell her. "This carnival is too weird.
\tAnd dangerous. Something's not right. We have
\tto get out of here. Now!"
\t  "Yeah," Brad agrees. "The faster, the better."
\t  "I have an idea," Patty announces. You and
\tBrad huddle around her. "I spotted a back way
\tout of here. But it's a little risky. We have to
\tsqueeze through a barbed-wire fence-and it's
\tguarded by the carnival's security forces. But
\twe should try!"
\t  Are you going to listen to Patty?

\t  Follow Patty? Turn to PAGE 48.
\t  You choose not to take the back way out? Go
\tto PAGE 86."""),
    
# PAGE 64
    '64': ("""\n\t64\n\n\t  The House of Horrors! You have to see it. You
\tjust have to!
\t  "I'll catch up with you guys later," you call
\tto Patty and Brad. "I'm going to check out the
\thaunted house."
\t  You glance down at your map for directions.
\tThe rickety wooden bridge over to your left
\tappears to lead straight there.
\t  As you start across the bridge, the wooden
\tplanks creak under your feet. Then the bridge
\tbegins to sway. You look down. A long way
\tdown. The bridge spans a deep, rocky gorge.
\tGulping, you grab the handrail. You move
\tslowly. A strong wind blows up from the canyon
\tbelow. The bridge is swaying wildly now, tossing
\tfrom side to side.
\t  A massive spear of lightning splits the sky.
\tThunder rumbles so loudly you jump and lose
\tyour balance. "Help!" you scream as you tumble
\tright over the side-and plunge towards the
\tjagged rocks below!

\t  How can you save yourself?
\t  Make a grab for the side of the bridge? Turn
\t to PAGE 46.
\t  Flap your arms and try to fly? Turn to PAGE
\t 30."""),

# PAGE 65
    '65': ("""\n\t65\n\n\t  The walls are closing in faster now.
\t  You throw your arms out and try to push them
\taway. But it's hopeless. You're going to be
\tcrushed like an insect.
\t  You suck in a deep breath-it could be the
\tlast breath you take.
\t  The floor opens beneath your feet!
\t  You drop down. Down. Down. Down. A long,
\tagonizing scream escapes from your throat as
\tyou tumble through space.
\t  Will you ever hit the bottom?
\t  "Incoming player," you hear a commanding
\tvoice shout. "Stations, everybody."
\t  A layer of webbing catches you like one of
\tthose nets trapeze artists use. Gasping, unable
\tto understand what's happening, you bounce up
\tand down.

\t  Bounce to PAGE 31."""),

# PAGE 66
    '66': ("""\n\t66\n\n\t  You start up the brick path to the House of
\tHorrors. Suddenly someone sneaks up behind
\tyou and taps you on the shoulder. You spin
\taround and jump back.
\t  Standing in front of you is a bony skeleton.
\t  And it talks.
\t  "Don't go in there," the skeleton says. "Or
\tyou'll end up like me..."
\t  You stare in terror at the hideous creature.
\tThen you burst out laughing.
\t  "Wow! You guys really want to make the
\thaunted house totally creepy. This is going to
\tbe great!" you say.
\t  You're still chuckling as you push open the
\tgiant oak door of the House of Horrors. It swings
\tback with a long, loud creak.
\t  You step inside and find yourself in a narrow
\thallway. The door slams shut behind you and
\tthe hall turns darker than a starless night. "I
\tcan't even see my hands!" you exclaim.
\t  You stumble ahead slowly, pressing your
\tpalms against the walls to guide you.
\t  When will this tunnel end?

\t  Look for a way out on PAGE 80."""),

# PAGE 67
    '67': ("""\n\t67\n\n\t  Thrumpff! Your foot ploughs into the doctor's
\tstomace again. But this time, it smashes right
\tthrough it. And hits ... solid steel!
\t  The crunch of the metal echoes in the room-
\talong with the doctor's screams. "Aiiii!" he wails
\tlike a siren.
\t  You gaze into the gaping hole you made by your
\ttrainer. Thousands of circuits and wires burn
\tand crackle inside it. The doctor is a robot! Well,
\tan ex-robot now. Your kick totally destroyed
\thim.
\t  That's the good news.
\t  The bad news is heading towards you. It's the
\tmonster with the blue horns and red, bulging
\teyes.
\t  You scramble out of the net and dash towards
\tthe door. But the monster is too quick for you.
\tHis tentacle arms shoot out and snatch you.
\tGiant suckers at the ends of his wrists circle
\tyour throat.
\t  You gasp for air as the monster pins you
\tagainst the wall. Can you free yourself from his
\toozing grasp?

\t  Try, on PAGE 91."""),

# Page 68
    '68': ("""\n\t68\n\n\t  You slowly lower yourself on to the slide. You
\tstart to stretch out your legs when the bottom
\ttilts underneath you and throws you forward.
\tYou're sliding fast!
\t  The surface must be made of some kind of
\tspecial material because you're zooming down
\tat top speed.
\t  You hold your breath as you fly through the
\tblackness. A bump sends you bouncing into the
\tair. You scream. And scream.
\t  When is it going to end?
\t  Oh, no! Could this be the Doom Slide?
\t  You hear screams echo in the darkness. You
\ttwist around. But you don't see anyone.
\t  The ghostly screams grow louder-in front of
\tyou, next to you, behind you. Screaming and
\tsliding. And sliding. Never stopping.
\t  You gasp for breath. And then you hear it.
\t  A voice cuts through the blackness. Through
\tthe screams. A voice that cries, "Welcome to the
\trest of your life. Welcome to the Doom Slide!"

\t\t\tTHE END"""),

# PAGE 69
    '69': ("""\n\t69\n\n\t  "Karru marri odonna loma molonu karrano."
\tYou say the magic words and-the dummy
\tcomes to life!
\t  He opens his mouth and speaks. "Hey, you.
\tYour face reminds me of a wart I once had
\tremoved."
\t  "Come on," you plead. "we're the ones who
\tbrought you back to life. Aren't you going to be
\tnice to us? We might need your help."
\t  "I'm sorry," the dummy says. "I'm sorry you're
\tso ugly ..." Then he laughs at his own lame
\tjoke.
\t  You stare at him and his face grows serious.
\t"You brought me to life," he says slowly, "but
\tnow you are my slaves.
\t  "For ever-until...

\t\t\t"THE END."

\n\t  Wait! This isn't the way this is supposed to
\tend. Quick-you have one last chance. If the for-
\ttune-teller told you a secret number, go to that
\tpage now!"""),

# PAGE 70
    '70': ("""\n\t70\n\n\t  "Nine ... ten ..."
\t  "Brad, shut up. Look at this!"
\t  You point to the letters on the front of the
\ttrain car.
\t  You've been staring at them the whole time.
\tWhy didn't you notice them before?
\t  "What about the letters?" Patty says sharply.
\t  "Eleven ..."
\t  "Don't you see what they say?" you shoot back.
\t  "Right-way Railroad," Patty reads. "So
\twhat"?
\t  The chants of the merry-go-round people echo
\tin your head. There's only one right way. There's
\tonly one right way.
\t  Could it be?
\t  "Twelve!"
\t  Now what?

\t  Turn to PAGE 52."""),

# PAGE 71
    '71': ("""\n\t71\n\n\t  Sorry. It's not your lucky day. As you dash to-
\twards the sign, the giant crane scoops the three
\tof you up and drops you off into a hollowed-
\tout log. You barely have time to sit up straight
\tbefore the craft reaches the waterfall!
\t  You hold your breath as the log teeters on the
\tfall's edge. As it plundges over, you scream.
\t A hard spray smacks you in the face and
\tdrenches your clothing as you race down the
\tlong slide. At the bottom, the log hits a pool of
\twater and sinks.
\t  You're still holding your breath as you wait
\tto bob to the surface again. But it never hap-
\tpens. You keep going down.
\t  Your last thought is that you're going to set
\ta world record for holding your breath
\tunderwater.
\t  You'd better set a world record for closing the
\tbook and starting over again. Maybe next time
\tyou dive in you'll have better luck.

\t\t\tTHE END"""),

# PAGE 72
    '72': ("""\n\t72\n\n\t  You step up to the Guess Your Weight on
\tMars booth. A woman in a space suit motions
\tyou inside a gate. You pass through and find
\tyourself in the middle of a courtyard that looks
\tjust like a miniature launching site-complete
\twith it's own rocket!
\t  "Security check," the lady says as she presses
\tyour hand on to a fake scanner.
\t  "So how does this game work?" you ask.
\t  "I'll guess how much you weigh on Mars," she
\texplains. "Then you'll enter the planet simu-
\tlation chamber and stand on the scales. If I'm
\twrong by more than one pound up or down, you
\twin a giant chocolate bar."
\t  "What if you guess right?"
\t  The space lady doesn't say anything at first.
\tShe just smiles. A nasty smile. Then she
\tanswers.
\t"You lose," is all she says.

\t  Go to PAGE 18."""),

# PAGE 73
    '73': ("""\n\t73\n\n\t  Your reflexes are great. You jumped out fast
\tenough and escaped the ghost-that ghost. But
\tyou didn't see the other one behind the car-
\twaiting for you.
\t  Your heart hammers away in your chest as it
\tcircles you.  Round and round and round.
\t  "It's all right," you tell yourself over and over.
\t"It's not real. This is just a ride in an amusement
\tpark."
\t  You're still telling yourself that as the ghost
\tplucks you off your feet.
\t  His black lips part.
\t  He opens his mouth-wider and wider. Until
\tit's as wide as an entrance to a cave.
\t  Then he stuffs you inside.
\t  Instantly you feel light-headed, then light all
\tover. You peek down at your hands.
\t  You can see straight through them. You've
\tbeen turned into a ghost! And as your senses
\tfade, you hear a distant bell chime twelve times.
\tToo bad. The Carnival of Horrors will be one of
\tyour favourite haunts-for ever!

\t\t\tTHE END"""),

# PAGE 74
    '74': ("""\n\t74\n\n\t  Round and round you go. The world is a blur
\tof colours. You can hear the crowd screaming.
\t"FI-NAL! FI-NAL!"
\t  And the wheel stops.
\t  "Ahhhhhh," the crowd gasps.
\t  What does it mean?
\t  "YOU WIN," Big Al says. "Now come this way
\tto collect your prize and go home."

\t  Turn to PAGE 131."""),

# PAGE 75
    '75': ("""\n\t75\n\n\t  The three of you duck inside the Hall of the
\tMountain King!
\t  A painted backdrop of rounded snowcapped
\tmountains rises on the left. Up in the moun-
\ttains a big stone castle rests in the sunshine. A
\tgroup of cheerful elves pick flowers in the
\tcastle's garden.
\t  To your right, you spot the ride-wooden carts
\tpulled by real horses. "Come on!" you call to
\tyour friends. "Jump in a cart. This is great. We'll
\tbe out of here in no time." No time-that
\treminds you. You glance at your watch. 11:45!
\t  You all scramble into one of the carts and grab
\tthe reins. Your horse plods forward, and you
\tpass through a painted archway.
\t  You gasp. Everything in the painted backdrop
\tis now in front of you. And it has suddenly
\tbecome real. But different!
\t  The snowcapped mountains rise to black,
\tjagged peaks that pierce the sky. The big stone
\tcastle huddles on a scary, dark hill. And the
\telves- they aren't picking flowers.
\t  They're...

\t  Turn to PAGE 96."""),

# PAGE 76
    '76': ("""\n\t76\n\n\t  You dig deep into the side pocket of your
\tjeans-and find it! The chocolate bar you won.
\t  It's a good thing you didn't eat it all-but will
\tthe vulture go for it?
\t  Without warning, the big bird starts his final
\tapproach, diving straight for the nest. You pull
\tout the chocolate and wave it frantically in front
\tof him. "Treat! Treat!" you holler. These words
\tmake your dog at home go wild. But will it work
\ton the vulture?
\t  Yes! He cracks open his beak-just enough for
\tyou to wiggle loose. Then you're falling, falling.
\t  You've landed on a giant trampoline.
\t  Fwanggg!
\t  Now you're going up again. Higher this time.
\tNow you're falling again.
\t  Fwanggg-you've bounced up even higher
\tthis time.
\t  Every life has it's ups and downs, but it looks
\tas if you'll be bouncing up and down for ever-
\tand boy, is it fun!

\t\t\tTHE END!
\t\t\tTHE END!
\t\t\tTHE END!
\t\t\tTHE END!"""),

# PAGE 77
    '77': (f"""\n\t77\n\n\t  "Lets's head for the sidestalls and play some
\tgames!" you say.
\t  You, Patty and Brad jog down a wide avenue.
\tTents of every colour line the street. Carnival
\tmusic blares from loudspeakers.
\t  You spot a green neon sign flashing above a
\tyellow-stiped tent. The sign reads: MADAME
\tZENO-FORTUNE-TELLER.
\t  "Excellent!" you proclaim. "I'm going in!"
\t  You tell your friends you'll catch up with them
\tin a minute.
\t  You lift the tent flap. Inside, one small candle
\tflickers in the dark. You hear a low voice call
\tout, "Enter my chamber {reader.title()}."
\t  Ther is Madame Zeno, sitting in the
\tshadows as she bends over a large crystal ball.
\t  "Welcome," she whispers. Then she reaches
\tout and gently lifts your hand. "Let me tell you
\tyour future."

\t  To find your future, go to PAGE 78."""),

# PAGE 78
    '78': ("""\n\t78\n\n\t  Madame Zeno studies your hand closely. She
\ttraces the line in your hand with her soft
\tfingers.
\t  "I see horror in your future. In your immediate
\tfuture," she warns.
\t  "Wh-what kind of horror?" you stammer.
\t"What do you mean?"
\t  Madame Zeno releases your hand. She picks
\tup a strange deck of cards. She spreads them
\tout on the table. You notice the cards have pic-
\ttures-a headless man, a bloody sword, a large,
\tevil eye.
\t  She gathers up all the cards and flips the deck
\tover. Then she deals out a red card and a blue
\tcard.
\t  "Turn one over," she commands. "Learn your
\tfate".

\t  Pick red? Go to PAGE 14.
\t  Pick blue? Got to PAGE 59."""),

# PAGE 79
    '79': ("""\n\t79\n\n\t  The doctor leans over. He's so close now, his
\tsour breath fills your nostrils. Then his finger-
\ttips brush your hand and-POW! Your foot flies
\tinto his stomach! A direct hit!
\t  But nothing happens.
\t  He doesn't scream. He doesn't even moan. In
\tfact, he doesn't seem to notice at all.
\t  He simply smiles at you.
\t  Now you're scared. Really scared. But you
\tknow you have to do whatever it takes to get
\tout of there. You have to find your friends and
\tescape from this Carnival of Horrors.
\t  You gather up every ounce of courage and
\tstrength you have-and kick him once more.
\tHarder!
\t  And this time something does happen-BIG
\tTIME!

\t  Turn to PAGE 67 to find out what."""),

# PAGE 80
    '80': ("""\n\t80\n\n\t  You turn a corner and are instantly blinded
\tby glaring lights.
\t  You are standing in a room of mirrors. Walls.
\tFloor. Ceiling. All mirrors!
\t  Everywhere you gaze, you are met with
\treflections of yourself! You take a few steps for-
\tward and-CRACK! You hit your head on solid
\tglass.
\t  You move one step to the left, and a dozen
\tcopies of you move in that direction.
\t  Totally dizzy, you close your eyes. Maybe you
\tcan find the exit with your hands. Keeping your
\teyes shut, you walk until your palms hit against
\tanother glass wall. Then you hear a voice.
\t"Come this way. Over here," it calls
\t  You walk towards the voice-CRACK-a
\tsolid wall again.
\t  Finally your hands find an open doorway! It
\tleads to a mirrored hallway that goes left and
\tright. Which way will you go?

\t  If you decide to turn right, go to PAGE 29.
\t  If you decide to turn left, go to PAGE 118."""),

# PAGE 81
    '81': ("""\n\t81\n\n\t  "You're lying!" you yell. "You are a robot."
\t  You quickly reach up with both hands and tug
\tat his head. His sharp jaws slash at you. But
\tyou're fast. You hold on firmly and pull!
\t  Oh, no! He really is a monster. And he's not
\thappy.
\t  You know you're dead meat, but you have to
\ttry one more time. Just to make sure. You give
\this head one more tug. He laughs. Then he gives
\tyour head a tug.
\t  Sorry. You were doing so well. But now you've
\tgone and lost your head. The only way you'll
\tbe able to face the challenge of the Carnival of
\tHorrors now is to close the book and begin
\tanother day. At least then-you'll have a head
\tstart.

\t\t\tTHE END"""),

# PAGE 82
    '82': ("""\n\t82\n\n\t  "Oooopah lupah dummie dupah." You say the
\tmagic words and wait for the dummy to spring
\tto life.
\t  And you wait.
\t  And you wait.
\t  The dummy remains the same.
\t  But something strange is happening to you.
\tWhat are those feathers sprouting out of your
\tskin? And what's happening to your feet? Are
\tthose claws you see growing out of them?
\t  Is it possible that the magic words are turning
\tyou-CLUCK-into a-CLUCK-chicken?
\t  That's eggs-actly what's happening.
\t  Well, you laid an egg this time. Let's hope you
\twon't be too chicken to open this book again and
\ttry once more to escape from the Carnival of
\tHorrors.

\t\t\tTHE END"""),

# PAGE 83
    '83': ("""\n\t83\n\n\t  You squint hard at the road ahead of you-
\tand see why Patty wants to turn. There
\tthey are-the people in the old-fashioned
\tclothes. Only they don't look the same.
\t  Some have green flesh. Some are deathly
\twhite. Their rotting skin hangs from their
\tbones.
\t  And they're all reaching out. Reaching out for
\tyou!
\t  "Turn! Turn!" Patty yells.
\t  You spin the wheel sharply to the left to avoid
\tthem. But you can't dodge the ghostly creature
\tthat's rising above you. He's ten feet tall-with
\tarms so long that they scrape the ground. His
\tmouth gapes open to reveal hundreds of black-
\tened, rotting teeth.
\t  He swoops down at you. You turn the steering
\twheel hard to the right. Too hard-it comes off
\tin your hands!
\t  "Jump!" you cry. "Jump and run! Run!"
\t  The three of you leap out of the moving car.
\tBut are you fast enough? That depends on how
\tgood your reflexes are.
\t  Try this test and find out. Throw a ball in the
\tair. Try and clap three times before you catch it.

\t  If you can do it-turn to PAGE 73.
\t  If you couldn't-turn to PAGE 127."""),

# PAGE 84
    '84': ("""\n\t84\n\n\t  Big Al shoves you and your friends into a huge
\tred tent. It seems to be set up for some kind of
\tshow. Red carpeted steps lead up to a platform,
\twhich sits under a golden arch. The arch
\ttwinkles with a thousand coloured lights that
\tspell out: FINAL CHALLENGE.
\t  Trumpets blast as people flood into the view-
\ting area. As they march in, they clap their hands
\tand yell, "FI-NAL. FI-NAL."
\t  Big Al leads you up the carpeted steps. You
\tare standing on the platform now-in front of
\ta shimmering curtain that hangs down from the
\tarch.
\t  The crowd begins to chant, "SUD-DEN
\tDEATH. SUD-DEN DEATH."
\t  "What do you think that means?" Patty asks.

\t  You're going to find out on PAGE 123."""),

# PAGE 85
    '85': ("""\n\t85\n\n\t  The giant hangs over you, flexing his muscles.
\tHe squints at you as if you are an insect-ready
\tto be squashed.
\t  "Did you call me a wimp?" he thunders.
\t  You are much too scared to answer.
\t  The giant answers for you. "You're right. I am
\ta wimp!"
\t  And with that, he bends the bars. and you,
\tPatty, and Brad scramble through.
\t  "Follow me," the giant says. "I know a way
\tout of here."
\t  "What about the others?" you ask, pointing to
\tthe freaks in the cells that line the wall.
\t  "No problem!" Patty yells, grabbing the keys
\tfrom a hook on the wall. "Here-catch!"
\t  You quickly unlock all the doors-setting the
\tfreaks free!

\t  Turn to PAGE 126."""),

# PAGE 86
    '86': ("""\n\t86\n\n\t  "I don't know," you say. "I don't think we
\tshould take any more risks. Especially not in
\tthis crazy carnival."
\t  "Don't you trust me?" Patty demands. Her
\teyes flash angrily.
\t  You glance at Brad. He stares at the ground.
\t  "I just have a bad feeling about this, Patty.
\tOkay?"
\t  But Patty doesn't answer. She throws her
\tshoulders back and stands up taller. And taller.
\tAnd taller.
\t  You gasp! Patty is growing! She's nearly ten
\tfeet tall!
\t  She reaches out a long arm and grabs you by
\tthe wrist. Her nails dig deep into your skin.
\t  You can't move.
\t  You scream as Patty continues to change. Her
\tskin turns green and lumpy. Horns sprout from
\ther head. And her teeth grow into sharp fangs.
\t  You remember the horrible monsters on the
\twalls of the slide. Patty has turned into one of them!
\t  "Let me go. Please!" you plead.
\t  "Too bad you didn't trust me," she growls. "I
\tcan't have you ruining my plans." Her nails sink
\tdeeper into your flesh.
\t  "Ha-ha-ha!" she cackles. Then she wraps he
\tslimy mouth around your arm and bites down
\thard!

\t\t\tTHE END"""),

# PAGE 87
    '87': ("""\n\t87\n\n\t  You're staring at a sign that reads: WORLD'S
\tFREAKIEST FREAK SHOW! The three of you gape
\tat the pictures.
\t  There's the Three-headed Man with the ugl-
\tiest collection of faces you've ever seen. And the
\tSnake Lady-a young blonde girl with a beauti-
\tful face and the body of a slithering snake.
\t  "This is, uh-uh-" you start to say. But you
\tdon't finish. Because a large hand has come
\tdown on your shoulder. Hard.
\t  You slowly turn and gaze up at a huge man
\twith shoulders wider than a refridgerator. He has
\tcoal-black eyes with a thick moustache to
\tmatch. He looks strong enough-and mean
\tenough-to throw you over the fence with one
\thand.
\t  "What are you doing?" his deep voice booms.
\t"You're not allowed in here," he says, pointing
\tdirectly at you.
\t  "We're sorry," you say, hoping you appear
\tsorry and not just scared. "We wanted to look
\taround. That's all. But we'll leave. Right now."
\t  His eyes stare into yours. He clamps both
\thands down on your shoulders and says, "You're
\tnot going anywhere!"

\t  Uh-oh. Quick! Better turn to PAGE 4."""),

# PAGE 88
    '88': ("""\n\t88\n\n\t  You head towards the Boat Trip to Nowhere.
\tAt the dock, you spot a stubby guy with long
\tarms slouching against one of the mooring posts.
\tIn the strange light of the swamp, his skin
\tshines with an oily, green glow. And his ears
\tand nose are as craggy as tree bark.
\t  "Step right up," he calls in a gravelly voice.
\t  He pulls one of the motorboats over. It's red
\twith a silver racing stripe! "you can do fifteen
\tknots in these babies," he says. "But stay away
\tfrom the tree stumps."
\t  You watch the little man's sharp green
\tfingernails tearing the mooring rope apart. As
\tsoon as the boat is free, you jump in, step on
\tthe accelerator, an roar away from the dock.
\t  The wind blows hard against your face. You're
\tflying over the water. This is totally cool! You
\thead for a channel that you see up ahead. Too
\tbad you didn't notice that sign that reads: TO
\tBOOGER BOG.

\t  Enter the bog on PAGE 32."""),

# PAGE 89
    '89': ("""\n\t89\n\n\t  Dr Stone extends a long bony hand to pull you
\tfrom the net. When you peer into his face, his
\teyes roll up into his head.
\t  "Pleased to meet you" he rumbles.
\t  Did he say, "Pleased to meet you," or "Pleased
\tto eat you"? You're not sure, and don't want
\tto hang around to find out.
\t  I've got to get out of here, you think.
\t  As the doctor lowers his hand a bit more, you
\twriggle your right foot free of the netting. If you
\tgive him one hard kick in the stomach, maybe
\tyou can make a run for the door.
\t  But what about the monsters? Can you dodge
\tthem?
\t  You change your mind. "I'll wait-play it cool
\tuntil at least one of the beasts leaves the room,"
\tyou say to yourself.
\t  Then you change your mind again. "No, I'd
\tbetter make my escape now!"
\t  The doctor looms centimetres away. And
\tyou're still not sure what to do. You'd better
\tdecide fast!

\t  Try to kick the doctor and run? Turn to PAGE
\t 79.
\t  Wait until one of the monsters leaves and the
\t odds are better than three against one? Turn to
\t PAGE 51."""),

# PAGE 90
    '90': ("""\n\t90\n\n\t  NO!
\t  At the last minute, you wrench the steering
\twheel hard to the left. The side of your boat
\tclears the tree with a sickening scrape.
\t  You breathe a sigh of relief, but it ends in a
\tgroan. A huge, sharp root below the water has
\tjust ripped into the bottom of your boat. You
\thear a tearing sound, then gurgling as the cock-
\tpit starts to fill with water.
\t  "Now what?" you mutter.
\t  Then through the mist you spot another boat.
\tBut it's some distance away.
\t  "Hey, over here!" you cry out.
\t  Did they hear you? You cry out again. Then
\tyou glance behind you. More than half your boat
\tis underwater-and you're going down fast.
\t  What should you do? Keep yelling for help?
\tOr try to swim for safety? Make your choice-
\tQUICK.

\t  If you decide to wait to be rescued, go to PAGE
\t 100.
\t  If you decide to swim for it, go to PAGE 56."""),

# PAGE 91
    '91': ("""\n\t91\n\n\t  The red-eyed beast leans against you now,
\tpressing you hard against the wall. The monster
\tmoves his face close to yours. The jagged horns
\tat the top of his head nick your cheeks.
\t  You can't bear it any more. You bring your
\thand up with all your might and shove his head
\taway from yours.
\t  As you watch in horror. The monster's head
\trolls off it's neck. The head tumbles to the floor
\tand lands at your feet.
\t  The eyes glance up at you, and you notice his
\thideous lips moving. "That hurt," the head says.
\t"That really h-h..."
\t  He never finishes. You've destroyed another
\trobot!
\t  "Almost out of here," you whisper to yourself.
\tNow all you have to do is slip by the crusty,
\talligator-snout creature guarding the door.
\t  "You robots aren't so tough," you say to him
\twith fake bravery.
\t  "Oh, really?" the scaly beast croaks. "Well
\tmaybe not. But what makes you think that I
\tam a robot?"

\t  Turn to PAGE 122."""),

# PAGE 92
    '92': ("""\n\t92\n\n\t  You decide to wait. Someone should be here
\tsoon, you think. But after waiting in the space
\tshuttle for at least fifteen minutes, you're not
\tso sure. No one has shown up to rescue you.
\t  A chill runs down your back. You feel as if a
\tthousand pairs of eyes are watching you from
\tthe shadows.
\t  Now that you're accustomed to the darkness,
\tyou can see dozens of tracks leading in and out
\tof the tunnel.
\t  And then you hear a rustling sound. You
\tfreeze. You listen hard. Could it be rats-or
\tsomething worse?
\t  You draw up your knees and wrap your arms
\taround them tightly. Then you hear a hissing
\tsound-and you smell something odd. It's quite
\ta sweet smell-like heavy purfume. You hold
\tyour nose because the smell is making you feel
\tstrange. Dizzy. Sick.

\t  Hold your breath and turn to PAGE 20."""),

# PAGE 93
    '93': ("""\n\t93\n\n\t  What a sight!
\t  You can hardly believe your eyes!
\t  You scream again.
\t  It's Patty and Brad!
\t  "Hey guys, wait up!" you yell.

\t  Quick! Hurry to PAGE 26 and you can go on
\tthe Space Coaster with them."""),

# PAGE 94
    '94': ("""\n\t94\n\n\t  The ride stops.
\t  Dead.
\t  You are sitting in the dark.
\t  Nothing is moving.
\t  "Patty! Brad!" you call.
\t  Silence.
\t  Why don't they answer? They have to be
\tthere.
\t  You try to twist around. But you're locked in
\tyour harness and clamped in your headrest.
\t  Blinking in the dim light, your eyes dart to
\tthe left. Then to the right. You spot the dozens of
\tempty space rockets lining the walls. They seem
\tto come in sections-to make longer and shorter
\tspace rockets.
\t  Your mind starts working feverishly. Did your
\tsection detach from Patty and Brad's section?
\t  Suddenly the silence is shattered. Your seat
\tlock grinds open, and you are released from your
\tharness. You quickly spin around. Patty's and
\tBrad's cars have disappeared! If this is all part
\tof the ride, maybe you should hop out. But if
\tthe ride is broken, maybe you should wait for
\thelp.

\t  Wait for help to come? Turn to PAGE 92.
\t  Hop out of the car? Go to PAGE 111."""),

# PAGE 95
    '95': ("""\n\t95\n\n\t  You sit down on the slide and push off. The
\tworld tilts as you plunge down. Down, down,
\tdown.
\t  You're scared. But you can't help feeling that
\tthis is quite cool! Sliding and swirling in the
\tdarkness.
\t  Until you hear screams. The eerie screams
\tthat follow you as you twist and turn.
\t  Your heart starts pounding wildly. Oh, no!
\tYou must have picked the Doom Slide. You're
\tgoing to slide for ever!
\t  And, then, bump.
\t  A chute opens up. You hit the ground hard.
\tYou tumble over and over and finally stop.
\t  You lie on the ground. Panting.
\t  You're outside!
\t  You scramble to your feet and gaze around.
\t  You hear laughter. It seems to be coming from
\tthe bright pink building a few feet in front of
\tyou.
\t  You walk over to its big pink door and press
\tyour ear against it.
\t  Yes. The laughter is definitely coming from
\tinside.

\t  To find out what's so funny, turn to PAGE 117."""),

# PAGE 96
    '96': ("""\n\t96\n\n\t  ...they're swinging axes.
\t  Your heart leaps into your throat. The elves
\tmove to the roadside now-and they're chop-
\tping down the horse-drawn carts ahead of you!
\tOne cart splinters into a million pieces before
\tyour horrified eyes.
\t  The elves continue on to the next cart. Their
\tsharp blades slice right through it!
\t  Your horse keeps trotting up the steep path.
\tYou're heading right for the wildly chopping
\telves!
\t  "Do something!" Patty cries.

\t  Turn to PAGE 23."""),

# PAGE 97
    '97': ("""\n\t97\n\n\t  Your hand clamps around the can of Monster
\tBlood in your pocket. Quickly you snap off the
\tlid and the green gunk pours out.
\t  "Look! It's alive!" Brad shouts.
\t  He's right. The Monster Blood oozes from the
\tcan, quivers, and appears to stretch and pull
\titself up! Then it starts to roll and bounce,
\tmaking horrible sucking sounds.
\t  Great! It's rolling into the crowd, sucking up
\teverything in its path!
\t  "Run!" Big Al screams as the huge green ball
\trolls over the people in the crowd-sucking
\tthem up with a loud plop.
\t  Then the Monster Blood hits the side of the
\ttent. It changes direction.
\t  It's coming after you!

\t  Hurry to PAGE 129."""),

# PAGE 98
    '98': ("""\n\t98\n\n\t  Well, looks can fool you. He is not a wimp.
\t  And he's very angry-at you.
\t  In the next moment, he scoops you up and
\thurls you at the cell wall. His throw is so force-
\tful, you smash right through the wall and soar
\tout of the carnival grounds.
\t  Congratulations! You escaped the Carnival of
\tHorrors-but not in one piece.

\t\t\tTHE END"""),

# PAGE 99
    '99': ("""\n\t99\n\n\t  "Okay, get me out of here," you say to the
\tdwarf. "Did you help my friends, too?"
\t  The dwarf does not answer. He sprints off and
\tyou have to race to keep up with him. Through a
\tconfusing maze of twisting tunnels. You're very
\tglad you have a guide.
\t  The dwarf suddenly stops. "That way," he
\tsays gruffly, pointing straight ahead.
\t  Before you can blink, he vanishes in a puff of
\tsmoke! And you're left standing in front of two
\tdoors. One red. One blue. The red one has a sign
\tthat reads: DANGER. The blue one has a sign
\tthat reads: BIG DANGER.

\t  If you leave by the red door, go to PAGE 104.
\t  If you try the blue door, go to PAGE 57."""),

# PAGE 100
    '100': ("""\n\t100\n\n\t  "Help! Help! Over here!" you scream, waving
\tyour arms wildly in the air.
\t  "Hold on! a deep voice answers through the
\theavy mist.
\t  The boat turns and speeds towards you. As it
\tnears, the voice calls out again. "Jump! Jump
\tover!"
\t  Jump? Is he crazy? Can you really jump on
\tto a moving boat?
\t  The boat is coming closer now. Closer. Closer.
\tYou stand up. You bend your knees. You're
\tabout to jump-and the boat speeds right past
\tyou.
\t  But wait! It is circling back now in a nice,
\tslow approach. It glides up to you, and gigantic
\thands pull you on to the boat.
\t  "You saved me!" you cry.
\t  You gaze up and gasp in surprise. The man
\tin the other boat isn't a man-it's a monster
\twith a drooling snout and rows of jagged teeth.
\t  "Save you? Save you?" the monster repeats.
\t  His red eyes light up. "Save you ... good idea,"
\the says. "I won't eat you now. I'll save you for
\ta midnight snack!"


\t\t\tTHE END (Burp!)"""),

# PAGE 101
    '101': ("""\n\t101\n\n\t  You make it! You make it out of the park!
\t  You also make it out of the state!
\t  In fact, the last time anyone saw you, Patty
\tand Brad, you were all a tiny blip on NASA's
\tradar screen.
\t  Congratulations! You escaped from the Carni-
\tval of Horrors.
\t  Happy landings!

\t\t\tTHE END"""),

# PAGE 102
    '102': ("""\n\t102\n\n\t  "I'm not going anywhere with you, Big Al. I
\tbelieve the Snake Lady!"
\t  "So do I," says Patty.
\t  "Me, too!" Brad echoes.
\t  "That's too bad," Big Al says. Then he turns
\tto the Snake Lady.
\t  "And as for you, Miss Reptilia-I told you,
\tyou've been overacting. If these kids believe you,
\twe won't be able to torture them with our real
\thorrors."
\t  "Sorry, boss," she says. "So what do you want
\tme to do with them?"
\t  You can hardly believe it! Real horrors?
\t  "What kind of carnival is this?" you shout.
\t  "The Carnival of Horrorssssss," the Snake
\tLady answers-and that's the good news.

\t  Turn to PAGE 120 for the bad news."""),

# PAGE 103
    '103': ("""\n\t103\n\n\t  "We've got to jump," you tell Patty and Brad.
\t"It's our only chance."
\t  "Okay," Brad agrees as your cart inches up to
\tthe chopping elves.
\t  "Come on," you cry. "Now!" But Brad is too
\tparalysed with fear to move. You and Patty grab
\thim and haul him towards the side of the cart.
\t  Your cart has reached the elves! One of them
\tsmirks as he lifts his axe.
\t  It's right above your neck.
\t  You picture your head tumbling down the side
\tof the mountain.
\t  With a loud cry, all three of you jump. You
\tland with a thud on a rocky ledge. It breaks
\tyour fall. But the rock is too weak to hold all of
\tyou.
\t  You scream again as the edge tears loose and
\tthe world drops from under your feet. You
\ttumble over and over, down the side of the
\tmountain.

\t  Go to PAGE 109."""),

# PAGE 104
    '104': ("""\n\t104\n\n\t  You push open the red door. Another tunnel
\tlies beyond it. You follow its twists and turns,
\tand you realize that you're sloshing through cold
\tmuddy water. It grows deeper and chillier as
\tyou go.
\t  With a cold shudder, you decide to head
\tback-until you hear a slurping noise behind
\tyou. Whirling around, you watch in horrible fas-
\tcination as giant earthworms crawl out of the
\tmud. Gross!
\t  There's no way you're going back there. You
\tclench your teeth and slog onward. Up ahead,
\tyou see a dim green light. Great! An exit.
\t  As you reach the end of the tunnel, you hear
\ta low growl behind you. At first you try to pre-
\ttend it's your imagination. But there's no mis-
\ttaking the sound of thudding footsteps. Getting
\tcloser. And closer. And now it's breathing down
\tyour neck!

\t  Go to PAGE 61."""),

# PAGE 105
    '105': ("""\n\t105\n\n\t  It's a tree branch! Grabbing at you. Tugging,
\ttugging at your hair. You can't break free. It's
\tgnarly stubs dig in deeper as you struggle.
\t  Suddenly you feel something wrap itself
\taround your arms. Then your legs. Closing in
\ttighter. Tighter.
\t  You gaze down and see them-black knobby
\ttree limbs twisting around you. Strangling you.
\t  You drop hold of the steering wheel and begin
\tto claw at the branches, ripping them away.
\t  And then you peer up-and see a terrifying
\tsight. It's a huge tree. And you're heading
\tstraight for it! You grasp the steering wheel to
\tregain control of the boat. The tree is just inches
\taway.
\t  Are you going to CRASH?!

\t  Turn to PAGE 90."""),

# PAGE 106
    '106': ("""\n\t106\n\n\t  "Unless what?" you scream. "Tell me!"
\t  "You can escape the Carnival of Horrors if you
\tleave before closing time."
\t  "When is closing time?" you shoot back.
\t  "When the last ride stops..." the lady whis-
\tpers. "At midnight."
\t  You glance at your watch-11:40. Twenty
\tminutes-that's not so bad. But how do you get
\tout of here?
\t  As if the lady can read your mind, she says,
\t"There's only one right way."
\t  Then all around you, the crowd begins to
\tchant.
\t  "Only one right way, only one right way." They
\trepeat it over and over again.
\t  "What is it? you scream. "Which way?"
\t  It's useless. They're not going to tell you.
\t  But it's not midnight yet. There's still time to
\tfigure it out.
\t  Until the floor begins to tremble. And the
\twalls begin to shake.
\t  Earthquake!

\t  Turn to PAGE 42."""),

# PAGE 107
    '107': ("""\n\t107\n\n\t  "Sorry, Brad. I think Patty's right," you tell
    \thim as you turn towards the Hall of the Moun-
    \ttain King. "I think I spotted an exit there when
    \twe first came in."
    \t  Patty runs ahead. "Look!" she cries out.
    \t"There's the path. It leads past the Hall of the
    \tMountain King to the exit."
    \t  "Yeah, but who are those people up there?"
    \tBrad asks. "They're blocking the way."
    \t  You peer up ahead and see them-the people
    \tin the old-fashioned clothes. And they're still
    \tchanting-"Only one right way, only one right
    \tway".
    \t  "They're not going to let us out!" Brad panics.
    \t  "Okay. Okay. I have an idea," you say calmly.
    \t"Let's go into the Mountain King ride-maybe
    \twe can jump off at the end and sneak past
    \tthem."
    \t  Do you have another choice? No.

    \t  If you want to go on the Mountain King ride,
    \t turn to PAGE 75.
    \t  If you want to go on the Mountain King ride,
    \t turn to PAGE 75."""),

# PAGE 108
    '108': ("""\n\t108\n\n\t  "We've got to get out of here, it's almost mid-
\tnight," you say as you run towards the Hal-
\tlowe'en Express ride.
\t  "Hey, maybe we should try one of these cars,"
\tBrad says, pointing to the red and orange cars
\tthat run on a track.
\t  The three of you crowd into a little car that's
\treally meant for two. You jam your foot on the
\taccelerator and you're flying!
\t  "All right!" Brad cheers. "We're on our way
\thome! Hey, I wonder why they call this Hal-
\tlowe-en Express?" he asks.
\t  You turn the wheel sharply to the left, and
\tthen you know why...

\t  Speed over to PAGE 54."""),

# PAGE 109
    '109': ("""\n\t109\n\n\t  You squeeze your eyes shut and wait for the
\tcrash. Finally, you land. You glance up. You're
\tat the foot of the Log Flume ride.
\t  You, Patty and Brad have lots of cuts and
\tbruises, but you're okay! Terrific! You think-
\tuntil you spot the army of elves with their axes.
\tThey're rushing down the mountain towards
\tyou! The only escape is to enter the flume ride,
\tso you dash inside.
\t  The Log Flume reminds you of a western log-
\tging camp, complete with log cabins, trees,
\ttrucks, and a sparkling blue lake.
\t  In the distance, you cam hear the buzz of
\tchain-saws. And down by the lake, giant cranes
\tpick up logs and plop them in the water. Some
\tof the logs are hollowed out in the middle with
\tseats for passengers. As you watch, the current
\tcatches one. It glides to the edge of a waterfall,
\tplunges over, and shoots down.
\t  As you glance around, you spot an EXIT sign.
\t  Then to your horror, you see a giant crane
\tswinging your way. "Duck!" you scream.
\t  Will you make it to the exit? Is this your lucky
\tday?

\t  If you are reading this book on a Monday,
\t Wednesday, Friday, or Saturday, go to PAGE
\t 114.
\t  If it's a Tuesday, Thursday, or Sunday, go to
\t PAGE 71."""), 

# PAGE 110
    '110': ("""\n\t110\n\n\t  Something tells you that this monster is not
\ta robot. This one is for real. Maybe it's the way
\the stares into your eyes. Or maybe it's the rows
\tand rows of razor-sharp teeth jutting from his
\tmouth.
\t  You take a step back. He takes a step closer.
\tA drop of his drool drips on your hand. It sizzles
\tand burns.
\t  This is the end, you figure. You'll never see your family
\tor Patty and Brad again.
\t  The monster lifts his gigantic, clawed hand.
\tHe waves it over your head. And you wait for
\tthe searing pain as it plunges down to strike
\tyou.
\t  But that's not what happens.
\t  The monster slowly lowers his hand and
\tclutches at his own neck, and then-pulls his
\town head off! And when you discover what's
\tunderneath, you know you're still in big trouble!

\t  Quick-head over to PAGE 133."""),

# PAGE 111
    '111': ("""\n\t111\n\n\t  Your pulse pounds in your ears as you care-
\tfully lift yourself out of the car. The tunnel is
\tdark and musty and really creepy. Anything
\tcould be lurking in the shadows.
\t  This must be part of the ride, you reason. And
\tthe more you think about it, the more convinced
\tyou are. You're scared. But you have to admit,
\tthis is pretty cool.
\t  In the distance, you spot several red lights
\tthat seem to lead to other dimly lit tunnels. you
\tcautiously head towards one of them. Overhead
\tsomething dark and slimy drips. Splattering on
\tthe top of your head. Stinging your forehead.
\t  As you desperately try to wipe the burning
\tslime away, something grabs you by the knees!
\t  Aaaah! You look down. A pair of red-rimmed
\teyes meet yours. It's a dwarf with scraggy red
\thair and a toothless smile.
\t  "Want me to lead you out of here, kid?" he
\tasks. You're about to follow the dwarf, but then
\tyou stop. Is he part of the ride? He looks really
\tevil. What do you do?

\t  Follow the dwarf? Go to PAGE 99.
\t  Decide not to follow the dwarf? Go to PAGE 33."""),

# PAGE 112
    '112': ("""\n\t112\n\n\t  Yeoow! Someone splashes cold water in your
\tface. Your eyes open.
\t  "Come on! Wake up! It's almost show time,"
\ta raspy voice says.
\t  "Show time?" you say, gazing into the eyes of
\ta dwarf. "What show?"
\t  "The Freak Show. You are the Amazing Sia-
\tmese Triplets."
\t  You glance around and see Patty on one side
\tof you and Brad on the other. You try to pull
\taway from them, but you can't.
\t  "We're stuck together with some kind of glue,"
\tPatty says.
\t  "It isn't glue," Brad argues.
\t  "Is too!"
\t  "Is not!"
\t  Well, whatever it is- you are stuck. Stuck
\tbetween your arguing friends for a long, long
\ttime-for ever. And here's something you can't
\targue about. This really is...

\t\t\tTHE END"""),

# PAGE 113
    '113': ("""\n\t113\n\n\t  Help some freaks? That's a good one! You
\tlaugh.
\t  You think about Madame Zeno, the fire, and
\tthe disappearing tent. Totally cool! You wonder
\twho thought up such awesome special effects.
\t  You can't wait to tell Brad and Patty all about
\tit.
\t  You search for your friends in the big wooden
\tbooths. Instead you find incredible games of
\tchance. Some test your eye-hand coordination.
\tOthers require pure luck. But they all offer the
\tmost amazing prizes you've ever seen-CD
\tplayers, video games, fifteen-speed mountain
\tbikes. You can't wait to play!
\t  You spot a booth with a crowd gathered in
\tfront. That's odd, you think. Didn't Big Al say
\twe were the only people at the carnival tonight?
\tYou wonder if your friends are in the crowd. You
\tmove closer.
\t  "Oh. I get it," you say aloud. "These people
\tmust work at the carnival."
\t  You're about to call out to them. Until you see
\ttheir eyes. Strange, haunted eyes.

\t  See what happens on PAGE 16."""),

# PAGE 114
    '114': ("""\n\t114\n\n\t  This is your lucky day.
\t  You duck as the crane swings over your head.
\t  "Run!" you shout to your friends.
\t  You glance at your watch-11:55. If you're
\treally lucky, you can still make it out of the
\tcarnival by midnight.
\t  You can see the exit up ahead. As you charge
\tthrough the gate, you feel really hopeful-until
\tyou run into Big Al.
\t  He blocks the exit with his huge body. His
\tmassive hands are planted on his hips. "No one
\tescapes from the Carnival of Horrors!" he roars.
\t  You've got to find a way out. Now!
\t  To your right is the entrance to Hallowe'en
\tExpress-you could try that.
\t  Or maybe you should run down a different
\tpath. There's got to be more exits around here
\tsomewhere.
\t  Choose fast!

\t  Run down a different path? Go to PAGE 5.
\t  Hallowe'en Express? Go to PAGE 108."""),

# PAGE 115
    '115': ("""\n\t115\n\n\t  There's nothing in your pocket but lint.
\t  "Help! Save me!" you cry.
\t  The vulture swoops down and drops you in
\tthe nest.
\t  The baby vultures approach.
\t  Mouths open-ready to peck you to death...
\t  But-good news! They don't eat you. You fall
\tout of the nest instead.
\t  Please, close the book fast, or the next sound
\tyou hear will be your body, hitting the ground
\twith an awesome thud.
\t\t\t THUD!
\t  Not fast enough. Okay, don't go to pieces. Pull
\tyourself together and prepare to visit the Carni-
\tval of Horrors again-the next time you're brave
\tenough to open this book!

\t\t\tTHE END"""),

# PAGE 116
    '116': ("""\n\t116\n\n\t  ZAP!
\t  Big Al throws a switch and the magnet shuts
\toff. You come flying down to earth-right where
\tBrad and Patty are waiting.
\t  "I've played your stupid game. Now let us go!"
\tyou tell Big Al.
\t  Big Al doesn't answer. But the crowd does.
\t"SUD-DEN DEATH! SUD-DEN DEATH!
\tSUD-DEN DEATH!"
\t  The crowd surges towards you. They are not
\tfriendly. They back you up against a wall. You're
\ttrapped.
\t  Trapped by a mob!
\t  You reach into your pocket, hoping to find
\tsomething that might help you. Something to
\tsave you...

\t  If you've won a can of Monster Blood, go to
\t PAGE 97.
\t  If you don't have the Monster Blood, run to
\t PAGE 27."""),

# PAGE 117
    '117': ("""\n\t117\n\n\t  You open the door and enter a room bursting
\twith people who seem to be waiting for you. You
\tthink that's weird until you study them-and
\trealize something even stranger. They're all
\tdressed up in old-fashioned costumes.
\t  "Welcome to the Carnival of Horrors," a tall
\twoman with a red parasol says, smiling. "Nice
\tof you to join us."
\t  The Carnival of Horrors. The words send shiv-
\ters down your spine.
\t  The woman with the red parasol whispers in your
\tear, "Don't you want to know the secret of the
\tCarnival of Horrors?"
\t  You nod "yes".
\t  "The Carnival of Horrors comes alive in a dif-
\tferent place and a different time each night.
\tTonight we're in your town. Tomorrow we could
\tbe in another country! But every place we stop,
\twe invite kids like you to join us..."
\t  "Thanks for the invitation," you say, "but I
\tgotta go."
\t  "I'm sorry." The lady chuckles. "You can never
\tescape from the Carnival of Horrors," she says
\tsolemnly. "Unless..."

\t  Unless what? Turn to PAGE 106."""), 

# PAGE 118
    '118': ("""\n\t118\n\n\t  You turn left. Somewhere ahead of you, you
\thear laughter.
\t  "Is somebody there?" you call out.
\t  Silence.
\t  You stare at your reflections in the mirrored
\thall.
\t  Am I trapped? you wonder. Am I in real
\tdanger? Or is this all a big, scary joke? Your
\theart begins to race.
\t  You inch forward a few more steps-moving
\ttowards the laughter. Slowly.
\t  "Over here," a voice calls again. But now the
\tvoice seems to be coming from behind you!

\t  Turn to PAGE 36.
\t  HELP!"""),

# PAGE 119
    '119': ("""\n\t119\n\n\t  You take charge of the reins to urge the horse
\ton.
\t  "Giddyup, boy," you and Patty shout. But your
\thorse won't move any faster.
\t  You shoot a glance up ahead. The elves are
\tchopping ... and a shiny blade ... is now ...
\tright over ... your head!
\t  "No," you scream. "NO! Let me out of here."
\t  You feel a sharp pain. And then you realize you've
\tjust had the shortest haircut of your life. Unfor-
\ttunately, they took a little too much off the top.

\t\t\tTHE END"""),

# PAGE 120
    '120': ("""\n\t120\n\n\t  The bad news is the Snake Lady fooled you.
\t  "Throw them into the large cell with Harold
\tand all the other prisoners," Big Al commands.
\t  You are shoved into a dark cell. You hear a
\tclick. You're locked in. As the Snake Lady leaves
\twith Big Al, you can hear their laughter echo
\tdown the hall.
\t  You glance into the other cells and think, the
\tfreaks are prisoners. They do need our help.
\tThen you peer into the darkness of your cell-
\tto find out who Harold is.
\t  There's no way you could miss him. Harold is
\ta giant. He's huge-twice as big as an American
\tfootball player. His hands are, in fact, the size
\tof two footballs. His arms look like tree trunks.
\t  At first you are afraid of him, but then you
\tthink, Hey! He's trapped, too. Maybe can
\tconvince him to help us. And then you get a big
\tidea!

\t  Turn to PAGE 28."""),

# PAGE 121
    '121': ("""\n\t121\n\n\t  You grab the sides of the slide and lower your-
\tself down. The second you sit, the slide's floor
\ttilts up beneath you and propels you forward.
\t  You shriek!
\t  You raise your arms and scream louder. You
\tslide faster and faster. In total darkness. Dark-
\tness so black, you can't even see your own feet
\tin front of you.
\t  Your eyes dart frantically from side to side.
\tFaces suddenly appear in the darkness in bright
\tflashes of light. Faces of hideous monsters with
\tdeformed heads and oozing flesh.
\t  But you're moving too fast to focus on them.
\tYou slide and slide-until the faces stop flash-
\ting and you're covered in the thick, heavy black-
\tness again.
\t  You scream as you round a sharp curve. Your
\thead is spinning. You pick up speed.
\t  When will it end?
\t  Then you hear the screams. Chilling screams
\tthat echo through the darkness.
\t  Oh, no! You must have picked the Doom Slide!

\t  Zoom to PAGE 63."""),

# PAGE 122
    '122': ("""\n\t122\n\n\t  The creature slides one step towards you, and
\twith a burning stare says, "I am not a robot. I
\tam not going to shut down. So don't bother with
\tany of your silly, human tricks!"
\t  You stare at him. You study him hard. Is he
\tlying. Is he a robot like the other two? Or could
\the be a lot more dangerous?
\t  Your knees begin to tremble when you think
\tabout never going home-never seeing your
\tfamily and friends again. Tears start to
\tsting your eyes. Angry tears! No carnival-not
\teven a Carnival of Horror-is going to defeat
\tyou!
\t  You stare deeply into the evil eyes of the crea-
\tture hovering before you.
\t  Robot? Real monster? You finally decide!

\t  If you think the creature is a robot, try to knock
\t his head off on PAGE 81.
\t  If you think he's a real monster or something
\t worse, stay cool on PAGE 110."""),

# 123
    '123': ("""\n\t123\n\n\t  "The Final Challenge," Big Al announces. And
\tthe crowd goes wild.
\t  Then he turns to you and says, "Remember-
\tthe fun games are over. Now you are playing
\tfor your life."
\t  "You go first," Big Al says to you. You see
\tBrad and Patty taken off to the side by a huge
\tman in a black hood.
\t  Two red-haired dwarfs in clown costumes
\tscurry up the steps. To your surprise, they fit
\tyou with new high-top trainers-trainers with
\tmetal studs running up the backs. This is going
\tto be some kind of race, you think. But then you
\tchange your mind-when they snap a heavy,
\tmetal helmet on your head.
\t  The crowd's cheers grow louder. Big Al throws
\ta switch. The curtain behind you parts and-
\tWhammo! The wall behind the curtain turns
\tinto a super magnet. You go zinging to the wall
\tlike a dart to a bull's-eye.

\t  Zing back to PAGE 25."""),

# 124
    '124': ("""\n\t124\n\n\t  "FI-NAL! FI-NAL! FI-NAL!" you hear the
\tcrowd yelling as you spin round and round.
\t  You're getting dizzy. Really dizzy. So dizzy
\tthat you faint.

\t  You eyes flutter open on PAGE 112."""),

# 125
    '125': ("""\n\t125\n\n\t  "This way!" You wave to Patty and Brad.
\t  The three of you turn to the left and keep
\trunning-straight into a pond!
\t  "Why didn't you tell us to stop?" Patty whines.
\t  "Don't complain to me!" you shout back. "We
\tfollowed you through the fence!"
\t  You turn and slog your way back to
\tshore. Patty and Brad make it there first. You
\tare a few feet away-when you see it.
\t  An alligator.
\t  With its mouth gaping open-revealing two
\trows of razor-sharp teeth.
\t  You freeze.
\t  Patty spots the alligator and yells, "Quick!
\tThere's a log! Jump on it!"
\t  You scramble up on the log, but it's no use.
\tYou're still an easy target.
\t  The alligator opens it's huge mouth even
\twider. He slithers right up to the log. And you
\tcan tell he's ready. Ready to crunch down on
\tyou!

\t  Don't scream yet. Turn to PAGE 43."""),

# 126
    '126': ("""\n\t126\n\n\t  "Yay! Our hero!" the freaks cheer as they bolt
\tout there cells.
\t  You follow the giant through a side exit. And
\tin no time, you're leading all your new friends
\tto your house.
\t  You're sure your parents won't mind taking
\tthem in. After all, how much can a twenty stone
\tgiant, a thirty stone fat lady, and a three-headed
\tman eat? Hmmmm. Better not answer that
\tquestion.
\t  Just be happy that you've come to...

\t\t\tTHE END"""),

# 127
    '127': ("""\n\t127\n\n\t  You're not fast enough to get away from the
\tghost. You're running now, but the ghost swoops
\tdown in front of you. You plough into him-and
\tpass right through him!
\t  The carnival people are swarming after you.
\tThey don't want you to leave the carnival.
\t  "Hurry!" you yell to your friends-only three
\tminutes to midnight! You dash off in one direc-
\ttion, then another. The carnival people are
\tapproaching from every whch way. They carry
\ttorches with flames that leap high in the air.
\t  You steal a glance at your watch-11:58.
\t  "We can't let them catch us!" you scream.
\t"Let's hide!"
\t  But where can you hide? Up ahead you see a
\tgigantic cannon. All three of you could fit easily
\tin there.
\t  You also spot a baby ride-the baby choo-choo
\ttrain-maybe you could squeeze into that.
\t  Quick! Pick one-and hope for the best.

\t  Cannon? Go to PAGE 130.
\t  Choo-choo? Got to PAGE 128."""),

# 128
    '128': ("""\n\t128\n\n\t  You squeeze into the choo-choo and scrunch
\tdown. 11:59.
\t  Lights from the carnival people's torches
\tsweep over you. Their foul smell fills your lungs.
\t  The blood pounds in your temples.
\t  You're sure they're going to find you. But
\tyou're trapped now.
\t  There's no way out.
\t  You hear someone shout in the distance.
\t"Closing time!" And then you hear a bell start
\tto chime...
\t  ...Midnight!
\t  "One, two, three," Brad counts the chimes.
\t  You want to stranggle him!
\t  "Four, five..."
\t  Suddenly the kiddie train starts to move.
\t  "six ... seven ... eight ..."
\t  You sit up and what you see is the biggest
\tshock of this whole horrible night...

\t  Turn to PAGE 70."""),

# 129
    '129': ("""\n\t129\n\n\t  The Monster Blood has grown so big-now
\tyou can't see over it or around it.
\t  "Run for your lives!" Patty screams. But
\treaching the door is impossible.
\t  The mound of green slime is bearing down on
\tyou. Fast! You stand frozen to the spot. Terri-
\tfied. And then-just in time-you, Patty, and
\tBrad leap to the side. And the Monster Blood
\tslams into the wall with a crushing force-and
\tploughs right through it.
\t  You stare at the giant gaping hole in the wall.
\tQuickly, the three of you jump through the
\topening. You are standing outside the main
\tgate-where you came in!
\t  There's a wide path of destruction across the
\tfield and the forest beyond. From somewhere, a
\tclock chimes twelve times, sending a chill down
\tyour spine. And when you peer back at the car-
\tnival, it has disappeared. All that's left is a
\tspooky silver mist.

\t\t\tTHE END"""),

# 130
    '130': ("""\n\t130\n\n\t  You and your friends squeeze into the cannon.
\t  "Ouch! You're sitting on my hand," Brad
\twhines.
\t  But you don't have time to apologize.
\t  "Do you smell something ... burning?" you
\task.
\t  BOOM! There's a tremendous explosion. You
\tfly though space. You are heading for a fence
\tthat encloses the carnival, and the field beyond.
\t  Will you make it out of the park?

\t  Go to PAGE 101."""),

#131
    '131': ("""\n\t131\n\n\t  SUCKER!
\t  You didn't really think you could get out this
\teasily, did you?
\t  Check out the title of this book: Escape From
\tthe Carnival of Horrors.
\t  Horrors! You need to face a lot more horrors-
\tand then (maybe) you'll escape.

\t  Quick! Turn to PAGE 116."""),

#132
    '132': ("""\n\t132\n\n\t  The fortune-teller said this number might
\tsave your life. But how?
\t  Then you see it. In the corner. A tall silver
\tlocker with the number 132 painted in red.
\t  "In here," you say, opening the door to the
\tlocker. You push Patty and Brad inside.
\t  As soon as you close the door, the locker
\tbegins to rattle and shake. You're nearly blinded
\tby a bright, white light. You hear a loud whoosh-
\ting sound. And then all is silent. The door pops
\topen-and you're amazed at what you see.

\t  Turn to PAGE 21."""),

# PAGE 133
    '133': ("""\n\t133\n\n\t  Those eyes behind the alligator snout-those
\tbeady eyes. You should have recognized them
\tbefore. It's Big Al.
\t  "Hey! You did a great job here," he says
\twarmly. "You've really got the stuff for the Car-
\tnival of Horrors."
\t  "Uh, thanks," you mumble. "But I really have
\tto go home now."
\t  "What's the rush?" he asks, patting you on
\tthe shoulder. "Aren't you having fun?"
\t  Fun? you think. Crushed between solid walls.
\tThen attacked by a bulging-eyed monster. Fun?
\tNo. This isn't fun. This is weird.
\t  "Uh, yeah. It's been really great. But, um, I
\treally do have to get home," you stammer. "So
\tif you'll just take me to wherever Patty and Brad
\tare-and show us the way out-we'll be going."
\t  "I'm afraid that isn't possible," Big Al says.
\t"Just open the door and you'll understand."

\t  You have no choice. You have to open the door
\t and go to PAGE 117."""),

#134
    '134': ("""\n\t134\n\n\t  You've got to figure out what you weigh on
\tMars. Fast. But how?
\t  You're about to give up when you notice a
\tflashing sign. It reads: THE GRAVITY ON MARS IS
\tALMOST 40 PERCENT OF WHAT IT IS ON EARTH.
\tOkay, now you can figure it out.
\t  Multiply your real Earth weight in pounds by
\tfour. (There are 14 pounds in a stone.) Now drop
\toff the last digit. For example, if you weigh 90
\tpounds, 90 x 4 = 360. Dropping off the last digit,
\tyou get 36 for your weight on Mars.
\t  If you don't want to do the maths, you can
\tleave it to luck. Just guess.

\t  If you think your Mars weight is 37 to 39, go
\tto PAGE 53.
\t  If you think your Mars weight is less that 37
\tor more than 39, go to PAGE 22."""),

#135
    '135': ("""\n\t135\n\n\t  You open the door and climb a steep ramp
\tthat curves round and round. It's cold and dark
\tinside. Halfway up the ramp, you stop. There's
\tanother sign: WARNING!-YOU MAY BE THE ONE
\tTO SLIDE TO YOUR DOOM!
\t  You continue up the ramp. You finally make
\tit to the top, and find yourself standing on a
\twide, dimly lit platform. A row of long, curving
\tslides stretches out before you. The slides are
\tnumbered from one to ten.
\t  You think hard. The Doom Slide. You know
\tyou've heard about it before. But where? Where
\twas it?
\t  And then you remember! It was in a GOOSE-
\tBUMPS book you read! One Day at HorrorLand.
\t  Now you know you're in big trouble. Because
\tyou remember all about the Doom Slide from
\tthe book. You remember that if you pick the
\twrong slide, you'll spend the rest of your life
\tsliding and sliding-for ever!
\t  Which number is the Doom Slide? Which one?

\t  If you remember which number slide is the
\tDoom Slide (or if you have the book and can look
\tit up), choose a slide that is not the Doom Slide.
\tIf you can't remember, you'll have to leave it to
\tluck. Pick a number between 1-10.
\t  Pick slide 1, 4, or 5, and go to PAGE 121.
\t  Pick slide 2, 7, or 9, and go to PAGE 95.
\t  Pick slide 3, 6, 8, or 10, and go to PAGE 68."""), 

}


# Start
page_topper('top')
from_start = input("\n\tAre you starting from scratch? YES(y) NO(n) ... ").lower()
reading = True
still_reading = 'y'


while reading == True:

    # Show introduction
    if (from_start == 'y'):
        from_start = 'n'
        page_topper('top')
        print(pages['0'])
        input()
        # Do you want to read on?
        still_reading = reading_still('ask')
        if still_reading == 'y':
            reading = True
        elif still_reading == 'n':
            reading = False

        
    # Start from selected page
    elif (from_start == 'n'):
        while (still_reading == 'y'):


            # Choose page
            new_page = choose_page('pick')

            # Wheel of Chance page
            if new_page == pages['9']:
                wheel_result = spin('wheel')
                pages['9'] = f"\n\t9\n\n\t  The wheel spins and lands on ...\n\t  {wheel_result}.\n\n\t  Quick! Go to the page you landed on!"
                page_topper('top')
                print(new_page)

                # Do you want to read on?
                still_reading = reading_still('ask')
                if still_reading == 'y':
                    reading = True
                elif still_reading == 'n':
                    reading = False
                else:
                    page_topper('top')
                    print("\n\tYou entered the wrong key.")
                    still_reading = reading_still('ask')


            # Any other page
            else:
                page_topper('top')
                print(new_page)
                still_reading = reading_still('ask')
                if still_reading == 'y':
                    reading = True
                elif still_reading == 'n':
                    reading = False
                else:
                    page_topper('top')
                    print("\n\tYou entered the wrong key.")
                    still_reading = reading_still('ask')

    
    # Starting from beginning, incorrect input        
    else:
        page_topper('top')
        print("\n\tYou entered the wrong key.")
        from_start = input("\n\tAre you starting from scratch? YES(y) NO(n) ... ").lower()

# Goodbye reader
else:
    page_topper('top')
    print(f"\n\tGOODBYE, {reader.upper()}")
    input()

                       
    
    
         
