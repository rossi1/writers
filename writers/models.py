from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class WritersProfile(models.Model):
    profile_id = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile',
    on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    headline = models.CharField(max_length=30)
    about = models.TextField()

    def __str__(self):
        return str(self.profile_id)


class Rating(models.Model):
    rating_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rating')
    reviews = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return str(self.reviews)


class Orders(models.Model):
    order_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order')
    num_of_orders_completed = models.IntegerField(default=0)
    rating_writer = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='rate')
    orders_completed = models.BooleanField(default=False)


    def __str__(self):
        return str(self.orders_completed)

    
class Bids(models.Model):
    writer_bids = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='writer_bids')

    def __str__(self):
        return str(self.writer_bids)



