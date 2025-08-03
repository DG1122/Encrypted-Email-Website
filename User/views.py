from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from django.http import JsonResponse
from datetime import datetime
from cryptography.fernet import Fernet
# Create your views here.

def Homepage(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    mail = tbl_mail.objects.filter(user_to=request.session["uid"],mail_status=0)
    for i in mail:
        count = tbl_wishlist.objects.filter(mail=i.id,user=request.session["uid"]).count()
        if count > 0:
            i.status = 1
        else:
            i.status = 0
    return render(request,'User/Homepage.html',{"mail":mail})


def Myprofile(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    return render(request,'User/Myprofile.html')
    
def Changepassword(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    user=tbl_user.objects.get(id=request.session['uid'])  
    if request.method =="POST":
        currentpass=request.POST.get("pas_current")
        newpass=request.POST.get("pass_new")
        confirmpass=request.POST.get("pass_confirm")
        userpass=user.user_password
        if currentpass==userpass:
            if newpass==confirmpass:
                if newpass==currentpass:
                    return render(request,"User/Changepassword.html",{"msg":"THE NEW PASSWORD MUST NOT BE SIMILAR TO THE OLD PASSWORD"})
                user.user_password=newpass
                user.save()
                return render(request,"User/Myprofile.html",{"msg":"PASSWORD CHANGED SUCCESSFULLY"})           
                return redirect("User:Myprofile") 
              
            else:
                return render(request,"User/Changepassword.html",{"msg":"PASSWORDS DOSEN'T MATCH"})
        else:
            return render(request,"User/Changepassword.html",{"msg":"Invalid Current Password"})
    else: 
        return render(request,'User/Changepassword.html')  


def Editprofile(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    user=tbl_user.objects.get(id=request.session['uid'])     #session id uid indicates currently logged in profile
    if request.method =="POST":
        user.user_name=request.POST.get("edit_name")
        emailcount=tbl_user.objects.filter(user_email=request.POST.get("edit_email")).count()
        if emailcount>0:
            return render(request,'User/Editprofile.html',{'user':user,'msg':"Already Added"})
        else:
            user.user_email=request.POST.get("edit_email")
        user.user_contact=request.POST.get("edit_numb")
        user.user_address=request.POST.get("edit_address")
        user.save()
        return redirect("User:Myprofile")
    else:
        return render(request,'User/Editprofile.html',{'user':user})   

def Myprofile(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/Myprofile.html',{'user':user})


def ajaxmessage(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    user = tbl_user.objects.get(user_email=request.GET.get("to"))
    fernet = Fernet(user.user_key.encode())
    encryptedtext = fernet.encrypt(request.GET.get("message").encode())
    tbl_mail.objects.create(
        user_from=tbl_user.objects.get(id=request.session["uid"]),
        user_to=tbl_user.objects.get(id=user.id),
        mail_subject=request.GET.get("subject"),
        mail_content=encryptedtext,
        mail_time=datetime.now()
    )
    return JsonResponse({'msg':"Mail Send Sucessfully.."})

def starred(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    mail = tbl_mail.objects.filter(tbl_wishlist__user=request.session["uid"],mail_status=0)
    return render(request,"User/Starred.html",{"mail":mail})

def ajaxaddfav(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    mailcount = tbl_wishlist.objects.filter(mail=request.GET.get("mailid"),user=request.session["uid"]).count()
    if mailcount > 0:
        tbl_wishlist.objects.get(mail=request.GET.get("mailid"),user=request.session["uid"]).delete()
        return JsonResponse({"msg":"Mail Remove From Favourite"})
    else:
        tbl_wishlist.objects.create(
            mail=tbl_mail.objects.get(id=request.GET.get("mailid")),
            user=tbl_user.objects.get(id=request.session["uid"])
        )
        return JsonResponse({"msg":"Mail Added To Favourite"})

def deletemail(request, id):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    msg = tbl_mail.objects.get(id=id)
    msg.mail_status = 1
    msg.save()
    return render(request,"User/Homepage.html", {"msg":"Mail Deleted"})

def send(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    mail = tbl_mail.objects.filter(user_from=request.session["uid"],mail_status__lte=1)
    return render(request,"User/Send.html",{"mail":mail})

def deletedmail(request):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    mail = tbl_mail.objects.filter(user_to=request.session["uid"],mail_status=1)
    return render(request,"User/DeletedMail.html",{"mail":mail})

def deletetrashmail(request, id):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    mail = tbl_mail.objects.get(id=id)
    mail.user_to = None
    mail.save()
    return render(request,"User/DeletedMail.html", {"msg":"Mail Deleted"})

def viewmail(request, id):
    if 'uid' not in request.session:
        return redirect("Guest:index")
    if request.method == "POST":
        fernet = Fernet(request.POST.get("txt_key").encode())
        mail = tbl_mail.objects.get(id=id)
        cont = fernet.decrypt(mail.mail_content).decode()
        return render(request, "User/ViewMail.html",{"mail":mail,"cont":cont})
    return render(request, "User/ViewMail.html")

def logout(request):
    del request.session["uid"]
    return redirect("Guest:index")