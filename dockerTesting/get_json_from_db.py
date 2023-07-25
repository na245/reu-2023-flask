# This script gets data of techniqueCapac edge collection from the BRON guest db

from arango import ArangoClient, DocumentInsertError, CursorNextError

def get_tech_capac(db):

    TECH_CAP = 'TechniqueCapec'
    
    # setting guest database and local database
    guest = ArangoClient(hosts='http://bron.alfa.csail.mit.edu:8529')

    # opening guest database and local database
    guest_db = guest.db('BRON', username='guest', password='guest')

    # opening guest db document for transfer
    guest_collection = guest_db.collection(TECH_CAP)

    # open local graph for edge placement
    graph = db.graph('BRONGraph')

    # if the collection does not exist in local, create it
    # (should by default)
    if graph.has_edge_definition(TECH_CAP):
        graph.delete_edge_definition(TECH_CAP)
    if db.has_collection(TECH_CAP):
        db.delete_collection(TECH_CAP)

    graph.create_edge_definition(
        edge_collection = TECH_CAP,
        from_vertex_collections = ['technique'],
        to_vertex_collections = ['capec'])
    
    tc = graph.edge_collection(TECH_CAP)
    # # wipe the local collection clean
    # TC = db.collection(TECH_CAP)
    # TC.truncate()

    # grab all documents in guest collection
    documents = guest_collection.all()
    
    #print(documents.count())

    cnt = 0
    # place all edges into the local database
    try:
        for document in documents:
            try:
                cnt += 1
                # print(cnt)
                edge_data = {'_from': document['_from'], '_to': document['_to']}
                tc.insert(edge_data)
            #print(document)

        # skip inserting data that has attack pattern that are not in our capec collection
            except DocumentInsertError:
                pass
            #print('Hello')
        #print(document['_to'])
    except CursorNextError:
        print(next(documents))

