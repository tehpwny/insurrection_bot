"""
# TODO
"""
import os
import sys
from time import sleep
from subprocess import Popen
from random import choice, randrange

PRETTY = '--pretty' in sys.argv

class Tiqqun:
    words = {
        "things_we_like": [
            "rupture", "insurrection", "crisis", "social war",
            "zones of indistinction which need no justification",
            "indifference", "direct action", "sabotage", "art",
            "self concisousness", "permanent revolution"
        ],
        "things_we_dont_like": [
            "activism", "representation", "humanism", "landlords",
            "totality", "passivity", "banality", "leftists",
            "fossilization of our desires", "vote", "power",
            "mobilization", "impotentiality", "individualism",
            "normalization", "absence", "patriarcat", "governements",
            "economy", "consumption", "marchandise", "music", "domination",
            "work", "productivity", "accumulation", "privatisation", "privation",
            "proletarian revolution", "leninism", "social democracy", "democracy",
            "classes war", "classes", "the state", "jails", "prisons",
            "state justice",
            "marxism"
        ],
        "people_we_dont_like": [
            "the milieu", "liberalism",
            "the bureaucrats of revolt",
            "anarcho-liberalism", "politicians",
            "bourgeoisie", "statists communists",
            "police"
        ],
        "things_we_do": [
            "desire", "riot", "occupy everything", "become ungovernable"
        ],
        "our_things": [
            "communes", "multiplicities", "encounters", "zads", "squats",
            "becomings", "zones of offensive opacity", "desiring-bodies",
        ],
        "symbolic_things": [
            "burning dumpster", "smashed window", "dead CEO",
            "moment of friendship", "car set aflame", "dead cop",
            "barricaded hallway", "barricades", "burnt cop", "smashed bank"
        ],
        "things_we_do_to_things": [
            "destroy", "shatter", "negate", "reject", "burn", "crush",
            "void", "cancel", ""
        ],
        "things_we_dont_do": [
            "organize", "negotiate",
            "make demands", "be productive"
        ],
        "how_we_do_things": [
            "in secret", "without illusions", "for once and for all",
            "absolutely"
        ],
        "describing_good_things": [
            "singular", "immanent", "inoperative", "radical"
        ],
        "describing_bad_things": [
            "homogenous", "pathetic", "compulsive", "alienated"
        ],
        "fancy_words": [
            "logic", "structure", "being", "temporality", "teleology"
        ],
        "happiness": ["joy", "ecstasy"],
        "sadness": ["misery", "catastrophe", "delusion"],
        "really": [
            "by any means necessary", "with every weapon at our disposal",
            "without looking back", "at all costs"
        ],
        "making_things": [
            "articulation", "construction", "elaboration", "setting forth",
            "realization"
        ],
        "plans": ["plan", "project", "concept"],
        "antiplans": [
            "a state of exception", "a line of flight",
            "an event"
        ],
        "events": ["orgies", "festivals", "conspiracies"],
        "fun_stuff": ["destruction", "negation"],
        "get_along": ["dialogue", "criticism", "sympathy"],
        "go_away": ["scorn", "contempt", "derision"],
        "dont_do": ["refuse", "neglect", "fail"],
        "preposition": ["on", "towards"],
        "alienation": ["alienation", "isolation", "detachment", "estrangement",
                       "distance", "separation", "severance", "parting",
                       "division", "divorce"],
        "unification": ["unification", "union", "amalgamation", "junction", "conjunction"]

    }

    def get_word(self, key):
        return self.words.get(key)

    def get_words(self, keys):
        for key in keys:
            yield self.words.get(key)

    def get_rand_word(self, key):
        return choice(self.words.get(key))

    def get_rand_words(self, *keys):
        already_said = []
        chosen = None
        for key in keys:
            words = self.words.get(key)
            if words is not None:
                while chosen in already_said or chosen is None:
                    chosen = choice(words)
                already_said.append(chosen)
                yield chosen

    def rant(self):
        rants = [
            self.recognize,
            self.do_something,
            self.in_the,
            self.break_things,
            self.this_call,
            self.whats_needed,
            self.every_what,
            self.joke,
            self.necessary,
            self.symbols,
            self.spectale
        ]
        rant = choice(rants)
        return str(rant()).replace("\n", " ")


    def recognize(self):
        return """Confronted with those who {} to recognize themselves in our {} of {}, we offer neither {} nor {} but only our {}.""".format(
            *self.get_rand_words("dont_do", "events", "fun_stuff", "get_along",
                                 "get_along", "go_away")
        )


    def do_something(self):
        return """Our need to {} is less the {} of a {} than the {} of {}.
        """.format(*self.get_rand_words(
            "things_we_do",
            "making_things",
            "plans",
            "making_things",
            "antiplans"
        ))


    def in_the(self):
        return """In the {} of {}, we {} those who would have us give up the {} {} of {} for the {} of {}.""".format(*self.get_rand_words(
            "making_things", "our_things", "things_we_do_to_things",
            "describing_good_things", "happiness", "things_we_like",
            "sadness", "things_we_dont_like"
        ))


    def title(self):
        return """Leaving {} behind: Notes {} {}
        """.format(*self.get_rand_words(
            "things_we_dont_like", "preposition", "things_we_like"
        ))


    def break_things(self):
        return """We must {} all {} {}.
        """.format(*self.get_rand_words(
            "things_we_do_to_things",
            "things_we_dont_like",
            "how_we_do_things"))


    def this_call(self):
        return """This is a call to {}, not an insistence on {}.
        """.format(*self.get_rand_words("things_we_like", "things_we_dont_like"))


    def whats_needed(self):
        return """What's needed is not {}, and even far less {}, but a putting-into-practice of {} {}, a rejection in all forms of the {} of {}.
        """.format(*self.get_rand_words("things_we_dont_like",
                                        "things_we_dont_like",
                                        "describing_good_things",
                                        "things_we_like",
                                        "fancy_words",
                                        "things_we_dont_like"))


    def every_what(self):
        return """Every {} is a refusal to {}, a blow against the {} of {}, a recognition of the {} {} inherent in the articulation of {}.
        """.format(*self.get_rand_words(
            "symbolic_things",
            "things_we_dont_do",
            "fancy_words",
            "people_we_dont_like",
            "describing_good_things",
            "fancy_words",
            "our_things"
        ))


    def joke(self):
        return """The {} {} proposed to us is like a bad joke, and instead of laughter we respond with {}.
        """.format(*self.get_rand_words(
            "describing_bad_things",
            "things_we_dont_like",
            "things_we_like"
        ))


    def necessary(self):
        return """It is necessary to commence {} to dream of new ways to {}, but to make manifest the subterranean {} in the heart of each {}.
        """.format(*self.get_rand_words(
            "how_we_do_things",
            "things_we_dont_do",
            "our_things",
            "symbolic_things"
        ))


    def symbols(self):
        return """To those who deride the {} {} in a {} or a {}, we propose nothing less than to {} their {} {}, {}.
        """.format(*self.get_rand_words(
            "describing_good_things",
            "happiness",
            "symbolic_things",
            "symbolic_things",
            "things_we_do_to_things",
            "describing_bad_things",
            "things_we_dont_like",
            "really"
        ))

    def spectale(self):
        return """We must {0} the {1} which is no more than the {3} spectacular reversal {4} of {2}
        """.format(*self.get_rand_words(
            "things_we_do_to_things",
            "alienation",
            "alienation",
            "describing_bad_things",
            "unification",
        ))


appelist = Tiqqun()

if '--fortune' in sys.argv:
    if PRETTY:
        print("""
        \n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n{}\n
        """.format(appelist.rant()))
        print('\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n')
    else:
        print(appelist.rant())
    sys.exit()

if '--trap' in sys.argv:
    beat = Popen(["mplayer", "-loop", "0", "-really-quiet", "./trap.m4a"])


print('\n\nScolie {} \n\t - {} \n'.format(randrange(1, 1312), appelist.title()))

while True:
    sleep(4)  # wait for it.
    if PRETTY:
        print('\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n\n')
    message = appelist.rant()
    print(message + '\n')
    cmd = 'espeak -p 45 -s 172 "{}"'.format(message)
    sleep(choice((0.75, 1)))
    os.system(cmd)
