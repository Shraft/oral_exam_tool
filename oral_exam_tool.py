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
        question_string = question.split("[")[0].replace("?", "?\n#\t")

        return(question_string,script)

    def show_question(self, question, num_questions, show_menu):
        question_string, script = self.decrypt_question(question)
        os.system("clear")
        if script == "unknown":
            script_number = "-"
            folie_number = "-"
        else:
            script = script.replace("S", "")
            script = script.replace("[", "")
            script = script.replace("]", "")
            script_number = script.split("F")[0]
            folie_number = script.split("F")[1]
        print(f"##### Script: \033[0;34;49m{script_number}\033[0m, Folie: \033[0;34;49m{folie_number}\033[0m ####### Fragen übrig: [\033[0;33;49m{num_questions}\033[0m] #####\n#")
        print(f"#\t{question_string}\n#")

        if show_menu == True:
            self.show_hint()
            self.show_menu()
        else:
            self.show_hint()

    def show_hint(self):
        self.print_blue("m"," - Menü anzeigen / verstecken")

    def show_menu(self):
        self.print_green("y", " - Richtig beantwortet")
        self.print_yellow("n", " - Falsch beantwortet")
        self.print_red("e", " - Sitzung beenden")
        self.print_blue("r", " - Sitzung zurücksetzen")

    def print_red(self, text, optional=""):
        print(f"#\t [\033[0;31;49m{text}\033[0m]{optional}")
    def print_green(self, text, optional=""):
        print(f"#\t [\033[0;32;49m{text}\033[0m]{optional}")
    def print_yellow(self, text, optional=""):
        print(f"#\t [\033[0;33;49m{text}\033[0m]{optional}")
    def print_blue(self, text, optional=""):
        print(f"#\t [\033[0;34;49m{text}\033[0m]{optional}")

class QuestionGenerator:
    def __init__(self, question_file):
        self.question_file = question_file
        self.persistency_file = "." + question_file.split(".")[0] + ".pers" 
        self.question_list = []
        self.show_menu = False

    def get_questions(self):
        if os.path.isfile(self.question_file):
            with open(self.question_file) as f:
                questions = [line.rstrip() for line in f]
            random.shuffle(questions)
            self.question_list = questions
        else:
            print("bitte mit --file <datei.txt> angeben :)")
            exit()    

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
            dg.show_question(self.question_list[-1], int(len(self.question_list)-1), self.show_menu)

            user_input = input("#\n#\tEingabe: ")
            if user_input == "y":
                self.question_list.pop()
            elif user_input == "n":
                random.shuffle(self.question_list)
            elif user_input == "e":
                self.save_questions()
                exit()
            elif user_input == "r":
                self.get_questions()
            elif user_input == "m":
                self.show_menu = True if (self.show_menu == False) else False
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help='filename of questionfile', default='questions.txt')
    args = parser.parse_args()

    generator = QuestionGenerator(args.file)

    generator.run()
