from kart import Kart
from kart import miners, mappers, renderers, modifiers

kart = Kart()


def tag_post_count(site):
    site["tag_post_count"] = {}
    for tag in site["tags"].values():
        posts = site["posts"].values()
        post_num = len([post for post in posts if tag["slug"] in post["tags"]])
        site["tag_post_count"][tag["slug"]] = post_num


kart.miners = [
    miners.DefaultCollectionMiner("posts"),
    miners.DefaultCollectionMiner("tags"),
    miners.DefaultCollectionMiner("projects"),
    miners.DefaultCollectionMiner("project_categories"),
    miners.DefaultDataMiner(),
    miners.DefaultPageMiner(),
]

kart.content_modifiers = [
    modifiers.RuleContentModifier([tag_post_count]),
    modifiers.CollectionSorter("posts", "date", True),
    modifiers.CollectionSorter("tags", "name"),
    modifiers.CollectionSorter("project_categories", "index"),
]

kart.mappers = [
    mappers.DefaultBlogMapper(base_url="/blog"),
    mappers.DefaultCollectionMapper(
        collection_name="projects", template="project.html"
    ),
    mappers.DefaultPageMapper(),
    mappers.DefaultFeedMapper(collections=["posts", "projects"]),
    mappers.ManualMapper(
        {
            "sitemap": {
                "url": "/sitemap.xml",
                "data": {},
                "template": "",
                "renderer": "default_sitemap_renderer",
            },
            "static": {
                "url": "/static/*",
                "data": {},
                "template": "",
                "renderer": "default_static_files_renderer",
            },
            "root": {
                "url": "/*",
                "data": {},
                "template": "",
                "renderer": "default_root_dir_renderer",
            },
        }
    ),
]

kart.map_modifiers = []

kart.renderers = [
    renderers.DefaultSiteRenderer(),
    renderers.DefaultFeedRenderer(),
    renderers.DefaultSitemapRenderer(),
    renderers.DefaultStaticFilesRenderer(),
    renderers.DefaultRootDirRenderer(),
]

kart.config["name"] = "Giacomo Caironi"
kart.config["base_url"] = "https://giacomocaironi.github.io"

kart.run()
