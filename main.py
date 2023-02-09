import sys



def get_params():
    if len(sys.argv) < 2:
        print("Bitte als zweiten Parameter den Dateinamen der Fragen angeben.")
        exit()
    return(sys.argv[1])
    
def get_questions(filename):
    with open(filename) as f:
        questions = [line.rstrip() for line in f]
    return(questions)



def main():
    
    questions = get_questions(get_params())



if __name__ == "__main__":
    main()









