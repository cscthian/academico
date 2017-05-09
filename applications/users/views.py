# from django.core.urlresolvers import reverse_lazy, reverse
# # Autentificacion de usuario
# from django.contrib.auth import authenticate, login, logout

# from .models import User
# from .forms import LoginForm, UserForm


# class LogIn(FormView):
#     '''
#     Logeo del usuario
#     '''
#     template_name = 'users/login.html'
#     success_url = reverse_lazy('home_app:inicio')
#     form_class = LoginForm

#     def form_valid(self, form):
#         # Verfiamos si el usuario y contrasenha son correctos.
#         user = authenticate(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password']
#         )

#         if user is not None:
#             if user.is_active and user.type_user == '0':
#                 login(self.request, user)
#                 return HttpResponseRedirect(
#                     reverse(
#                         'home_app:inicio'
#                     )
#                 )
#              else:
#              	return HttpResponseRedirect(
#                     reverse(
#                         'user_app:login'
#                     )
#                 )


# class LogoutView(View):
#     """
#     cerrar sesion
#     """
#     url = '/auth/login/'

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return HttpResponseRedirect(
#             reverse(
#                 'users_app:login'
#             )
#         )