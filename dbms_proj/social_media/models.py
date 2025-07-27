from django.db import models

class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PassWordHash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True, null=True, unique=True)  # Field name made lowercase.
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
    def __str__(self):
        return str(self.userid)

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
    def __str__(self):
        return str(self.postid)

class Notification(models.Model):
    notificationid = models.AutoField(db_column='NotificationID', primary_key=True)  # Field name made lowercase.
    notification_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='Notification_UserID', blank=True, null=True)  # Field name made lowercase.
    noti_type = models.CharField(db_column='Noti_Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(db_column='Time_Stamp', blank=True, null=True)  # Field name made lowercase.
    isread = models.CharField(db_column='isRead', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notification'
    def __str__(self):
        return self.noti_type

class Like(models.Model):
    likeid = models.AutoField(db_column='LikeID', primary_key=True)  # Field name made lowercase.
    like_postid = models.ForeignKey('Post', models.DO_NOTHING, db_column='Like_PostID', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(db_column='Time_Stamp', blank=True, null=True)  # Field name made lowercase.
    like_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='Like_UserID', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'like'

class Comment(models.Model):
    commentid = models.AutoField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    comment_postid = models.ForeignKey('Post', models.DO_NOTHING, db_column='Comment_PostID', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(db_column='Time_Stamp', blank=True, null=True)  # Field name made lowercase.
    comment_content = models.CharField(db_column='Comment_Content', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'