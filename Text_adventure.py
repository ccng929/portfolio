start = '''

You are at Accenture Mall, and you heard about sales going on. Your favorite
stores are PINK and Urban Outfitters.
'''

left=("""You decide to go left and now you are in PINK. While shopping you
find $20 in a bin. Shortly after you receive a 100 dollar bill. After a
while you've collected $200 and now it is time to pay.""")

steal=("""A mall cop runs after you and you get caught while tripping over a
bag. The cop fines you for $200.""")

pay=("""You pay and get a coupon for unlimited PINK merch for a year.""")

right=("""You choose to go right and you are at Urban Outfitters.""")

match_making=("""You choose to talk to the skaterboy and he seems chill and he
even lets you ride on his skateboard. You bang into a pole and die.""")

walk_away=("""You walk away from the skaterboy and get offered a job by an
Urban outfitters worker.""")

print(start)
store = "store"
done= False
while not done:
    user_input = input("Type 'left' to go left to PINK or 'right' to go right
Urban Outfitters.")
    if user_input == "left":

        print (left)

        store = "PINK"
        done= True

    elif user_input == "right"

        print (right)

        store = "urban"
        done= True
    else:
        print ("try again:")

if store
    user_input = input("Type 'steal' to go steal or 'pay' to pay")
    if user_input == "steal":
        print (steal)
        done= True
elif user_input == "pay":
        print (pay)
        done= True
    else:
        print ("try again")
done= False
while not done:
    user_input = input("Type 'matchmaking' to matchmake or 'job' to get a job)
    if user_input == "matchmaking":
        print (matchmaking)
        done= True
elif user_input == "walk away":
        print (walk away)
        done= True
    else:
        print ("try again")
done= False
print(done)
