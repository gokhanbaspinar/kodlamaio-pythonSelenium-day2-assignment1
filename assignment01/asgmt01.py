# ÖDEV TANIMI:

# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

studentList = ["John Doe ", "Jane Doe", "Adam Smith"]
 
def addStudent():
    studentList.append(input("Enter the name and last name of the student to add: "))
    print("***Student added to the list***")
    print(studentList)

def removeStudent():
    studentName = input("Enter the name and last name of the student to remove: ")
    studentList.remove(f"{studentName}")
    print("***Student removed from the list***")
    print(studentList)

def printStudents():
    for i in range(len(studentList)):
        print(studentList[i])

def addMultipleStudent():
    while True:
     student = input("Enter the name and last name of the student to add, if you do not want to add more type 'finish': ")
     if student == "finish":
        break
     studentList.append(student)
    print("***Students added to the list***")
    print(studentList)
     
def studentId():
   student = input("Enter the name and last name of the student for his/her Id number: ")
   i=0
   while i <= len(studentList):
      if studentList[i] == student: 
         print(i)
         break
      i+=1

def removeMultipleStudent():
    for i in range(len(studentList)):
     studentName = input("Enter the name and last name of the student to remove, if you do not want to remove more, type 'finish': ")
     if studentName == "finish":
        break
     studentList.remove(f"{studentName}")
    print("***Students removed from the list***")
    print(studentList)
     
addStudent()
removeStudent()
printStudents()
addMultipleStudent()
studentId()
removeMultipleStudent()
