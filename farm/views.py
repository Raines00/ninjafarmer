from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth import get_user_model,logout
from . models import *
from django.contrib.auth.views import LoginView, TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,View
from .forms import *

# Create your views here.

class Index(TemplateView):
    template_name = 'farm/home/index.html'
class Dashboard(LoginRequiredMixin,TemplateView):
    template_name = 'farm/dashboard/index.html'
    login_url = 'farm:login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workerscount"] = Staff.objects.all().count()
        context["workers"] = Staff.objects.all()
        context['depts'] = Department.objects.all().count()
        context['produce'] = Produce.objects.all().aggregate(Sum('total'))
        return context
    

class Login(LoginView):
    template_name = 'farm/home/login.html'
    form_class = LoginForm
    model = get_user_model()
    def get_success_url(self):
        query = get_user_model().objects.get(pk=self.request.user.pk)
        self.request.session['username'] = query.username
        #self.request.session['']
        url = resolve_url('farm:dashboard')
        return url

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('farm:login', permanent=True)

class AccountUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'farm:login'
    model = get_user_model()
    form_class = RegisterForm
    template_name = 'farm/account.html'
    success_url = reverse_lazy('farm:dashboard')

class Register(CreateView):
    template_name = 'farm/home/signup.html'
    form_class = RegisterForm
    model = get_user_model()
    success_url =  reverse_lazy('farm:login')


class FarmNew(LoginRequiredMixin,CreateView):
    login_url = 'farm:login'
    model = Farm
    form_class = FarmForm
    template_name = 'farm/farm/create.html'
    success_url = reverse_lazy('farm:all_farm')

class FarmList(LoginRequiredMixin,ListView):
    model = Farm
    login_url = 'farm:login'
    template_name = 'farm/farm/index.html'
    context_object_name = 'farmlist'

class FarmEdit(LoginRequiredMixin,UpdateView):
    model = Farm
    login_url = 'farm:login'
    template_name = 'farm/farm/edit.html'
    form_class = FarmForm
    success_url = reverse_lazy('farm:all_farm')    

#Staff Controller
class StaffNew(LoginRequiredMixin,CreateView):
    model  = Staff
    login_url = 'farm:login'
    form_class = StaffForm
    template_name = 'farm/staff/create.html'
    
class StaffSingle(LoginRequiredMixin,DetailView):
    model = Staff
    login_url = 'farm:login'
    template_name = 'farm/staff/single.html'
    context_object_name = 'staffer'

class Staffers(LoginRequiredMixin,ListView):
    model = Staff
    login_url = 'farm:login'
    template_name = 'farm/staff/index.html'
    context_object_name = 'staffs'

class StaffEdit(LoginRequiredMixin,UpdateView):
    model =Staff
    login_url = 'farm:login'
    template_name = 'farm/staff/edit.html'
    form_class =  StaffForm

class StaffDestroy (LoginRequiredMixin,View):
    login_url = 'farm:login'
    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect('farm:all_staff')

#Department Controller
class DepartmentNew(LoginRequiredMixin,CreateView):
    model = Department
    login_url = 'farm:login'
    form_class = DepartmentForm
    template_name  = 'farm/department/create.html'

class DepartmentDetail(LoginRequiredMixin,DetailView):
    model = Department
    login_url = 'farm:login'
    template_name = 'farm/department/index.html'
    context_object_name = 'dpt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        staff = Staff.objects.filter(department=pk)
        context["staffer"] = staff 
        return context
    

class DepartmentUpdate(LoginRequiredMixin,UpdateView):
    model = Department
    login_url = 'farm:login'
    template_name = 'farm/department/edit.html'
    form_class = DepartmentForm

class DepartmentDestroy(LoginRequiredMixin,View):
    login_url = 'farm:login'
    def get(self, request,pk):
        dept = Department.objects.get(pk=pk)
        dept.delete()
        return redirect('farm:dashboard')

#Produce Views

class AddProduce(LoginRequiredMixin,CreateView):
    model = Produce
    login_url = 'farm:login'
    form_class = ProduceForm
    template_name = 'farm/produce/create.html'
    success_url = reverse_lazy('farm:all_produce')

class UpdateProduce(LoginRequiredMixin,UpdateView):
    model = Produce
    login_url = 'farm:login'
    form_class = ProduceForm
    template_name = 'farm/produce/edit.html'
    success_url = reverse_lazy('farm:dashboard')

class ListProduce(LoginRequiredMixin,ListView):
    model = Produce
    login_url = 'farm:login'
    template_name = 'farm/produce/index.html'
    context_object_name = 'produce'


class ProduceDestroy(LoginRequiredMixin,View):
    login_url = 'farm:login'
    def get(self, request,pk):
        produce = Produce.objects.get(pk=pk)
        produce.delete()
        return redirect('farm:dashboard')

#Harvest Views
class AllHarvest(LoginRequiredMixin,ListView):
    model = TimeLine
    login_url = 'farm:login'
    template_name = 'farm/timeline/index.html'
    context_object_name = 'timelines'

class AddHarvest(LoginRequiredMixin,CreateView):
    login_url = 'farm:login'
    model = TimeLine
    template_name = 'farm/timeline/create.html'
    form_class = HarvestForm
    success_url = reverse_lazy('farm:harvests')

class EditHarvest(LoginRequiredMixin,UpdateView):
    login_url = 'farm:login'
    model = TimeLine
    template_name = 'farm/timeline/edit.html'
    form_class = HarvestForm
    success_url = reverse_lazy ('farm:harvests')


class DeleteHarvest(LoginRequiredMixin,View):
    login_url = 'farm:login'

    def get(self, request,pk):
        harvest = TimeLine.objects.get(pk=pk)
        harvest.delete()
        return redirect('farm:harvests')

class SingleHarvest(LoginRequiredMixin,DetailView):
    model = TimeLine
    login_url = 'farm:login'
    template_name = 'farm/timeline/single.html'
    context_object_name = 'harvest'

# Sales All
class SalesAdd(LoginRequiredMixin,CreateView):
    model = Sales
    login_url = 'farm:login'
    form_class = SalesForm
    template_name = 'farm/sales/create.html'
    success_url = reverse_lazy('farm:sales')
class SalesAll(LoginRequiredMixin,ListView):
    login_url = 'farm:login'
    model = Sales
    template_name = 'farm/sales/index.html'
    context_object_name = 'sales'

class SalesUpdate (LoginRequiredMixin,UpdateView):
    model = Sales
    login_url = 'farm:login'
    form_class = SalesForm
    template_name = 'farm/sales/edit.html'
    success_url = reverse_lazy ('farm:sales')

class DeleteSales(LoginRequiredMixin,View):
    login_url = 'farm:login'

    def get(self, request,pk):
        sale = Sales.objects.get(pk=pk)
        sale.delete()
        return redirect('farm:sales')

#Activities All

class ActivitiesAdd(LoginRequiredMixin,CreateView):
    model = Activities
    login_url = 'farm:login'
    form_class = ActivitiesForm
    template_name = 'farm/activities/create.html'
    success_url = reverse_lazy('farm:activities')

class ActivitiesAll(LoginRequiredMixin,ListView):
    login_url = 'farm:login'
    model = Activities
    template_name = 'farm/activities/index.html'
    context_object_name = 'activities'

class ActivitiesUpdate (LoginRequiredMixin,UpdateView):
    model = Activities
    login_url = 'farm:login'
    form_class = ActivitiesForm
    template_name = 'farm/activities/edit.html'
    success_url = reverse_lazy ('farm:activities')

class DeleteActivities(LoginRequiredMixin,View):
    login_url = 'farm:login'

    def get(self, request,pk):
        activity = Activities.objects.get(pk=pk)
        activity.delete()
        return redirect('farm:activities')



#Expenses All
class ExpensesAdd(LoginRequiredMixin,CreateView):
    model = Expenses
    login_url = 'farm:login'
    form_class = ExpensesForm
    template_name = 'farm/expenses/create.html'
    success_url = reverse_lazy('farm:expenses')
    
class ExpensesAll(LoginRequiredMixin,ListView):
    login_url = 'farm:login'
    model = Expenses
    template_name = 'farm/expenses/index.html'
    context_object_name = 'expenses'

class ExpensesUpdate (LoginRequiredMixin,UpdateView):
    model = Expenses
    login_url = 'farm:login'
    form_class = ActivitiesForm
    template_name = 'farm/expenses/edit.html'
    success_url = reverse_lazy ('farm:expenses')

class DeleteExpenses(LoginRequiredMixin,View):
    login_url = 'farm:login'

    def get(self, request,pk):
        expense = Expenses.objects.get(pk=pk)
        expense.delete()
        return redirect('farm:expenses')


#Creditors/Debitors
class DebtorsAdd(LoginRequiredMixin,CreateView):
    model = Debtors
    login_url = 'farm:login'
    form_class = DebtorsForm
    template_name = 'farm/credit/create.html'
    success_url = reverse_lazy('farm:debts')
class DebtorsAll(LoginRequiredMixin,ListView):
    model = Debtors
    login_url = 'farm:login'
    template_name = 'farm/credit/index.html'
    context_object_name = 'debts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = Debtors.objects.all().aggregate(Sum('amount'))
        return context
    

class DebtorsUpdate (LoginRequiredMixin,UpdateView):
    model = Debtors
    login_url = 'farm:login'
    form_class = DebtorsForm
    template_name = 'farm/credit/edit.html'
    success_url = reverse_lazy ('farm:debts')

class DeleteDebtors(LoginRequiredMixin,View):
    login_url = 'farm:login'
    def get(self, request,pk):
        debt = Debtors.objects.get(pk=pk)
        debt.delete()
        return redirect('farm:debts')



