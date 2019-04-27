class Agent:
    def __init__(self, agreeableness):
        self.agreeableness = agreeableness

    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"


agent = Agent(0)

print(agent.say_hello('Romain'))
print(agent.agreeableness)
