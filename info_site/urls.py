from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^about_us/$', mainapp.about_us, name='about_us'),
    re_path(r'^media/$', mainapp.media, name='media'),
    re_path(r'^feedback/$', mainapp.feedback, name='feedback'),
    re_path(r'^media/first_album/$', mainapp.first_album, name='first_album'),
    re_path(r'^media/second_album/$', mainapp.second_album, name='second_album'),
    re_path(r'^media/third_album/$', mainapp.third_album, name='third_album'),
    re_path(r'^media/four_album/$', mainapp.four_album, name='four_album'),
    re_path(r'^media/five_album/$', mainapp.five_album, name='five_album'),
    re_path(r'^media/six_album/$', mainapp.six_album, name='six_album'),
    re_path(r'^media/seven_album/$', mainapp.seven_album, name='seven_album'),
    re_path(r'^media/eight_album/$', mainapp.eight_album, name='eight_album'),
    re_path(r'^posts/post_1/$', mainapp.post_1, name='post_1'),
    re_path(r'^posts/post_2/$', mainapp.post_2, name='post_2'),
    re_path(r'^posts/post_3/$', mainapp.post_3, name='post_3'),
    re_path(r'^posts/post_4/$', mainapp.post_4, name='post_4'),
    re_path(r'^posts/post_5/$', mainapp.post_5, name='post_5'),
    re_path(r'^posts/post_6/$', mainapp.post_6, name='post_6'),
    re_path(r'^posts/post_7/$', mainapp.post_7, name='post_7'),
    re_path(r'^posts/post_8/$', mainapp.post_8, name='post_8'),
    re_path(r'^posts/post_9/$', mainapp.post_9, name='post_9'),
    re_path(r'^posts/post_10/$', mainapp.post_10, name='post_10'),
    re_path(r'^posts/post_11/$', mainapp.post_11, name='post_11'),
    re_path(r'^posts/post_12/$', mainapp.post_12, name='post_12'),
    re_path(r'^posts/post_13/$', mainapp.post_13, name='post_13'),
    re_path(r'^posts/post_14/$', mainapp.post_14, name='post_14'),
    re_path(r'^posts/post_15/$', mainapp.post_15, name='post_15'),
    re_path(r'^posts/post_16/$', mainapp.post_16, name='post_16'),

]
