# mini_fb/models.py
# define data models (objects) for use in the mini_fb application

from django.db import models
from django.urls import reverse

class Profile(models.Model):
    '''Encapsulate the data for a user profile.'''
    # This Profile model will include the following data attributes: 
    # first name, last name, city, email address, and a profile image url.

    first_name = models.TextField(blank=False) # field is required
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    image_url = models.URLField(blank=True) # field is optional

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.first_name} {self.last_name}"

    # an accessor method get_status_messages to obtain all status messages for this Profile.
    def get_status_messages(self):
        '''Return all status messages for this Profile.'''
        status_messages = StatusMessage.objects.filter(profile=self).order_by('-timestamp')
        return status_messages

    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        # return reverse('show_all_profiles')
        return reverse('show_profile', kwargs={'pk': self.pk})

    def get_friends(self):
        '''Return a list of friend’s profiles.'''
        friends = Friend.objects.filter(profile1=self) | Friend.objects.filter(profile2=self)
        return friends

    def add_friend(self, other):
        '''Add a new friend relationship.'''
        if not (self == other):
            if not Friend.objects.filter(profile1=self, profile2=other).exists():
                friend = Friend(profile1=self, profile2=other)
                friend.save()

    def get_friend_suggestions(self):
        '''Return a list of friend suggestions.'''
        friends = self.get_friends()
        friend_pks = [f.profile1.pk if f.profile1 != self else f.profile2.pk for f in friends]
        suggestions = Profile.objects.all().exclude(pk=self.pk).exclude(pk__in=friend_pks)
        return suggestions

    # method get_news_feed(self) on the Profile object, which will return a list (or QuerySet) of all StatusMessages for the profile on which the method was called, as well as all of the friends of that profile.

    # Hint: it will be easiest to develop this by using the ORM to filter StatusMessages.


    def get_news_feed(self):
        '''Return a list (or QuerySet) of all StatusMessages for the profile on which the method was called, as well as all of the friends of that profile.'''
        friends = self.get_friends()
        friend_pks = [f.profile1.pk if f.profile1 != self else f.profile2.pk for f in friends]
        news_feed = StatusMessage.objects.filter(profile__in=friend_pks) | StatusMessage.objects.filter(profile=self)
        print(news_feed)
        return news_feed



class StatusMessage(models.Model):
    '''Encapsulate the data for a status message.'''
    # timestamp (the time at which this status message was created/saved)
    # message (the text of the status message)
    # profile (the foreign key to indicate the relationship to the Profile of the creator of this message)

    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.message}"

    def get_images(self):
        '''Retrieve all comments for this status.'''
        # use the ORM to filter Images where this object is the FK
        images = Image.objects.filter(status_message=self)
        return images


class Image(models.Model):
    '''Encapsulate the data for an image model.'''

    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"image for '{self.status_message}' message for {self.status_message.profile}"



class Friend(models.Model):
    '''Encapsulate the data for a friend relationship.'''
    profile1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile1")
    profile2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile2")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.profile1} and {self.profile2}"





