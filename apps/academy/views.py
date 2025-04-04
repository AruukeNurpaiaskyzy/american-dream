from django.shortcuts import render
from apps.academy.models import  Settings, Contacts, Teacher, AboutPage, AboutObjects, AboutObjects2, Courses, Feedback
from django.core.mail import send_mail
from django.conf import settings as st
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .forms import CourseApplicationForm
import requests

# Create your views here.
def settings(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Сохраняем в базу
        Feedback.objects.create(name=name, phone=phone, email=email)

        # Отправляем на почту
        subject = 'Новая заявка с сайта'
        message = f'Имя: {name}\nТелефон: {phone}\nEmail: {email}'
        recipient_list = ['your_email@example.com']  # замени на нужный email

        send_mail(subject, message, st.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect('/')
    settings = Settings.objects.latest("id")
    contact = Contacts.objects.latest("id")
    # courses = PageCourses.objects.latest('id')
    teachers = Teacher.objects.prefetch_related('achievements')
    courses = Courses.objects.prefetch_related('programs')
    return render (request, 'index.html', locals())

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_id"] = AboutPage.objects.latest("id")
        objs1 = list(AboutObjects.objects.all())
        objs2 = list(AboutObjects2.objects.all())
        combined = []
        max_len = max(len(objs1), len(objs2))
        for i in range(max_len):
            if i < len(objs1):
                combined.append({'item': objs1[i], 'reverse': False, 'color': 'grey'})
            if i < len(objs2):
                combined.append({'item': objs2[i], 'reverse': True, 'color': 'green'})
        context["about_combined"] = combined
        return context

def courses(request):
    return render (request, 'courses.html', locals())


def submit_application(request, course_id):
    course = get_object_or_404(Courses, id=course_id)

    if request.method == 'POST':
        form = CourseApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.course = course
            application.save()

            # отправка в WhatsApp (пример)
            message = f"Заявка на курс: {course.title}\nИмя: {application.full_name}\nТелефон: {application.phone}\nEmail: {application.email}"
            whatsapp_url = f"https://api.whatsapp.com/send?phone=+996xxxxxxxxx&text={message}"
            requests.get(whatsapp_url)  # или используем Twilio, CallMeBot, Chat API

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'error': 'Invalid method'})