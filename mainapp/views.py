from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import FeedbackForm


def main(request):
    return render(request, 'mainapp/index.html')


def about_us(request):
    return render(request, 'mainapp/pages/about_us.html')


def media(request):
    return render(request, 'mainapp/pages/page_media/media.html')


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("feedback"))
    else:
        form = FeedbackForm()

    content = {"form": form}
    return render(request, "mainapp/pages/feedback.html", content)


def first_album(request):
    return render(request, 'mainapp/pages/page_media/albums/first-album.html')


def second_album(request):
    return render(request, 'mainapp/pages/page_media/albums/second-album.html')


def third_album(request):
    return render(request, 'mainapp/pages/page_media/albums/third-album.html')


def four_album(request):
    return render(request, 'mainapp/pages/page_media/albums/four-album.html')


def five_album(request):
    return render(request, 'mainapp/pages/page_media/albums/five-album.html')


def six_album(request):
    return render(request, 'mainapp/pages/page_media/albums/six-album.html')


def seven_album(request):
    return render(request, 'mainapp/pages/page_media/albums/seven-album.html')


def eight_album(request):
    return render(request, 'mainapp/pages/page_media/albums/eight-album.html')


def post_1(request):
    return render(request, 'mainapp/posts/post_1.html')


def post_2(request):
    return render(request, 'mainapp/posts/post_2.html')


def post_3(request):
    return render(request, 'mainapp/posts/post_3.html')


def post_4(request):
    return render(request, 'mainapp/posts/post_4.html')


def post_5(request):
    return render(request, 'mainapp/posts/post_5.html')


def post_6(request):
    return render(request, 'mainapp/posts/post_6.html')


def post_7(request):
    return render(request, 'mainapp/posts/post_7.html')


def post_8(request):
    return render(request, 'mainapp/posts/post_8.html')


def post_9(request):
    return render(request, 'mainapp/posts/post_9.html')


def post_10(request):
    return render(request, 'mainapp/posts/post_10.html')


def post_11(request):
    return render(request, 'mainapp/posts/post_11.html')


def post_12(request):
    return render(request, 'mainapp/posts/post_12.html')


def post_13(request):
    return render(request, 'mainapp/posts/post_13.html')


def post_14(request):
    return render(request, 'mainapp/posts/post_14.html')


def post_15(request):
    return render(request, 'mainapp/posts/post_15.html')


def post_16(request):
    return render(request, 'mainapp/posts/post_16.html')


