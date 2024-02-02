from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Profile, Review
from .forms import AddBooksForm, CheckOutForm
from django.utils.datastructures import MultiValueDictKeyError

books = Book.objects.all()

# Create your views here.
def addbooks(request):
    submitted = False
    if request.method == "POST":
        form = AddBooksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/userprofile/addbooks?submitted=True')
    else:
        form = AddBooksForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addbooks.html', {'form': form, 'submitted':submitted})

def dashboard(request):
    profiles = Profile.objects.all()
    books = Book.objects.all()
    current_user = request.user
    current_profile = profiles.filter(user=current_user)
    
    profile_genres=''

    for obj in current_profile:
        profile_genres = obj.fav_genres

    books_genres = []

    for book in books:
        x = book.genre.replace("[","")
        y = x.replace("]","")
        z = y.replace("'","")
        a = z.split(",")
        books_genres.append(a)
    
    profile_genres1=string_to_list(profile_genres)

    recs = []
    x=0

    for book in books:
        for genre1 in books_genres:
            if genre1 == string_to_list(book.genre):
                if common_els(genre1,profile_genres1):
                    x+=1
                    if book not in recs and x<=5:
                        recs.append(book)
                        

    return render(request, 'dashboard.html', {'profiles': profiles,'books':books,'recs':recs,})

def search_books(request):
    if request.method == "POST":
        try:
            searched = request.POST['searched']
        except MultiValueDictKeyError:
            searched = False
        return render(request, 'search_books.html', {'searched':searched})
    else:
        return render(request, 'search_books.html')

def common_els(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

def string_to_list(list):
    x = list.replace("[","")
    y = x.replace("]","")
    z = y.replace("'","")
    list = z.split(",")
    return list

def list_books(request):
    books_list = Book.objects.all()
    return render(request, 'list_books.html',{'books_list':books_list})

def bookprofile(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = Review.objects.all()

    x = book.genre.replace("[","")
    y = x.replace("]","")
    z = y.replace("'","")
    a = z.split(",")

    reviews_list = []

    for review in reviews:
        if book == review.book:
            reviews_list.append(review)

    submitted = False

    if request.method == "POST":
        form = CheckOutForm(request.POST)
        submitted = True
    else:
        form = CheckOutForm()
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'bookprofile.html',{'book':book,'reviews':reviews,'book_genres':a, 'reviews_list':reviews_list,'form':form,'submitted':submitted})