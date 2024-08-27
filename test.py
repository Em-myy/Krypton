#A code that will give you your matric number so far you inputted the coeerct details
class student:
    def __init__(self, name, age, gpa, gender, faculty, department, year):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.gender = gender
        self.faculty = faculty
        self.department = department
        self.year = year

    '''
    def hello(self):
        if self.gpa >= 4.5:
            print("You are in first class")
        else:
            print("You are not in first class")
    '''
        
    def matric_no(self):
        if self.gpa > 5.0:
            print("Incorrect entry of gpa\n",self.name.capitalize(),"\n""Please enter a new gpa")
        else:
            if self.year == 2023:

                if self.faculty == "science":

                    if self.department == "computer science":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230501096")

                    elif self.department == "biochemistry":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230511086")

                    elif self.department == "botany":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230521076")

                    elif self.department == "chemistry":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230531066")

                    elif self.department == "mathematics":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230541056")

                    elif self.department == "fisheries":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230551046")

                    elif self.department == "microbiology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230561036")

                    elif self.department == "physics":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230571026")

                    elif self.department == "zoology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230581016")

                    else:
                        print(self.name.capitalize(),"\n" "You are not in faculty of science therefore you do not have a matric number")


                elif self.faculty == "law":
                    if self.department == "business law":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230301096")

                    elif self.department == "islamic law":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230311086")

                    elif self.department == "international law":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230321076")

                    elif self.department == "general law":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230331066")

                    elif self.department == "public and private law":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230341056")

                    else:
                        print(self.name.capitalize(),"\n" "You are not in the faculty of law therefore you do not have a matric number")


                elif self.faculty == "engineering":
                    if self.department == "aerospace engineering":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230101099")

                    elif self.department == "chemical and polymer engineering":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230111088")

                    elif self.department == "electronics and computer engineering":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230121078")

                    elif self.department == "mechanical engineering":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230131068")

                    elif self.department == "aeronautics and astronaut engineering":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 239141058")

                    else:
                        print(self.name.capitalize(),"\n" "You are not in the faculty of engineering therefore you do not have a matric number")
                
                elif self.faculty == "medicine":
                    if self.department == "anatomy":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230701092")
                    elif self.department == "chemical pathology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230711082")
                    elif self.department == "hematology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230721072")
                    elif self.department == "medical biochemistry":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230731062")
                    elif self.department == "medical microbiology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230741052")
                    elif self.department == "medicine and surgery":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230751042")
                    elif self.department == "pharamacology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230761032")
                    elif self.department == "physiology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230771022")
                    else:
                        print(self.name.capitalize(),"\n" "You are not in this faculty therefore you do not have a matric number")


                elif self.faculty == "management science":
                    if self.department == "accounting":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230901094")
                    elif self.department == "banking and finance":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230911084")
                    elif self.department == "business administration":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230921074")
                    elif self.department == "industrial relations":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230931064")
                    elif self.department == "insurance":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230941054")
                    elif self.department == "management technology":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230951044")
                    elif self.department == "marketing":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230961034")
                    elif self.department == "public administration":
                        print(self.name.capitalize(),"\n" "Your matric number is:\n 230971024")
                    else:
                        print(self.name.capitalize(),"\n" "You are not in this faculty therefore you do not have a matric number")


                else:
                    print("You are not enrolled in any faculty")

            else:
                print("You are not enrolled for this session")