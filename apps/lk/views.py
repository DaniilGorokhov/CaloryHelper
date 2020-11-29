from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from apps.index.models import User, UserHistory
from apps.admin_panel.models import Course
from sova_avia.settings import MEDIA_ROOT

from imageai.Prediction import ImagePrediction
import os

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

    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(MEDIA_ROOT + "/media/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
    prediction.loadModel()

    result = []

    predictions, probabilities = prediction.predictImage(MEDIA_ROOT + '/media/' + str(file_name), result_count=10)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        tmp = dict()
        tmp['foodName'] = eachPrediction
        tmp['foodDescription'] = eachProbability
        result.append(tmp)

    return result


def chooseFood(request, user_login, foodName, foodDescription):
    UserHistory.objects.create(userId=User.objects.get(login=user_login), foodName=foodName, foodDescription=foodDescription)
    return HttpResponseRedirect(reverse('lk:index', args=(user_login,)))


# def upload_image(request, user_login):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = ArticleForm()
#
#     return render(request, 'lk/newPhoto.html', {'form': form})

# def upload_image(request, user_login):
#     # Document.objects.create(doc_file)
#     form = UploadFileForm(request.POST, request.FILES)
#     if form.is_valid():
#         handle_uploaded_file(request.FILES['file'])
#         return render(request, 'lk/list.html', {'form': form, 'user_login': user_login})
#     else:
#         form = UploadFileForm()
#     return render(request, 'lk/newPhoto.html', {'form': form, 'user_login': user_login})
#     # return render(request, 'lk/list.html', {'files': request.FILES['file'], 'user_login': user_login})
#
#
# def handle_uploaded_file(f):
#     destination = open('some/file/name.txt', 'wb+')
#     for chunk in f.chunks():
#         destination.write(chunk)
#     destination.close()
    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         new_doc = Document(docfile=request.FILES['file'])
    #         new_doc.save()
    #
    #         # Redirect to the document list after POST
    #         return HttpResponseRedirect(reverse('lk:upload_image', args=(user_login,)))
    # else:
    #     form = DocumentForm()  # A empty, unbound form
    #
    # # Load documents for the list page
    # documents = Document.objects.all()
    #
    # # Render list page with the documents and the form
    # return render_to_response(
    #     'lk/list.html',
    #     {'documents': documents, 'form': form, 'user_login': user_login},
    #       context_
    # )
    # return HttpResponseRedirect(reverse('lk:index', args=(user_login,)))
