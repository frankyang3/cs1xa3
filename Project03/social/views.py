from django.http import HttpResponse,HttpResponseNotFound,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User

from . import models

from django import forms

class UserInfoChangeForm(forms.Form):
    employment = forms.CharField(max_length=30)
    location = forms.CharField(max_length=50)
    birthday = forms.DateField()
    interest = forms.CharField(max_length=100)

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)


        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = []
        for post in models.Post.objects.all().order_by('-timestamp'):
            posts.append(post)
        if 'numPost' not in request.session:
            request.session['numPost'] = 1
        

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post

        context = { 'user_info' : user_info
                  , 'posts' : posts
                  , 'numPost' : request.session['numPost'] }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        if request.method == 'POST':
            u_form = UserInfoChangeForm(request.POST)
            pass_form = PasswordChangeForm(request.user, request.POST)
            if pass_form.is_valid():
                user = pass_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('social:account_view')
            else:
                messages.error(request, 'Please correct the error below.')
            if u_form.is_valid():
                newemployment=u_form.cleaned_data['employment']
                newlocation=u_form.cleaned_data['location']
                newbirthday=u_form.cleaned_data['birthday']
                newinterest=u_form.cleaned_data['interest']
                user_info.employment=newemployment
                user_info.location=newlocation
                user_info.birthday=newbirthday
                user_info.save()
                if models.Interest.objects.filter(label=newinterest).exists():
                    if not user_info.interests.filter(label=newinterest).exists():
                        i=models.Interest.objects.get(label=newinterest)
                        user_info.interests.add(i)
                else:
                    i=models.Interest.objects.create(label=newinterest)
                    user_info.interests.add(i)
                return redirect('social:account_view')
        else:
            u_form = UserInfoChangeForm(request.POST)
            pass_form = PasswordChangeForm(request.user)
        return render(request, 'account.djhtml', {'u_form': u_form, 'pass_form': pass_form, 'user_info' : user_info})
    else:
        return redirect('login:login_view')

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml

    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        all_people = []
        for user in models.UserInfo.objects.all():
            if (not (user == user_info) and user not in user_info.friends.all()):
                all_people.append(user)
        
        if('disPpl' not in request.session):
            request.session['disPpl'] = 1
        

        # TODO Objective 5: create a list of all friend requests to current user
        friend_requests = []
        for friend in models.FriendRequest.objects.filter(to_user=user_info):
            friend_requests.append(friend)
        context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests,
                    'disPpl' : request.session['disPpl'] }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
        ID = int(postIDReq[5:])
        post = models.Post.objects.get(id = ID)
        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user = request.user)
            if (not post.likes.filter(user = user_info.user).exists()):
                post.likes.add(user_info)
            out = {}
            return JsonResponse(out)
            # TODO Objective 10: update Post model entry to add user to likes field
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    if postContent is not None:
        if request.user.is_authenticated:

            # TODO Objective 8: Add a new entry to the Post model
            user_info = models.UserInfo.objects.get(user = request.user)
            message = models.Post.objects.create(owner = user_info, content = postContent)
            out = {}
            return JsonResponse(out)
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        posts = []
        for post in models.Post.objects.all():
            posts.append(post)
        if('numPost' not in request.session):
            request.session['numPost'] = 1

        sesh={'fail':True}
        if request.session['numPost'] < len(posts):
            request.session['numPost'] += 2
        return JsonResponse(sesh)

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        all_people = []
        for user in models.UserInfo.objects.all():
            if (not (user == user_info) and user not in user_info.friends.all()):
                all_people.append(user)
        if('disPpl' not in request.session):
            request.session['disPpl'] = 1

        sesh={'fail':True}
        if request.session['disPpl'] < len(all_people):
            request.session['disPpl'] += 2
        return JsonResponse(sesh)
    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an entry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID

    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            # TODO Objective 5: add new entry to FriendRequest
            to = User.objects.get(username=username)

            fr = models.UserInfo.objects.get(user=request.user)
            to_info = models.UserInfo.objects.get(user=to)
            if (not models.FriendRequest.objects.filter(from_user=fr, to_user=to_info).exists()):
                fr=models.FriendRequest.objects.create(from_user=fr, to_user=to_info)
                out = {}
                return JsonResponse(out)
            # return status='success'
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    print("HI")
    if data is not None:
        # TODO Objective 6: parse decision from data
        username= data[2:]
        if request.user.is_authenticated:
            fr = User.objects.get(username = username)

            to = models.UserInfo.objects.get(user = request.user)
            fr_info = models.UserInfo.objects.get(user = fr)

            #delete from requests
            models.FriendRequest.objects.filter(from_user = fr_info, to_user = to).delete()

            if (data[:2] == 'A-'):
                fr_info.friends.add(to)
                to.friends.add(fr_info)
                
            out = {}
            return JsonResponse(out)

        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
