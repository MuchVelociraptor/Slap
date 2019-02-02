from __future__ import print_function

from random import choice
import wikipedia

import hexchat

__module_name__ = 'UltraSlap 200m'
__module_version__ = 'vWOW.0'
__module_description__ = 'Slaps specified users with random fish'
__author__ = 'Douglas Brunal (AKA) Frankity made Ultra by RaptorJesus'

slaps = [
    'slaps {} around a bit with a {}.',
    'gives {} a clout round to the head with a {}.',
    'slaps {} with a large smelly {}.',
    'breaks out the slapping {1} and looks sternly at {0}.',
    'slaps {}\'s bottom with a {} and grins cheekily.',
    'slaps {} a few times with a {}.',
    'slaps {} with a {} and starts getting carried away.',
    'would slap {} with a {}, but is not being violent today.',
    'gives {} a hearty slap with a {}.',
    'finds the closest large {1} and gives {0} a slap with it.',
    'likes slapping people and randomly picks {} to slap with a {}.',
    'dusts off a kitchen {1} and slaps {0} with it.'
]
def slap_cb(word, word_eol, userdata):
    if len(word) > 1:
        nick = word[1]
        p = wikipedia.page('List_of_aquarium_fish_by_scientific_name')
        fishpix = choice(p.links)
        hexchat.command('me ' + choice(slaps).format(nick,fishpix) + ' https://en.wikipedia.org/wiki/' + fishpix.replace(" ", "_"))
    else:
        hexchat.command('help slap')
    return hexchat.EAT_ALL


def unload_cb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_command('slap', slap_cb, help='SLAP <nick>')
hexchat.hook_unload(unload_cb)
print(__module_name__, 'version', __module_version__, 'loaded.')
