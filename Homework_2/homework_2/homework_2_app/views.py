from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """
    <h1>Главная страница.</h1>
    <p>Это главная страница домашнего задания к 1-му семинару.</p>
    """
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Привет, меня зовут Анатолий</h1>
    <p>Я создаю свой первый сайт на Django.<br/>Посмотрите на мой сайт.</p>
    """
    return HttpResponse(html)
