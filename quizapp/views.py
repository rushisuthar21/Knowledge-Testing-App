from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import Question, Quiz, Result
from .forms import CustomUserCreationForm
import random

# RegisterView: This view allows new users to create an account
def RegisterView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Account created successfully for {user.username}')
            return redirect('quizapp:quiz')
    else:
        form = CustomUserCreationForm()
    return render(request, 'quizapp/register.html', {'form': form})

# LoginView: This view handles user login
def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('quizapp:quiz')
    else:
        form = AuthenticationForm()
    return render(request, 'quizapp/login.html', {'form': form})

# LogoutView: This view handles user logout
def LogoutView(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('quizapp:home')

# QuizView: This view handles the quiz interaction
@login_required
def QuizView(request):
    if request.method == 'POST':
        # Retrieve the questions from the session
        question_ids = request.session.get('question_ids', [])
        print(f"DEBUG: Retrieved question IDs from session (POST): {question_ids}")
        selected_options = {}

        # Collect selected options based on question IDs
        for question_id in question_ids:
            selected_option = request.POST.get(f'options_{question_id}')
            selected_options[str(question_id)] = selected_option

            # Fetch the question and its correct answer
            question = Question.objects.get(id=question_id)
            correct_answer = question.correct_option

            # Log the selected and correct answers
            print(f"DEBUG: Question: {question.question_text}")
            print(f"DEBUG: Selected Answer: {selected_option}")
            print(f"DEBUG: Correct Answer: {correct_answer}")

        # Retrieve the questions using the stored IDs
        questions = [Question.objects.get(id=question_id) for question_id in question_ids]

        # Create and save the quiz instance
        quiz = Quiz.objects.create(user=request.user)
        quiz.questions.set(questions)

        # Calculate the score and save the result
        quiz.calculate_score(selected_options)
        Result.objects.create(user=request.user, quiz=quiz, score=quiz.score)

        # Clear the session
        del request.session['question_ids']

        return redirect('quizapp:scores')

    else:
        # Shuffle and select questions
        questions = list(Question.objects.all())
        random.shuffle(questions)
        selected_questions = questions[:5]
        print(f"DEBUG: Selected question IDs (GET): {[q.id for q in selected_questions]}")

        # Store the question IDs in the session in the exact order they are presented
        request.session['question_ids'] = [question.id for question in selected_questions]

        return render(request, 'quizapp/quiz.html', {'questions': selected_questions})

# ScoreView: This view displays all the past scores of a user
@login_required
def ScoreView(request):
    results = Result.objects.filter(user=request.user)
    total_quizzes = results.count()
    total_score = sum(result.score for result in results)
    average_score = total_score / total_quizzes if total_quizzes > 0 else 0
    highest_score = max(result.score for result in results) if total_quizzes > 0 else 0
    lowest_score = min(result.score for result in results) if total_quizzes > 0 else 0

    # Determine if the user should be allowed to retake the quiz
    last_result = results.last() if results.exists() else None
    allow_retake = last_result and (last_result.score / 5.0 * 100) < 50

    # Calculate the percentage and performance message for the last quiz
    if last_result:
        last_percentage = (last_result.score / 5.0) * 100
        if last_percentage == 100:
            performance_message = "You are a genius!"
        elif last_percentage >= 50:
            performance_message = "Good job!"
        else:
            performance_message = "Please try again!"
    else:
        last_percentage = None
        performance_message = None

    context = {
        'results': results,
        'average_score': average_score,
        'highest_score': highest_score,
        'lowest_score': lowest_score,
        'allow_retake': allow_retake,
        'last_percentage': last_percentage,
        'performance_message': performance_message,
    }
    return render(request, 'quizapp/scores.html', context)

# AdminDashboardView: This view is for admin users to access the admin dashboard
@staff_member_required
def AdminDashboardView(request):
    return render(request, 'quizapp/admin_dashboard.html')

# HomePageView: This view renders the home page
def HomePageView(request):
    return render(request, 'quizapp/home.html')
