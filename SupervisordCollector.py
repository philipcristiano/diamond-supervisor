import diamond
import xmlrpclib


class SupervisordCollecor(diamond.collector.Collector):
    """Collects data from supervisord."""

    def collect(self):
        server = xmlrpclib.Server('http://localhost:9001')
        states = server.getAllProcessInfo()

        state_counts = {}

        for state in states:
            statename = state['statename']
            state_counts[statename] = state_counts.get(statename, 0) + 1

        for statename, count in state_counts.items():
            self.publish('statename', count)
