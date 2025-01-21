from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]

    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=7, choices=OPTION_CHOICES)

    def __str__(self):
        return self.question_text

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    score = models.IntegerField(default=0)
    date_taken = models.DateTimeField(auto_now_add=True)

    def calculate_score(self, selected_options):
        correct_answers = 0

        for question in self.questions.all():
            selected_option = selected_options.get(str(question.id))
            print(f"DEBUG: Checking question: {question.question_text}")
            print(f"DEBUG: Selected option: {selected_option}")
            print(f"DEBUG: Correct option: {question.correct_option}")

            if selected_option == question.correct_option:
                correct_answers += 1
                print(f"DEBUG: Correct answer for: {question.question_text}")
            else:
                print(f"DEBUG: Incorrect answer for: {question.question_text}")

        self.score = correct_answers
        print(f"DEBUG: Total correct answers: {correct_answers}")
        self.save()

    def __str__(self):
        return f'Quiz by {self.user.username} on {self.date_taken}'

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.score}'
