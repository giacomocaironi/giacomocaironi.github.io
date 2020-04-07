from kart import Kart
from kart import miners, mappers

kart = Kart()

kart.miners.extend([miners.DefaultCollectionMiner("projects")])

kart.mappers[0].base_url = "/blog"
kart.mappers.extend(
    [
        mappers.DefaultCollectionMapper(
            collection_name="projects", template="project.html"
        ),
        # mappers.ManualMapper([]),
    ]
)

kart.config["name"] = "Giacomo Caironi"
kart.config["base_url"] = "https://giacomocaironi.github.io"

kart.run()
