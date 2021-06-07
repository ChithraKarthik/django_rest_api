from django.db import models

class StudentList(models.Model):
    student_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=20)
    semester = models.CharField(max_length=100)

    def __str__ (self):
        return self.name+ "  "+self.department

class MarkList(models.Model):
    student = models.ForeignKey(StudentList,related_name='marks', on_delete= models.CASCADE)
    language = models.IntegerField()
    paper1=models.IntegerField()
    paper2=models.IntegerField()
    paper3=models.IntegerField()
    practical = models.IntegerField()

    def __str__ (self):
        return self.student
