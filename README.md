# Bazinga
Bazinga is a cult where we commit to Bazingor the Great through offerings of media.
. .venv/bin/activate
python manage.py runserver
pip3 freeze > requirements.txt
create environment variables MAIL_PASSWORD in .env file
pip install -r requirments.txt
python manage.py makemigrations videos
python manage.py migrate videos
python manage.py shell
from videos.models import Video

first_video = Video(
    title="My First video",
    description="A video.",
    link="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
)
second_video = Video(
    title="My Second video",
    description="A video.",
    link="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
)
third_video = Video(
    title="My Third video",
    description="A video.",
    link="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
)
first_video.save()
second_video.save()
thrid_video.save()
