#Welcome to the HackerRank-Challenge wiki!

#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    
    
    records = []
    for _ in range(int(input("Number of students : "))):
        name = input("Name : ")
        score = float(input("Score : "))
        records.append((score,name)) 
    records.sort()
    
    def sec_low_grade(a) :
        global i
        global codename
        a_min = a[0][0]
        i = 0
        for _ in range(len(a)) :
            
            if a[i][0] > a_min :
                codename = a[i][0]
                i = 0
                break
            i += 1
        return(codename)
    
    numcode = sec_low_grade(records)

    print("the name of students have the second lowest grade in : ")
    
    for _ in range(len(records)) :
        
        if records[i][0] == numcode :
                
            name = records[i][1]
            print(name) #<<<use this for Answer.
                
        i += 1
            

    
    #print(records)
    #print()
