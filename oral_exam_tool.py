import argparse
import random
import re
import os

class DisplayGenerator:
    def decrypt_question(self,question):
        try:
            script = re.findall(r'\[.*?\]', question)[0]
        except:
            script = "unknown"
        question_string = question.split("[")[0].replace("?", "?\n#\t")

        return(question_string,script)

    def show_question(self, question, num_questions, show_menu):
        question_string, script = self.decrypt_question(question)
        os.system("clear")
        if script == "unknown":
            script_number, folie_number = "-", "-"
        else:
            script = script.replace("S", "").replace("[", "").replace("]", "")
            script_number, folie_number = script.split("F")[0], script.split("F")[1]
        print(f"##### Script: \033[0;34;49m{script_number}\033[0m, Folie: \033[0;34;49m{folie_number}\033[0m ####### Fragen übrig: [\033[0;33;49m{num_questions}\033[0m] #####\n#")
        print(f"#\t{question_string}\n#")

        self.show_hint()
        if show_menu == True:
            self.show_menu()

    def show_hint(self):
        print(f"#\t [\033[0;34;49mm\033[0m] - Menü anzeigen / verstecken") # blau

    def show_menu(self):
        print(f"#\t [\033[0;32;49my\033[0m] - Richtig beantwortet") # green
        print(f"#\t [\033[0;33;49mn\033[0m] - Falsch beantwortet")  # rot
        print(f"#\t [\033[0;31;49me\033[0m] - Sitzung beenden")     # gelb
        print(f"#\t [\033[0;35;49mr\033[0m] - Sitzung zurücksetzen")# grau


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
            print(f"Datei {self.question_file} konnte im aktuellen Verzeichnis nicht gefunden werden")
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

            user_input = input("#\n#\tEingabe: \033[0;34;49m")
            print("\033[0m]")
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