# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the setly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import json
import os
import random
import string
import time
import requests
from typing import Dict, List


def give_me_five() -> int:
    """Returns the integer five."""
    give_me_five = 5
    return give_me_five


def password_please() -> str:
    """Returns a string, 8 or more characters long, contains at
    least one upper case letter and one lowercase letter.
    TIP: don't put in a real password!"""
    password_please = 'cacheHC0u7'
    return password_please


def list_please() -> list:
    """Returns a list, you can put anything in the list."""
    list_please = ['hello', 'coffe', 'puppy']
    return list_please


def int_list_please() -> list:
    """Returns a list of integers, any integers are fine."""
    list_please = [1, 5, 9, 7]
    return list_please


def string_list_please() -> list:
    """Returns a list of strings, any string are fine."""
    string_list_please = ['ground', 'hog', 'day']
    return string_list_please


def dictionary_please() -> dict:
    """Returns a dictionary, anything you like."""
    dictionary_please = {'hello':1, 'coffee':5, 'puppy':9,}
    return dictionary_please


def is_it_5(some_number) -> bool:
    """Returns True if the argument passed is 5, otherwise returns False."""
    
    well_is_it = some_number
    
    return well_is_it == 5


def take_five(some_number) -> int:
    """Subtracts 5 from some_number."""
    take_five = some_number - 5
    return take_five


def greet(name="Towering Timmy") -> str:
    """Return a greeting.
    return a string of "Well hello, " and the name argument.
    E.g. if given as "Towering Timmy" it should
         return "Well hello, Towering Timmy"
    """
    greet = ("Well hello, " + name)
    return greet



def one_counter(input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of 1s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 2
    """
    count = 0
    for num in input_list:
        if num == 1:
            count += 1
    
    return count


def n_counter(search_for_this, input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    count = 0
    for item in input_list:
        if item == search_for_this:
            count += 1
    
    return count


def fizz_buzz() -> List:
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."

    from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special,
    and a string if it is. E.g.
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14,
         'FizzBuzz', 16, 17, ...]
    """
    fizz_buzz_list = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            fizz_buzz_list.append('FizzBuzz')
        elif num % 3 == 0:
            fizz_buzz_list.append('Fizz')
        elif num % 5 == 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(num)

    return fizz_buzz_list


def set_it_on_fire(input_string="very naughty boy") -> str:
    """Interleave the input_string with the 🔥 emoji.

    Given any string, interleave it with 🔥. Also make it be upper case.
    e.g. "very naughty boy" should return the string
    "🔥V🔥E🔥R🔥Y🔥 🔥N🔥A🔥U🔥G🔥H🔥T🔥Y🔥 🔥B🔥O🔥Y🔥"
    TIP: strings are pretty much lists of chars.
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a 🔥 on both ends of the string.
    """
    input_string = input_string.upper()
    fire_emoji = "🔥"
    set_it_on_fire = fire_emoji + fire_emoji.join(input_string) + fire_emoji

    return set_it_on_fire


def pet_filter(letter="a") -> List:
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
        "dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken", 
        "guinea pig", "donkey", "duck", "water buffalo", "python", "scorpion",
        "western honey bee", "dromedary camel", "horse", "silkmoth", 
        "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca", 
        "guineafowl", "ferret", "muscovy duck", "barbary dove", "cichlid",
        "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi", 
        "canary", "society finch", "fancy mouse", "siamese fighting fish", 
        "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"
    ]
    # fmt: on
    filtered = [pet for pet in pets if letter.lower() in pet.lower()]

    return filtered


def best_letter_for_pets() -> str:
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    TIP: use the function you just wrote to help you here!
    TIP: you've seen this before in the pokedex.
    """
    import string

    the_alphabet = string.ascii_lowercase
    most_popular_letter = ""
    max_count = 0

    for letter in the_alphabet:
        pet_list = pet_filter(letter)
        if len(pet_list) > max_count:
            max_count = len(pet_list)
            most_popular_letter = letter

    return most_popular_letter


def make_filler_text_dictionary() -> Dict:
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4
    If we set wordlength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    {
        3: ['Seb', 'the', 'yob', "boy"],
        4: ['aaaa', 'bbbb', 'cccc', "ddd"],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc', 'ddddddd']
    }
    Use the API to get the 4 words.

    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 4 words for each)
    TIP: you'll need the requests library
    """

    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="
    wd = {}
    for length in range(3, 8):
        words_list = []
        for _ in range(4):
            response = requests.get(url + str(length))
            if response.status_code == 200:
                word = response.text.strip()
                words_list.append(word)
        wd[length] = words_list
    return wd


def random_filler_text(number_of_words=200) -> str:
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library,
        e.g. random.randint(low, high)
    """

    my_dict = make_filler_text_dictionary()
    word_lengths = list(my_dict.keys())

    words = []
    for _ in range(number_of_words):
        word_length = random.choice(word_lengths)
        word_list = my_dict[word_length]
        random_word = random.choice(word_list)
        words.append(random_word)
    return " ".join(words)

def fast_filler(number_of_words=200) -> str:
    """Makes filler text, but really fast.

    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_cache.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the
    dictionary into and out of the file. Be careful when you read it back in,
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """
    
    filename = "dict_cache.json"

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            cached_dict = json.load(f)
    else:
        cached_dict = make_filler_text_dictionary()
        with open(filename, 'w') as f:
            json.dump(cached_dict, f)

    words = []
    for _ in range(number_of_words):
        word_length = random.choice(list(cached_dict.keys()))
        word_list = cached_dict[word_length]
        random_word = random.choice(word_list)
        words.append(random_word)

    if words:
        words[0] = words[0].capitalize()

    return " ".join(words)

if __name__ == "__main__":
    print("give_me_five", give_me_five(), type(give_me_five()))
    print(
        "strong_password_please",
        password_please(),
        type(password_please()) == str,
    )
    print("int_list_please", int_list_please(), type(int_list_please()) == list)
    print(
        "string_list_please", string_list_please(), type(string_list_please()) == list
    )
    print("dictionary_please", type(dictionary_please()) == dict)
    print("is_it_5", is_it_5(5))
    print("is_it_5", is_it_5(6))
    print("take_five", take_five(5))
    print("take_five", take_five(3))
    print("greet:", greet())
    print("three_counter:", one_counter())
    print("n_counter:", n_counter(7))
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", set_it_on_fire())
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(4):
        print(i, fast_filler(number_of_words=20), "\n")
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )