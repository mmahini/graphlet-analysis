from entities.graph import Graph, GraphFactory
from entities.graphlet import SubGraphletFactory, SubGraphlet

if __name__ == "__main__":
    g : Graph = GraphFactory().get_instance()
    g.load()
    print(g)

    gl : SubGraphlet = SubGraphletFactory().get_instance(g)
    gl.add(2)
    gl.add(3)
    gl.add(4)
    gl.add(5)
    gl.write_all()
