class myClass:

    def __init__(self, id):
        self.id = id
        self.children = []

    def f(self):
        return self.id

    def add_child(self, id):
        self.children.append(id)

    def get_children(self):
        return self.children

    def print_children(self, level, m, indent):
        m.write(indent + str(level.id) + '\r\n')
        print(indent + str(level.id))
        if len(level.children) > 0:
            for c in level.children:
                self.print_children(m, c, indent+'\t')

