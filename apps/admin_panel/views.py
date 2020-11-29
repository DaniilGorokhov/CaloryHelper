from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from apps.index.models import Admin
from apps.admin_panel.models import Course, Topic, StaticGraph, Specialization


def index(request, admin_login=None):
    if admin_login is None:
        return HttpResponseRedirect(reverse('index:index'))
    else:
        courses_list = Course.objects.filter(admin=(Admin.objects.get(login=admin_login)))
        return render(request, 'admin_panel/index.html', {'courses_list': courses_list, 'admin_login': admin_login})


def course(request, admin_login, course_id):
    topics_list = Topic.objects.filter(course=(Course.objects.get(id=course_id)))
    return render(request, 'admin_panel/course_inner.html', {'course_id': course_id, 'admin_login': admin_login,
                                                             'topics_list': topics_list,
                                                             'ex_image0': StaticGraph.objects.all()[0],
                                                             'ex_image1': StaticGraph.objects.all()[1]})


def topic_edit(request, admin_login, course_id, topic_id):
    return render(request, 'admin_panel/topic_edit.html')


def add_course(request, admin_login):
    try:
        admin = Admin.objects.get(login=admin_login)
    except:
        raise Http404
    Course.objects.create(title=request.POST['title_course'], admin=admin)
    return HttpResponseRedirect(reverse('admin_panel:index', args=(admin_login, )))


def delete_course(request, admin_login, course_id):
    try:
        admin = Admin.objects.get(login=admin_login)
        course = Course.objects.get(id=course_id)
    except:
        raise Http404
    course.delete()
    return HttpResponseRedirect(reverse('admin_panel:index', args=(admin_login,)))


def add_topic(request, admin_login, course_id):
    is_private = request.POST.get('is_private', False)
    try:
        admin = Admin.objects.get(login=admin_login)
        course = Course.objects.get(id=course_id)
    except:
        raise Http404
    Topic.objects.create(title=request.POST['title_topic'], content=request.POST['content'], course=course)
    return HttpResponseRedirect(reverse('admin_panel:course', args=(admin_login, course_id)))


def delete_topic(request, admin_login, course_id, topic_id):
    try:
        admin = Admin.objects.get(login=admin_login)
        course = Course.objects.get(id=course_id)
        topic = Topic.objects.get(id=topic_id)
    except:
        raise Http404
    topic.delete()
    return HttpResponseRedirect(reverse('admin_panel:course', args=(admin_login, course_id)))


def to_spez(request, admin_login):
    try:
        admin = Admin.objects.get(login=admin_login)
    except:
        raise Http404
    try:
        courses_list = Course.objects.filter(admin=admin)
    except:
        courses_list = []
    return render(request, 'admin_panel/course_spez.html', {'courses_list': courses_list, 'admin_login': admin_login})


def edit_depends(request, admin_login, course_id):
    try:
        admin = Admin.objects.get(login=admin_login)
        course = Course.objects.get(id=course_id)
    except:
        raise Http404
    try:
        depends_list = Specialization.objects.filter(courses=course)
    except:
        depends_list = []
    all_spez = Specialization.objects.all()
    return render(request, 'admin_panel/depends.html', {'depends_list': depends_list, 'all_spez': all_spez,
                                                        'admin_login': admin_login, 'course_id': course_id})


def save_depends(request, admin_login, course_id):
    try:
        admin = Admin.objects.get(login=admin_login)
        course = Course.objects.get(id=course_id)
    except:
        raise Http404
    is_private = request.POST.get('is_private', False)
    all_spez = Specialization.objects.all()
    for spec in all_spez:
        tmp = request.POST['csrfmiddlewaretoken']
        if tmp == 'on':
            try:
                spec.courses.add(course)
            except:
                pass
        else:
            try:
                spec.courses.remove(course)
            except:
                pass
    try:
        depends_list = Specialization.objects.filter(courses=course)
    except:
        depends_list = []
    return HttpResponseRedirect(reverse('admin_panel:edit_depends', args=(admin_login, course_id, )))


def add_spec(request, admin_login, course_id):
    try:
        admin = Admin.objects.get(login=admin_login)
        course = Course.objects.get(id=course_id)
    except:
        raise Http404
    a = Specialization(title=request.POST['title_spec'])
    a.save()
    a.courses.add(course)
    return HttpResponseRedirect(reverse('admin_panel:edit_depends', args=(admin_login, course_id, )))
