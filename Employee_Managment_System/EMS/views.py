# from django.shortcuts import render, get_object_or_404, redirect
# from datetime import datetime
# from django.core.mail import EmailMessage
# from itertools import count

# from django.db.models import Q, Sum
# from django.http import HttpResponse, HttpResponseRedirect

# # Create your views here.
# from django.http import HttpResponse
# from django.urls import reverse

# from EMS.models.managermodel import Manager


# def homepage(request):
#     return render(request,'index.html')

# def htmlpage(request):
#     return render(request, 'index.html')
# # def hello_world(request):
#     #return HttpResponse("Hello, world!")

# # ----- Manager -----


# def saveManager(request):
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     phone = request.POST['contact']
#     gender = request.POST['gender']
#     dob=request.POST['dob']
#     address = request.POST['address']
#     state=request.POST['state']
#     joinDate=request.POST['joinDate']
#     qualification=request.POST['qualification']
#     emailId = request.POST['email']
#     password = request.POST['password']
#     image = request.FILES['image']
#     resume = request.FILES['resume']
#     e = Manager(fname=fname, lname=lname, phone=phone, gender=gender,
#                  dob=dob, address=address, state=state, joinDate=joinDate, qualification=qualification,
#                  emailId=emailId, password=password, image=image, resume=resume)

#     e.save()
#     if e:
#         msg = "Your Application has been Submited. We will Back to you Soon"
#         return HttpResponseRedirect(reverse("home"))
#     else:
#         return HttpResponse("error")

def managerLogin(request):
    return render(request, "manager/managerLogin.html")

# def loginManager(request):
#     emailId = request.POST['email']
#     password = request.POST['password']
#     c = Manager.objects.filter(emailId=emailId, password=password,account='Active')
#     if c:
#         request.session['mngid'] = c[0].managerCode
#         request.session['managerFname'] = c[0].fname
#         request.session['managerLname'] = c[0].lname
#         date = datetime.now().date()
#         return HttpResponseRedirect(reverse("managerDashboard"))
#     else:
#         msg = 'You Are Not Valid User'
#         return render(request, "managerLogin.html", {'msg': msg})

# # ----- Employee -----
# from EMS.models import attendance, holiday, leave, salary, tasks, notice
# from EMS.models.employeemodel import Employee, employeeDailyWork

def employeeRegistration(request):
    return render(request, "employee/employeeReg.html")

# def saveEmployee(request):
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     phone = request.POST['contact']
#     gender = request.POST['gender']
#     dob=request.POST['dob']
#     address = request.POST['address']
#     state=request.POST['state']
#     qualification=request.POST['qualification']
#     emailId = request.POST['email']
#     password = request.POST['password']
#     # image = request.FILES['image']
#     # resume = request.FILES['resume'
    
#     e = Employee(fname=fname, lname=lname, phone=phone, gender=gender,
#                  dob=dob, address=address, state=state,  qualification=qualification,
#                  emailId=emailId, password=password)
#     e.save()
#     if e:
#         msg = "Your Application has been Submited. We will Back to you Soon"
#         return HttpResponseRedirect(reverse("home"))
#     else:
#         return HttpResponse("error")

def employeeLogin(request):
    return render(request, "employee/employeeLogin.html")

# def loginEmployee(request):
#     emailId = request.POST['email']
#     password = request.POST['password']
#     c = Employee.objects.filter(emailId=emailId, password=password,account='Active')
#     if c:
#         time = datetime.now()
#         date = datetime.now().date()
#         request.session['empid'] = c[0].empCode
#         request.session['fname'] = c[0].fname
#         request.session['lname'] = c[0].lname
#         request.session['managerId'] = c[0].managerId
#         request.session['leave'] = c[0].leave
#         employeeName = request.session['fname'] + request.session['lname']
#         res = employeeDailyWork(employeeId=c[0].empCode, managerId=c[0].managerId,loginTime=time,date=date)
#         res.save()
#         eid = employeeDailyWork.objects.latest('id')
#         feid = eid.id
#         request.session['workId'] = feid
#         print(feid)

#         c = attendance.objects.filter(employeeId=request.session['empid'], date=date)
#         if not c:
#             attendance = attendance(employeeId=request.session['empid'], loginTime=time, logoutTime=time, date=date,
#                                     status='Present', employeeName=employeeName)
#             attendance.save()
#         else:
#             print('OK')
#         return HttpResponseRedirect(reverse("employeeDashboard"))
#     else:
#         msg = 'You Are Not Valid User'
#         return render(request, "employeeLogin.html", {'msg': msg})

# # ----- Admin -----
# from EMS.models.adminmodel import admin

# def index(request):
#     return render(request, "index.html")

def newAdmin(request):
    return render(request, "EMSadmin/adminReg.html")

# def saveAdmin(request):
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     phone = request.POST['contact']
#     gender = request.POST['gender']
#     emailId = request.POST['email']
#     password = request.POST['password']
#     r = admin(fname=fname, lname=lname, phone=phone, gender=gender, emailId=emailId, password=password)
#     r.save()
#     if r:
#         return HttpResponseRedirect(reverse("home"))
#     else:
#         HttpResponseRedirect("Registration Failed")
    
# def adminDetails(request):
#     r = admin.objects.all()
#     return render(request, "adminDashboard/adminDetails.html", {'r': r})


# def loginAdmin(request):
#     # print(request)
#     emailId = request.POST.get('email')
#     password = request.POST.get('password')
#     c = admin.objects.filter(emailId=emailId, password=password)
#     if c:
#         return HttpResponseRedirect(reverse("home"))
#        # return render(request, 'adminDashboard/index.html')
#     else:
#         msg = 'You Are Not The Valid User'
#         print(msg)
#         return render(request, "EMSadmin/adminLogin.html", {'msg': msg})
    



# def login(request):
#     if request.method == 'POST':
#         # Get email and password from POST data
#         email = request.POST.get('email')  # Form field 'email'
#         password = request.POST.get('password')  # Form field 'password'
        
#         # Verify user credentials
#         c = admin.objects.filter(emailId=email, password=password)  # Adjust to your admin model
#         if c.exists():  # Check if there's a matching admin
#             return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#         else:
#             # Invalid login credentials, show error message
#             msg = 'You are not a valid user'
#             print(msg)
#             return render(request, "EMSadmin/adminLogin.html", {'msg': msg})  # Render the login page with error message
#     else:
#         # For GET request, simply render the login page
#         print('NOTTTT')
#         # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#         return render(request, "employee/employeeReg.html")

def adminIndexPage(request):
#     employee = Employee.objects.filter(account='Active').count()
#     manager = Manager.objects.filter(account='Active').count()
#     # clientTotal = client.objects.filter(account='Active').count()
#     # projectTotal = clientProject.objects.all().count()
#     # p = clientProject.objects.filter(status='Working')
#     # l = list(p)
#     # for i in l:
#     #     #m = get_object_or_404(Manager, managerCode=i.managerId)
#     #     m = Manager.objects.filter(managerCode=i.managerId)
#     #     print(m)
#     # param = {'m': m, 'p': p, 'employee': employee, 'manager': manager, 'clientTotal': clientTotal,'projectTotal': projectTotal}
#     # param = {'employee': employee, 'manager': manager, }
    return render(request, "EMSadmin/indexDash.html")


# """ def projectProgressAdmin(request,pk):
#     pj = get_object_or_404(clientProject, pk=pk)
#     pid =pj.projectId
#     m = pj.managerId
#     mng = Manager.objects.filter(managerCode=m)
#     emp = Employee.objects.filter(managerId=m)

#     p = employeeDailyWork.objects.filter(projectId=pid).order_by('-id')

#     param = {'emp': emp, 'mng': mng, 'pj': pj, 'p': p}
#     return render(request, "adminDashboard/projectProgress.html", param)"""

# def employeeRequest(request):
#     e1 = Employee.objects.filter(account='Deactive')
#     return render(request, "adminDashboard/employeeRequest.html", {'e1': e1})

def managerRequest(request):
    # e1 = Manager.objects.filter(account='Deactive')
    return render(request, "EMSadmin/manager.html")

# def allEmployee(request):
#     e1 = Employee.objects.filter(account='Active')
#     return render(request, "adminDashboard/allEmployee.html", {'e1': e1})

# def allManager(request):
#     e1 = Manager.objects.filter(account='Active')
#     return render(request, "adminDashboard/allManager.html", {'e1': e1})

# def editEmployee(request,pk):
#     e = get_object_or_404(Employee, empCode=pk)
#     e1 = e.managerId
#     m = Manager.objects.filter(managerCode=e1)
#     fname = m[0].fname
#     lname = m[0].lname
#     return render(request, "adminDashboard/editEmployee.html", {'e': e, 'fname': fname, 'lname': lname})

# def editManager(request,pk):
#     e = get_object_or_404(Manager, managerCode=pk)
#     return render(request, "adminDashboard/editManager.html",  {'e': e})

# def testlogin(request):
#     if request.method == 'POST':
#         emailId = request.POST['email']
#         password = request.POST['password']
#         c = admin.objects.filter(emailId=emailId, password=password)  # Adjust to your admin model
#         if c:
#             # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#             # return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#             return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#         else:
#             return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#     else:
#         return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#         # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful

# def testloginEmployee(request):
#     if request.method == 'POST':
#         emailId = request.POST['email']
#         password = request.POST['password']
#         c = Employee.objects.filter(emailId=emailId, password=password)  # Adjust to your admin model
#         if c:
#             # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#             # return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#             return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#         else:
#             return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#     else:
#         return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#         # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful

# def testloginManager(request):
#     if request.method == 'POST':
#         emailId = request.POST['email']
#         password = request.POST['password']
#         c = Manager.objects.filter(emailId=emailId, password=password)  # Adjust to your admin model
#         if c:
#             # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#             # return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#             return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful
#         else:
#             return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#     else:
#         return render(request, "EMSadmin/adminLogin.html")  # Render the login page with error message
#         # return HttpResponseRedirect(reverse("home"))  # Redirect to home if login is successful

# def updateEmployee(request):
#     id = request.POST['id']
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     phone = request.POST['phone']
#     bloodGroup = request.POST['bloodGroup']
#     address = request.POST['address']
#     state = request.POST['state']
#     qualification = request.POST['qualification']
#     emailId = request.POST['email']
#     password = request.POST['password']
#     leave = request.POST['leave']
#     account = request.POST['account']
#     e = Employee.objects.filter(empCode=id).update(fname=fname, lname=lname, phone=phone,
#                   bloodGroup=bloodGroup, address=address, state=state, qualification=qualification,
#                   emailId=emailId, password=password, account=account, leave=leave)
#     if e:
#         return HttpResponseRedirect(reverse('allEmployee'))
#     else:
#         return HttpResponse("Record Not Updated")

# def updateManager(request):
#     id = request.POST['id']
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     phone = request.POST['phone']
#     bloodGroup = request.POST['bloodGroup']
#     address = request.POST['address']
#     state = request.POST['state']
#     qualification = request.POST['qualification']
#     emailId = request.POST['email']
#     password = request.POST['password']
#     account = request.POST['account']
#     Manager.objects.filter(managerCode=id).update(fname=fname,lname=lname,phone=phone,
#                             bloodGroup=bloodGroup,address=address,state=state,qualification=qualification,
#                             emailId=emailId,password=password,account=account)
#     return HttpResponseRedirect(reverse('allManager'))

# def deleteEmployee(request,pk):
#     emp = get_object_or_404(Employee, empCode=pk)
#     emp.delete()
#     return HttpResponseRedirect(reverse('allEmployee'))

# def deleteManager(request,pk):
#     mng = get_object_or_404(Manager, managerCode=pk)
#     mng.delete()
#     return HttpResponseRedirect(reverse('allManager'))

# def employeeProfile(request,pk):
#     emp = get_object_or_404(Employee, pk=pk)
#     n = emp.managerId
#     mng = Manager.objects.get(managerCode=n)
#     return render(request, "adminDashboard/employeeProfile.html", {'emp': emp, 'mng': mng})

# def managerProfile(request,pk):
#     mng = get_object_or_404(Manager, pk=pk)
#     return render(request, "adminDashboard/managerProfile.html", {'mng': mng})

# def assignManager(request):
#     id = request.POST['id']
#     manager = request.POST['manager']
#     joindate = request.POST['joinDate']
#     activationDate = datetime.now()
#     print(activationDate)
#     Employee.objects.filter(empCode=id).update(managerId=manager,joinDate=joindate,account='Active',
#                                                activation_Date=activationDate)
#     return HttpResponseRedirect(reverse("employeeRequest"))

# def employeeRequestView(request,pk):
#     emp = get_object_or_404(Employee, pk=pk)
#     mng = Manager.objects.filter(account='Active')
#     return render(request, "adminDashboard/employeeRequestView.html", {'emp': emp, 'mng': mng})

# def managerRequestView(request,pk):
#     mng = get_object_or_404(Manager, pk=pk)
#     request.session['id'] = mng.managerCode
#     return render(request, "adminDashboard/managerRequestView.html", {'mng': mng})

# def managerRequestEdit(request):
#     id = request.POST['id']
#     joindate = request.POST['joinDate']
#     activationDate = datetime.now()
#     Manager.objects.filter(managerCode=id).update(joinDate=joindate, account='Active',
#                                                activation_Date=activationDate)
#     return HttpResponseRedirect(reverse("managerRequest"))

# def holidays(request):
#     e1 = holiday.objects.all()
#     return render(request, "adminDashboard/holidays.html", {'e1': e1})

# def saveHoilday(request):
#     holidayName = request.POST['holidayName']
#     holidayDate = request.POST['hoildayDate']
#     holidayDay = request.POST['hoildayDay']
#     holidayDescription = request.POST['hoildayDescription']

#     h = holiday(holidayName=holidayName, holidayDate=holidayDate, hoildayDay= holidayDay, holidayDescription=holidayDescription)
#     h.save()
#     return HttpResponseRedirect(reverse("hoildays"))

# def showStatus(request):
#     s = get_object_or_404(employeeDailyWork)
#     return render(request, "adminDashboard/showStatus.html", {'s': s})

# def filterEmployee(request):
#     emp = Employee.objects.filter(account='Active')
#     return render(request, "adminDashboard/filterEmployee.html", {'emp': emp})

# from EMS.models.salary import perDaySalary, monthSalary

# def savefilterEmployee(request):
#     employeeId = request.POST['employeeId']
#     date = request.POST['date']
#     res = employeeDailyWork.objects.filter(employeeId=employeeId, date=date)
#     p = perDaySalary.objects.filter(empCode=employeeId, date=date)
#     return render(request, "adminDashboard/filterEmployee.html", {'res': res, 'p': p})

# def attendance(request):
#     date = datetime.now().date()
#     s = attendance.objects.filter(date=date)
#     param = {'s': s}
#     return render(request, 'adminDashboard/attendance.html', param)

# def attendanceFilter(request):
#     return render(request, 'adminDashboard/attendanceFilter.html')

# def salary(request):
#     e = Employee.objects.filter(account='Active')
#     return render(request, "adminDashboard/salary.html", {'e': e})

# def salaryView(request):
#     employeeId = request.session['empid']
#     c = monthSalary.objects.filter(empCode=employeeId)
#     return render(request, "adminDashboard/salaryView.html", {'c': c})

# def genrateSalary(request,pk):
#     employeeId = get_object_or_404(Employee,empCode=pk)
#     id = employeeId.empCode
#     print(employeeId)
#     date = datetime.now().date()
#     mon = date.strftime('%B')
#     year = date.year
#     print(mon)
#     print(year)
#     items = perDaySalary.objects.filter(empCode=id)
#     totalSalary1 = sum(items.values_list('daySalary', flat=True))
#     totalSalary = totalSalary1 + 400 + 400 + 400
#     totalTime = sum(items.values_list('totalTime', flat=True))
#     print(totalSalary)
#     print(totalTime)
#     s = monthSalary.objects.filter(empCode=id, month=mon, year=year)
#     if s:
#         pass
#     else:
#         SalaryCal = monthSalary(empCode=id, dateCreated=datetime.now(), month=mon, year=year,
#                                 totalTime=totalTime, finalSalary=totalSalary,status='Paid')
#         SalaryCal.save()
#     c = monthSalary.objects.get(empCode=id)
#     return render(request, "adminDashboard/salaryView.html", {'e': employeeId, 'c': c, 'totalTime': totalTime, 'totalSalary': totalSalary})

# from EMS.models import leave

# def adminLeave(request):
#     l = leave.objects.filter(status='Pending')
#     n = l[0].employeeId
#     name = Employee.objects.filter(empCode=n)
#     return render(request, "adminDashboard/leave.html", {'l': l, 'name':name})

# def notice(request):
#     return render(request, "adminDashboard/notice.html")

# def saveNotice(request):
#     n = request.POST['notice']
#     activationDate = datetime.now().date()
#     r = notice(noticeDetails=n, noticeDate=activationDate)
#     r.save()
#     if r:
#         return render(request, "adminDashboard/notice.html")

# #----------------------------Employee Dashboard Base-------------------------------

# def Ebase(request):
#     if request.session.has_key('empid'):
#         fname = request.session['fname']
#         lname = request.session['lname']
#         return render(request, "employeeDashboard/index.html", {'fname': fname, 'lname': lname})
#     else:
#         return render(request, "employeeLogin.html")
    
# def employeeIndexPage(request):
#     if request.session.has_key('empid'):
#         fname =  request.session['fname']
#         lname =  request.session['lname']
#         eid = request.session['empid']
#         m = request.session['managerId']
#         img = Employee.objects.get(empCode=eid)
#         id = request.session['empid']
#         empImage = get_object_or_404(Employee, empCode=id)
#         date = datetime.now().date()

#         items = employeeDailyWork.objects.filter(employeeId=eid,date=date)
#         tHour = Sum(items.values_list('duration', flat=True))
#         print(tHour)
#         lTime = attendance.objects.get(employeeId=eid, date=date)
#         param = {'lTime': lTime, 'fname': fname, 'lname': lname, 'date': date, 'tHour': tHour,
#                       'img': img, 'empImage':empImage,}
#         return render(request, "employeeDashboard/index.html", param)
#     else:
#         return render(request, "employeeLogin.html")
    
# def employeeLeave(request):
#     if request.session.has_key('empid'):
#         fname = request.session['fname']
#         lname = request.session['lname']
#         managerId = request.session['managerId']
#         id = request.session['empid']
#         empImage = get_object_or_404(Employee, empCode=id)
#         return render(request, "employeeDashboard/leave.html", {'fname': fname, 'lname': lname,
#                 'managerId': managerId, 'empImage': empImage})
#     else:
#         return render(request, "employeeLogin.html")
    
# def saveLeave(request):
#     fname = request.session['fname']
#     lname = request.session['lname']
#     eid = request.session['empid']
#     startDate = request.POST['startDate']
#     endDate = request.POST['endDate']
#     reason = request.POST['reason']
#     totalDays = request.POST['totalDays']
#     managerId = request.POST['manager_id']
#     leaveType = request.POST['leaveType']
#     ename = fname+ lname
#     l = request.session['leave']
#     print(ename)
#     l = leave(employeeId=eid, employeeName=ename, startDate=startDate, endDate=endDate,totalDays=totalDays, employeeReason=reason,
#               status='Pending', managerId=managerId, leaveType=leaveType)
#     l.save()
#     if l:
#         return HttpResponseRedirect(reverse("employeeLeave"))
#     else:
#         return HttpResponse("error")

# def leaveStatus(request):
#     if request.session.has_key('empid'):
#         fname = request.session['fname']
#         lname = request.session['lname']
#         empid = request.session['empid']
#         id = request.session['empid']
#         empImage = get_object_or_404(Employee, empCode=id)
#         param = {'fname': fname, 'lname': lname, 'empImage':empImage}
#         res =leave.objects.filter(employeeId=empid)
#         return render(request, "employeeDashboard/leaveStatus.html",{'res': res, 'empImage':empImage})
#     else:
#         return render(request, "employeeLogin.html")

# def searchLeaveStatus(request):
#     leave = leave.objects.all()
#     empid = request.session['empid']
#     startDate = request.POST['startDate']
#     endDate = request.POST['endDate']
#     status = request.POST['status']
#     id = request.session['empid']
#     empImage = get_object_or_404(Employee, empCode=id)
#     res =leave.objects.filter(startDate__gte=startDate, startDate__lte=endDate,status=status,employeeId=empid)
    
#     return render(request, "employeeDashboard/leaveStatus.html", {'res': res, 'empImage':empImage})
  
# def userProfile(request):
#     if request.session.has_key('empid'):
#         fname = request.session['fname']
#         lname = request.session['lname']
#         id = request.session['empid']
#         empImage = get_object_or_404(Employee, empCode=id)
#         e = Employee.objects.get(empCode=id)
#         param = {'fname': fname, 'lname': lname, 'e':e, 'empImage': empImage}
#         return render(request, "employeeDashboard/userProfile.html", param)
#     else:
#         return render(request, "employeeLogin.html")        

# def saveUserProfile(request):
#     id = request.session['empid']
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     phone = request.POST['phone']
#     bloodGroup = request.POST['bloodGroup']
#     address = request.POST['address']
#     gender = request.POST['gender']
#     state = request.POST['state']
#     qualification = request.POST['qualification']
#     emailId = request.POST['email']
#     about = request.POST['aboutMe']
#     e = Employee.objects.filter(empCode=id).update(fname=fname, lname=lname, contact=phone,
#            bloodGroup=bloodGroup,address=address,gender=gender, state=state,qualification=qualification,
#                 emailId=emailId,about=about)
#     if e:
#         return render(request, "employeeDashboard/userProfile.html")
#     else:
#         return HttpResponse("Record Not Updated")

def base(request):
    return render(request, "EMSadmin/base.html")


def managerRegistration(request):
    return render(request, "manager/managerReg.html")


def managerlist(request):
    return render(request, "EMSadmin/managerList.html")

def managerrequest(request):
    return render(request,"EMSadmin/managerRequest.html")

def employeelist(request):
    return render(request, "EMSadmin/employeeList.html")

def employeerequest(request):
    return render(request, "EMSadmin/employeeRequest.html")


def adminReg(request):
    return render(request, 'EMSadmin/adminReg.html')

def adminlogin(request):
    return render(request, 'EMSadmin/adminLogin.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models.profile import Profile
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Registration view
def register_emp(request):
    if request.method == 'POST':
        role = 'employee' 
        # Additional fields for the Manager model
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        username = email
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        state = request.POST.get('state')
        qualification = request.POST.get('qualification')
        password = request.POST.get('password')
        # image = request.FILES.get('image')  # Handling file uploads
        # resume = request.FILES.get('resume')  # Handling file uploads
        # Create the user
        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password,is_active = False)
        user.save()

        # Create the Profile model with additional fields
        profile = Profile.objects.create(user=user, role=role,fname=fname,lname=lname,phone=phone,gender=gender,dob=dob,address=address,state=state,qualification=qualification)
        r = profile.save()
        if r:
            return render(request, 'employee/employeeLogin.html') 
    return render(request, 'employee/employeeReg.html')    
    

# Login view
def emp_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username , password)
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active: 
                print('y')
                login(request, user)
                return redirect('home') 
            else:
                print('User is inactive')
                messages.error(request, 'Your account is inactive. Please contact support.')
            # return redirect('home')  # Redirect to home page or desired page

        else:
            print('User is inactive')
            messages.error(request, 'Invalid username or password.')
    return render(request, 'employee/employeeLogin.html')

# Example home view (to be redirected after login/registration)



def register_admin(request):
    if request.method == 'POST':
        role = 'admin' 
        # Additional fields for the Manager model
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        username = email
        gender = request.POST.get('gender')
        # dob = request.POST.get('dob')
        # address = request.POST.get('address')
        # state = request.POST.get('state')
        # qualification = request.POST.get('qualification')
        password = request.POST.get('password')
        # image = request.FILES.get('image')  # Handling file uploads
        # resume = request.FILES.get('resume')  # Handling file uploads
        # Create the user
        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
        user.save()

        # Create the Profile model with additional fields
        profile = Profile.objects.create(user=user, role=role,fname=fname,lname=lname,phone=phone,gender=gender)
        r = profile.save()
        if r:
            return render(request, 'EMSadmin/adminLogin.html') 
    return render(request, 'EMSadmin/adminReg.html')    
    

# Login view
def admin_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username , password)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('y')
            login(request, user)
            # return redirect('home')  # Redirect to home page or desired page
            return redirect('home') 

        else:
            print('N')
            messages.error(request, 'Invalid username or password.')
    return render(request, 'EMSadmin/adminLogin.html')



def register_man(request):
    if request.method == 'POST':
        role = 'manager' 
        # Additional fields for the Manager model
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        username = email
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        state = request.POST.get('state')
        qualification = request.POST.get('qualification')
        password = request.POST.get('password')
        # image = request.FILES.get('image')  # Handling file uploads
        # resume = request.FILES.get('resume')  # Handling file uploads
        # Create the user
        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password,is_active = False)
        user.save()

        # Create the Profile model with additional fields
        profile = Profile.objects.create(user=user, role=role,fname=fname,lname=lname,phone=phone,gender=gender,dob=dob,address=address,state=state,qualification=qualification)
        r = profile.save()
        if r:
            return render(request, 'manager/managerLogin.html') 
    return render(request, 'manager/managerReg.html')    
    

# Login view
def man_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username , password)
        # Authenticate the user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        if user.is_active: 
            print('y')
            login(request, user)
            return redirect('home') 
        else:
            print('User is inactive')
            messages.error(request, 'Your account is inactive. Please contact support.')
            # return redirect('home')  # Redirect to home page or desired page
    else:
        print('User is inactive')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'manager/managerLogin.html')



def index(request):
    return render(request, 'index.html')
    
def home(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role == 'admin':
            return render(request, 'EMSadmin/indexDash.html')
        elif role == 'manager':
            return render(request, 'manager/managerDash.html')
        else:
            return render(request, 'employee/employeeDash.html')
        

    return redirect('login')

def employeerequest(request):
    return render(request, "EMSadmin/employeeRequest.html")

def employeeStatus(request):
    return render(request, "EMSadmin/employeeStatus.html")
    
def baseEmployee(request):
    return render(request, "employee/base.html")

def employeeIndexPage(request):
    return render(request,"employee/employeeDash.html")

def baseManager(request):
    return render(request, "manager/base.html")

def managerIndexPage(request):
    return render(request,"manager/managerDash.html")

def managerEmployeelist(request):
    return render(request, "manager/employeeList.html")

def managerEmployeerequest(request):
    return render(request, "manager/employeeRequest.html")


def employeelist(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role=='admin':
            e1 = User.objects.filter(profile__role='employee')  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request,'EMSadmin/employeeList.html',{'e1':e1})
        elif role=='manager':
            e1 = User.objects.filter(profile__role='employee')  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request,'manager/employeeList.html',{'e1':e1})
    else:
        return render(request,'index.html')


def managerlist(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role=='admin':
            e1 = User.objects.filter(profile__role='manager')  # Fetch all User records
            e1 = e1.select_related('profile')
            return render(request,'EMSadmin/managerlist.html',{'e1':e1})
    else:
        return render(request,'index.html')

def all_logout(request):
    # Log out the user
    now = datetime.now()
    
    # Print the date separately
    print("Date:", now.date())  # This will print only the date
    
    # Print the time separately
    print("Time:", now.strftime("%H:%M:%S"))  # This will print only the time in HH:MM:SS format
    
    logout(request)
    
    # Redirect to the login page or a different page after logout
    return render(request,'index.html')  # Replace with your login page name or URL