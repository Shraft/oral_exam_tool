import sys
import argparse
import random
import re

class DisplayGenerator:
    def decrypt_question(self,question):
        script = re.findall(r'\[.*?\]', question)[0]
        points = re.findall(r'\(.*?\)', question)[0]
        question_string = question.split("[")[0].split("(")[0]

        return(question_string,script,points)
        

    def show_question(self, question):
        question_string, script, points = self.decrypt_question(question)

        print("#######################################")
        print(f"\n{question_string}\n")
        print(f"Hilfe im Skript: {script}")
        print(f"Punkte: {points}\n") if points != None else print("\n")
        print("#######################################")

class QuestionGenerator:
    def __init__(self, file):
        self.filename = file

    def get_questions(self):
        with open(self.filename) as f:
            questions = [line.rstrip() for line in f]
        random.shuffle(questions)
        return(questions)

    def run(self):
        question_list = self.get_questions()
        

        dg = DisplayGenerator()
        dg.show_question(question_list[0])

        # TODO: ask question
        # TODO: wait for input
        # TODO: delte question
        
        

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help='input file with questions', default='questions.txt')
    args = parser.parse_args()

    generator = QuestionGenerator(args.file)
    generator.run()









