from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=1000)
    password=models.CharField(max_length=1000)
    type=models.CharField(max_length=1000)

class staff_table(models.Model):
    login=models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname=models.CharField(max_length=1000)
    lname=models.CharField(max_length=1000)
    gender = models.CharField(max_length=1000)
    place = models.CharField(max_length=1000)
    post = models.CharField(max_length=1000)
    pin = models.IntegerField()
    email = models.CharField(max_length=1000)
    phone = models.BigIntegerField()
    image = models.FileField()

class course_table(models.Model):
    coursename=models.CharField(max_length=1000)
    details=models.CharField(max_length=900)
    date=models.DateField()

class subject_table(models.Model):
    course=models.ForeignKey(course_table,on_delete=models.CASCADE)
    subject=models.CharField(max_length=1000)
    details=models.CharField(max_length=900)

class student_table(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    fname=models.CharField(max_length=1000)
    lname=models.CharField(max_length=1000)
    gender=models.CharField(max_length=1000)
    place=models.CharField(max_length=1000)
    post=models.CharField(max_length=1000)
    pin=models.IntegerField()
    course = models.ForeignKey(course_table, on_delete=models.CASCADE)
    email=models.CharField(max_length=1000)
    contact=models.BigIntegerField()
    dob=models.DateField()
    image=models.FileField()

class studymaterials_tables(models.Model):
    subject=models.ForeignKey(subject_table,on_delete=models.CASCADE)
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    material=models.FileField()
    date=models.DateField()
    topic=models.CharField(max_length=900)



class allocate_table(models.Model):
    subject = models.ForeignKey(subject_table, on_delete=models.CASCADE)
    staff = models.ForeignKey(staff_table, on_delete=models.CASCADE)

class feedback_table(models.Model):
    student=models.ForeignKey(student_table,on_delete=models.CASCADE)
    feedback=models.TextField()
    subject = models.ForeignKey(subject_table, on_delete=models.CASCADE)
    date=models.DateField()

class complaint_table(models.Model):
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    student = models.ForeignKey(student_table, on_delete=models.CASCADE)
    complaint=models.TextField()
    reply=models.TextField()
    date=models.DateField()

class doubt_table(models.Model):
    subject = models.ForeignKey(subject_table, on_delete=models.CASCADE)
    staff = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    student = models.ForeignKey(student_table, on_delete=models.CASCADE)
    doubt = models.TextField()
    reply = models.TextField()

class staff_noti_table(models.Model):
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    SUBID = models.ForeignKey(allocate_table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    content = models.CharField(max_length=100)


class work_result(models.Model):
    WORK = models.ForeignKey(staff_noti_table, on_delete=models.CASCADE)
    STUDENT= models.ForeignKey(student_table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    report = models.FileField()
    remark=models.CharField(max_length=30)
    mark=models.FloatField()


class studentperformance_table(models.Model):
    work=models.ForeignKey(work_result, on_delete=models.CASCADE)
    subject=models.ForeignKey(subject_table,on_delete=models.CASCADE)
    student=models.ForeignKey(student_table,on_delete=models.CASCADE)
    grade=models.CharField(max_length=1000)

class emotion_table(models.Model):
    STUDENT= models.ForeignKey(student_table, on_delete=models.CASCADE)
    emotion=models.CharField(max_length=100)
    pose=models.CharField(max_length=20)
    datetime=models.DateTimeField()


