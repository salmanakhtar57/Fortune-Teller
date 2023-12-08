from django.shortcuts import render
import random
from .forms import FortuneForm
# Create your views here.


fortuneList = [
   "All will go well with your new project.",
    "Coding is the art of turning caffeine into code.",
    "The best code is like a poem – elegant, concise, and impactful.",
    "Code speaks louder than words.",
    "Words weave worlds.",
    "Logic: where magic meets reality.",
    "Productivity fuels dreams.",
    "Ink spills, ideas bloom.",
    "In the world of programming, bugs are just unintended features waiting to be discovered.",
    "The key to mastering productivity is not managing time but managing focus and energy.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Caffeine: coder's companion.",
    "Logic whispers in code.",
    "Words dance on keys.",
    "Dream big, work small.",
    "Code: poetry in binary.",
]

fortune = random.choice(fortuneList)

def fortune(request):
    form = FortuneForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form = FortuneForm()  # Reset the form
        fortune = random.choice(fortuneList)
    else:
        fortune = random.choice(fortuneList)

    context = {
        'fortune': fortune,
        'form': form,
    }

    return render(request, 'randomfortune/fortune.html', context)