from classes.agent import Agent
from classes.agreeableness_graph import AgreeablenessGraph
from classes.position import Position
from classes.zone import Zone
import json

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)

    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONES)


main()
