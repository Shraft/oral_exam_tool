import sys
import argparse
import random
import re

class DisplayGenerator:
    def decrypt_question(self,question):
        try:
            script = re.findall(r'\[.*?\]', question)[0]
        except:
            print("Scriptangabe fehlt")
            script = "unknown"
        try:
            points = re.findall(r'\(.*?\)', question)[0]
        except:
            print("Punkteangabe fehlt")
            points = 0
        question_string = question.split("[")[0].split("(")[0]

        return(question_string,script,points)
        

    def show_question(self, question):
        question_string, script, points = self.decrypt_question(question)

        print("\n#################################################################")
        print(f"\n\t{question_string}\n")
        print(f"\tHilfe im Skript: {script}")
        print(f"\tPunkte: {points}\n")

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

        while len(question_list) != 0:    
            dg.show_question(question_list[-1])

            user_input = input("\n\tNext Question? (y/n): ")
            if user_input == "y":
                question_list.pop()
            elif user_input == "n":
                exit()
        
        # TODO: delte question
        
        

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help='input file with questions', default='questions.txt')
    args = parser.parse_args()

    generator = QuestionGenerator(args.file)
    generator.run()









