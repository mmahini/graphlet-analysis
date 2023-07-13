import numpy as np

from utils.singleton import singleton
from utils.timing import TimingUtils


@singleton
class BoundaryMatrixUtils():

    def __len__(self, boundary):
        return len(boundary)

    def __contains__(self, boundary, item):
        return item in boundary

    def __iter__(self, boundary):
        return (simplex for simplex in boundary)

    def make_co_boundary(self, boundary):     # add_co_bnd function
        TimingUtils().start("Make Co-Boundary")

        co_boundary = {simplex: set() for simplex in boundary}
        for simplex in boundary:
            for sub_simplex in boundary[simplex]:
                co_boundary[sub_simplex].add(simplex)

        TimingUtils().stop("Make Co-Boundary")
        return co_boundary

    def get_restricted_boundary(self, complex, simplices_set: set):
        return {simplex: complex.boundary[simplex] & simplices_set for simplex in set(complex.boundary) & simplices_set}

    ######################
    def get_bar_lengths(self, group, dim):
        '''Return a list of lengths of all finite bars of the given dimension'''
        # bar_lengths function
        return [death - birth for birth, death in self.get_bars(group, dim=dim) if death != np.inf]

    ######################
    def get_ker_share(self, dim):
        '''Return the ker_share_dim = (finite 1-norm of dgm_dim(ker))/(finite 1-norm of dgm_dim(dom))'''
        # kershare function
        ker1norm = sum(self.bar_lengths('ker', dim))
        dom1norm = sum(self.bar_lengths('sub_complex', dim))
        return ker1norm/dom1norm if dom1norm > 0 else 0

    def print_matrix(self, matrix, order_function):
        order = sorted(matrix, key=order_function)
        for row in order:
            for column in order:
                print('1' if row in matrix[column] else '0', end='')
            print()
