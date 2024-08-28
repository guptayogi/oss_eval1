Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


students={}

def add_s(s_id, name, s_class, grades=None):
    if grades is None:
        grades = []
    students[s_id] = {
        'name': name,
        'class': s_class,
        'grades': grades
    }

    
def u_grades(s_id, n_grades):
    if s_id in students:
        students[s_id]['grades'] = n_grades
    else:
        print("Student not found ")

        
def c_a(s_id):
    if s_id in students:
        grades = students[s_id]['grades']
        if grades:
            return sum(grades) / len(grades)
        else:
            return 0
    else:
        print("Student not found.")
        return None


def g_top():
    c_a = {}
    
    for s_id, details in students.items():
        s_class = details['class']
        average = c_a(s_id)
        
        if s_class not in c_a:
            c_a[s_class] = []
        
        c_a[s_class].append((s_id, details['name'], average))
    
    report = {}

    
add_s("001" ,"al","math",[45,14])
u_grades("001",[44,21])

print("class average",c_a("001"))
class average 32.5
print("top students report",g_top())
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print("top students report",g_top())
  File "<pyshell#10>", line 6, in g_top
    average = c_a(s_id)
TypeError: 'dict' object is not callable

add_s("002","a","physics",[20,54])
u_grades("008",[43])
Student not found 
c_a("002")
37.0
