import sys
import argparse


class QuestionGenerator:
    def __init__(self, filename):
        self.filename = filename

    def get_questions(self):
        with open(self.filename) as f:
            questions = [line.rstrip() for line in f]
        return(questions)
    
    def run(self):
        self.get_questions()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help='input file with questions', default='questions.txt')
    args = parser.parse_args()

    generator = QuestionGenerator(args.file)
    generator.run()









