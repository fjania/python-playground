import re
import string
from itertools import combinations

states_and_neighbors = {
    "AL": ("TN" ,"GA" ,"FL" ,"MS"),
    "AR": ("MO" ,"TN" ,"MS" ,"LA" ,"TX" ,"OK"),
    "AZ": ("UT" ,"CO" ,"NM" ,"CA" ,"NV"),
    "CA": ("OR" ,"NV" ,"AZ"),
    "CO": ("WY" ,"NE" ,"KS" ,"OK" ,"NM" ,"AZ" ,"UT"),
    "CT": ("MA" ,"RI" ,"NY"),
    "DC": ("MD" ,"VA"),
    "DE": ("PA" ,"NJ" ,"MD"),
    "FL": ("GA" ,"AL"),
    "GA": ("NC" ,"SC" ,"FL" ,"AL" ,"TN"),
    "IA": ("MN" ,"WI" ,"IL" ,"MO" ,"NE" ,"SD"),
    "ID": ("MT" ,"WY" ,"UT" ,"NV" ,"OR" ,"WA"),
    "IL": ("WI" ,"IN" ,"KY" ,"MO" ,"IA"),
    "IN": ("MI" ,"OH" ,"KY" ,"IL"),
    "KS": ("NE" ,"MO" ,"OK" ,"CO"),
    "KY": ("OH" ,"WV" ,"VA" ,"TN" ,"MO" ,"IL" ,"IN"),
    "LA": ("AR" ,"MS" ,"TX"),
    "MA": ("NH" ,"RI" ,"CT" ,"NY" ,"VT"),
    "MD": ("PA" ,"DE" ,"DC" ,"VA" ,"WV"),
    "ME": ("NH",),
    "MI": ("OH" ,"IN" ,"WI"),
    "MN": ("WI" ,"IA" ,"SD" ,"ND"),
    "MO": ("IA" ,"IL" ,"KY" ,"TN" ,"AR" ,"OK" ,"KS" ,"NE"),
    "MS": ("TN" ,"AL" ,"LA" ,"AR"),
    "MT": ("ND" ,"SD" ,"WY" ,"ID"),
    "NC": ("VA" ,"SC" ,"GA" ,"TN"),
    "ND": ("MN" ,"SD" ,"MT"),
    "NE": ("SD" ,"IA" ,"MO" ,"KS" ,"CO" ,"WY"),
    "NH": ("ME" ,"MA" ,"VT"),
    "NJ": ("NY" ,"DE" ,"PA"),
    "NM": ("CO" ,"OK" ,"TX" ,"AZ" ,"UT"),
    "NV": ("ID" ,"UT" ,"AZ" ,"CA" ,"OR"),
    "NY": ("VT" ,"MA" ,"CT" ,"NJ" ,"PA"),
    "OH": ("PA" ,"WV" ,"KY" ,"IN" ,"MI"),
    "OK": ("KS" ,"MO" ,"AR" ,"TX" ,"NM" ,"CO"),
    "OR": ("WA" ,"ID" ,"NV" ,"CA"),
    "PA": ("NY" ,"NJ" ,"DE" ,"MD" ,"WV" ,"OH"),
    "RI": ("MA" ,"CT"),
    "SC": ("NC" ,"GA"),
    "SD": ("ND" ,"MN" ,"IA" ,"NE" ,"WY" ,"MT"),
    "TN": ("KY" ,"VA" ,"NC" ,"GA" ,"AL" ,"MS" ,"AR" ,"MO"),
    "TX": ("OK" ,"AR" ,"LA" ,"NM"),
    "UT": ("ID" ,"WY" ,"CO" ,"NM" ,"AZ" ,"NV"),
    "VA": ("MD" ,"DC" ,"NC" ,"TN" ,"KY" ,"WV"),
    "VT": ("NH" ,"MA" ,"NY"),
    "WA": ("ID" ,"OR"),
    "WI": ("MI" ,"IL" ,"IA" ,"MN"),
    "WV": ("PA" ,"MD" ,"VA" ,"KY" ,"OH"),
    "WY": ("MT" ,"SD" ,"NE" ,"CO" ,"UT" ,"ID")
}

def travel_to_next_state(trip, states_per_trip, all_possible_trips):
    if len(trip) == states_per_trip:
        key = ''.join(sorted(''.join(trip))).lower()
        if all_possible_trips.get(key) == None:
            all_possible_trips[key] = trip

    else:
        for s in states_and_neighbors[trip[-1]]:
            if not s in trip:
                travel_to_next_state(trip[:] + [s], states_per_trip, all_possible_trips)


def compute_all_possible_trips(all_possible_trips, states_to_visit):
    for state in states_and_neighbors.keys():
        travel_to_next_state([state], states_to_visit, all_possible_trips)


def compute_all_possible_words(all_possible_words, states_to_visit):
    word_pattern = "[a-z]{{{}}}".format(states_to_visit * 2)
    word_regex = re.compile(word_pattern)

    with open('wordlist') as fp:
        for line in fp.readlines():
            word = line.strip()
            if word_regex.fullmatch(word):
                key = ''.join(sorted(word))
                if all_possible_words.get(key) == None:
                    all_possible_words[key] = [word]
                else:
                    all_possible_words[key].append(word)


def find_all_legal_words(states_to_visit):
    all_possible_trips = {}
    all_possible_words = {}
    number_of_possible_words = 0

    compute_all_possible_trips(all_possible_trips, states_to_visit)
    compute_all_possible_words(all_possible_words, states_to_visit)
    number_of_possible_words = sum([len(x) for x in all_possible_words.values()])

    print()
    print("Number of possible trips covering {} states: {}".format(
            states_to_visit,
            len(all_possible_trips)
        )
    )

    print("Number of words with {}*2 = {} letters : {}".format(
            states_to_visit,
            states_to_visit * 2,
            number_of_possible_words
        )
    )

    trip_keys = set(all_possible_trips.keys())
    word_keys = set(all_possible_words.keys())

    generatable_keys = trip_keys.intersection(word_keys)

    for key in generatable_keys:
        print("Travel {} to spell: {}".format(
            "->".join(all_possible_trips[key]),
            " or ".join(all_possible_words[key])
            )
        )

for x in range(3,11):
    find_all_legal_words(x)
