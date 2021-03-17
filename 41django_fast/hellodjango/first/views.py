from random import sample

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
HttpResponse
from django.http import HttpResponse
"""
# def show_index(request):
#     # return HttpResponse("<h1>你好，Django!</h1>")
#     fruits = [
#         'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
#         'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
#     ]
#     fruits_today = sample(fruits, 3)
#     content = '<h1>今日推荐的水果是：</h1>'
#     content += '<hr>'
#     content += '<ul>'
#
#     for fruit in fruits_today:
#         content += f'<li>{fruit}</li>'
#
#     content += '</ul>'
#
#     return HttpResponse(content)


"""
使用模板渲染
from django.shortcuts import render
"""


def show_index(request):
    # return HttpResponse("<h1>你好，Django!</h1>")
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    fruits_today = sample(fruits, 3)
    # content = '<h1>今日推荐的水果是：</h1>'
    # content += '<hr>'
    # content += '<ul>'
    #
    # for fruit in fruits_today:
    #     content += f'<li>{fruit}</li>'
    #
    # content += '</ul>'

    # return HttpResponse(content)
    content = {
        'fruits_today': fruits_today
    }
    return render(request, 'index.html', context=content)
