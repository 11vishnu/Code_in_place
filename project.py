""" SGPA and CGPA Calculator based on my college grading system.
grades and their points,
    O  = 10
    A+ = 9
    A  = 8
    B+ = 7
    B  = 6
    RA/F = 0

"""

O  = 10
A1 = 9
A  = 8
B1 = 7
B  = 6
F  = 0
def main():
    semester=int(input("no. of semester: "))
    for i in range(semester):
        subjects = total_subjects(i)
        s_c = subject_credits(subjects)
        subject_list = get_subject_name(s_c)
        grades=get_grade(subject_list)
        tp=calculate_tp(s_c,grades)
        tc=calculate_tc(s_c)
        calculate_sgpa(tp,tc,i)
        all_sem_tp=a_s_tp(tp)
        all_sem_tc=a_s_tc(tc)
    calculate_cgpa(all_sem_tp,all_sem_tc)

def total_subjects(i):
    #Total subjects in a semester.
    s=int(input("Total subjects in sem "+str(int(i+1))+': '))
    return s

def subject_credits(s):
    #getting the subject name and credit from user.
    credits={}
    for i in range(s):
        subj = input("enter subject name: ")
        c =int(input("Enter credit: "))
        credits[subj]=c
    return credits

def get_subject_name(sc):
    #storing subject names in a list.
    s_l=list(sc.keys())
    return s_l

def get_grade(sub_list):
    #getting grades obtained by user for the subjects.
    grade={}
    print("Enter Grades")
    for i in sub_list:
        grade[i]=input(i + ": ")
    return grade

def calculate_tp(cred,grad):
    #calculating the points obtained for each subject and finding their total in a semester.
    tp=[]
    for i in grad.keys():
        if grad[i]== 'O':
            p=O*cred[i]
        elif grad[i]=='A+':
            p=A1*cred[i]
        elif grad[i]=='A':
            p=A*cred[i]
        elif grad[i]=='B+':
            p=B1*cred[i]
        elif grad[i]=='B':
            p=B*cred[i]
        elif grad[i] == 'RA' or 'F':
            p=F*cred[i]
        tp.append(p)
    total_points=sum(tp)
    return total_points

def calculate_tc(s_c):
    #calculating the sum of credit points allowted in a semester.
    c=[]
    for i in s_c.values():
        c.append(i)
    total_credits=sum(c)
    return total_credits

def calculate_sgpa(tp,tc,i):
    #sgpa can be calculated by dividing the tp(sum of points obtained in each subject in a semester)
    # and tc(sum of all subject credit points in a semester).
    sgpa=tp/tc
    print('sem',i+1,'sgpa:',sgpa)

def a_s_tp(tp):
    #calculating the sum of points obtained in all semester.
    atp=[]
    atp.append(tp)
    return sum(atp)

def a_s_tc(tc):
    #calculating the total credits in all semester.
    atc=[]
    atc.append(tc)
    return sum(atc)

def calculate_cgpa(all_gp,all_cp):
    #cgpa can be calculated by dividng sum of all grade points by sum of all credit points in all semester.
    cgpa=all_gp/all_cp
    print('CGPA:',cgpa)

if __name__ == '__main__':
    main()
