from flask import render_template, Blueprint
import mysql.connector
import random
import sys

game = Blueprint('game', __name__)
@game.route('/')
def index():
    words = fetch_words()
    definition, options, correct_word = create_quiz(words)
    definition1= clean_definitions(definition)
    return render_template('index.html', question=definition1, a=options[0],b=options[1],c=options[2],d=options[3], e=options[4], correct = correct_word)


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="Vocabulary"
    )

def fetch_words():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT word_id, word, definition FROM Vocab")
    words = cursor.fetchall()
    cursor.close()
    connection.close()
    return words

def create_quiz(words):
    options = []
    random.shuffle(words)
    for word_entry in words:
        correct_word = word_entry['word']
        definition = word_entry['definition']
        print(definition)
        incorrect_words = random.sample([w['word'] for w in words if w['word'] != correct_word], 4)
        options = incorrect_words + [correct_word]
        random.shuffle(options)
        return definition, options, correct_word
    
def clean_definitions(definition):
    return definition.replace('�', '<br>-')

        

