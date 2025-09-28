from django.shortcuts import render

from .models import *


def Index_view(request):
    correct=None
    incorrects=None
    messege=None
    word= request.GET.get('word')
    if word is not None:
        word=word.lower()
        corrects=Correct.objects.filter(word=word)
        if corrects.exists():
            correct=corrects.first()
            incorrects=Incorrect.objects.filter(correct=correct)

        else:
            incorrects=Incorrect.objects.filter(word=word)
            if incorrects.exists():
                incorrect=incorrects.first()
                correct=incorrect.correct
                incorrects=correct.incorrect_set.all()
            else:
                if 'x' not in word and 'h' not in word:
                    messege="so'z tarkibida x yoki h mavjud emas!"
                else:
                    messege="ro'yhatta mavjud emas"



    context={
        'word':word,
        'correct':correct,
        'incorrects':incorrects,
        'messege':messege,
    }


    return render (request, 'index.html', context)
