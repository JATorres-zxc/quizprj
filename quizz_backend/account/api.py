from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import *
from .serializer import *
from django.contrib.auth.forms import PasswordChangeForm


# for SignupView.vue
@api_view(['POST'])
@authentication_classes([]) # override the default since not authenticated dapat diba
@permission_classes([]) # override the default since not authenticated dapat diba
def signup(request):
    data = request.data
    
    form = SignupForm({ # SignupForm from forms.py
        'email':data.get('email'),
        'name':data.get('name'),
        'password1':data.get('password1'),
        'password2':data.get('password2'),
        
    })
    
    if form.is_valid():
        form.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


# magagamit sa profileview.vue and hindi lang ata don, brb to check
@api_view(['GET'])
def me(request):
    
    # will be used alot later
    return JsonResponse({ 
        'id':request.user.id,
        'name':request.user.name,
        'email':request.user.email,
        'avatar': request.user.get_avatar(),
    })
    

# will be used for editPRofikeView.vue
@api_view(['POST'])
def editprofile(request):
    user = request.user
    email = request.data.get('email') # since pwede i edit yung email here

    if User.objects.exclude(id=user.id).filter(email=email).exists(): # xheck if there's another user with the same email
        return JsonResponse({'message': 'email already exists'}) #if may same
    else:
        # if the email is unique, proceed with updating the user's profile
        
        # create a form instance with the request data and associate it with the current user
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
        
        serializer = UserSerializer(user)

        return JsonResponse({'message': 'information updated', 'user': serializer.data})
    

@api_view(['POST'])
def editPassword(request):
    user = request.user
    
    # create a form instance for changing the password with the request data and the current user
    form = PasswordChangeForm(data=request.POST, user=user) # import lang from django hindi sa forms.py galing to
    
    if form.is_valid():
        form.save()

        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)