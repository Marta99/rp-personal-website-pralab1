from django.shortcuts import render
from apps.blog import models, forms


# Create your views here.
def post_list(request):
    posts = models.Post.objects.all().order_by('-created_on')

    context = {
        'posts': posts

    }

    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    post = models.Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment(author=form.cleaned_data['author'], body=form.cleaned_data['body'], post=post)
            comment.save()

    comments = models.Comment.objects.filter(post=post)
    form = forms.CommentForm()

    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'post_detail.html', context)


def category_post_list(request, category):
    posts = models.Post.objects.filter(categories__name__contains=category).order_by('-created_on')

    context = {'category': category, 'posts': posts}

    return render(request, 'category_post_list.html', context)
