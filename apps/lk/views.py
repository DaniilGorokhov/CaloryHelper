from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from apps.index.models import User, UserHistory
from sova_avia.settings import MEDIA_ROOT

from imageai.Prediction import ImagePrediction
import json

from .models import Article
from .forms import ArticleForm


def index(request, user_login):
    try:
        user = User.objects.get(login=user_login)
    except:
        raise Http404
    return render(request, 'lk/index.html', {'user_instance': user, 'user_login': user_login})


def view_history(request, user_login):
    # try:
    #     history = UserHistory.objects.get(userId = user_login)
    # except:
    #     raise Http404
    user_id = User.objects.get(login=user_login).id
    return render(request, 'lk/history.html', {'history': UserHistory.objects.all().filter(userId = user_id),
                                               'user_login': user_login})


def settings(request, user_login):
    try:
        user = User.objects.get(login=user_login)
    except:
        raise Http404
    return render(request, 'lk/settings.html', {'user_instance': user, 'user_login': user_login})


def wait(request, user_login):
    if request.POST['password0u'] == request.POST['password1u']:
        User.objects.get(login=user_login).password = request.POST['password0u']
        return HttpResponseRedirect(reverse('lk:index', args=(user_login,)))
    else:
        return render(request, 'lk/settings.html', {'user_instance': User.objects.get(login=user_login),
                                                    'user_login': user_login})


def newPhoto(request, user_login):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_name = request.FILES['file_obj']
            result = process_image(file_name)
            return render(request, 'lk/newPhoto.html', {'form': form, 'user_login': user_login, 'foodVariants': result})
            # return render(request, 'lk/newPhoto.html', {'form': request.POST, 'user_login': user_login})
    else:
        form = ArticleForm()

    return render(request, 'lk/newPhoto.html', {'form': form, 'user_login': user_login})
    # return render(request, 'lk/newPhoto.html', {'user_login': user_login})
    # return render(request, 'lk/newPhoto.html', {'user_login':user_login, 'foodVariants':
    # [{'foodName': 'котлетка', 'foodDescription': "мамина"}]})


def process_image(file_name):
    execution_path = "../../media/media/"

    with open(MEDIA_ROOT + '/media/' + 'foods.json') as f:
        foods = json.load(f)

    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(MEDIA_ROOT + "/media/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
    prediction.loadModel()

    result = []

    predictions, probabilities = prediction.predictImage(MEDIA_ROOT + '/media/' + str(file_name), result_count=10)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        tmp = dict()
        eachPrediction = eachPrediction.replace('_', ' ')

        tmp['foodName'] = eachPrediction
        tmp['foodDescription'] = eachProbability
        calorieAmount = "124 cal"

        flag = False
        for food in foods:
            if food['foodName'] == eachPrediction:
                calorieAmount = food['foodDescription']
                flag = True
                break

        if flag:
            tmp['foodDescription'] = calorieAmount
            result.append(tmp)

    return result


def chooseFood(request, user_login, foodName, foodDescription):
    UserHistory.objects.create(userId=User.objects.get(login=user_login), foodName=foodName, foodDescription=foodDescription)
    return HttpResponseRedirect(reverse('lk:index', args=(user_login,)))


