from datetime import datetime
from http import HTTPStatus

from connexion import NoContent
from flask import request
from lib.models import Article, db


def get(user):
    query = Article.query

    query = query.filter(
        Article.author_user_id == user['user_id'],
    )
    if request.args.get('release_date__year'):
        query = query.filter(
            db.extract('year', Article.release_date) == request.args.get('release_date__year'),
        )

    articles = query.all()

    return [
       {
           'article_id': article.article_id,
           'title': article.title,
           'content': article.content,
           'release_date': article.release_date_str,
       }
       for article in articles
    ], HTTPStatus.OK


def post(user, body):
    release_date_body = body.get('release_date')
    release_date = None
    if release_date_body:
        release_date = datetime.strptime(release_date_body, '%Y-%m-%d %H:%M:%S')
    db.session.add(Article(
        author_user_id=user['user_id'],
        title=body['title'],
        content=body['content'],
        release_date=release_date,
    ))
    db.session.commit()

    return NoContent, HTTPStatus.OK


def put(user, article_id, body):
    article = Article.query.filter(
        Article.article_id == article_id,
        Article.author_user_id == user['user_id'],
    ).first()

    if not article:
        return NoContent, HTTPStatus.NOT_FOUND

    article.title = body['title']
    article.content = body['content']
    release_date_body = body.get('release_date')
    release_date = None
    if release_date_body:
        release_date = datetime.strptime(release_date_body, '%Y-%m-%d %H:%M:%S')
    article.release_date = release_date
    db.session.commit()

    return NoContent, HTTPStatus.OK


def delete(user, article_id):
    Article.query.filter(
        Article.article_id == article_id,
        Article.author_user_id == user['user_id'],
    ).delete()

    db.session.commit()
    return NoContent, HTTPStatus.OK


