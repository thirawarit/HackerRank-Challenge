if __name__ == '__main__':
    
    
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((score,name)) 
    records.sort()
    # "Just Test" >>>> c = range(len(records))
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
    
    for _ in range(len(records)) :
        
        if records[i][0] == numcode :
                
            name = records[i][1]
            print(name)
                
        i += 1
            

    
    #print(records)
    #print(list(name))
