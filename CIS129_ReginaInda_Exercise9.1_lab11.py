def main():
    with open('grades.txt', 'w') as file:
        while True:
            grade = input("Enter a grade or type 'finished' if finished: ")

            if grade.lower() == 'finished':
                break

            try:
                grade = float(grade) 
                file.write(f'{grade}\n') 
            except ValueError:
                print('Input is invalid. Enter a number. ')
        
if __name__ == '__main__':
    main()