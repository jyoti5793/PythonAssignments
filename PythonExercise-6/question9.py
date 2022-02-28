subject_marks = {"Mathematics" : 80, "Physics" :58, "Chemistry" :62, "English" :72, "Biology" : 50}

def find_marks_greater_than_60(name,subject_marks):
    subjects=[]
    for subject,marks in subject_marks.items():
        if marks > 60 :
            subjects.append(subject)
    print("Name:",name,"-subjects", l)

find_marks_greater_than_60("Brandon",subject_marks)
