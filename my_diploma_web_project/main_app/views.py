from django.shortcuts import render


def main_view(request):
    context = {"russian_text": 'Здравствуйте, мои дорогие любители английского языка! '
                               'Я рада приветствовать вас на этом сайте. '
                               'Здесь вы можете найти много полезной информации, '
                               'касающейся изучения английского языка и методики его преподавания. '
                               'Есть много бесплатных материалов и тех, которые вы можете купить. '
                               'Я буду счастлива помочь вам улучшить ваши навыки и расширить знания английского языка, '
                               'разнообразить ваши уроки, если вы учитель. '
                               'Оставайтесь на связи и помните – совершенству нет предела!',
               "english_text": 'Hello, my dear English lovers! '
                               'I’m glad to welcome you at this site. '
                               'Here you can find much useful information concerning to '
                               'English studying and teaching methodic. '
                               'There are many free materials and those ones you can buy. '
                               'I’ll be happy to help you to improve your skills and widen your knowledge of English, '
                               'to vary your lessons if you’re a teacher. '
                               'Stay tune and remember – the sky is the limit!'
               }
    return render(request, 'main_app/main.html', context)
