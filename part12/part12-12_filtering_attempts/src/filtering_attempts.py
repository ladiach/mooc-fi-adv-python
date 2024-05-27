class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts:list):
    return filter(lambda course:course.grade >=1, attempts)
	 
def attempts_with_grade(attempts:list, grade:int):
    return filter(lambda course:course.grade == grade, attempts)
    
def passed_students(attempts:list, course:str):
    passed = filter(lambda s:s.course_name == course and s.grade >0, attempts)
    passed_name = map(lambda s:s.student_name, passed)
    
    
    return sorted(passed_name)
    
if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 0)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)
    
    for attempt in passed_students([s1, s2, s3],"Introduction to Programming"):
        print(attempt)