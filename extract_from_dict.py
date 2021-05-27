import pandas as pd
import ast

def extract_dict(string):
    """Helper function to extract dict from string if string exists 
    else the function returns an empty dict (Thanks, Tweepy...)"""
    try:
        out=ast.literal_eval(string)
    except:
        out=dict()
    return out

def extract_from_entities(tweet,ent_key,tag_key):
    """Helper function to extract information from tweet_entities.
    tweet_entities is a dict-of-dicts containing all information on 
    twitter entities from a given tweet.
    ent_key: key used to access the dictionary of interest e.g. "hastags"
    tag_key: key used to access value of interest e.g. "text"
    Why, Tweepy? WHY?!"""
    try:
        out=[tag[tag_key] for tag in tweet[ent_key] if tweet[ent_key]!=ent_key]
    except:
        out=list()
    return out