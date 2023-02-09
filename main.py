import sys
import argparse
import random


class QuestionGenerator:
    def __init__(self, file):
        self.filename = file

    def get_questions(self):
        with open(self.filename) as f:
            questions = [line.rstrip() for line in f]
        return(questions)

    def create_random_order(self):
        question_list = self.get_questions()

        random_list = []
        while len(question_list) != 0:
            question_count = len(question_list)
            random_index = random.randint(0, question_count-1)
            random_list.append(question_list[random_index])
            del question_list[random_index]

        return(random_list)

    def run(self):
        question_list = self.create_random_order()
        print("Finished!")
        print(question_list)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help='input file with questions', default='questions.txt')
    args = parser.parse_args()

    generator = QuestionGenerator(args.file)
    generator.run()









