class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age
        

    def add_track(self, tracks):
        if tracks not in self.tracks:
            self.tracks.append(tracks)
        #print(self.tracks)

    def get_score(self):
        print(self.score)
        return self.score

    def displayInfo(self):
        print("Name: ", self.name, ", Age: ", self.age, "years old, " 
     , "Enrolled in: ", self.tracks, ", Score: ", self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("FE")
Bob.get_score()
Bob.displayInfo()

