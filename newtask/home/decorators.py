from .models import User

def user_task(function):
    def wrap(request, *args, **kwargs):
        entry = request.path
        print('iiiiiiiiiii',entry)
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap