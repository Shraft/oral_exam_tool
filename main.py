import sys
import argparse
import random


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
        print("Finished!")
        print(question_list)
        

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help='input file with questions', default='questions.txt')
    args = parser.parse_args()

    generator = QuestionGenerator(args.file)
    generator.run()









