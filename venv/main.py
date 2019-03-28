from Class import myClass
import sqlite3

conn = sqlite3.connect('depth.db')
c = conn.cursor()

j = myClass(669302684)

# Example tree root 669302684
# 669302684|40388751
# 669302684|35595439
sl_query = "select id from smart_lists where id>34524175;"
# sl_query = "select id from smart_lists where id>1319;"
c.execute(sl_query)

lists = c.fetchall()

outfile = open('output.txt', 'w')

def build_tree(node):
    # print('hi')
    current_id = node.id
    query = "select smart_lists.id, depth.reference from smart_lists join depth on smart_lists.id = depth.list " \
            "where smart_lists.id = '" + str(current_id) + "';"
    # print(query)
    c.execute(query)
    all_rows = c.fetchall()
    if len(all_rows) == 0:
        return node
    else:
        for row in all_rows:
            node.add_child(build_tree(myClass(row[1])))
    return node


master_list = []


def print_node(node, indent):
    print(indent + str(node.id))
    if len(node.get_children()) > 0:
        for c in node.get_children():
            print_node(c, indent+'\t')

for l in lists:
    new_node = myClass(l[0])
    master_list.append(build_tree(new_node))
    print_node(new_node, '')



conn.close()