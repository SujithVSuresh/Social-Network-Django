from django.urls import path 
from . views import AddFollower, CommentReplyFormView, PostEditView, PostListView, PostDetailView, PostDeleteView, CommentDeleteView, ProfileEditView, ProfileView, RemoveFollower, AddLike, AddDisLike, UserSearch, ListFollowers, AddCommentDisLike, AddCommentLike, PostNotification, FollowNotification

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/comment-reply', CommentReplyFormView.as_view(), name='comment-reply-form'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDisLike.as_view(), name='comment-dislike'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDisLike.as_view(), name='dislike'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers', ListFollowers.as_view(), name='list-followers'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('notification/<int:notification_pk>/post/<post_pk>', PostNotification.as_view(), name='post-notification'),
    path('notification/<int:notification_pk>/profile/<profile_pk>', FollowNotification.as_view(), name='follow-notification')
]