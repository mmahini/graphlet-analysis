from graph.graph import Graph, GraphFactory
from utils.singleton import singleton


@singleton
class GraphletTemplates():
    def __init__(self):
        self.initialized = False
        self.graphlets: dict[int, Graph] = dict()

    def list(self) -> dict[int, Graph]:
        if self.initialized:
            return self.graphlets

        self.graphlets[0] = GraphFactory().create_instance_with_sets(
            2, [[0, 1]])
        self.graphlets[1] = GraphFactory().create_instance_with_sets(
            3, [[0, 1], [1, 2]])
        self.graphlets[2] = GraphFactory().create_instance_with_sets(
            3, [[0, 1], [1, 2], [0, 2]])
        self.graphlets[3] = GraphFactory().create_instance_with_sets(
            4, [[0, 1], [1, 2], [2, 3]])
        self.graphlets[4] = GraphFactory().create_instance_with_sets(
            4, [[0, 1], [0, 2], [0, 3]])
        self.graphlets[5] = GraphFactory().create_instance_with_sets(
            4, [[0, 1], [0, 2], [1, 2], [1, 3]])
        self.graphlets[6] = GraphFactory().create_instance_with_sets(
            4, [[0, 1], [1, 2], [2, 3], [3, 0]])
        self.graphlets[7] = GraphFactory().create_instance_with_sets(
            4, [[0, 1], [1, 2], [1, 3], [2, 0], [2, 3]])
        self.graphlets[8] = GraphFactory().create_instance_with_sets(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]])
        self.graphlets[9] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [1, 2], [2, 3], [3, 4]])
        self.graphlets[10] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [1, 2], [2, 3], [2, 4]])
        self.graphlets[11] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [1, 2], [3, 4]])
        self.graphlets[12] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 4], [1, 3], [2, 3]])
        self.graphlets[13] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3]])
        self.graphlets[14] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3], [2, 3]])
        self.graphlets[15] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [1, 2], [2, 0], [2, 3], [1, 3], [1, 4], [2, 4]])
        self.graphlets[16] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4]])
        self.graphlets[17] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4]])
        self.graphlets[18] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 4]])
        self.graphlets[19] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 3], [0, 4], [1, 2], [2, 0]])
        self.graphlets[20] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [3, 4]])
        self.graphlets[21] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [2, 3], [2, 4]])
        self.graphlets[22] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 4], [2, 3], [3, 4]])
        self.graphlets[23] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [0, 4]])
        self.graphlets[24] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4]])
        self.graphlets[25] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]])
        self.graphlets[26] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [1, 2], [1, 3], [2, 0], [2, 4]])
        self.graphlets[27] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 4], [1, 2], [1, 4], [2, 3], [3, 0]])
        self.graphlets[28] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [2, 3], [4, 3]])
        self.graphlets[29] = GraphFactory().create_instance_with_sets(
            5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])

        return self.graphlets


@singleton
class OrbitTemplates():
    def __init__(self):
        self.initialized = False
        self.orbits: dict[int, set()] = dict()

    def list(self) -> dict[int, set()]:
        if self.initialized:
            return self.orbits
        self.initialized = True

        # graphlet_type -> (orbit, vertex_id_in_graphlet_type)
        self.orbits = {0: {(0, 0)},
                       1: {(1, 0), (2, 1)},
                       2: {(3, 0)},
                       3: {(4, 0), (5, 1)},
                       4: {(6, 1), (7, 0)},
                       5: {(8, 3), (9, 1), (10, 0)},
                       6: {(11, 0)},
                       7: {(12, 1), (13, 0)},
                       8: {(14, 0)},
                       9: {(15, 0), (16, 1), (17, 2)},
                       10: {(18, 0), (19, 1), (20, 2), (21, 3)},
                       11: {(22, 4), (23, 3), (24, 0), (25, 1)},
                       12: {(26, 4), (27, 0), (28, 1), (29, 3)},
                       13: {(30, 4), (31, 0), (32, 1), (33, 3)},
                       14: {(34, 4), (35, 0), (36, 1), (37, 3)},
                       15: {(38, 0), (39, 1)},
                       16: {(40, 0), (41, 2), (42, 4)},
                       17: {(43, 3), (44, 0)},
                       18: {(45, 4), (46, 0), (47, 1)},
                       19: {(48, 1), (49, 0), (50, 3)},
                       20: {(51, 1), (52, 0)},
                       21: {(53, 0), (54, 1), (55, 4)},
                       22: {(56, 1), (57, 0)},
                       23: {(58, 1), (59, 0)},
                       24: {(60, 0), (61, 1)},
                       25: {(62, 0)},
                       26: {(63, 0), (64, 1), (65, 4)},
                       27: {(66, 4), (67, 0), (68, 2)},
                       28: {(69, 1), (70, 0), (71, 2)},
                       29: {(72, 0)},
                       }

        # Orbit degree weight
        self.orbit_degree_weight = {0: 1,
                                    1: 1, 2: 2,                             
                                    3: 2,
                                    4: 2, 5: 1,                             
                                    6: 1, 7: 3,                             
                                    8: 1, 9: 3, 10: 2,                                                          
                                    11: 2,
                                    12: 3, 13: 2,                             
                                    14: 3,
                                    15: 1, 16: 2, 17: 2,                                                          
                                    18: 1, 19: 2, 20: 3, 21: 1,                             
                                    22: 1, 23: 2, 24: 3, 25: 2,                                                                                       
                                    26: 1, 27: 3, 28: 2, 29: 2,                                                                                       
                                    30: 1, 31: 4, 32: 2, 33: 3,                                                                                       
                                    34: 1, 35: 3, 36: 3, 37: 2,                                                                                       
                                    38: 2, 39: 4,                             
                                    40: 3, 41: 4, 42: 2,                             
                                    43: 3, 44: 4,                             
                                    45: 1, 46: 4, 47: 3,                                                          
                                    48: 2, 49: 4, 50: 1,                                                          
                                    51: 2, 52: 4,                             
                                    53: 3, 54: 3,                             
                                    55: 2, 56: 3, 57: 4,                                                          
                                    58: 1, 59: 4,                             
                                    60: 3, 61: 2,                             
                                    62: 2,
                                    63: 2, 64: 3, 65: 1,                                                          
                                    66: 2, 67: 3, 68: 2,                                                          
                                    69: 4, 70: 2, 71: 3,                                                          
                                    72: 4
                                    }

        return self.orbits
