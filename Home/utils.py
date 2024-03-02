from django.utils.text import slugify
import string,random

def random_string_generator(N):
    res = ''.join(random.choices(string.ascii_uppercase, k = N))
    return res



def slug_generator(text):
    from Home.models import Blog
    slug=slugify(text)
    if Blog.objects.filter(slug=slug).exists():
        text=text+random_string_generator(5)
        return slug_generator(text)
    return slug