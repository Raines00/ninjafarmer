from django.urls import path
from . import views

app_name = 'farm'

urlpatterns = [
    path('', views.Index.as_view(), name='index' ),
    path('administrator/login/', views.Login.as_view(), name='login'),
    #path('administrator/register/', views.Register.as_view(), name='register'),
    path("dashboard/", views.Dashboard.as_view(), name="dashboard"),
    path("dashboard/logout/", views.Logout.as_view(), name="logout"),
    path("dashboard/administrator/edit/<int:pk>/", views.AccountUpdate.as_view(), name="account_update"),

   
   #Farm Routes

   path("dashboard/farm/new", views.FarmNew.as_view(), name="create_farm"),
   path("dashboard/farm/", views.FarmList.as_view(), name="all_farm"),
   path("dashboard/farm/<int:pk>/edit/", views.FarmEdit.as_view(), name="farm_edit"),

   #Staff Path
   path("dashboard/staff/new/",views.StaffNew.as_view(), name="create_staff"),
   path("dashboard/staff/<int:pk>/single/", views.StaffSingle.as_view(), name="staff_single"),
   path("dashboard/staff/<int:pk>/edit/", views.StaffEdit.as_view(), name="staff_edit"),
   path("dashboard/staff/<int:pk>/delete/", views.StaffDestroy.as_view(), name="staff_delete"),
   path("dashboard/staff/", views.Staffers.as_view(), name="all_staff"),


   #Department Routes

   path("dashboard/department/new/",views.DepartmentNew.as_view(), name="create_dept"),
   path("dashboard/department/<int:pk>/single/",views.DepartmentDetail.as_view(), name="dept_single"),
   path("dashboard/department/<int:pk>/edit/",views.DepartmentUpdate.as_view(), name="dept_edit"),
   path("dashboard/department/<int:pk>/delete/",views.DepartmentDestroy.as_view(), name="dept_delete"),

   #Produce Routes
   path("dashboard/produce/add/",views.AddProduce.as_view(), name="create_produce"),
   path("dashboard/produce/all/",views.ListProduce.as_view(), name="all_produce"),
   path("dashboard/produce/<int:pk>/edit/",views.UpdateProduce.as_view(), name="edit_produce"),
   path("dashboard/produce/<int:pk>/delete/",views.ProduceDestroy.as_view(), name="delete_produce"),

   #Harvest TimeLine
   path("dashboard/harvest/all/",views.AllHarvest.as_view(), name="harvests"),
   path("dashboard/harvest/add/",views.AddHarvest.as_view(), name="add_harvest"),
   path("dashboard/harvest/<int:pk>/edit/",views.EditHarvest.as_view(), name="edit_harvest"),
   path("dashboard/harvest/<int:pk>/delete/",views.DeleteHarvest.as_view(), name="delete_harvest"),
   path("dashboard/harvest/<int:pk>/single/",views.SingleHarvest.as_view(), name="single_harvest"),

   #Sales Routes
   path("dashboard/sales/all/",views.SalesAll.as_view(), name="sales"),
   path("dashboard/sales/add/",views.SalesAdd.as_view(), name="create_sale"),
   path("dashboard/sales/<int:pk>/edit/",views.SalesUpdate.as_view(), name="edit_sale"),
   path("dashboard/sales/<int:pk>/delete/",views.DeleteSales.as_view(), name="delete_sale"),

   #Activities Routes
   path("dashboard/activities/all/",views.ActivitiesAll.as_view(), name="activities"),
   path("dashboard/activities/add/",views.ActivitiesAdd.as_view(), name="create_activity"),
   path("dashboard/activities/<int:pk>/edit/",views.ActivitiesUpdate.as_view(), name="edit_activity"),
   path("dashboard/activities/<int:pk>/delete/",views.DeleteActivities.as_view(), name="delete_activity"),


   #Expenses Routes
   path("dashboard/expenses/all/",views.ExpensesAll.as_view(), name="expenses"),
   path("dashboard/expenses/add/",views.ExpensesAdd.as_view(), name="create_expense"),
   path("dashboard/expenses/<int:pk>/edit/",views.ExpensesUpdate.as_view(), name="edit_expense"),
   path("dashboard/expenses/<int:pk>/delete/",views.DeleteExpenses.as_view(), name="delete_expense"),


   #Credit Sales
   path("dashboard/credit-sales/all/",views.DebtorsAll.as_view(), name="debts"),
   path("dashboard/credit-sales/add/",views.DebtorsAdd.as_view(), name="create_debt"),
   path("dashboard/credit-sales/<int:pk>/edit/",views.DebtorsUpdate.as_view(), name="edit_debt"),
   path("dashboard/credit-sales/<int:pk>/delete/",views.DeleteDebtors.as_view(), name="delete_debt")

]
