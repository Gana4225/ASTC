from django.db import models

class Regulation(models.Model):
    regulation = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.regulation

class Department(models.Model):
    department = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.department


class Student(models.Model):
    roll_number = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    regulation = models.ForeignKey('Regulation', on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=250, unique=True, null=False)
    image = models.ImageField(upload_to="profile_images",null=True, blank=True)

    def __str__(self):
        return f"{self.roll_number} {self.name}"

class Re(models.Model):
    user_name = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=200)  # Store hashed passwords
    roll_number = models.OneToOneField(Student, on_delete=models.CASCADE)  # Prevent duplicate roll_numbers
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.user_name} ({self.roll_number})"

class test(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.roll_number} {self.department}"

class Course(models.Model):
    course_id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False, default="")

class mids(models.Model):
    subject_code = models.CharField(max_length=20, null=False)



class Placements(models.Model):
    name = models.CharField(max_length=500,null=False)
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.CharField(max_length=1000,null=False)
    package = models.IntegerField(default=0,null=False)
    image = models.ImageField(upload_to="placements/",blank=True,null=True)
    batch = models.CharField(max_length=100,null=True,default="")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"{self.name}"
