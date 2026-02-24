from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='faculties/', blank=True, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='teachers')
    bio = models.TextField()
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.title

class Minor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='minors')

    def __str__(self):
        return self.name

class Review(models.Model):
    student_name = models.CharField(max_length=100)
    content = models.TextField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.student_name} - {self.faculty.name}'