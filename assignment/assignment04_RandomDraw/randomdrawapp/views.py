from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'randomdrawapp/home.html')

def result_pair(request):
    list = ('강연우', '김서영', '김소은', '김유진', '김정운', '노은성', '문다연', '박경나', '박혜준', '안현주', '오예림', '이민정', '이연수', '장한빛', '조원아', '황서경')
    order = random.sample(list, 16)

    pair = {
        'pair_1': order[0]+" "+order[1],
        'pair_2': order[2]+" "+order[3],
        'pair_3': order[4]+" "+order[5],
        'pair_4': order[6]+" "+order[7],
        'pair_5': order[8]+" "+order[9],
        'pair_6': order[10]+" "+order[11],
        'pair_7': order[12]+" "+order[13],
        'pair_8': order[14]+" "+order[15]
    }
    return render(request, 'randomdrawapp/result_pair.html', pair)

def result_team(request):
    list = ('강연우', '김서영', '김소은', '김유진', '김정운', '노은성', '문다연', '박경나', '박혜준', '안현주', '오예림', '이민정', '이연수', '장한빛', '조원아', '황서경')
    order = random.sample(list, 16)

    team = {
        'team_1': order[0]+" "+order[1]+" "+order[2]+" "+order[3],
        'team_2': order[4]+" "+order[5]+" "+order[6]+" "+order[7],
        'team_3': order[8]+" "+order[9]+" "+order[10]+" "+order[11],
        'team_4': order[12]+" "+order[13]+" "+order[14]+" "+order[15],
    }
    return render(request, 'randomdrawapp/result_team.html', team)
