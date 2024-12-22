from django.db import models

# Create your models here.

### banking application
class Person(models.Model):

    name = models.CharField(max_length=120)
    ssn = models.CharField(max_length=9)

    def __str__(self):
        return self.name

class BankAccount(models.Model):

    account_num = models.IntegerField()
    balance = models.FloatField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account_num} ({self.person})"


### class registration exam
class Course(models.Model):

    name = models.CharField(max_length=120)
    number = models.CharField(max_length=10)
    # teacher, meeting time, etc...

    def __str__(self):
        return f'{self.number}: {self.name}'

class Student(models.Model):

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Registration(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} - {self.course}'

    def get_students_for_course(self, course):

        registrations = Registration.objects.filter(course=course)
        return [r.student for r in registrations]


###################################
### Family Tree example

class FamilyPerson(models.Model):

    name = models.CharField(max_length=120)
    date_of_birth = models.DateField()

    # define parent relationship
    mother = models.ForeignKey('FamilyPerson', on_delete=models.CASCADE, related_name='mother_person', null=True, blank=True)
    father = models.ForeignKey('FamilyPerson', on_delete=models.CASCADE, related_name='father_person', null=True, blank=True)

    def __str__(self):
        return self.name

