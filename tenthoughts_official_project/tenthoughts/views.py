from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tenthoughts.models import SubmitedArticles, UserArticles

from tenthoughts.models import UserProf, Article, Group
from tenthoughts.forms import UserForm, UserProfileForm, ArticleForm, GroupSelectForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
import json

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')



@login_required
def follow(request, client):

    user_profile = UserProf.objects.get(user=request.user)
    follow_user = User.objects.get(username=client)
    follow_userprof = UserProf.objects.get(user=follow_user)

    following_list = user_profile.following.split(',')

    if client in following_list:
        return HttpResponseRedirect('/followFriends')

    else:
        user_profile.following = user_profile.following + ',' + client
        user_profile.save()
        follow_userprof.followers = follow_userprof.followers + ',' + user_profile.user.username
        follow_userprof.save()

        return HttpResponseRedirect('/followFriends')



@login_required
def register_follow(request, client):

    user_profile = UserProf.objects.get(user=request.user)
    follow_user = User.objects.get(username=client)
    follow_userprof = UserProf.objects.get(user=follow_user)

    following_list = user_profile.following.split(',')

    if client in following_list:
        return HttpResponseRedirect('/register_followers')

    else:
        user_profile.following = user_profile.following + ',' + client
        user_profile.save()
        follow_userprof.followers = follow_userprof.followers + ',' + user_profile.user.username
        follow_userprof.save()

        return HttpResponseRedirect('/register_followers')





@login_required
def unfollow(request, client):

    user_profile = UserProf.objects.get(user=request.user)
    following_user = User.objects.get(username=client)
    following_userprof = UserProf.objects.get(user=following_user)

    following_list = user_profile.following.split(',')

    if client in following_list:
        following_list.remove(client)
        following_list_new=",".join(following_list)
        user_profile.following = following_list_new
        user_profile.save()

        follower_list = following_userprof.followers.split(',')
        follower_list.remove(user_profile.user.username)
        follower_list_new=",".join(follower_list)
        following_userprof.followers = follower_list_new
        following_userprof.save()

        return HttpResponseRedirect('/followers')

    else:
        return HttpResponseRedirect('/followers')




def community(request, bschool):
    context_dict={}

    try:
        clientPic = UserProf.objects.get(user=request.user)
        profilepic = request.user.first_name
        bschool = Group.objects.get(name=bschool)
        context_dict['bschool_name'] = bschool.name

        thismember = request.user.username
        following_list = UserProf.objects.values_list('user').filter(followers__contains=thismember)

        members = UserProf.objects.filter(groups=bschool.name).exclude(user__in=following_list).order_by('user__last_name', 'user__first_name')

        client = UserProf.objects.get(user=request.user)

        context_dict['num_followers'] = client.num_followers()
        context_dict['num_following'] = client.num_following()
        context_dict['members'] = members
        context_dict['bschool'] = bschool
        context_dict['logo'] = "10THOUGHTS"
        context_dict['headline'] =  "FOLLOW FRIENDS"
        context_dict['profilepic'] = profilepic
        context_dict['clientPic'] = clientPic

    except Group.DoesNotExist:
        pass

    return render(request, 'tenthoughts/community.html', context_dict)




def submitArticle(request):
    profilepic = request.user.first_name
    client = UserProf.objects.get(user=request.user)
    clientPic = UserProf.objects.get(user=request.user)

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        article = form.save(commit=False)

        if form.is_valid():
            article.submitter = UserProf.objects.get(user=request.user)
            article.views = 0
            article.submission_date = datetime.now()
            article.save()
            return HttpResponseRedirect('/home')


        else:
            print(form.errors)

    else:
        form = ArticleForm()

    context = RequestContext(request)

    context_dict = {'clientPic':clientPic,'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(),'form':form, 'boldmessage': "This is the Submit Articles Page", 'logo':"10THOUGHTS", 'content' : "This is the SUBMIT ARTICLES PAGE", 'headline': "SUBMIT ARTICLES"}

    return render_to_response('tenthoughts/submit_articles_10.html', context_dict, context)





def register_followers(request):
    context = RequestContext(request)

    try:
        allmembers = UserProf.objects.all()
        member = request.user.username
        following_list = UserProf.objects.values_list('user').filter(followers__contains=member)

        notFollowMembers = UserProf.objects.exclude(user__in=following_list)

    except Group.DoesNotExist:
        pass

    context_dict = {'members': notFollowMembers, 'boldmessage': "This is the About Page", 'logo':"10THOUGHTS", 'content' : "This is the ABOUT PAGE", 'headline': "ABOUT"}

    return render_to_response('tenthoughts/register_followers.html', context_dict, context)




def register_about(request):
    context = RequestContext(request)

    context_dict = {'boldmessage': "This is the About Page", 'logo':"10THOUGHTS", 'content' : "This is the ABOUT PAGE", 'headline': "ABOUT"}

    return render_to_response('tenthoughts/register_about.html', context_dict, context)



def instructions(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    client = UserProf.objects.get(user=request.user)

    context_dict = {'clientPic':clientPic,'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(), 'boldmessage': "This is the About Page", 'logo':"10THOUGHTS", 'content' : "This is the ABOUT PAGE"}



    return render_to_response('tenthoughts/instructions.html', context_dict, context)



def lastWeekFeaturedArticles(request):
    context = RequestContext(request)

    context_dict = {'boldmessage': "This is the About Page", 'logo':"10THOUGHTS", 'content' : "This is the ABOUT PAGE", 'headline': "ABOUT"}

    return render_to_response('tenthoughts/10ThoughtsFeaturedArticles.html', context_dict, context)



def retreivePassword(request):
    context = RequestContext(request)

    context_dict = {'boldmessage': "This is the About Page", 'logo':"10THOUGHTS", 'content' : "This is the ABOUT PAGE", 'headline': "ABOUT"}

    return render_to_response('tenthoughts/retreivePassword.html', context_dict, context)

def register(request):
    registered = False
    group_form = GroupSelectForm()

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        group_form = GroupSelectForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and group_form.is_valid():

            if user_form.cleaned_data['password'] != user_form.cleaned_data['password_again']:
                return HttpResponse("The passwords entered did not match, please try again")

            if user_form.cleaned_data['email'] != user_form.cleaned_data['confirm_email']:
                return HttpResponse("The emails entered did not match, please try again")

            user = user_form.save()
            user.set_password(user.password)
            user.email=user.email.lower()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            #add group to profile and update group member list
            bschool = group_form.cleaned_data['bschool']
            if bschool.name != 'None':
                profile.groups = bschool.name
                bschool.members = bschool.members + ',' + user.username
            else:
                profile.groups = ''

            profile.save()
            bschool.save()
            registered = True


        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'tenthoughts/register.html',
            {'user_form': user_form,  'profile_form': profile_form,
             'group_form': group_form, 'registered': registered})




def user_login(request):
    # Get the context from the request.

    if request.method == 'POST':
        email = request.POST['Email'].lower()
        password = request.POST['password']

        find_user = User.objects.filter(email=email)

        if find_user:

            user = authenticate(username=find_user[0].username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home')
                else:
                    return HttpResponse("Your 10thoughts account is disabled.")
            else:
                #print("Invalid login details: {0}, {1}".format(email, password))
                return HttpResponse("Invalid login details supplied.")
                return HttpResponseRedirect('/login')

        else:
            #code to generate error for template goes here
            return HttpResponse("That Email address is not registered")
            return HttpResponseRedirect('/login')

    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'tenthoughts/login.html', {})


def button_user_login(request):
    # Get the context from the request.

    if request.method == 'POST':
        email = request.POST['Email'].lower()
        password = request.POST['password']

        find_user = User.objects.filter(email=email)

        if find_user:

            user = authenticate(username=find_user[0].username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/loginSuccess')
                else:
                    return HttpResponse("Your 10thoughts account is disabled.")
            else:
                #print("Invalid login details: {0}, {1}".format(email, password))
                return HttpResponse("Invalid login details supplied.")
                return HttpResponseRedirect('/submitArticles')

        else:
            #code to generate error for template goes here
            return HttpResponse("That Email address is not registered")
            return HttpResponseRedirect('/login')

    else:
        return render(request, 'tenthoughts/button_login.html', {})





def index(request):

    context = RequestContext(request)

    context_dict = {'boldmessage': "I am bold font from the context", 'logo':"10THOUGHTS", 'content' : "This is the HOME PAGE", 'headline': "READ ARTICLES RECOMMENDED BY FRIENDS", 'headlineparagraph': "10THOUGHTS SENDS YOU 10ARTICLES ONCE A WEEK THAT ARE RECOMMENDED BY FRIENDS, PEERS AND COMMUNITIES YOU SELECT"}

    return render_to_response('tenthoughts/landing.html', context_dict, context)




def home(request):
    context = RequestContext(request)

    profilepic = request.user.first_name
    myArticles = False

    userarticles_info = UserArticles.objects.filter(client_name = request.user.username)
    client = UserProf.objects.get(user=request.user)

    if userarticles_info.exists():
        myArticles = True

    userarticles_data = {
    "userarticles_detail" : userarticles_info
    }

    context_dict = {'client': client, 'myArticles':myArticles, 'profilepic':profilepic, 'num_followers':client.num_followers(), 'num_following':client.num_following(),'boldmessage': "I am bold font from the context", 'logo':"10THOUGHTS", 'content' : "This is the HOME PAGE", 'headline': "HOME", 'userarticles_detail' : userarticles_info}

    print(userarticles_info)

    return render_to_response('tenthoughts/home.html', context_dict, context)




def about(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    client = UserProf.objects.get(user=request.user)

    context_dict = {'clientPic': clientPic, 'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(), 'boldmessage': "This is the About Page", 'logo':"10THOUGHTS", 'content' : "This is the ABOUT PAGE", 'headline': "ABOUT"}

    return render_to_response('tenthoughts/about.html', context_dict, context)




def improvements(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    client = UserProf.objects.get(user=request.user)

    context_dict = {'clientPic':clientPic,'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(), 'boldmessage': "This is the About Page", 'logo':"10THOUGHTS", 'content' : "This is the ABOUT PAGE"}

    return render_to_response('tenthoughts/improvements.html', context_dict, context)




def blog(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    client = UserProf.objects.get(user=request.user)

    context_dict = {'clientPic':clientPic,'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(), 'boldmessage': "This is the About Page", 'logo':"10THOUGHTS"}

    return render_to_response('tenthoughts/blog.html', context_dict, context)




def accountPreferences(request):
    context = RequestContext(request)

    profilepic = request.user.first_name
    clientPic = UserProf.objects.get(user=request.user)

    client = UserProf.objects.get(user=request.user)
    context_dict = {'clientPic':clientPic,'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(), 'boldmessage': "This is the About Page", 'logo':"10THOUGHTS"}

    return render_to_response('tenthoughts/accountPreferences.html', context_dict, context)




def followers(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    client = UserProf.objects.get(user=request.user)
    #context_dict['num_followers'] = client.num_followers()
    #context_dict['num_following'] = client.num_following()

    #Profile = UserProf.objects.get(user=request.user)
    member = request.user.username
    follower_list = UserProf.objects.filter(following__contains=member).order_by('user__last_name', 'user__first_name')
    following_list = UserProf.objects.filter(followers__contains=member).order_by('user__last_name', 'user__first_name')


    context_dict = {'clientPic':clientPic,'profilepic' : profilepic, 'num_followers': client.num_followers(), 'num_following':client.num_following(), 'follower_list' : follower_list, 'following_list' : following_list, 'boldmessage': "This is the Followers Page", 'logo':"10THOUGHTS", 'content' : "This is the FOLLOWERS PAGE", 'headline': "FOLLOWERS"}

    return render_to_response('tenthoughts/followers.html', context_dict, context)




def followFriends(request):
    context = RequestContext(request)

    try:
        clientPic = UserProf.objects.get(user=request.user)
        profilepic = request.user.first_name
        allmembers = UserProf.objects.all()
        member = request.user.username
        following_list = UserProf.objects.values_list('user').filter(followers__contains=member)
        #fList = following_list.objects.all().values_list(username)
        client = UserProf.objects.get(user=request.user)

        notFollowMembers = UserProf.objects.exclude(user__in=following_list).order_by('user__last_name', 'user__first_name')


    except Group.DoesNotExist:
        pass

        print(allmembers)
        print(member)
        print(following_list)

    context_dict = {'clientPic':clientPic, 'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(),'members' : notFollowMembers, 'following_list' : following_list,  'boldmessage': "This is the Followers Page", 'logo':"10THOUGHTS", 'content' : "This is the FOLLOWERS PAGE", 'headline': "FOLLOW FRIENDS"}

    return render_to_response('tenthoughts/followFriends.html', context_dict, context)





def submitArticles(request):
    profilepic = request.user.first_name
    client = UserProf.objects.get(user=request.user)
    clientPic = UserProf.objects.get(user=request.user)

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        article = form.save(commit=False)

        if form.is_valid():
            article.submitter = UserProf.objects.get(user=request.user)
            article.views = 0
            article.submission_date = datetime.now()
            article.save()
            return HttpResponseRedirect('/home')


        else:
            print(form.errors)

    else:
        form = ArticleForm()

    context = RequestContext(request)

    context_dict = {'clientPic':clientPic,'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(),'form':form, 'boldmessage': "This is the Submit Articles Page", 'logo':"10THOUGHTS", 'content' : "This is the SUBMIT ARTICLES PAGE", 'headline': "SUBMIT ARTICLES"}

    return render_to_response('tenthoughts/submitArticlesButton.html', context_dict, context)





def featuredArticles(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    client = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    context_dict = {'clientPic':clientPic, 'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(),'boldmessage': "This is the Featured Articles Page", 'logo':"10THOUGHTS", 'content' : "This is the FEATURED ARTICLES PAGE", 'headline': "FEATURED ARTICLES"}

    return render_to_response('tenthoughts/featured_articles.html', context_dict, context)




def dardenFeaturedArticles(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    client = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    context_dict = {'clientPic':clientPic, 'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(),'boldmessage': "This is the Featured Articles Page", 'logo':"10THOUGHTS", 'content' : "This is the FEATURED ARTICLES PAGE", 'headline': "DARDEN COMMUNITY FEATURED ARTICLES"}

    return render_to_response('tenthoughts/darden_featured_articles.html', context_dict, context)




def yaleFeaturedArticles(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    client = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    context_dict = {'clientPic':clientPic,'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(),'boldmessage': "This is the Featured Articles Page", 'logo':"10THOUGHTS", 'content' : "This is the FEATURED ARTICLES PAGE", 'headline': "YALE - SOM COMMUNITY FEATURED ARTICLES"}

    return render_to_response('tenthoughts/yale_featured_articles.html', context_dict, context)




def referFriend(request):
    context = RequestContext(request)

    clientPic = UserProf.objects.get(user=request.user)
    client = UserProf.objects.get(user=request.user)
    profilepic = request.user.first_name

    context_dict = {'clientPic':clientPic, 'profilepic' : profilepic,'num_followers':client.num_followers(), 'num_following':client.num_following(),'boldmessage': "This is the Refer A Friend Page", 'logo':"10THOUGHTS", 'content' : "This is the REFER A FRIEND PAGE", 'headline': "REFER A FRIEND"}

    return render_to_response('tenthoughts/refer.html', context_dict, context)




def buttontest(request):
    context_dict={}
    return render(request, 'tenthoughts/buttontest.html', context_dict)

def loginSuccess(request):
    context_dict={}
    return render(request, 'tenthoughts/loginSuccess.html', context_dict)




@login_required
def remote_submit(request, article_string):
    if request.user.is_authenticated():
        new_url, serpator, new_title = article_string.partition('&title=')
        new_url = new_url[4:]
        user_profile = UserProf.objects.get(user=request.user)
        new_article = Article()
        new_article.url = new_url
        new_article.title = new_title
        new_article.submitter = user_profile
        new_article.submission_date = datetime.now()
        new_article.save()
        context_dict = {'url':new_url, 'title':new_title}

    else:
        return HttpResponseRedirect("/login")

    return render(request, 'tenthoughts/remote_submit.html', context_dict)


