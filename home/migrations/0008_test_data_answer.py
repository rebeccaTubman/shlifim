from django.db import migrations, transaction
from django.utils import timezone


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0007_answer'),
    ]

    def generate_data(apps, schema_editor):
        from home.models import Profile, Question, Answer

        answer_test_data = [(1, 1, 'pretty sure its 2 but I suggesting you to check with another resources ',
                            timezone.now(), [1, 2], [3, 4], False),
                            (2, 2, 'IDK', timezone.now(), [1], None, False),
                            ]

        with transaction.atomic():

            for (user_id, question, content, publish_date, likes_profiles,
                 dislike_profiles, is_edited) in answer_test_data:
                curr_question = Question.objects.get(id=question)
                profile = Profile.objects.get(user=user_id)
                answer = Answer(profile=profile, question=curr_question, content=content, publish_date=publish_date,
                                is_edited=is_edited)
                answer.save()

                if likes_profiles is not None:
                    for profile_id in likes_profiles:
                        answer.likes.add(profile_id)

                if dislike_profiles is not None:
                    for profile_id in dislike_profiles:
                        answer.dislikes.add(profile_id)

    operations = [
        migrations.RunPython(generate_data),
    ]
