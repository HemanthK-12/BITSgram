# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    commentid = models.AutoField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    comment_postid = models.ForeignKey('Post', models.DO_NOTHING, db_column='Comment_PostID', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(db_column='Time_Stamp', blank=True, null=True)  # Field name made lowercase.
    comment_content = models.CharField(db_column='Comment_Content', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Like(models.Model):
    likeid = models.AutoField(db_column='LikeID', primary_key=True)  # Field name made lowercase.
    like_postid = models.ForeignKey('Post', models.DO_NOTHING, db_column='Like_PostID', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(db_column='Time_Stamp', blank=True, null=True)  # Field name made lowercase.
    like_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='Like_UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'like'


class Notification(models.Model):
    notificationid = models.AutoField(db_column='NotificationID', primary_key=True)  # Field name made lowercase.
    notification_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='Notification_UserID', blank=True, null=True)  # Field name made lowercase.
    noti_type = models.CharField(db_column='Noti_Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(db_column='Time_Stamp', blank=True, null=True)  # Field name made lowercase.
    isread = models.CharField(db_column='isRead', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notification'


class Post(models.Model):
    postid = models.AutoField(db_column='PostID', primary_key=True)  # Field name made lowercase.
    post_content = models.CharField(db_column='Post_Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    post_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='Post_UserID', blank=True, null=True)  # Field name made lowercase.
    mediaurl = models.CharField(db_column='MediaURL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    post_time_stamp = models.DateTimeField(db_column='post_Time_stamp', blank=True, null=True)  # Field name made lowercase.
    post_privacysetting = models.CharField(db_column='post_PrivacySetting', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PassWordHash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bio = models.CharField(db_column='Bio', max_length=300, blank=True, null=True)  # Field name made lowercase.
    profilepictureurl = models.CharField(db_column='ProfilePictureUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='WebsiteURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.BigIntegerField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    user_privacysetting = models.CharField(db_column='user_PrivacySetting', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_accountstatus = models.CharField(db_column='user_AccountStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_accounttype = models.CharField(db_column='user_AccountType', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
