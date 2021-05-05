from django import template

register = template.Library()
@register.filter(name='multiply')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):  # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') #  в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку

#@register.filter(name='censor')
#def censor():