from entities.graph import Graph, GraphFactory
from utils.singleton import singleton

@singleton
class GraphletTemplates():
    def __init__(self):
        self.initialized = False
        self.graphlets : dict[int, Graph] = dict()

    def list(self) -> dict[int, Graph]:
        if self.initialized:
            return self.graphlets

        self.graphlets[0] = GraphFactory().create_instance_with_sets(2, [[0,1]])
        self.graphlets[1] = GraphFactory().create_instance_with_sets(3, [[0,1],[1,2]])
        self.graphlets[2] = GraphFactory().create_instance_with_sets(3, [[0,1],[1,2],[0,2]])
        self.graphlets[3] = GraphFactory().create_instance_with_sets(4, [[0,1],[1,2],[2,3]])
        self.graphlets[4] = GraphFactory().create_instance_with_sets(4, [[0,1],[0,2],[0,3]])
        self.graphlets[5] = GraphFactory().create_instance_with_sets(4, [[0,1],[0,2],[1,2],[1,3]])
        self.graphlets[6] = GraphFactory().create_instance_with_sets(4, [[0,1],[1,2],[2,3],[3,0]])
        self.graphlets[7] = GraphFactory().create_instance_with_sets(4, [[0,1],[1,2],[1,3],[2,0],[2,3]])
        self.graphlets[8] = GraphFactory().create_instance_with_sets(4, [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])
        self.graphlets[9] = GraphFactory().create_instance_with_sets(5, [[0,1],[1,2],[2,3],[3,4]])
        self.graphlets[10] = GraphFactory().create_instance_with_sets(5, [[0,1],[1,2],[2,3],[2,4]])
        self.graphlets[11] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[1,2],[3,4]])
        self.graphlets[12] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,4],[1,3],[2,3]])
        self.graphlets[13] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3]])
        self.graphlets[14] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,4],[1,2],[1,3],[2,3]])
        self.graphlets[15] = GraphFactory().create_instance_with_sets(5, [[0,1],[1,2],[2,0],[2,3],[1,3],[1,4],[2,4]])
        self.graphlets[16] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3],[2,4],[3,4]])
        self.graphlets[17] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4]])
        self.graphlets[18] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3],[0,4]])
        self.graphlets[19] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,3],[0,4],[1,2],[2,0]])
        self.graphlets[20] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[3,4]])
        self.graphlets[21] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[1,3],[1,4],[2,3],[2,4]])
        self.graphlets[22] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,4],[2,3],[3,4]])
        self.graphlets[23] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[0,4]])
        self.graphlets[24] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[1,4],[2,4],[3,4]])
        self.graphlets[25] = GraphFactory().create_instance_with_sets(5, [[0,1],[1,2],[2,3],[3,4],[4,0]])
        self.graphlets[26] = GraphFactory().create_instance_with_sets(5, [[0,1],[1,2],[1,3],[2,0],[2,4]])
        self.graphlets[27] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,4],[1,2],[1,4],[2,3],[3,0]])
        self.graphlets[28] = GraphFactory().create_instance_with_sets(5, [[0,1],[1,2],[2,0],[1,3],[1,4],[2,3],[4,3]])
        self.graphlets[29] = GraphFactory().create_instance_with_sets(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])

        return self.graphlets

