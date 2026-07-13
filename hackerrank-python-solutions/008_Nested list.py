#is where you prepare your tool
def sort_students(names_scores):
    scores = []
    for student in names_scores:
        scores.append(student[1])
        
    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1]
    
    names_second_lowest = []
    for student in names_scores:
        if student[1] == second_lowest:
            names_second_lowest.append(student[0])
    names_second_lowest = sorted(names_second_lowest)
    
    for name in names_second_lowest:
        print(name)
        
        
        
        
        
              
#execution
if __name__ == '__main__':
    names_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name,score])
         
    #use your tools!!!
    sort_students(names_scores)
         