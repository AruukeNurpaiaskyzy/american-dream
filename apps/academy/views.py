from django.shortcuts import render
from apps.academy.models import Settings, Contacts, Teacher, AboutPage, AboutObjects, AboutObjects2
from django.views.generic import TemplateView

# Create your views here.
def settings(request):
    settings = Settings.objects.latest("id")
    contact = Contacts.objects.latest("id")
    # courses = PageCourses.objects.latest('id')
    teachers = Teacher.objects.prefetch_related('achievements')

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