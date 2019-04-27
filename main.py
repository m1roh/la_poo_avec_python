import json
from classes.agent import Agent
from classes.position import Position
from classes.zone import Zone


def main():
    Zone.initialize()
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        print('Zone population : ', zone.population)


main()
