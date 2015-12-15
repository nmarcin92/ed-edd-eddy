class UserGraphGenerator:
    def __init__(self):
        pass

    def generate_csv_file(self, filename, connections):
        result = self.generate_edge_dictionary({}, connections)
        self.write_to_file(filename, result)

    def generate_csv_file2(self, filename, connections1, connections2):
        result = self.generate_edge_dictionary({}, connections1)
        result = self.generate_edge_dictionary(result, connections2)
        self.write_to_file(filename, result)

    @staticmethod
    def generate_edge_dictionary(dictionary, connections):
        result = dictionary
        for connection in connections:
            if connection[0] in result:
                if connection[1] in result[connection[0]]:
                    result[connection[0]][connection[1]] += 1
                else:
                    result[connection[0]][connection[1]] = 1
            else:
                result[connection[0]] = {}
                result[connection[0]][connection[1]] = 1
        return result

    @staticmethod
    def write_to_file(filename, result):
        f = open(filename, 'w')
        for k1 in result:
            for k2 in result[k1]:
                line = "%s;%s;%d\n" % (k1, k2, result[k1][k2])
                f.write(line)
        f.close()
