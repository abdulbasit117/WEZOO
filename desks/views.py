from django.shortcuts import render, redirect
from .models import Booking, City,Cards,Category, CustomUser
from desks.models import CustomUser as User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Cards, Booking
from django.contrib.auth.decorators import login_required



def main_page(request):
    hot = City.objects.all()
    category = Category.objects.all()
    cards = Cards.objects.all()[:2]
    context = {'hot': hot, 'category': category,'cards':cards}
    return render(request, 'desks/index.html',context=context)





def city_detail(request, city_name):
    city = City.objects.get(name_city=city_name)
    context = {'city': city}
    return render(request, 'desks/card.html', context)



def cat_by_filter(request,category_name):
    categoryyyyy = Category.objects.get(name=category_name)
    hot = City.objects.filter(category = categoryyyyy)
    category = Category.objects.all()
    cards = Cards.objects.all()[:2]
    context = {'hot':hot,'category':category,'cards':cards}

    return render(request,'desks/index.html',context=context)

def hot_filter(request, city_name):
    city = City.objects.get(name_city=city_name)
    cards = Cards.objects.filter(city=city)

    return render(request, 'desks/card.html', {
        'cards': cards,
        'city': city
    })



def logout_view(request):
    logout(request)
    return redirect('login')

def about_as(request):
    return render(request,'desks/about.html')

def cards(request):
    cards = Cards.objects.all()
    context = {
        'cards':cards
    }

    return render(request,'desks/card.html', context=context)





def contact(request):
    return render(request,'desks/contact.html')

def hov_does(request):
    return render(request,'desks/index2.html',)

def index2(request):
    hot = City.objects.all()
    return render(request,'desks/index_0.html', context={'hot':hot})

def day(request):
    return render(request,'desks/days.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
            return redirect('main-page')
        else:
            messages.error(request, 'Неверный логин или пароль')
            return redirect('login')
        
    return render(request, 'desks/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']
        password2 = request.POST['password2']
        image = request.FILES.get('image') 
        print("FILES:", request.FILES)
        print("IMAGE:", image)

        if password != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже есть')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        if image:
            user.images = image
            user.save()

        messages.success(request, 'Регистрация успешна! Теперь войдите.')
        return redirect('login')

    return render(request, 'desks/register.html')


@login_required
def profile(request):
    user = request.user
    cards = Cards.objects.filter(author=user)
    book = Booking.objects.filter(user=user).select_related("card")

    tab = request.GET.get("tab", "my")      

    context = {
        "cards": cards,
        "book": book,
        "user": user,
        "tab": tab,
        "count_cards": cards.count(),
        "count_book": book.count(),
    }
    return render(request, "desks/profile.html", context)


def delete(request,title):
    card = Cards.objects.get(title=title)
    card.delete()
    return render(request,'/desks/profile.html')


@login_required
def change_profile(request):
    user = request.user
    categories = Category.objects.all()

    if request.method == "POST":
        username = request.POST.get('username', user.username).strip()
        email = request.POST.get('email', user.email).strip()
        new_password = request.POST.get('password', '').strip()
        image = request.FILES.get('image')

        user.username = username
        user.email = email

        if image:
            user.images = image

        if new_password:
            user.set_password(new_password)

        user.save()

        if new_password:
            messages.success(request, "Профиль обновлён. Войди заново, потому что пароль изменился.")
            return redirect('/login/')

        messages.success(request, "Профиль обновлён!")
        return redirect('profile')

    context = {
        'categories': categories,
        'user': user
    }
    return render(request, 'desks/change_profile.html', context)




@login_required
def detail_bron(request, title):
    card = Cards.objects.get(title=title)

    if request.method == "POST":
        Booking.objects.create(user=request.user, card=card,)
        return redirect("/profile/?tab=bookings")

    return render(request, "desks/bron.html", {"cards": card})




def create_card(request):
    cities = City.objects.all()
    cards = Cards.objects.all()
    categories = Category.objects.all()
    if request.POST:
        info = request.POST
        title = info.get('title')
        images = request.FILES.getlist('image')
        image = images[0] if images else None
        address = info.get('address')
        description = info.get('description')
        price = info.get('price')
        feedback = info.get('feedback')
        city_id = info.get('city')
        category_id = info.get('category')
        author = request.user
        city = City.objects.get(id=city_id) 
        category = Category.objects.get(id=category_id) 
        
        

        cards = Cards.objects.create(
            title = title,
            image = image,
            address = address,
            description = description,
            price = price,
            feedback = feedback,
            author = author,
            city = city,
            category = category
        )
        return redirect('main-page')

    return render(request,'desks/create_card.html',{'city':cities,'categories':categories,'cards':cards})


