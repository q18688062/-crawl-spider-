from django import template

register = template.Library()


@register.filter(is_safe=True)  #代表传入的是安全的不需要转义
def fil(bq, arg):  #最多两个参数
    print(arg)
    if isinstance(arg, str) or isinstance(arg, int):
        res = bq + str(arg)
    else:
        res = bq + str(arg.pic_name)

    return res