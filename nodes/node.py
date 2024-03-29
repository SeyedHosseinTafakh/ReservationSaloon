from services.neo4j import driver


def find_node_by_id(id):
    with driver.session() as session:
        node = session.run("match (n {id:$id}) return n",id=id)
        node = node.data()
    if node:
        return True,node
    return False,None
