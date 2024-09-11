from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, request
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from .models import *
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os
from datetime import datetime
from happytransformer import HappyTextToText
from happytransformer import TTSettings
from textblob import TextBlob
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Get the current date

# Create your views here.
from django.views.decorators.cache import cache_control
from docx import Document
brailleDict = {
  'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛',
  'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝',
  'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥',
  'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵','A': '⠠⠁', 'B': '⠠⠃', 
  'C': '⠠⠉', 'D': '⠠⠙', 'E': '⠠⠑', 'F': '⠠⠋', 'G': '⠠⠛','H': '⠠⠓', 'I': '⠠⠊',
  'J': '⠠⠚', 'K': '⠠⠅', 'L': '⠠⠇', 'M': '⠠⠍', 'N': '⠠⠝','O': '⠠⠕', 'P': '⠠⠏',
  'Q': '⠠⠟', 'R': '⠠⠗', 'S': '⠠⠎', 'T': '⠠⠞', 'U': '⠠⠥',
  'V': '⠠⠧', 'W': '⠠⠺', 'X': '⠠⠭', 'Y': '⠠⠽', 'Z': '⠠⠵',
  '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢', '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔',
  ' ': ' ', 
  '.': '⠲',
  ',': '⠂', 
  '!': '⠖', 
  '?': '⠦', 
  "'": '⠄' 
}



def convert_to_braille(text):
    return ''.join(brailleDict.get(char, char) for char in text)

def uppercase(data):
    return str(data).upper()


def check_text(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Correct spelling
    corrected_text = blob.correct()
    
    # Print the original and corrected text
    print("Original Text:", text)
    print("Corrected Text:", corrected_text)
    
    return(corrected_text)

@csrf_exempt
def grammar_check(request):
    if request.method == 'POST':
        data = request.POST.get('text', '')
        if not data:
            return JsonResponse({'error': 'No text provided'}, status=400)
        
        text = check_text(data)
        happy_tt = HappyTextToText("T5",  "prithivida/grammar_error_correcter_v1")
        settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)

        text = "gec: " + str(text)
        

        result = happy_tt.generate_text(text, args=settings)
        print('grammar_check: ' + str(result.text))
        
        return JsonResponse({'corrected_text': result.text})
    return JsonResponse({'error': 'Invalid request method'}, status=405)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials!")
    return render(request, 'login.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        first_name =uppercase(request.POST.get('first_name')) 
        last_name = uppercase(request.POST.get('last_name'))
        email = request.POST.get('email')
        username = request.POST.get('username')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')

        email_check =  User.objects.filter(email = email).count()
        fname_check =  User.objects.filter(first_name = first_name,last_name = last_name).count()
        username_check = User.objects.filter(username = username).count()
        if email_check > 0:
            messages.error(request,'Email Already Exists')
        elif fname_check>0:
            messages.error(request,'Your Fullname Already Exists')
        elif username_check > 0:
            messages.error(request,'Username Already Exists, Try Another')
        elif pw1 != pw2:
            messages.error(request,'Passwords Not Equal')

        else:

            try:
                validate_password(pw1)
                user = User.objects.create_user(username=username, email=email, password=pw1, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request,'Registered Successfully')
                return redirect('login')
            except ValidationError as e:
                # Handle the validation error (e.g., log it, display a message)
                messages.error(request, f'Invalid: {", ".join(e.messages)}')

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username
        }
        return render(request, "register.html", context)
    return render(request, 'register.html')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        braille_infos_count = BrailleInfo.objects.filter(user_id=user_id).count()
        activity_history = ActivityHistory.objects.filter(user_id=user_id).order_by('-date_log')

        context = {
            'braille_infos_count': braille_infos_count,
            'activity_history':activity_history
        }
    return render(request, 'dashboard.html',context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def tutorial(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        braille_infos_count = BrailleInfo.objects.filter(user_id=user_id).count()
        activity_history = ActivityHistory.objects.filter(user_id=user_id).order_by('-date_log')

        context = {
            'braille_infos_count': braille_infos_count,
            'activity_history':activity_history
        }
    return render(request, 'tutorial.html',context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def create_braille(request):
    current_date = datetime.now().strftime('%Y%m%d_%H%M%S')  # Format the date as YYYYMMDD
    if request.user.is_authenticated:
       if request.method == 'POST':
            title = request.POST.get('title')
            user_id = request.user.id
            braille_draft = request.POST.get('braille_draft')
            if (braille_draft.strip() == '' or title.strip() == ''):
                messages.error(request, 'Invalid content!')
                return redirect('create_braille')
            else:
                filename = f'{request.user.id}_{title}_{current_date}.docx'
                braille_text = convert_to_braille(braille_draft)
                braille_instance = BrailleInfo.objects.create(
                        user=request.user,
                        title=title,
                        braille_draft=braille_draft,
                        braille_text=braille_text,
                        filename = filename
                    )
                created_id = braille_instance.id
                # Ensure the directory exists
                # documents_dir = 'static/documents'
                # if not os.path.exists(documents_dir):
                #     os.makedirs(documents_dir)

                # document = Document()
                # document.add_heading(title, level=1)
                # document.add_paragraph(braille_text)
                # document.add_paragraph(braille_draft)

                # file_path = os.path.join('static/documents', filename)
                # document.save(file_path)
                activity_history = ActivityHistory(user_id = user_id,activity_log="Created a New Braille File(File # " +str(created_id) + ")")
                activity_history.save()
                messages.success(request, 'Braille Successfully Created!')
                # return redirect('download_braille', file_name= filename)
                return redirect('create_braille')
       
    return render(request, 'create_braille.html')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def view_braille(request):
    user_id = request.user.id
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_type = request.POST.get('form_type')
            if form_type == 'view_braille':
                filename = request.POST.get('filename')
                documents_dir = 'static/documents'

                if not os.path.exists(documents_dir):
                    os.makedirs(documents_dir)

                return redirect('download_braille', file_name= filename) 
        braille_infos = BrailleInfo.objects.filter(user_id=user_id)
        context = {'braille_infos': braille_infos}
    else: 
        return redirect('login')
    return render(request, 'view_braille.html',context)


@login_required(login_url='login')
def download_braille(request, file_name):
    file_path = os.path.join('static/documents', file_name)
    with open(file_path, 'rb') as doc_file:
        response = HttpResponse(doc_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def archives(request):

    return render(request, 'archives.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def report(request):

    return render(request, 'report.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def shared(request):

    return render(request, 'shared.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def account_settings(request):
    if request.user.is_authenticated:
       if request.method == 'POST':
            user_id = request.user.id
            old_password = request.POST.get('old_password')
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')
            if not request.user.check_password(old_password):
                    messages.error(request, 'Old password is incorrect.')
                    return redirect('account_settings')
            # Check if new passwords match
            if new_password1 != new_password2:
                messages.error(request, 'New passwords do not match.')
                return redirect('account_settings')
            
            # Update user password
            request.user.set_password(new_password1)
            request.user.save()

            # save log every password change
            activity_history = ActivityHistory(user_id = user_id,activity_log='Password Changed')
            activity_history.save()
            # Update session to avoid auto-logout
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password changed successfully.')
            return redirect('logout_user')
       
    else:
         return redirect('login')
    return render(request, 'account_settings.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
  logout(request)
  return redirect("login")