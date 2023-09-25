from keep_alive import keep_alive
import os
import discord
import random
import math # for prime number

def is_prime(n):
    # Function to check if a number is prime (same as above)
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# new lines
pucci_lines = [
    "Do you believe in gravity?", #1
    "Made in Heaven!",
    "Time accelerates!",
    "Do you understand what this means?",
    "Heaven... I shall bring it about.",
    "The world's happiness... is within my grasp!",
    "All will become one.",
    "This world will end and a new one will be born!",
    "Gravity is not the culprit that holds people down; it is the guilt in their hearts that weighs them down.",
    "Life is nothing more than a series of fleeting moments. Only when you reach the end and look back can you see the full story.",
    "To erase one's past is akin to erasing one's own existence. Without the past, there is no foundation for the future.",
    "The desire for a perfect world is not madness. It is a yearning for true salvation and understanding.",
    "The culmination of every action leads to fate. It is a chain reaction, intricately woven, leading us all to our destinies.",
    "In this ever-changing world, the only constant is the pursuit of truth and the search for the ultimate meaning of existence.",
    "In the grand tapestry of time, every thread contributes to the final masterpiece. Embrace your role, no matter how insignificant it may seem.",
   "The path to righteousness is paved with the intention to create a world of absolute justice and unity.",
  "Only by experiencing the depths of despair can one truly appreciate the heights of euphoria.",
  "The pursuit of heaven is not an act of selfishness, but a selfless endeavor to bring harmony to the entire universe.",
  "Time flows, not to bring moments of happiness you want, but to create your destiny.",
  "The meaning of fate is not to wait for someone, but to do something on your own.",
  "Embrace your desires, for they are the driving force that shapes your existence.",
  "The concept of righteousness differs from person to person. It is subjective, yet powerful enough to define our actions.",
  "The threads of fate are woven intricately, connecting every living being in a grand symphony of existence.",
  "Stand users possess the ability to change the world, and I shall use it to bring about my vision of heaven.",
  "In the cycle of rebirth, we are given a chance to correct our past mistakes and fulfill our true purpose.",
  "Sacrifices are necessary for the realization of one's ideals. I bear the burden of destiny for the greater good.",
  "Heaven is not a mere destination; it is a state of absolute understanding and harmony with the universe.",
  "The pursuit of an eternal paradise is the culmination of human evolution and enlightenment.", 
  "JOLYNE CUJOH!!!!!", #29
]
# end of new lines 1

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message contains the command "!pucci"
    if message.content.startswith('!pucci'):
        # Split the message content into words
        words = message.content.split()

        # Check if there is an additional word after "!pucci"
        if len(words) > 1:
            command = words[1]

            if command == 'prime':
                # Generate a random prime number between 1 and 1000
                random_prime = random.choice([n for n in range(1, 1000) if is_prime(n)])
                await message.channel.send(f"Calm down.. count prime numbers to keep your composure, prime numbers are solitary numbers that can only be divided by 1 and itself, they give me strength: {random_prime}")
            else:
                response = random.choice(pucci_lines)
                await message.channel.send(response)
        else:
            # If no additional word, respond with a random Pucci line
            response = random.choice(pucci_lines)
            await message.channel.send(response)

keep_alive()

my_secret = os.environ['DISCORD_BOT_SECRET']
client.run(my_secret)
