from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def outside(request):
    return render(request, 'outside.html')

def AnniversaryBuilding(request):
    return render(request, 'AnniversaryBuilding.html')

def HumanSocialBuilding(request):
    return render(request, 'HumanSocialBuilding.html')

def Noori(request):
    return render(request, 'Noori.html')
       
# def Score(request):
#     if (request.method == 'POST'):
#         average=[]
#         while 1:
#             s=int(input())
#             average.append(s)
#             sum=0
#             for i in average:
#                 sum=sum+i
#                 score=sum/len(average)
#     return (score)