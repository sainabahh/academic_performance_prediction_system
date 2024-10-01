from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from acd_app.models import *
from sample import sent
from .encode_faces import enf

def login(request):
    ob=student_table.objects.all()
    r=[]
    for i in ob:
        s=[i.id,r"C:\Users\sainaba shahanas kk\OneDrive\Desktop\Main project\acdamic (2)\acdamic\media/"+str(i.image),"student"]
        r.append(s)
    enf(r)
    return render(request,'Admin/login_index.html')



def logout(request):
    auth.logout(request)
    return render(request,'Admin/login_index.html')





def logincode(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob = login_table.objects.get(username=username, password=password)

        if ob.type == 'admin':
            ob1=auth.authenticate(username='admin',password='admin')
            if ob1 is not None:
                auth.login(request,ob1)
            return HttpResponse('''<script>alert("Login Successfull");window.location='adminhome'</script>''')
        elif ob.type == 'student':
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            obs=student_table.objects.get(login__id=ob.id)
            request.session['stu_crs']=obs.course.id
            return HttpResponse('''<script>alert("Login Successfull");window.location='homepagestudent'</script>''')
        elif ob.type == 'staff':
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("Login Successfull");window.location='staffhomepage'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("Invalid");window.location='/'</script>''')



@login_required(login_url='/')
def addcourse(request):
    return render(request,'Admin/ADD_COURSE.html')


@login_required(login_url='/')
def addcourse1(request):
    name = request.POST['textfield']
    details = request.POST['textfield2']

    ob = course_table()
    ob.coursename = name
    ob.details = details
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("inserted");window.location='/managecourse'</script>''')

@login_required(login_url='/')
def deletecourse(request,id):
    ob=course_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/managecourse'</script>''')

@login_required(login_url='/')
def adminhome(request):
    return render(request,'Admin/admin_index.html')

@login_required(login_url='/')
def addstaff(request):
    return render(request,'Admin/ADD_STAFF.html')

@login_required(login_url='/')
def deletestaff(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/managestaff'</script>''')

@login_required(login_url='/')
def deletesub(request,id):
    ob=subject_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/managesub'</script>''')

@login_required(login_url='/')
def editstaff(request,id):
    request.session['sid']=id
    ob=staff_table.objects.get(id=id)

    return render(request,'Admin/EDIT_STAFF.html',{"v":ob})

@login_required(login_url='/')
def updatestaff(request):
    try:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        gen = request.POST['gen']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        contact = request.POST['textfield6']
        email = request.POST['textfield7']
        img = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(img.name, img)
        ob1 = staff_table.objects.get(id=request.session['sid'])
        ob1.fname = fname
        ob1.lname = lname
        ob1.gender = gen
        ob1.place = place
        ob1.post = post
        ob1.pin = pin
        ob1.phone = contact
        ob1.email = email
        ob1.image = fn
        ob1.save()
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        gen = request.POST['gen']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        contact = request.POST['textfield6']
        email = request.POST['textfield7']
        ob1 = staff_table.objects.get(id=request.session['sid'])
        ob1.fname = fname
        ob1.lname = lname
        ob1.gender = gen
        ob1.place = place
        ob1.post = post
        ob1.pin = pin
        ob1.phone = contact
        ob1.email = email
        ob1.save()
    return HttpResponse('''<script>alert("Updated");window.location='/managestaff'</script>''')

@login_required(login_url='/')
def addstaff1(request):

        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        gen=request.POST['gen']
        place=request.POST['textfield3']
        post=request.POST['textfield4']
        pin=request.POST['textfield5']
        contact=request.POST['textfield6']
        email=request.POST['textfield7']
        username=request.POST['textfield8']
        password=request.POST['textfield9']
        img=request.FILES['file']
        fs=FileSystemStorage()
        fn=fs.save(img.name,img)

        ob=login_table()
        ob.username=username
        ob.password=password
        ob.type="staff"
        ob.save()

        ob1=staff_table()
        ob1.login=ob
        ob1.fname=fname
        ob1.lname=lname
        ob1.gender=gen
        ob1.place=place
        ob1.post=post
        ob1.pin=pin
        ob1.phone=contact
        ob1.email=email
        ob1.username=username
        ob1.password=password
        ob1.image=img
        ob1.save()
        return HttpResponse('''<script>alert("Inserted");window.location='/managestaff'</script>''')

@login_required(login_url='/')
def addsubject(request):
    obc=course_table.objects.all()
    return render(request,'Admin/ADD_SUBJECT.html',{"val":obc})

@login_required(login_url='/')
def addsubject1(request):
    subjectname=request.POST['textfield']
    details=request.POST['textfield2']
    coursename=request.POST['textfield3']

    ob=subject_table()
    ob.subject=subjectname
    ob.details=details
    ob.course=course_table.objects.get(id=coursename)
    ob.save()

    return HttpResponse('''<script>alert("Updated");window.location='/managesub'</script>''')

@login_required(login_url='/')
def viewalloc(request):
    ob = allocate_table.objects.all()
    ob1 = subject_table.objects.all()
    return render(request,'Admin/VIEW_ALLOCATE.html',{"val":ob, "val1": ob1})

@login_required(login_url='/')
def viewalloc_search(request):
    sub_id = request.POST['select']
    ob = allocate_table.objects.filter(subject_id=sub_id)
    ob1 = subject_table.objects.all()
    return render(request,'Admin/VIEW_ALLOCATE.html',{"val":ob, "val1": ob1, 'sub_id': int(sub_id)})

@login_required(login_url='/')
def allocsubject(request):
    ob=subject_table.objects.all()
    obb=staff_table.objects.all()
    return render(request,'Admin/ALLOCATE_SUBJECT.html',{"val":ob,"val1":obb})

@login_required(login_url='/')
def allocsubject1(request):
    subjectname = request.POST['select']
    staffname = request.POST['select2']

    ob = allocate_table()
    ob.subject=subject_table.objects.get(id=subjectname)
    ob.staff=staff_table.objects.get(id=staffname)
    ob.save()

    return HttpResponse('''<script>alert("Assigned");window.location='/viewalloc'</script>''')

@login_required(login_url='/')
def deletealloc(request,id):
    ob=allocate_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/viewalloc'</script>''')

@login_required(login_url='/')
def managecourse(request):
    ob = course_table.objects.all()
    return render(request,'Admin/MANAGE_COURSE.html',{"val":ob})

def managecourse_search(request):
    search = request.POST['textfield']
    ob = course_table.objects.filter(coursename__istartswith=search)
    return render(request,'Admin/MANAGE_COURSE.html',{"val":ob, 'search': search})

@login_required(login_url='/')
def managestaff(request):
    ob=staff_table.objects.all()
    return render(request,'Admin/manage_staff.html',{"val":ob})

@login_required(login_url='/')
def managestaff_search(request):
    search =request.POST['textfield']
    ob=staff_table.objects.filter(fname__istartswith=search)
    return render(request,'Admin/manage_staff.html',{"val":ob, 'search': search})

@login_required(login_url='/')
def managesub(request):
    ob = subject_table.objects.all()
    return render(request,'Admin/MANAGE_SUBJECT.html',{"val":ob})

@login_required(login_url='/')
def managesub_search(request):
    search=request.POST['textfield']
    ob = subject_table.objects.filter(subject__istartswith=search)
    return render(request,'Admin/MANAGE_SUBJECT.html',{"val":ob, "search": search})

@login_required(login_url='/')
def viewcomplaint(request):
    ob = complaint_table.objects.all()
    return render(request,'Admin/VIEW_COMPLAINT.html',{"val":ob})

@login_required(login_url='/')
def viewcomplaint_search(request):
    search = request.POST['textfield']
    ob = complaint_table.objects.filter(date=search)
    return render(request,'Admin/VIEW_COMPLAINT.html',{"val":ob, 'search': search})

@login_required(login_url='/')
def viewfeedback(request):
    ob = feedback_table.objects.all()
    return render(request,'Admin/VIEW_FEEDBACK.html',{"val":ob})

@login_required(login_url='/')
def viewreply(request):
    return render(request,'Admin/VIEW_REPLY.html.')

@login_required(login_url='/')
def viewstudentperformance(request):
    ob = studentperformance_table.objects.all()
    return render(request,'Admin/VIEW_STUDENT PERFORMANCE.html',{"val":ob})

@login_required(login_url='/')
def viewperformance3(request):
    search = request.POST['textfield']
    ob = studentperformance_table.objects.filter(student__fname__istartswith=search)
    oba = student_table.objects.all()
    return render(request,'Admin/VIEW_STUDENT PERFORMANCE.html',{"val":ob,"val1":oba, 'search': search})


#staff

@login_required(login_url='/')
def addstudymaterial(request):
    ob1=subject_table.objects.all()
    ob=allocate_table.objects.filter(staff__login__id=request.session['lid'])
    print(ob,"kk")
    return render(request,'Staff/Add Study Material.html',{"val":ob,'sub':ob1})

@login_required(login_url='/')
def addstudymaterial1(request):
    subject = request.POST['select']
    material = request.FILES['file']
    topic=request.POST['textfield']
    fs = FileSystemStorage()
    fn = fs.save(material.name, material)
    ob=studymaterials_tables()
    ob.subject = subject_table.objects.get(id=subject)
    ob.STAFF = staff_table.objects.get(login__id=request.session['lid'])
    ob.date = datetime.today()
    ob.material = fn
    ob.topic = topic
    ob.save()
    return HttpResponse('''<script>alert("Inserted");window.location='/managestudymaterial'</script>''')

@login_required(login_url='/')
def managestudymaterial(request):
    obs=allocate_table.objects.filter(staff__login__id=request.session['lid'])
    sids=[]
    for i in obs:
        sids.append(i.subject.id)
    ob = studymaterials_tables.objects.filter(subject__id__in=sids)
    return render(request,'Staff/manage study material.html',{"val":ob,"val1":obs})

@login_required(login_url='/')
def managestudymaterial1(request):
    # obc = studymaterials_tables.objects.all()
    subjectname = request.POST['Select']
    obs=allocate_table.objects.filter(staff__login__id=request.session['lid'])
    sids=[]
    for i in obs:
        sids.append(i.subject.id)
    ob = studymaterials_tables.objects.filter(subject__id__in=sids,subject__id=subjectname)
    return render(request, 'Staff/manage study material.html', {"val": ob, "val1": obs})

@login_required(login_url='/')
def deletematerial(request,id):
    ob=studymaterials_tables.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/managestudymaterial'</script>''')


@login_required(login_url='/')
def sendreply(request,id):
    request.session['pp']=id
    return render(request,'Staff/Send Reply.html')

@login_required(login_url='/')
def sendreply1(request):
    reply = request.POST['textfield']

    ob=complaint_table.objects.get(id=request.session['pp'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>alert("Reply sent");window.location='/viewcomplaints'</script>''')


@login_required(login_url='/')
def staffhomepage(request):
    return render(request,'Staff/staff_index.html')

def register(request):
    ob=course_table.objects.all()
    return render(request,'regindex.html',{'val':ob})


def register_code(request):
    print(request.POST)
    fn=request.POST['first_name']
    ln=request.POST['last_name']
    mail=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    dob=request.POST['dob']
    gender=request.POST['gender']
    pic=request.FILES['file']
    fs = FileSystemStorage()
    fnn = fs.save(pic.name, pic)
    username=request.POST['username']
    psw=request.POST['psw']
    courseid=request.POST['aaa']
    ob1 = login_table()
    ob1.username = username
    ob1.password = psw
    ob1.type="student"
    ob1.save()
    ob=student_table()
    ob.fname=fn
    ob.lname=ln
    ob.email=mail
    ob.contact=phone
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.course_id=courseid
    ob.dob=dob
    ob.gender=gender
    ob.image=fnn
    ob.login=ob1
    ob.save()
    return HttpResponse('''<script>alert("INSERTERD");window.location='/'</script>''')



@login_required(login_url='/')
def viewcomplaints(request):
    ob = complaint_table.objects.all()
    return render(request,'Staff/View Complaints.html',{"val":ob})

@login_required(login_url='/')
def viewcomplaints1(request):
    search = request.POST['select']
    ob = complaint_table.objects.filter(date=search)
    return render(request,'Staff/View Complaints.html',{"val":ob, 'search': search})


@login_required(login_url='/')
def viewfeedback1(request):
    # obs = allocate_table.objects.filter(staff__login__id=request.session['lid'])
    obs = subject_table.objects.all()
    ob = feedback_table.objects.all()
    return render(request,'Staff/View Feedback.html',{"val":ob,"val1":obs})

@login_required(login_url='/')
def viewfeedback1_search(request):
    # obs = allocate_table.objects.filter(staff__login__id=request.session['lid'])
    search = request.POST['select']
    obs = subject_table.objects.all()
    ob = feedback_table.objects.filter(subject_id=search)
    return render(request,'Staff/View Feedback.html',{"val":ob,"val1":obs, 'search': int(search)})


@login_required(login_url='/')
def viewperformance(request):
    on=allocate_table.objects.filter(staff__login__id=request.session['lid'])
    oid=[]
    for i in on:
        oid.append(i.subject.id)
    oba = allocate_table.objects.filter(staff__login__id=request.session['lid'])
    ob = studentperformance_table.objects.filter(subject__id__in=oid)
#     if len(ob) == 0:
#         return HttpResponse(
# '''<script>alert("there is no performance marked");window.location='/viewperformance'</script>''')

    return render(request,'Staff/view performance.html',{"val":ob,"val1":oba})

@login_required(login_url='/')
def viewperformance2(request):
    search = request.POST['select']
    ob = studentperformance_table.objects.filter(student__id=search)
    oba = allocate_table.objects.filter(staff__login__id=request.session['lid'])
    return render(request,'Staff/view performance.html',{"val":ob,"val1":oba})

@login_required(login_url='/')
def viewsubject(request):
    ob = subject_table.objects.all()
    obc=course_table.objects.all()
    return render(request,'Staff/view subject.html',{"val":ob,"val1":obc})

@login_required(login_url='/')
def viewsubject2(request):
    obc=course_table.objects.all()
    coursename = request.POST['select']
    ob = subject_table.objects.filter(course=coursename)
    return render(request,'Staff/view subject.html',{"val":ob,"val1":obc})



@login_required(login_url='/')
def staffVIEWworkStudent(request):
    ob1=work_result.objects.filter(WORK__STAFF__login__id=request.session['lid'])
    return render(request,'Staff/view uploaded work.html',{'val1':ob1})




#student

@login_required(login_url='/')
def complaintreply(request):
    ob = staff_table.objects.all()
    return render(request,'Student/COMPLAINT_REPLY.html',{"val": ob})

@login_required(login_url='/')
def sendreply2(request):
    comp = request.POST['textfield']
    staff_id = request.POST['select']
    ob=complaint_table()
    ob.complaint=comp
    ob.reply = "pending"
    ob.date = datetime.today()
    ob.STAFF = staff_table.objects.get(id=staff_id)
    ob.student = student_table.objects.get(login__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Reply sent");window.location='/sendcomplaint'</script>''')

@login_required(login_url='/')
def homepagestudent(request):
    return render(request,'Student/student_index.html')

@login_required(login_url='/')
def sendcomplaint(request):
    ob = complaint_table.objects.filter(student__login_id=request.session['lid'])
    return render(request,'Student/SEND_COMPLAINT.html', {"val":ob})

@login_required(login_url='/')
def sendcomplaints1(request):
    search = request.POST['date']
    ob = complaint_table.objects.filter(date=search)
    return render(request,'Student/SEND_COMPLAINT.html',{"val":ob, 'search': search})

@login_required(login_url='/')
def viewcomplaint1(request):
    ob = complaint_table.objects.all()
    return render(request, 'Student/View Complaints.html', {"val": ob})

@login_required(login_url='/')
def sendfeedback(request):
    ob = subject_table.objects.all()
    return render(request, 'Student/SEND_FEEDBACK.html', {"val": ob})

@login_required(login_url='/')
def sendfeedback1(request):
    feed = request.POST['textfield']
    sub = request.POST['select']
    ob = feedback_table()
    ob.feedback = feed
    ob.date = datetime.today()
    ob.subject=subject_table.objects.get(id=sub)
    ob.student = student_table.objects.get(login__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Feedback sent");window.location='/sendfeedback'</script>''')



@login_required(login_url='/')
def viewstudymaterial(request):
    ob = subject_table.objects.filter(course__id=request.session['stu_crs'])
    obsm=studymaterials_tables.objects.all()
    return render(request,'Student/view study material.html',{"val":ob,"val1":obsm})

@login_required(login_url='/')
def viewstudymaterial1(request):
    search = request.POST['select']
    ob = subject_table.objects.filter(course__id=request.session['stu_crs'])
    obsm=studymaterials_tables.objects.filter(subject=search)
    return render(request,'Student/view study material.html',{"val":ob,"val1":obsm})

@login_required(login_url='/')
def viewstudymaterial3(request):
    subjectname = request.POST['Select']
    obs = subject_table.objects.filter(course__id=request.session['stu_crs'])
    sids=[]
    for i in obs:
        sids.append(i.subject.id)
    ob = studymaterials_tables.objects.filter(subject__id__in=sids,subject__id=subjectname)
    return render(request, 'Student/view study material.html', {"val": ob, "val1": obs})

@login_required(login_url='/')
def viewsubject1(request):
    ob = subject_table.objects.all()
    ob1=course_table.objects.all()
    return render(request,'Student/view subject_1.html',{"val":ob,'val1':ob1})

@login_required(login_url='/')
def viewsubject3(request):
    obc=course_table.objects.all()
    coursename = request.POST['select']
    ob = subject_table.objects.filter(course=coursename)
    return render(request,'Student/view subject_1.html',{"val":ob,"val1":obc})

@login_required(login_url='/')
def viewperformance1(request):
    ob = studentperformance_table.objects.filter(student__login__id=request.session['lid'])
    return render(request,'Student/VIEW_PERFORMANCE.html',{"val":ob})

@login_required(login_url='/')
def addwork(request):
    ob1=allocate_table.objects.filter(staff__login__id=request.session['lid'])
    return render(request,'Staff/add work.html',{'val1':ob1})


@login_required(login_url='/')
def addworkpost(request):
    content = request.POST['content']
    asid = request.POST['select']
    ob = staff_noti_table()
    ob.STAFF = staff_table.objects.get(login__id=request.session['lid'])
    ob.SUBID = allocate_table.objects.get(id=asid)
    ob.content = content
    ob.date_time = datetime.now()
    ob.save()
    return HttpResponse('''<script>alert(" Added Work ");window.location='/addwork'</script>''')


@login_required(login_url='/')
def VIEWwork(request):
    ob1=staff_noti_table.objects.all()
    return render(request,'Student/view work.html',{'val1':ob1})


@login_required(login_url='/')
def uploadwork(request,id):
    request.session['wid']=id
    return render(request,'Student/upload work.html')


@login_required(login_url='/')
def update_work(request):
    profile = request.FILES["file"]
    wid = request.session['wid']
    stid = request.session['lid']
    fs = FileSystemStorage()
    fsave = fs.save(profile.name, profile)
    ob=work_result()
    ob.WORK = staff_noti_table.objects.get(id=wid)
    ob.STUDENT=student_table.objects.get(login__id=stid)
    ob.report=fsave
    ob.date_time=datetime.now()
    ob.remark="pending"
    ob.mark=0
    ob.save()
    return HttpResponse('''<script>alert(" Added Work ");window.location='/homepagestudent'</script>''')


@login_required(login_url='/')
def sendremark(request,id):
    request.session['rid']=id
    return render(request,'Staff/send remark.html')

def sendremarks(request):
    rid = request.session['rid']
    review = request.POST['review']
    obj=work_result.objects.get(id=rid)
    obj.remark = review
    res=sent(review)
    print(res,"jjjjjjjjjjjjjjjjjjjjjjjjj")
    obj.mark=res[1]
    obj.save()
    kk=obj.WORK.SUBID.subject.id
    ss=obj.STUDENT.id
    # avg=(obj.mark*5/100)
    wid = []
    res = 0
    ob = staff_noti_table.objects.filter(SUBID__subject__id=kk)
    print(ob, "mmmmmmmmmmmm")
    for i in ob:
        wid.append(i.id)
        obb = work_result.objects.get(WORK__id=i.id,STUDENT__id=ss)
        print(obb, "obbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        res = res + obb.mark
    print(res, "UUUUUUUUUUUUUUUUUUUUUU")
    wlen = len(wid)
    jj = (res / (wlen * 5)) * 100
    pp=int(jj)
    emolist=['happy','surprise', 'neutral']
    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

    obh=emotion_table.objects.filter(STUDENT__id=ss,emotion__in=emolist)
    obs=emotion_table.objects.filter(STUDENT__id=ss).exclude(emotion__in=emolist)
    if len(obh)>len(obs):
        pp=pp+5

    elif len(obh)<len(obs):
        pp=pp/2
    emo=[]
    if pp >90:
        avg="S"
    elif pp > 85:
        avg="A+"
    elif pp > 80:
        avg = "A"
    elif pp > 70:
        avg="B+"
    elif pp > 60:
        avg="B"
    elif pp > 50:
        avg="C"
    elif pp > 40:
        avg="P"
    else:
        avg="F"

    print(avg)
    o=studentperformance_table.objects.filter(student=obj.STUDENT.id,subject__id=kk,work=request.session['rid'])

    if len(o)==0:
        on=studentperformance_table()
        on.subject=subject_table.objects.get(id=kk)
        on.student=student_table.objects.get(id=ss)
        on.grade=avg
        on.work=work_result.objects.get(id=rid)
        on.save()
    else:
        on = studentperformance_table.objects.get(id=o[0].id)
        on.grade = avg
        on.save()
    return HttpResponse('''<script>alert(" Added remark ");window.location='/staffVIEWworkStudent'</script>''')


def emotion_post(request):
    emotion = request.GET['emo']
    student_id = request.GET['student_id']

    ob = emotion_table()
    ob.emotion = emotion
    ob.pose = 'pending'
    ob.STUDENT = student_table.objects.get(id=student_id)
    ob.datetime = datetime.now()
    ob.save()
    return JsonResponse({"task":str(ob.id)})
