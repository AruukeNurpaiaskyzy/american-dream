from django.shortcuts import render
from apps.academy.models import  Settings, Contacts, Teacher, \
AboutPage, AboutObjects, AboutObjects2, Courses, Feedback, CoursesModel, CoursesPage, CourseApplication, TypeCourse
from django.core.mail import send_mail
from django.conf import settings as st
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
# from .forms import CourseApplicationForm
import requests
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def settings(request):
    if request.method == 'POST':
        print("\n== POST получен ==")

        # Проверка, это форма записи на курс или форма обратной связи
        name_register = request.POST.get('name_register')
        phone_register = request.POST.get('phone_register')
        email_register = request.POST.get('email_register')
        # course_id = request.POST.get('course_id')

        # === Если форма записи на курс ===
        if request.method == "POST":
                name_register = request.POST.get('name_register')
                phone_register = request.POST.get('phone_register')
                email_register = request.POST.get('email_register')
                course_id = request.POST.get('course_id')

        if name_register and phone_register and course_id:
            try:
                course = get_object_or_404(Courses, id=course_id)

                # Сохраняем в БД
                CourseApplication.objects.create(
                    full_name=name_register,
                    phone=phone_register,
                    email=email_register,
                    course=course
                )

                # Отправка в WhatsApp
                whatsapp_number = '996558486448'
                api_key = '9478477'
                message = f"\U0001F4DA Новая заявка:\n\U0001F464 {name_register}\n\U0001F4DE {phone_register}\n\U0001F4E7 {email_register}\n\U0001F393 {course.title}"
                requests.get(
                    f"https://api.callmebot.com/whatsapp.php?phone={whatsapp_number}&text={requests.utils.quote(message)}&apikey={api_key}"
                )
            except Exception as e:
                print(f"Ошибка: {e}")

        # === Иначе это форма обратной связи ===
        else:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            print("Это обратная связь")
            print("Имя:", name)
            print("Тел:", phone)

            Feedback.objects.create(name=name, phone=phone, email=email)

            subject = 'Новая обратная связь'
            message = f'Имя: {name}\nТелефон: {phone}\nEmail: {email}'
            recipient_list = ['aruukelisa@gmail.com.com']
            send_mail(subject, message, st.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect('/')

    # === GET запрос ===
    settings_obj = Settings.objects.latest("id")
    contact = Contacts.objects.latest("id")
    teachers = Teacher.objects.prefetch_related('achievements')
    courses = Courses.objects.prefetch_related('programs', 'modals')
    model_all_dict = {model.courses.id: model for model in CoursesModel.objects.all()}

    return render(request, 'index.html', {
        'settings': settings_obj,
        'contact': contact,
        'teachers': teachers,
        'courses': courses,
        'model_all': model_all_dict
    })



class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_id"] = AboutPage.objects.latest("id")
        context["settings_obj"] = Settings.objects.latest("id")
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
    courses_page = CoursesPage.objects.latest("id")
    courses_all = Courses.objects.select_related('direction').prefetch_related('programs', 'modals')
    directions = TypeCourse.objects.all()
    settings_obj = Settings.objects.latest("id")
    return render(request, 'courses.html', {
        'courses_page': courses_page,
        'courses_all': courses_all,
        'directions': directions,
        'settings': settings_obj,
    })

