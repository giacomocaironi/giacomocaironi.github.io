from kart import Kart
from kart import miners, mappers, renderers

kart = Kart()


def blog_index(site):
    urls = {}
    posts = site["posts"][1:]
    try:
        per_page = site["config"]["pagination"]["per_page"]
    except Exception:
        per_page = 5
    urls.update(
        mappers.paginate(
            posts, per_page, "blog_index.html", "/blog" + "/index", "blog_index"
        )
    )
    return urls


def tags(site):
    urls = {}
    if "tags" not in site.keys():
        return urls
    site["config"]["tag_post_num"] = {}
    for tag in site["tags"]:
        posts = site["posts"]
        posts = [post for post in posts if tag["slug"] in post["tags"]]
        site["config"]["tag_post_num"][tag["slug"]] = len(posts)
        try:
            per_page = site["config"]["pagination"]["per_page"]
        except Exception:
            per_page = 5
        urls.update(
            mappers.paginate(
                posts,
                per_page,
                "tag.html",
                "/blog" + f"/tags/{tag['slug']}",
                f"tags.{tag['slug']}",
                additional_data=tag,
            )
        )
    return urls


kart.miners = [
    miners.DefaultPostMiner("posts"),
    miners.DefaultCollectionMiner("tags"),
    miners.DefaultCollectionMiner("projects"),
    miners.DefaultDataMiner(),
    miners.DefaultPageMiner(),
]

kart.mappers = [
    mappers.ManualMapper(rules=[tags, blog_index]),
    mappers.DefaultCollectionMapper(
        base_url="/blog", collection_name="posts", template="post.html"
    ),
    mappers.DefaultCollectionMapper(
        collection_name="projects", template="project.html"
    ),
    mappers.DefaultPageMapper(),
    mappers.DefaultFeedMapper(),
]

kart.renderers = [
    renderers.DefaultSiteRenderer(),
    renderers.DefaultFeedRenderer(collections=["posts", "projects"]),
]

kart.config["name"] = "Giacomo Caironi"
kart.config["base_url"] = "https://giacomocaironi.github.io"

kart.run()
