import os

from app import app
from lib.config import CONFIG
from lib.models import db, User, Article
from utils import random_datetime


def setup_db():
    if 'production' in os.getenv('APP_SETTINGS', '').lower() or CONFIG.ENVIRONMENT == 'production':
        app.logger.error('restore_staging_dataset cannot be used in production env!!!')
        exit()

    with app.app_context():
        db.drop_all()
        db.create_all()

        user = User(username='test', password='test')
        db.session.add(user)
        db.session.flush()  # required to create user_id

        db.session.add(Article(
            author_user_id=user.user_id,
            title='Article title',
            content='No Pulitzer candidate here, lets focus on the code.',
            release_date = random_datetime(),
        ))
        db.session.commit()

        titles = [
            "10 Things You Didn't Know About Python",
            "The Future of AI in Healthcare",
            "A Beginner's Guide to Data Science",
            "How to Improve Your Programming Skills",
            "The Impact of Social Media on Society",
            "Exploring the Latest Technologies in Robotics",
            "The Importance of Cybersecurity in the Digital Age",
            "Tips for Successful Remote Work",
            "Understanding Blockchain Technology",
            "The Rise of Virtual Reality: A New Era of Gaming"
        ]

        contents = [
            "Python is a versatile programming language...",
            "Artificial intelligence has made significant strides...",
            "Data science is a multidisciplinary field...",
            "Improving your programming skills requires dedication...",
            "Social media platforms have transformed communication...",
            "Robotics is advancing rapidly, with applications...",
            "Cybersecurity is crucial for protecting sensitive data...",
            "Remote work has become increasingly common...",
            "Blockchain is a decentralized ledger technology...",
            "Virtual reality technology is revolutionizing gaming..."
        ]

        for i in range(10):
            db.session.add(Article(
                author_user_id=user.user_id,
                title=titles[i],
                content=contents[i],
                release_date=random_datetime()
            ))
        db.session.commit()


if __name__ == '__main__':
    setup_db()
