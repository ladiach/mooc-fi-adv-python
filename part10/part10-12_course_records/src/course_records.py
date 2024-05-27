# tee ratkaisusi tänne
class Course:
    
    def __init__(self, course:str, grade:int, crs:int):
        self.__name = course
        self.__grade = grade
        self.__credits = crs
    
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
    
    def add_credits(self, crs:int):
        self.__credits = crs
    
    def add_grade(self, grade:int):
        if self.grade() < grade:
            self.__grade = grade
    
    def name(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def get_credits(self):
        return self.__credits
    
    
class CourseRecords:
    
    def __init__(self):
        self.__records = {}
    
    
    def add_course(self, course_name:str, grade:int, crs:int):
        if not course_name in self.__records:
            course = Course(course_name, grade, crs)
            self.__records[course_name] = course
        else:
            self.__records[course_name].add_credits(crs)
            self.__records[course_name].add_grade(grade)
    
    def search(self, course:str):
        if not course in self.__records:
            return None
        
        return self.__records[course]
    
    
    def completed_courses(self):
        return len(self.__records)
    
    def total_credits(self):
        tot_crs=0
    
        for cr in self.__records.values():
            tot_crs +=cr.get_credits()
    
        return tot_crs
    
    def mean_course(self):
        tot_grade = 0
    
        for course in self.__records.values():
            tot_grade += course.grade()
    
        if self.completed_courses() > 0:
            mn = tot_grade/self.completed_courses()
        else:
            mn = 0
    
        return mn
    
    def grade_distribution(self):
        grades_distr = {5:"", 4:"", 3:"", 2:"", 1:""}
    
        for gd in self.__records.items():
            if (gd[1].grade()) in grades_distr:
                grades_distr[gd[1].grade()] += "x"
    
        return grades_distr
    
    
    
class CourseRecordsApplication:
    
    def __init__(self):
        self.__register = CourseRecords()
    
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        crs = int(input("credits: "))
    
        self.__register.add_course(course,grade, crs)
    
    def search(self):
        name = input("course: ")
        course = self.__register.search(name)
    
        if course == None:
            print("no entry for this course")
        else:
            print(course)
    
    def stats(self):
        print(f"{self.__register.completed_courses()} completed courses, a total of {self.__register.total_credits()} credits")
        print(f"mean {self.__register.mean_course():.1f}")
        print("grade distribution")
        distribution = self.__register.grade_distribution()
    
        for grade, dis in distribution.items():
            print(f"{grade}: {dis}")
    
    
    def execute(self):
        self.help()
    
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.stats()
            else:
                self.help()
    
test = CourseRecordsApplication()
test.execute()