from django.contrib import admin
from django import forms
from django.db.models import Count
from django.db import connection
from .models import User,Post,Notification,Like,Comment

def get_user_by_id(userid):
    with connection.cursor() as cursor:
        cursor.callproc('add_user_proc', [userid])
        results = cursor.fetchall()
    return results
def update_user(userid):
    with connection.cursor() as cursor:
        cursor.callproc('UpdateUser', [userid])
        results = cursor.fetchall()
    return results
class userAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'dateofbirth': forms.SelectDateWidget(years=range(1900, 2100)),  # replace 'dateofbirth' with your actual date field name if different
            'joindate': forms.SelectDateWidget(years=range(1900, 2100))  # replace 'dateofbirth' with your actual date field name if different
        }
class userAdmin(admin.ModelAdmin):
    form = userAdminForm
    list_display = ['userid','firstname','lastname','email','passwordhash','joindate','username','dateofbirth','gender','bio','profilepictureurl','websiteurl','phonenumber','user_privacysetting','user_accountstatus','user_accounttype']
    search_fields = ['userid','firstname','lastname','email','passwordhash','joindate','username','dateofbirth','gender','bio','profilepictureurl','websiteurl','phonenumber','user_privacysetting','user_accountstatus','user_accounttype']
    list_filter = ['userid','firstname','lastname','email','passwordhash','joindate','username','dateofbirth','gender','bio','profilepictureurl','websiteurl','phonenumber','user_privacysetting','user_accountstatus','user_accounttype']
    list_per_page = 10
class postAdmin(admin.ModelAdmin):
    list_display = ['postid','post_content','post_userid','get_likes_count','get_comment_count','mediaurl','post_time_stamp','post_privacysetting']
    search_fields = ['postid','post_content','post_userid','mediaurl','post_time_stamp','post_privacysetting']
    list_filter = ['postid','post_content','post_userid','mediaurl','post_time_stamp','post_privacysetting']
    list_per_page = 10
    def get_likes_count(self, obj):
        return Like.objects.filter(like_postid=obj.postid).count()
    get_likes_count.short_description = 'No. of Likes'
    def get_comment_count(self, obj):
        return Comment.objects.filter(comment_postid=obj.postid).count()
    get_comment_count.short_description = 'No. Of Comments'

class notificationAdmin(admin.ModelAdmin):
    list_display = ['notificationid','notification_userid','noti_type','time_stamp','isread']
    search_fields = ['notificationid','notification_userid','noti_type','time_stamp','isread']
    list_filter = ['notificationid','notification_userid','noti_type','time_stamp','isread']
    list_per_page = 10
class likeAdmin(admin.ModelAdmin):
    list_display = ['likeid','like_postid','time_stamp','like_userid']
    search_fields = ['likeid','like_postid','time_stamp','like_userid']
    list_filter = ['likeid','like_postid','time_stamp','like_userid']
    list_per_page = 10
class commentAdmin(admin.ModelAdmin):
    list_display = ['commentid','comment_postid','time_stamp','comment_content']
    search_fields = ['commentid','comment_postid','time_stamp','comment_content']
    list_filter = ['commentid','comment_postid','time_stamp','comment_content']
    list_per_page = 10
admin.site.register(User, userAdmin)
admin.site.register(Post, postAdmin)
admin.site.register(Like, likeAdmin)
admin.site.register(Comment, commentAdmin)
admin.site.register(Notification, notificationAdmin)