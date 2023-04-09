from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import CommentForm
from .forms import PostForm
from .models import Post, Category
from django.db.models import Q

def home(request):
    recent_posts = Post.objects.order_by('-date_added')[:4]
    context = {'recent_posts': recent_posts}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def essential_elements(request):
    return render(request, 'resource-1.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'portfolio.html')

def image_civil_engineering(request):
    return render(request, 'portfolio-details.html')

def mambwe_chafs_portfolio(request):
    return render(request, 'portfolio-details-1.html')

def python_password_checker(request):
    return render(request, 'portfolio-details-2.html')

def python_web_scraper(request):
    return render(request, 'portfolio-details-3.html')

def python_email_sender(request):
    return render(request, 'portfolio-details-4.html')

def eco_first_innovations(request):
    return render(request, 'portfolio-details-5.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Send an email with the form data
        try:
            send_mail(
                subject=subject,
                message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return render(request, 'contact.html', {'sent': True})
        except Exception as e:
            return render(request, 'contact.html', {'error': True})
    else:
        return render(request, 'contact.html')
    


class Blog(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['-date_added']
    paginate_by = 6
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context['object_list']
        paginator = Paginator(posts, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        categories = Category.objects.all()
        context['page_obj'] = page_obj
        context['categories'] = categories
        return context
    


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        try:
            post = self.model.objects.get(slug=slug)
        except self.model.MultipleObjectsReturned:
            raise Http404("Multiple posts found matching the slug.")
        except self.model.DoesNotExist:
            raise Http404("Post not found.")
        return post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect(reverse_lazy('post_detail', kwargs={'slug': self.object.slug}))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})
    


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update.html'
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')



class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'

class CategoryView(ListView):
    paginate_by = 6
    ordering = ['-date_added']
    template_name = 'blog/categories.html'

    def get(self, request, cats):
        category = get_object_or_404(Category, name=cats.replace('-', ' '))
        category_posts = Post.objects.filter(category=category)
        post_count = category_posts.count()

        paginator = Paginator(category_posts, self.paginate_by)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        categories = Category.objects.all()

        context = {
            'category': category,
            'category_posts': page_obj,
            'post_count': post_count,
            'categories': categories,
        }
        return render(request, self.template_name, context)
    
