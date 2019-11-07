from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from .models import BlogPost
from .froms import BlogPostForm, BlogUpdateForm
# Create your views here.


def index(request):
    ''' Blog Method
    '''
    blogs = BlogPost.objects.order_by('-created_on')[0:10]
    template_name = 'blog/index.html'
    return render(request, template_name, {'blogs': blogs})


def blogpost(request, blog_id):
    ''' fetches Blog Post by ID from database
    '''
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    template_name = 'blog/blogpost.html'
    return render(request, template_name, {'blog_post': blog_post})


def bloglist(request, author_id):
    ''' shows list of blog post from database with current user id
    '''
    blog_list = BlogPost.objects.filter(author=author_id)
    template_name = 'blog/bloglist.html'
    return render(request, template_name, {'blog_list': blog_list})


def blogpublish(request):
    '''
        Publish your blogs
    '''
    template_name = 'blog/blogpublish.html'
    blog_publish_form = BlogPostForm()
    if request.method == 'POST':
        blog_publish_form = BlogPostForm(request.POST, request.FILES)
        if blog_publish_form.is_valid():
            blog_publish_form.save()
            messages.success(request, 'Successfully Created')
            return redirect('blogpublish')
        else:
            messages.error(request, 'Error in form filling')
            return redirect('blogpublish')
    else:
        context = {'form': blog_publish_form}
        return render(request, template_name, context)


def blogupdate(request, id):
    '''
        Update Blog Details
    '''
    template_name = 'blog/blogupdate.html'
    blog_edit = BlogUpdateForm()

    try:
        blog_edit = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        return redirect('/bloglist/')
    blog_update_form = BlogUpdateForm(request.POST or None, instance=blog_edit)
    if blog_update_form.is_valid():
        blog_update_form.save()
        return redirect('/bloglist/')
    
    return render(request, template_name, {'form': blog_update_form})



def blogdelete(request, id):
    '''
        Delete Blog Details
    '''

    try:
        blog_del = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        return redirect('/bloglist/')
    blog_del.delete()
    return redirect('/bloglist/')

    
         