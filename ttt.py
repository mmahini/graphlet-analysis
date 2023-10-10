from complex.core.simplicial_complex_factory import SimplicialComplexFactory
from complex.core.miniplex_factory import MiniplexFactory
from complex.entities.simplicial_complex import SimplicialComplex
from complex.entities.miniplex import Miniplex
from complex.templates import MiniplexTemplates, NUM_OF_MINIPLEXES
from complex.utils.simplex_utils import SimplexUtils
from complex.algorithms.exact import Exact


# Test guise graphlet count diff with exact count
def create_random_simplex():
    n = int(50)    # number of nodes in complex
    p = float(0.1) # probability of vertices ,between 0 and 1
    t = float(0.5)  # probability of triplets ,between 0 and 1
    q = float(0.5)  # probability of quartets ,between 0 and 1

    complex: SimplicialComplex = SimplicialComplexFactory().create_random_instance(n, p, t, q)

    complex.write()

# if __name__ == "__main__":
#     complex: SimplicialComplex = SimplicialComplexFactory().load_from_cmd()
#     miniplex: Miniplex = MiniplexFactory().create_miniplex(complex, [0, 1, 2])
#     miniplex.write()

# if __name__ == "__main__":
#     miniplex_templates = MiniplexTemplates().list()
#     for i in range(NUM_OF_MINIPLEXES):
#         complex: SimplicialComplex = miniplex_templates[i]
#         type: int = SimplexUtils().calc_miniplex_type(complex)
#         if type == i:
#             print(f"success for  %s" % i)
#         else:
#             print(f"fail for %s" % i)

# if __name__ == "__main__":
#     complex: SimplicialComplex = SimplicialComplexFactory().load_from_cmd()
#     # miniplex = MiniplexFactory().create_miniplex(complex, [0, 1, 2])
#     # print(miniplex.get_type())
#     # miniplex.write()

#     # exact: Exact = Exact(complex)
#     # exact.log = True
#     # exact.run()

#     ss : bool = False
#     for t in complex.triplets:
#         if 0 in t:
#             ss = True
#             break
#     print(ss)

# average degree of input complex from cmd
if __name__ == "__main__":
    n = int(10)    # number of nodes in complex
    p = float(0.56)  # probability of vertices ,between 0 and 1
    t = float(0.5)  # probability of triplets ,between 0 and 1
    q = float(0.5)  # probability of quartets ,between 0 and 1

    complex: SimplicialComplex = SimplicialComplexFactory().create_random_instance(n, p, t, q)

    n = len(complex.vertices)
    degrees = 0
    for i in range(n):
        degrees = degrees + len(complex.nei[i])

    average_degree = degrees / n

    complex.write()
    print(f"average degree {average_degree}")
    
# create random comlex
# if __name__ == "__main__":
#     SimplicialComplexFactory().create_random_instance()
