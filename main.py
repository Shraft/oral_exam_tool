import sys
import argparse
import random
import re
import os

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
        

    def show_question(self, question, num_questions):
        question_string, script, points = self.decrypt_question(question)

        print("\n#################################################################")
        print(f"\n\t{question_string}\n")
        print(f"\tHilfe im Skript: {script}")
        print(f"\tPunkte: {points}")
        print(f"\tQuestions remaining: {num_questions}\n")

class QuestionGenerator:
    def __init__(self, question_file, persistency_file):
        self.question_file = question_file
        self.persistency_file = persistency_file
        self.question_list = []

    def get_questions(self):
        with open(self.question_file) as f:
            questions = [line.rstrip() for line in f]
        random.shuffle(questions)
        self.question_list = questions

    def load_questions(self):
        if os.path.isfile(self.persistency_file):
            with open(self.persistency_file) as f:
                self.question_list = [line.rstrip() for line in f]

    def save_questions(self):
        file = open(self.persistency_file, 'w')
        for question in self.question_list:
            file.write(question +"\n")
        file.close()
    

    def run(self):
        self.load_questions()
        dg = DisplayGenerator()

        while True:
            if(len(self.question_list) == 0):
                "Questionlist empty! generated new one..."
                self.get_questions()
            dg.show_question(self.question_list[-1], len(self.question_list))

            user_input = input("\n\tQuestion succesfull (y/n)\n\tExit(e)\n\tGenerate new List(l): ")
            if user_input == "y":
                self.question_list.pop()
            elif user_input == "n":
                random.shuffle(self.question_list)
            elif user_input == "e":
                self.save_questions()
                exit()
            elif user_input == "l":
                self.get_questions()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--question-file", help='filename of questionfile', default='questions.txt')
    parser.add_argument("--persistency-file", help='filename of storaged questions', default='persistency.txt')
    args = parser.parse_args()

    generator = QuestionGenerator(args.question_file, args.persistency_file)

    generator.run()