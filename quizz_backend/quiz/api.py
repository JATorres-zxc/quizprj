from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Quiz, Question, Answer
from .forms import QuizForm, QuestionForm, AnswerForm

# View for creating a new quiz
@api_view(['POST'])
# depende pa if gagawin kong pwede no acc
# @authentication_classes([])  # Adjust based on your authentication needs
# @permission_classes([])  # Adjust based on your permission needs
def create_quiz(request):
    data = request.data
    form = QuizForm(data)
    if form.is_valid():
        quiz = form.save(commit=False)
        quiz.creator = request.user
        quiz.save()
        return JsonResponse({'status': 'success', 'quiz_id': quiz.id})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})

# View for deleting a question
@api_view(['DELETE'])
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return JsonResponse({'status': 'success'})

# View for saving a question
@api_view(['POST'])
def save_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    data = request.data
    form = QuestionForm(data)
    if form.is_valid():
        question = form.save(commit=False)
        question.quiz = quiz
        question.save()
        return JsonResponse({'status': 'success', 'question_id': question.id})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})

# View for editing a question
@api_view(['POST'])
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    data = request.data
    form = QuestionForm(data, instance=question)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})

# View for adding an answer to a question
@api_view(['POST'])
def add_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    data = request.data
    form = AnswerForm(data)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.question = question
        answer.save()
        return JsonResponse({'status': 'success', 'answer_id': answer.id})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})

# View for deleting an answer
@api_view(['DELETE'])
def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    answer.delete()
    return JsonResponse({'status': 'success'})

# View for displaying quiz details
@api_view(['GET'])
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    quiz_data = {
        'id': quiz.id,
        'title': quiz.title,
        'description': quiz.description,
        'questions': [
            {
                'id': question.id,
                'text': question.text,
                'question_type': question.question_type,
                'answers': [
                    {'id': answer.id, 'text': answer.text, 'is_correct': answer.is_correct}
                    for answer in question.answers.all()
                ]
            }
            for question in questions
        ]
    }
    return JsonResponse({'status': 'success', 'quiz': quiz_data})
