from django.db import models


class FeedBack(models.Model):
    full_name = models.CharField(max_length=256, verbose_name="Full name")
    phone = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name="Phone")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    active = models.BooleanField(default=True, verbose_name="Active")

    class Meta:
        db_table = "feedback"
        unique_together = ("full_name", "email", "active")
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"