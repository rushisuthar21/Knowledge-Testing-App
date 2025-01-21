from django.contrib import admin
from .models import Question, Quiz, Result

# QuestionAdmin: Custom admin for managing questions
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_option')  # Display these fields in the list view
    search_fields = ('question_text',)  # Allow searching by question text
    list_filter = ('correct_option',)  # Filter by the correct option

# QuestionInline: Inline for associating questions with quizzes
class QuestionInline(admin.TabularInline):
    model = Quiz.questions.through  # Through model to display M2M relationship in inline
    extra = 1  # Number of extra blank fields for new questions

# QuizAdmin: Custom admin for managing quizzes
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'date_taken')  # Display these fields in the list view
    search_fields = ('user__username', 'date_taken')  # Allow searching by username and date taken
    list_filter = ('date_taken', 'score')  # Filter by date taken and score
    inlines = [QuestionInline]  # Include the QuestionInline to manage questions within quizzes

# ResultAdmin: Custom admin for managing results
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'date_taken')  # Display these fields in the list view
    search_fields = ('user__username', 'quiz__date_taken')  # Allow searching by username and quiz date taken
    list_filter = ('date_taken', 'score')  # Filter by date taken and score
    readonly_fields = ('date_taken',)  # Make date_taken read-only to prevent editing
