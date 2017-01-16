
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from blog_apps.models import Post


from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from blog_apps.models import Commentary


class PostList(ListView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'user']
    success_url = reverse_lazy('blog_apps:post_list')


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body', 'user']
    success_url = reverse_lazy('blog_apps:post_list')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_apps:post_list')


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ['commentary', 'post', 'user']


def commentary_list(request, template_name='blog_apps2/comment_list.html'):
    commentary = Commentary.objects.all()
    data = {}
    data['object_list'] = commentary
    return render(request, template_name, data)


def commentay_create(request, template_name='blog_apps2/comment_form.html'):
    form = CommentaryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_apps:commentary_list')
    return render(request, template_name, {'form': form})


def commentary_update(request, pk, template_name='blog_apps2/comment_form.html'):
    commentary = get_object_or_404(Commentary, pk=pk)
    form = CommentaryForm(request.POST or None, instance=commentary)
    if form.is_valid():
        form.save()
        return redirect('blog_apps:commentary_list')
    return render(request, template_name, {'form': form})


def commentary_delete(request, pk, template_name='blog_apps2/comment_confirm_delete.html'):
    commentary = get_object_or_404(Commentary, pk=pk)
    if request.method=='POST':
        commentary.delete()
        return redirect('blog_apps:commentary_list')
    return render(request, template_name, {'object':commentary})


class Home(TemplateView):

    template_name = 'main/home.html'
