team_batting_first = input("Enter the team that batted first (India or Pakistan): ")
stadium = input("Enter the stadium name: ")
top_batsman = input("Enter the name of a top batsman from Pakistan: ")
top_bowler = input("Enter the name of a top bowler from Pakistan: ")
winning_team = input("Enter the winning team: ")
losing_team = input("Enter the losing team: ")
target_score = input("Enter the target score: ")
overs_played = input("Enter the number of overs played in the chase: ")
winning_margins = input("Enter the winning margin (e.g., '10 wickets'): ")


story = f"""
🏏 **The Night History Was Made** 🏏  

The atmosphere at **{stadium}** was electrifying.  
The tension was unbearable as **{team_batting_first}** won the toss and decided to bat first.  

The crowd roared as the first ball was bowled.  
But soon, the game took an unexpected turn.  

🔥 **{top_bowler} was on fire!**🔥  
With fiery pace and deadly accuracy, he dismantled the opposition.  
Every delivery felt like a bullet, and wickets started tumbling.  
**{losing_team}** struggled but managed to put up **{target_score}** on the scoreboard.  

Now, it was time for the chase.  

The entire stadium held its breath. Could **{winning_team}** do the impossible?  
The pressure was immense, but **{top_batsman}** stepped onto the field with a steely gaze.  
From the very first shot, it was clear—he meant business.  

🎯 Cover drives.  
🚀 Flicks over mid-wicket.  
💥 Blazing sixes into the stands.  

Every stroke sent shockwaves through the opposition.  

The partnership between the openers was **unstoppable**.  
The crowd’s cheers grew louder with every run.  

As the target got closer, fans held their breath.  
**{winning_team}** was rewriting history!  

And then… the final shot was played.  

🏆 **Pakistan won by {winning_margins}!** 🏆  

The players erupted in joy. The crowd screamed in celebration.  
Tears of happiness rolled down fans' faces.  

🔥 **A historic victory. A night to remember. A game for the ages.** 🔥  
"""

print("\nHere’s your legendary cricket story:\n")
print(story)
