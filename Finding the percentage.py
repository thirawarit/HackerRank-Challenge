if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    i = 0
    answer = 0
    for _ in range(len(student_marks[query_name])):
        answer = answer + student_marks[query_name][i]
        i += 1
    answer =answer / i
    print('{0:.2f}'.format(answer))
    ## average score use sum variable and i variable
