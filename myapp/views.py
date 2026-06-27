# from django.shortcuts import render, redirect
# from .models import Person
# from .forms import PersonForm
#
#
# # Create your views here.
# def Person_form(request):
#     form = PersonForm(request.POST)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect("person_list")
#     ctx = {
#         'form': form
#     }
#     return render(request, 'form.html', ctx)
#
#
# def person_list(request):
#     persons = Person.objects.all()
#     ctx = {
#         'persons': persons
#     }
#     return render(request, 'person_list.html', ctx)
# def register_view(request):
#     if request.method == 'POST':
#         # ... ma'lumotlarni olish va saqlash kodingiz ...
#         # MASA: user.save()
#
#         # ENG MUHIM QISM: BU QATORNI YOZING
#         # 'my_app' nomli app ichidagi 'books_page' nomli manzilga o'tadi
#         return redirect('books_page')
#
#     return render(request, 'your_template.html')
#
#
# from django.shortcuts import render, redirect
#
#
# def register_view(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#
#         # Agar kerakli maydonlar bo'sh bo'lsa, xabar ko'rsatib, formada qoldir
#         if not first_name or not last_name or not email:
#             # Bu yerda istalgan xabarni yozishingiz mumkin
#             return render(request, 'index.html', {'error': 'Iltimos, barcha maydonlarni to\'ldiring!'})
#
#         # Agar hammasi to'ldirilgan bo'lsa, bazaga saqlang
#         # ... bu yerga sizning avvalgi ma'lumotlarni saqlash kodingiz keladi (masalan: User.objects.create...) ...
#
#         return redirect('books_page')  # Kitoblar sahifasiga o'tadi
#
#     return render(request, 'index.html')
#
#
# def main(request):
#     if request.POST:
#         model = Person()
#         model.first_name = request.POST.get('first_name', '')
#         model.last_name = request.POST.get('last_name', '')
#         # model.company = request.POST.get('company', '')
#         model.email = request.POST.get('email', '')
#         model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
#         model.course_type = request.POST.get('course_type', '')
#         model.subject = request.POST.get('subject', '')
#         model.exist = request.POST.get('exist', '')
#         model.save()
#         print(request.POST)
#     return render(request, 'index.html')
#
# # def register(request):
# #     if request.POST:
#
# #         print(request.POST)
# #     return render(request,'register.html')
from django.shortcuts import render, redirect
from .models import Person

def register_view(request):
    # Agar forma POST so'rov bilan kelsa (ya'ni foydalanuvchi "Register" tugmasini bossa)
    if request.method == 'POST':
        # 1. Maydonlarni olish
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        area_code = request.POST.get('area_code')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        exist = request.POST.get('exist')

        # 2. Bo'sh maydonlarni tekshirish (Agar bo'sh bo'lsa, qizil xabar bilan formada qoldir)
        if not first_name or not last_name or not email:
            return render(request, 'index.html', {
                'error': 'Iltimos, Ism, Familiya va Email maydonlarini to\'ldiring!'
            })

        # 3. Bazaga saqlash (sizning main funksiyangizdagi mantiq)
        model = Person()
        model.first_name = first_name
        model.last_name = last_name
        model.email = email
        model.phone = area_code + phone  # Telefon raqamini birlashtirish
        model.subject = subject
        model.exist = exist
        model.save()

        # 4. Muvaffaqiyatli saqlangandan so'ng, Kitoblar sahifasiga o'tish
        return redirect('books_page')  # Bu manzil my_app/urls.py da name='books_page' bo'lishi shart

    # Agar sahifa birinchi marta ochilsa (GET so'rov), formani ko'rsat
    return render(request, 'index.html')