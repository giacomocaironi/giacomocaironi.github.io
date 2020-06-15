from kart import Kart
from kart import miners, mappers, renderers, modifiers

kart = Kart()


def tag_dict(site):
    site["tag_post_count"] = {}
    for tag in site["tags"]:
        posts = site["posts"]
        post_num = len([post for post in posts if tag["slug"] in post["tags"]])
        site["tag_post_count"][tag["slug"]] = post_num


kart.miners = [
    miners.DefaultPostMiner("posts"),
    miners.DefaultCollectionMiner("tags"),
    miners.DefaultCollectionMiner("projects"),
    miners.DefaultDataMiner(),
    miners.DefaultPageMiner(),
]

kart.mappers = [
    mappers.DefaultBlogMapper(base_url="/blog"),
    mappers.DefaultCollectionMapper(
        collection_name="projects", template="project.html"
    ),
    mappers.DefaultPageMapper(),
    mappers.DefaultFeedMapper(),
]

kart.modifiers = [modifiers.TagModifier(), modifiers.RuleModifier([tag_dict])]

kart.renderers = [
    renderers.DefaultSiteRenderer(),
    renderers.DefaultFeedRenderer(collections=["posts", "projects"]),
    renderers.DefaultSitemapRenderer(),
]

kart.config["name"] = "Giacomo Caironi"
kart.config["base_url"] = "https://giacomocaironi.github.io"

kart.run()
