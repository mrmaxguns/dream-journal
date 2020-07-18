import datetime
import re
from collections import OrderedDict

import markdown2
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///entries.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Dream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    tags = db.Column(db.Text, unique=False, nullable=False)
    characters = db.Column(db.Text, unique=False, nullable=False)
    locations = db.Column(db.Text, unique=False, nullable=False)
    type = db.Column(db.String(200), unique=False, nullable=False)
    dream_date = db.Column(db.DateTime)

    def __repr__(self):
        return "<Dream %r>" % self.title


def create_db():
    db.create_all()


def parse_tags(data, mode="enc"):
    if mode == "enc":
        return ",".join(data)
    return [i.lower().strip() for i in data.split(",")]


def get_raw_data_by_id(id):
    dream = Dream.query.filter_by(id=id).first_or_404()
    return {
        "id": dream.id,
        "title": dream.title,
        "content": dream.content,
        "tags": dream.tags,
        "characters": dream.characters,
        "locations": dream.locations,
        "type": dream.type,
        "date": dream.dream_date.strftime("%Y-%m-%d"),
    }


def filter_query(query):
    query = query.strip()
    filtered_query = re.sub("\?|\.|!", "", query)
    lowercase_query = query.lower()
    return lowercase_query


@app.route("/")
def index():
    dreams = Dream.query.order_by(Dream.dream_date).all()
    dreams.reverse()
    dream_data = OrderedDict()

    for dream in dreams:
        dream_data[str(dream.id)] = {
            "title": dream.title,
            "date": dream.dream_date,
            "tags": parse_tags(dream.tags, mode="dec"),
            "excerpt": dream.content[:100],
        }

    return render_template("index.html", dreams=dream_data)


@app.route("/dreams/<dream_id>")
def dream_page(dream_id):
    dream = Dream.query.filter_by(id=dream_id).first_or_404()
    dream_data = {
        "id": dream.id,
        "title": dream.title,
        "content": markdown2.markdown(dream.content),
        "tags": dream.tags,
        "characters": parse_tags(dream.characters, mode="dec"),
        "locations": parse_tags(dream.locations, mode="dec"),
        "type": dream.type,
        "date": dream.dream_date.strftime("%m / %d / %Y"),
    }
    return render_template("dream.html", dream_data=dream_data)


@app.route("/edit/<dream_id>", methods=["GET", "POST"])
def edit_dream(dream_id):
    if request.method == "POST":
        dream = Dream.query.filter_by(id=dream_id).first_or_404()

        dream_date = request.form["date"]

        for item in Dream.query.all():
            if item.title == request.form["title"] and item.id != dream.id:
                dream_prefill = request.form.copy()
                dream_prefill["id"] = dream.id
                return render_template(
                    "edit_dream.html", dream_prefill=dream_prefill, duplicate_title=True
                )

        dream.title = request.form["title"]
        dream.content = request.form["content"]
        dream.tags = request.form["tags"]
        dream.characters = request.form["characters"]
        dream.locations = request.form["locations"]
        dream.type = request.form["type"]
        dream.dream_date = datetime.datetime.strptime(dream_date, "%Y-%m-%d")

        db.session.commit()

        return redirect(url_for("dream_page", dream_id=dream_id))

    return render_template(
        "edit_dream.html", dream_prefill=get_raw_data_by_id(dream_id)
    )


@app.route("/create/", methods=["GET", "POST"])
def create_dream():
    if request.method == "POST":
        # check duplicate title
        for item in Dream.query.all():
            if item.title == request.form["title"]:
                dream_prefill = request.form.copy()
                return render_template(
                    "create_dream.html",
                    dream_prefill=dream_prefill,
                    duplicate_title=True,
                )

        new_dream = Dream(
            title=request.form["title"],
            content=request.form["content"],
            tags=request.form["tags"],
            characters=request.form["characters"],
            locations=request.form["locations"],
            type=request.form["type"],
            dream_date=datetime.datetime.strptime(request.form["date"], "%Y-%m-%d"),
        )

        db.session.add(new_dream)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("create_dream.html", dream_prefill={})


@app.route("/delete/<dream_id>", methods=["GET", "POST"])
def delete_dream(dream_id):
    to_delete = Dream.query.filter_by(id=dream_id).first_or_404()
    if request.method == "POST":
        db.session.delete(to_delete)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("delete_dream.html", id=dream_id)


@app.route("/search")
def search():
    query = request.args.get("q")
    if query is None:
        return render_template("search.html", searched=False, results=[])
    else:
        dream_ids = {}
        query_list = filter_query(query).split()

        for dream in Dream.query.all():
            matched_items = []
            for item in query_list:
                matched_items.extend(re.findall(item, dream.content.lower()))
                matched_items.extend(re.findall(item, dream.title.lower()))
            dream_ids[dream.id] = len(matched_items)

        sorted_dream_ids = []
        for key, value in sorted(dream_ids.items(), key=lambda item: item[1]):
            sorted_dream_ids.append((key, value))
        sorted_dream_ids.reverse()

        for id in sorted_dream_ids[:]:
            if id[1] == 0:
                sorted_dream_ids.remove(id)

        search_result_data = {}
        for i in sorted_dream_ids:
            query_dream = Dream.query.filter_by(id=i[0]).first()
            search_result_data[query_dream.id] = {
                "title": query_dream.title,
                "excerpt": query_dream.content[:100],
            }

        return render_template(
            "search.html",
            searched=True,
            results=sorted_dream_ids,
            result_data=search_result_data,
        )


@app.route("/filter")
def filter_by():
    filter_by = request.args.get("by")
    query = request.args.get("q")

    if filter_by is None and query is None:
        return render_template("filter.html", results=[])

    if filter_by is None or query is None:
        return render_template("filter.html", results=[], error=True)

    query = filter_query(query)

    if filter_by == "tag":
        results = []
        for dream in Dream.query.all():
            if query in parse_tags(dream.tags, mode="dec"):
                results.append(dream)

        return render_template("filter.html", results=results)
    elif filter_by == "char":
        results = []
        for dream in Dream.query.all():
            if query in parse_tags(dream.characters, mode="dec"):
                results.append(dream)

        return render_template("filter.html", results=results)
    elif filter_by == "loc":
        results = []
        for dream in Dream.query.all():
            if query in parse_tags(dream.locations, mode="dec"):
                results.append(dream)

        return render_template("filter.html", results=results)
    elif filter_by == "type":
        results = []
        for dream in Dream.query.all():
            if query in parse_tags(dream.type, mode="dec"):
                results.append(dream)

        return render_template("filter.html", results=results)
    else:
        return render_template("filter.html", results=[], error=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
