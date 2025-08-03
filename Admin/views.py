from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
# views.py


    


def district(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        districtcount=tbl_district.objects.filter(district_name=request.POST.get("txt_district")).count()
        if districtcount>0:
            return render(request,'Admin/district.html',{"districtData":data,'msg':"Already Added"})
        else:
            tbl_district.objects.create(district_name=request.POST.get("txt_district"))
            return render(request,'Admin/district.html',{"districtData":data})
    else:
        return render(request,'Admin/district.html',{"districtData":data})  

        

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:district")  

def UpdateDistrict(request,uid):
    dis=tbl_district.objects.get(id=uid)
    if request.method=="POST":
        dis.district_name=request.POST.get("txt_district")
        dis.save()
        return redirect("Admin:district")  
    else:
        return render(request,"Admin/District.html",{"disdata":dis})

def category(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("txt_category"))
        return render(request,'Admin/category.html',{"categoryData":data})
    else:
        return render(request,'Admin/category.html',{"categoryData":data})

def UpdateCategory(request,uid):
    dis=tbl_category.objects.get(id=uid)
    if request.method=="POST":
        dis.category_name=request.POST.get("txt_category")
        dis.save()
        return redirect("Admin:category")  
    else:
        return render(request,"Admin/category.html",{"disdata":dis})


def DeleteCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("Admin:category")          

def details(request):
    data=tbl_adminreg.objects.all()

    if request.method=="POST":
        tbl_adminreg.objects.create(details_name=request.POST.get("txt_details"),details_email=request.POST.get("email_details"),details_password=request.POST.get("password_details"))


        return render(request,'Admin/details.html',{"DetailsData":data})
    else:
        return render(request,'Admin/details.html',{"DetailsData":data})

def DeleteDetails(request,did):
    tbl_adminreg.objects.get(id=did).delete()
    return redirect("Admin:details")  

def UpdateDetails(request,uid):
    dis=tbl_adminreg.objects.get(id=uid)
    if request.method=="POST":
        dis.details_name=request.POST.get("txt_details")
        dis.save()
        return redirect("Admin:details")  
    else:
        return render(request,"Admin/details.html",{"disdata":dis})



def Brand(request):
    data=tbl_Brand.objects.all()
    if request.method=="POST":
        tbl_Brand.objects.create(Brand_Name=request.POST.get("brand_txt"))
        return render(request,'Admin/Brand.html',{"BrandData":data})
    else:
        return render(request,'Admin/Brand.html',{"BrandData":data})

def DeleteBrand(request,did):
    tbl_Brand.objects.get(id=did).delete()
    return redirect("Admin:Brand") 

def Place(request):
    districtdata=tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placename=request.POST.get("place_name")
        disid=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placename,district=disid)  
        return render(request,'Admin/Place.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Place.html',{"PlaceData":data,'dis':districtdata})

def Subcategory(request):
    categorydata=tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        categoryname=request.POST.get("sub_name")
        catid=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=categoryname,category=catid)  
        return render(request,'Admin/Subcategory.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Subcategory.html',{"categoryData":data,'dis':categorydata})       
    
def Homepage(request):
    user=tbl_user.objects.all().count()
    mail=tbl_mail.objects.all().count()
    useremail=tbl_user.objects.all()
    return render(request,'Admin/Homepage.html',{'user':user,'mail':mail,'useremail':useremail})

def main(request):
    if request.method=="POST":
        return render(request,'Admin/main.html')

    else:
        return render(request,'Admin/main.html')

