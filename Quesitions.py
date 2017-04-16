'''
This is a test script. We open file, read it content, a question, answers, correct answer and prompt user for input.
if a right answer is given- next question is loaded. If no right answer- script reads a line with explanation.
If end of a file reached- program prints a goodbye message and quits.


text file format:
[theme - only on the top of the list]
[question N]
[answer 1]
[answer 2]
[answer 3]
[answer 4]
[correct answer number]
[explanation]
[empty line]
[question N+1]
[answer 1]
...
so on
file ends without empty line after last line.
No empty line == file ended.


'''

#PATH = 'English_Advanced_grammar.txt'
from Get_files import get_files


def quiz(filename):
    with open(filename, 'r') as file:

        # read the first line and print quiz name
        quiz_theme = file.readline()
        print(quiz_theme, end='')

        # start first cycle
        nextline = '\n'
        correct_answers = 0
        question_number = 0
        while nextline == '\n':
            # increase question number by 1
            question_number += 1
            # read question theme
            # question_theme = file.readline()

            # read question
            question = file.readline()

            # create list with answers
            answers = list()
            for i in range(0, 4):
                answers.append(file.readline())

            # remember a correct answer
            correct_answer = int(file.readline())

            # read explanation
            explanation = file.readline()

            # read empty line
            # if this line == '\n', then a new question is coming
            # if line is empty or == '', then there are no new questions
            nextline = file.readline()

            # print questions
            print('Question ' + str(question_number) + ': ' + question, end='')
            # print(question, end='')
            for i in range(0, 4):
                print(i + 1, ': ' + answers[i], end='')

            # get answer
            user_answer = int(input())
            if user_answer == correct_answer:
                print('Correct!')
                correct_answers += 1
            else:
                print('Incorrect.', explanation)

            # print empty line
            print('\n', end='')

        print('You answered %d/%d questions correctly!' % (correct_answers, question_number))
        # input('Press any key to quit.')


def main():
    try:
        file = get_files()
        quiz(file)
    except FileNotFoundError:
        print('Cant find file to open. Check file name a try again.')


if __name__ == '__main__':
    main()
