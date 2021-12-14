from django.views import View
from django.views.generic.edit import DeleteView
from .models import Todo


'''View'''
'''به درد ویو های ساده میخوره'''
# class Hello(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'todo/home.html')


from django.views.generic.base import TemplateView

'''TemplateView'''
'''امکان کوئری نوشتن را به ما میدهد'''
# class Hello(TemplateView):
#     template_name = 'todo/home.html'

#     def get_context_data(self, **kwargs):
#         contex = super().get_context_data(**kwargs)
#         contex['TODO'] = Todo.objects.all()
#         return contex


from django.views.generic.list import ListView
'''ListView'''
"""امکان این که بدون کوئری نوشتن یک لیست از یک مدل را به کاربر نشان دهیم"""
class Hello(ListView):
    template_name = 'todo/home.html'

    #query
    '''way1 : '''
    model = Todo

    '''way2 : '''
    queryset = Todo.objects.all() # object_list
    context_object_name = 'TODO'

    #ordering
    ordering = ['-created']


from django.views.generic.detail import DetailView
'''DetailView'''
"""امکان نشان دادن جزئیات هر پست را به کاربر میدهد اما فقط در یو ار ال میتواند ایدی یا اسلاگ دریافت کند"""
class HelloDetail(DetailView):
    model = Todo
    template_name = 'todo/home_detail.html'
    context_object_name = 'TODO'

    slug_field = 'slug'
    slug_url_kwarg = 'my_slug'


from django.views.generic import FormView
from .models import Todo
from .forms import Todo_form
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
'''FormView'''
'''way1'''
class CreateForm(View):
    def get(self):
        pass
    def post(self):
        pass
'''way2'''
class CreateForm(FormView):
    form_class = Todo_form
    template_name = 'todo/create_home.html'
    success_url = reverse_lazy('todo:todo_view') #redirect in class base

    def form_valid(self, form):
        self.save_data(form.cleaned_data)
        return super().form_valid(form)

    def save_data(self, data):
        new_todo = Todo(title=data['title'], slug=slugify(data['title']))
        new_todo.save()
        messages.success(self.request, 'your todo added', 'success')



from django.views.generic import CreateView
'''CreateView'''
class CreateAddForm(CreateView):
    model = Todo
    fields = ['title']
    template_name = 'todo/create_home.html'
    success_url = reverse_lazy('todo:todo_view')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request, 'your todo added', 'success')
        return super().form_valid(form)


from django.views.generic import DeleteView
'''DeleteView'''
'''به طور پیشفرض بجای ارسال کانتکس به اچ تی ام ال آبجکت ارسال میشود'''
class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'todo/delete_todo.html'
    success_url = reverse_lazy('todo:todo_view')
    # context_object_name = 'TODO'


from django.views.generic import UpdateView
'''UpdateView'''
class UpdateTodo(UpdateView):
    model = Todo
    fields = ('title')
    template_name = 'todo/update_todo.html'
    success_url = reverse_lazy('todo:todo_view')
