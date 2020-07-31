from django.shortcuts import render
import random


def generate(request):
    if request.method == 'POST':
        context = request.POST['text']
        passw = ''
        for i in range(10):
            passw = passw + random.choice(context)

        print(passw)
        return render(request, 'home.html', {'pass': passw})
    return render(request, 'home.html')
