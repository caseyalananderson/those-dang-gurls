from django.shortcuts import render

from .models import BeautyPost
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect

# Pertaining to Comments
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from comments.forms import CommentForm
from comments.models import Comment

# For Pagination
from django.core.paginator import Paginator
# Login Required
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def beautypost_list(request):
    """
    Main index that displays blog post.
    Grabs "filter" from cookies in order to filter the query of the database
    :param request:
    :return:
    """

    beauty_posts = BeautyPost.objects.published()
    paginator = Paginator(beauty_posts, 6)  # Show 3 contacts per page

    page_number = request.GET.get('page')

    if page_number is not None:
        pagnated_beauty_posts = paginator.page(page_number)
    else:
        pagnated_beauty_posts = paginator.page(1)

    context = {
        'posts': pagnated_beauty_posts,
    }

    return render(request, 'post_list.html', context)


# Create your views here.
@login_required
def beautypost_detail(request, pk):
    """
    Main index that displays beauty blog post
    :param request: django request
    :param pk: Primary key of the food post
    :return:
    """

    instance = get_object_or_404(BeautyPost, pk=pk)
    thumbnail = instance.cover_photo
    comments = instance.comments

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }

    comment_form = CommentForm(request.POST or None, initial=initial_data)

    if comment_form.is_valid():  # If the comment form is valid
        parent_obj = None
        c_type = comment_form.cleaned_data.get("content_type")
        try:  # TODO: Hack to fix <food entry> -> <foodentry> ContentType
            content_type = ContentType.objects.get(model=c_type)
        except:
            content_type = ContentType.objects.get(model=c_type.replace(' ', ''))
        obj_id = comment_form.cleaned_data.get("object_id")

        try:  # Get the id of the parent comment
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:  # Verify parent id exists, get the first
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        content_data = comment_form.cleaned_data.get("content")

        if request.user.username:  # Must be logged in to post comment
            new_comment, created = Comment.objects.get_or_create(
                user=request.user,
                content_type=content_type,
                object_id=obj_id,
                content=content_data,
                parent=parent_obj,
            )
            return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
        else:
            return HttpResponseRedirect('.')

    context = {
        'post': instance,
        'thumbnail': thumbnail,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'post_detail.html', context)
