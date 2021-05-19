from django.shortcuts import render,redirect
from login.models import User_Info,Time_Data,Friend
from django.contrib import messages
from django.http import JsonResponse
import datetime, time

session_start = None
cur_usr = None

def Index(request):
    return render(request, 'base.html')

def Login(request):
    global session_start
    if request.method == 'POST':
        usr = request.POST["username"]
        pas = request.POST["pass"]
        session_start = datetime.datetime.now()
        if User_Info.objects.filter(username = usr, password = pas).exists():
            user = User_Info.objects.get(username=usr)
            following = Friend.objects.filter(left_user=usr)
            followers = Friend.objects.filter(right_user=usr)
            return render(request,'home.html', {"use": user, "followers":followers, "following":following})
        else :
            messages.error(request,'Invalid Credentials !')
            return redirect('/')

def Logout(request):
    usr = request.POST["log_user"]
    session_end = datetime.datetime.now()+datetime.timedelta(hours=5,minutes=30)
    messages.error(request,'Thank You !')
    time = Time_Data(username=usr,duration=session_start+datetime.timedelta(hours=5,minutes=30),end_duration=session_end)
    time.save()
    return redirect('/')

def SignUp(request):
    return render(request,"signup.html")

def Transfer(request):
    global session_start
    fir = request.POST["firstname"]
    las = request.POST["lastname"]
    usr = request.POST["username"]
    mid = request.POST["mailid"]
    dob = request.POST["dob"]
    pas = request.POST["pass"]
    desc = request.POST["desc"]

    if User_Info.objects.filter(username = usr).exists():
        messages.error(request,'Username Taken !')
        return redirect('SignUp')
    elif User_Info.objects.filter(email = mid).exists():
        messages.error(request,'Email_id already exists !')
        return redirect('SignUp')
    else:
        user = User_Info(username=usr ,password=pas ,first_name=fir ,last_name=las ,email=mid ,dob=dob ,des=desc ,joined=datetime.datetime.now()+datetime.timedelta(hours=5,minutes=30))
        following = Friend.objects.filter(left_user=usr)
        followers = Friend.objects.filter(right_user=usr)
        session_start = datetime.datetime.now()
        user.save()
        return render(request,'home.html', {"use": user, "followers":followers, "following":following})

def Update(request):
    fir = request.POST["first_name"]
    las = request.POST["last_name"]
    mid = request.POST["mailid"]
    usr = request.POST["username"]
    pas = request.POST["pass"]
    desc = request.POST["desc"]
    if User_Info.objects.filter(email = mid).exists():
        messages.error(request,'Email_id already exists !')
    user = User_Info.objects.get(username=usr)
    user.first_name = fir
    user.last_name = las
    user.email = mid
    user.des = desc
    user.password = pas
    user.save()
    following = Friend.objects.filter(left_user=usr)
    followers = Friend.objects.filter(right_user=usr)
    return render(request,'home.html', {"use": user, "followers":followers, "following":following})

def filter_friends(usr):
    users = User_Info.objects.exclude(username=usr)
    lst = []
    if Friend.objects.filter(left_user = usr).exists():
        friends = Friend.objects.filter(left_user=usr)
        for user in users:
            flag=1
            x = user.username
            for friend in friends:
                if user.username == friend.right_user:
                    flag=0
                    break
            if flag:
                lst.append(x)
    else:
        for use in users:
            lst.append(use.username)
    return lst

def Friends(request):
    usr = request.POST["user"]
    user = User_Info.objects.get(username=usr)
    friends = Friend.objects.filter(left_user=usr)
    all_users = User_Info.objects.exclude(username=usr)
    usrs = filter_friends(usr)
    return render(request, "friends.html", {"use": user, "users":usrs, "friends":friends, "all":all_users})

def Change_Friends(request):
    usr = request.POST["user"]
    operation = request.POST["operation"]
    uid = request.POST["uid"]
    user = User_Info.objects.get(username=usr)
    all_users = User_Info.objects.exclude(username=usr)
    
    if operation == 'add':
        data = Friend(left_user=usr, right_user=uid)
        data.save()
    elif operation == 'remove':
        data = Friend.objects.get(left_user=usr, right_user=uid)
        data.delete()
    
    friends = Friend.objects.filter(left_user=usr)
    usrs = filter_friends(usr)
    return render(request, "friends.html", {"use": user, "users":usrs, "friends":friends, "all":all_users})

def Return(request):
    usr = request.POST["log_user"]
    user = User_Info.objects.get(username=usr)
    following = Friend.objects.filter(left_user=usr)
    followers = Friend.objects.filter(right_user=usr)
    return render(request,'home.html', {"use": user, "followers":followers, "following":following})

def Dash(request):
    global cur_usr
    usr = request.POST.get("user",False)
    cur_usr = usr
    user = User_Info.objects.get(username=usr)
    count = User_Info.objects.exclude().count()
    following = Friend.objects.filter(left_user=usr)
    followers = Friend.objects.filter(right_user=usr)
    return render(request, "dash.html", {"use": user, "count": count, "followers":followers, "following":following})

def usage_chart(request):
    usr1 = Time_Data.objects.filter(username = cur_usr)
    y = []
    label = []
    dates = []
    for data in usr1:
        cur = data.duration.strftime("%d-%m-%Y")
        if cur not in dates:
            dates.append(cur)
            usage = 0
            for obj in usr1:
                if obj.duration.strftime("%d-%m-%Y") == cur:
                    minutes = round((obj.end_duration - obj.duration).total_seconds()/60, 2)
                    usage = usage + minutes
        else:
            continue
        y.append(usage)
        label.append(cur)
    
    return JsonResponse(data={
        'labels': label,
        'data': y,
    })