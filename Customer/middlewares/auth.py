# from asgiref.sync import iscoroutinefunction
# from django.utils.decorators import sync_and_async_middleware
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# @sync_and_async_middleware
# def auth_middleware(get_response):
#     # One-time configuration and initialization goes here.
#     if iscoroutinefunction(get_response):

#         async def middleware(request):
#             # Do something here!
#             response = await get_response(request)
#             return response

#     else:

#         def middleware(request):
#             # Do something here!
#             response = get_response(request)
#             return response

#     return middleware



def auth_middleware(get_response):
    # One-time configuration and initialization goes here.
   

    def middleware(request):
        if not request.session.get('user'):
            return redirect('login')
       
        response = get_response(request)
        return response

    return middleware