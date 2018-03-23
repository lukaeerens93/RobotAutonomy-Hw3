import numpy as np

class DiscreteEnvironment(object):

    def __init__(self, resolution, lower_limits, upper_limits):

        # Store the resolution
        self.resolution = resolution
        # Store the bounds
        self.lower_limits = lower_limits
        self.upper_limits = upper_limits
        # Calculate the dimension ex: 2
        self.dimension = len(self.lower_limits)
        # Figure out the number of grid cells that are in each dimension
        self.num_cells = self.dimension*[0]



        # Store the bounds
        self.np_lower_limits = np.asarray(lower_limits)
        self.np_upper_limits = np.asarray(upper_limits)
        # Figure out the number of grid cells that are in each dimension
        self.np_num_cells = np.asarray(self.dimension*[0])

        # ex: num_cells = [100.0,100.0]
        for idx in range(self.dimension):
            self.num_cells[idx] = np.ceil((upper_limits[idx] - lower_limits[idx])/resolution)

    def ConfigurationToNodeId(self, config):
        
        # TODO:
        # This function maps a node configuration in full configuration
        # space to a node in discrete space
        #
        grid_coord = self.ConfigurationToGridCoord(config)
        node_id = self.GridCoordToNodeId(grid_coord)
        return node_id

    def NodeIdToConfiguration(self, nid):
        
        # TODO:
        # This function maps a node in discrete space to a configuraiton
        # in the full configuration space
        #
        config = [0] * self.dimension
        grid_coord = self.NodeIdToGridCoord(nid)
        config = self.GridCoordToConfiguration(grid_coord)
        return config
        
    def ConfigurationToGridCoord(self, config):
        
        # TODO:
        # This function maps a configuration in the full configuration space
        # to a grid coordinate in discrete space
        #
        # input: config = [0.26, 0.64]
        # output = [1, 3]
        # resolution = 0.1
        # lower_limits = [-5.0,-5.0]
        # Upper_limits = [5.0,5.0]
        # cell num
        np_config = np.asarray(config)
        np_coord = (np_config - self.np_lower_limits)/self.resolution
        coord = np_coord.tolist()
        return coord

    def GridCoordToConfiguration(self, coord):
        
        # TODO:
        # This function smaps a grid coordinate in discrete space
        # to a configuration in the full configuration space
        #
        np_coord = np.asarray(coord)
        np_config = np_coord * self.resolution + self.lower_limits
        config = np_config.tolist()
        return config

    def GridCoordToNodeId(self,coord):
        
        # TODO:
        # This function maps a grid coordinate to the associated
        # node id 
        node_id = 0
        np_coord = np.asarray(coord)
        dimension = 3
        # dim_range = [5,5,5]
        dim_range = abs(self.upper_limits - self.lower_limits)/self.resolution
        # coord = [5,4,3]
        # output: 31
        nid = 0
        # 2,1,0
        for i in range(self.dimension,-1,-1):
            if i is 0:
                nid+=coord[i]
                break
            nid += (coord[i]-1)*reduce(lambda x, y: x * y, dim_range[:i])
        return node_id

    def NodeIdToGridCoord(self, node_id):
        
        # TODO:
        # This function maps a node id to the associated
        # grid coordinate
        dimension = 3
        node_id = 52
        coord = [0] * dimension
        dim_range = [5, 3, 6]
        remainder = node_id
        for i in range(2,-1,-1):
            if i is 0:
                coord[i] = remainder +1
                break
            (quotient,remainder) = divmod(remainder, reduce(lambda x, y: x * y, dim_range[:i]))
            coord[i] = quotient +1
        return coord
        
        
        
