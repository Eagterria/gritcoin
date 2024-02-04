#!/usr/bin/env python3

# Gritcoin

# A simple reward system that is intentionally easy at first, but gradually gets MUCH harder over time,
# eventually requiring you to go outside your comfort zone more and more until you finally get some GRIT.

import json
import time

def main():
    try:
        # Try to load previous system
        with open('gritcoin.json', 'r') as f:
            stats = json.load(f)
    except FileNotFoundError:
        # Create a new gritcoin system. A JSON-compatible format is used in order to simplify things.
        stats = {}
        stats['coins'] = 0
        stats['accomplishments'] = []

        # Things people typically either enjoy doing or require in order to function.
        # Each item increases in price by 1 each time it is bought.
        # Feel free to add/remove items as needed in order to ensure maximum personalization.
        stats['sell'] = {}
        stats['sell']['Go to a website/link'] = 1
        stats['sell']['Refresh a website'] = 1
        stats['sell']['Close a website'] = 1
        stats['sell']['Play/replay one song/video'] = 1
        stats['sell']['Stop a song/video early'] = 1 # Pausing/seeking is fine.
        stats['sell']['Turn on a device'] = 1 # Turning on your main device that runs this program is free, for obvious reasons.
        stats['sell']['Turn off a device'] = 1
        stats['sell']['Save an unsaved file'] = 1
        stats['sell']['Open an app or program'] = 1 # Opening this specific program is free, for obvious reasons.
        stats['sell']['Close an app or program'] = 1
        stats['sell']['Take medicine'] = 1
        stats['sell']['Drink water'] = 1
        stats['sell']['Eat food'] = 1
        stats['sell']['Go to sleep'] = 1
        stats['sell']['Exit a building'] = 1
        stats['sell']['Have a conversation with someone'] = 1
        stats['sell']['Access $1 more of your bank money'] = 1 # Increase as needed if $1 is not enough.
        stats['sell']['Use the bathroom'] = 1

        # Things like doing overtime, finishing a project, exercise/dieting, getting a job, doing work in class, studying, self-care, meditation, etc.
        # This is a fixed rate so that as prices increase, spamming enter won't be enough anymore, forcing you to do easy tasks instead.
        # Soon easy tasks won't be enough, and then medium tasks won't be enough, and then hard tasks won't be enough.
        # You can probably stop using this program when hard or extreme tasks are no longer enough, as you may not want to overwork yourself too much.
        # Note: The higher these numbers are, the more gradual the difficulty increases over time, and thus the longer it will take for the user to get better.
        # Note: Feel free to change these numbers as needed in order to ensure maximum personalization.
        stats['buy'] = {}
        stats['buy']['Easy accomplishment'] = 10000
        stats['buy']['Medium accomplishment'] = 100000
        stats['buy']['Hard accomplishment'] = 1000000
        stats['buy']['Extreme accomplishment'] = 10000000

        with open('gritcoin.json', 'w') as f:
            json.dump(stats, f)

        print("Remember, this is a long-term commitment you have to make, no matter how hard it gets. The more you put into this, the more you'll get out of it.")

    while True:
        # Main interface
        print(f'Current balance: {stats["coins"]} gritcoin(s). Type "store" for things you can do/buy, or "accomplishments" for a list of your accomplishments. Otherwise press Enter to earn 1 gritcoin. ')

        try:
            line = input('> ')
        except KeyboardInterrupt:
            print()
            break
        except EOFError:
            print()
            break

        if line == 'store':
            # List prices by saying "store"

            print('Things you can afford (type the exact name of an item in the list in the command line in order to pay for it):')

            for key in stats['sell']:
                print(f'    "{key}": Pay {stats["sell"][key]} gritcoin(s).')

            print('Things you can do (type the exact name of an item in the list in the command line in order to get rewarded for it):')

            for key in stats['buy']:
                print(f'    "{key}": Get {stats["buy"][key]} gritcoin(s).')
        elif line == 'accomplishments':
            print('Accomplishments so far:')

            for accomplishment in stats['accomplishments']:
                print(accomplishment)
        elif len(line) > 0:
            # Make a payment or receive a reward.

            if line in stats['sell']:
                if stats['coins'] >= stats['sell'][line]:
                    stats['coins'] -= stats['sell'][line]
                    stats['sell'][line] += 1 # Price increases for every purchase
                else:
                    print('Insufficient funds.')
            elif line in stats['buy']:
                accomplishment = input('What did you accomplish? ')
                stats['accomplishments'].append(f'{time.ctime(time.time())}: {line}: "{accomplishment}"')
                stats['coins'] += stats['buy'][line]
            else:
                print('Unknown input.')
        else:
            # Gain gritcoins by pressing Enter. For hard mode, don't hold the enter key as this might make things a lot easier.
            stats['coins'] += 1

        # Save system to a file.
        with open('gritcoin.json', 'w') as f:
            json.dump(stats, f)

if __name__ == '__main__':
    main()
