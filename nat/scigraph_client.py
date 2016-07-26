#!/usr/bin/env python3
""" WARNING: DO NOT MODIFY THIS FILE
    IT IS AUTOMATICALLY GENERATED BY ../scigraph.py
    AND WILL BE OVERWRITTEN
    Swagger Version: 1.2, API Version: 1.0.1
    generated for http://matrix.neuinfo.org:9000/scigraph/api-docs
    by scigraph.py
"""
import requests
from json import dumps

exten_mapping = {'image/png': 'png', 'text/csv': 'csv', 'text/tab-separated-values': 'tab-separated-values', 'application/json': 'json', 'application/xgmml': 'xgmml', 'application/xml': 'xml', 'text/plain; charset=utf-8': 'plain; charset=utf-8', 'text/html': 'html', 'application/graphson': 'graphson', 'image/jpeg': 'jpeg', 'text/plain': 'plain', 'application/graphml+xml': 'graphml+xml', 'text/gml': 'gml'}

class restService:
    """ Base class for SciGraph rest services. """

    def _get(self, method, url, params=None, output=None):
        s = requests.Session()
        if method == 'POST':
            req = requests.Request(method=method, url=url, data=params)
        else:
            req = requests.Request(method=method, url=url, params=params)
        if output:
            req.headers['Accept'] = output
        prep = req.prepare()
        if not self._quiet: print(prep.url)
        resp = s.send(prep)
        if not resp.ok:
            return None
        elif resp.headers['content-type'] == 'application/json':
            return resp.json()
        elif resp.headers['content-type'].startswith('text/plain'):
            return resp.text
        else:
            return resp

    def _make_rest(self, default=None, **kwargs):
        kwargs = {k:v for k, v in kwargs.items() if v}
        param_rest = '&'.join(['%s={%s}' % (arg, arg) for arg in kwargs if arg != default])
        param_rest = param_rest if param_rest else ''
        return param_rest


class Graph(restService):
    """ Graph services """

    def __init__(self, basePath='http://matrix.neuinfo.org:9000/scigraph', quiet=True):
        self._basePath = basePath
        self._quiet = quiet

    def getProperties(self, callback=None, output='application/json'):
        """ Get all property keys from: /graph/properties
            Arguments:
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
            outputs:
                application/json
        """

        kwargs = {'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest(None, **kwargs)
        url = self._basePath + ('/graph/properties').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != None}
        return self._get('GET', url, requests_params, output)

    def getNode(self, id, project='*', callback=None, output='application/json'):
        """ Get all properties of a node from: /graph/{id}
            Arguments:
            id: This ID should be either a CURIE or an IRI
            project: Which properties to project. Defaults to '*'.
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
            outputs:
                application/json
                application/graphson
                application/xml
                application/graphml+xml
                application/xgmml
                text/gml
                text/csv
                text/tab-separated-values
                image/jpeg
                image/png
        """

        kwargs = {'id':id, 'project':project, 'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('id', **kwargs)
        url = self._basePath + ('/graph/{id}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'id'}
        return self._get('GET', url, requests_params, output)

    def getEdges(self, type, entail='true', limit=100, skip=0, callback=None, output='application/json'):
        """ Get nodes connected by an edge type from: /graph/edges/{type}
            Arguments:
            type: The type of the edge
            entail: Should subproperties and equivalent properties be included
            limit: The number of edges to be returned
            skip: The number of edges to skip
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
            outputs:
                application/json
                application/graphson
                application/xml
                application/graphml+xml
                application/xgmml
                text/gml
                text/csv
                text/tab-separated-values
                image/jpeg
                image/png
        """

        kwargs = {'type':type, 'entail':entail, 'limit':limit, 'skip':skip, 'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('type', **kwargs)
        url = self._basePath + ('/graph/edges/{type}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'type'}
        return self._get('GET', url, requests_params, output)

    def getRelationships(self, callback=None, output='application/json'):
        """ Get all relationship types from: /graph/relationship_types
            Arguments:
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
            outputs:
                application/json
        """

        kwargs = {'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest(None, **kwargs)
        url = self._basePath + ('/graph/relationship_types').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != None}
        return self._get('GET', url, requests_params, output)

    def getNeighbors(self, id, depth=1, blankNodes='false', relationshipType=None, direction='BOTH', project='*', callback=None, output='application/json'):
        """ Get neighbors from: /graph/neighbors/{id}
            Arguments:
            id: This ID should be either a CURIE or an IRI
            depth: How far to traverse neighbors
            blankNodes: Traverse blank nodes
            relationshipType: Which relationship to traverse
            direction: Which direction to traverse: INCOMING, OUTGOING, BOTH (default). Only used if relationshipType is specified.
            project: Which properties to project. Defaults to '*'.
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
            outputs:
                application/json
                application/graphson
                application/xml
                application/graphml+xml
                application/xgmml
                text/gml
                text/csv
                text/tab-separated-values
                image/jpeg
                image/png
        """

        kwargs = {'id':id, 'depth':depth, 'blankNodes':blankNodes, 'relationshipType':relationshipType, 'direction':direction, 'project':project, 'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('id', **kwargs)
        url = self._basePath + ('/graph/neighbors/{id}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'id'}
        return self._get('GET', url, requests_params, output)

    def getNeighborsFromMultipleRoots(self, id, depth=1, blankNodes='false', relationshipType=None, direction='BOTH', project='*', callback=None, output='application/json'):
        """ Get neighbors from: /graph/neighbors
            Arguments:
            id: This ID should be either a CURIE or an IRI
            depth: How far to traverse neighbors
            blankNodes: Traverse blank nodes
            relationshipType: Which relationship to traverse
            direction: Which direction to traverse: INCOMING, OUTGOING, BOTH (default). Only used if relationshipType is specified.
            project: Which properties to project. Defaults to '*'.
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
            outputs:
                application/json
                application/graphson
                application/xml
                application/graphml+xml
                application/xgmml
                text/gml
                text/csv
                text/tab-separated-values
                image/jpeg
                image/png
        """

        kwargs = {'id':id, 'depth':depth, 'blankNodes':blankNodes, 'relationshipType':relationshipType, 'direction':direction, 'project':project, 'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('id', **kwargs)
        url = self._basePath + ('/graph/neighbors').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'id'}
        return self._get('GET', url, requests_params, output)


class Refine(restService):
    """ OpenRefine Reconciliation Services """

    def __init__(self, basePath='http://matrix.neuinfo.org:9000/scigraph', quiet=True):
        self._basePath = basePath
        self._quiet = quiet

    def suggestFromTerm_POST(self, query=None, queries=None):
        """ Reconcile terms from: /refine/reconcile
            Arguments:
            query: A call to a reconciliation service API
            for a single query looks like either
            of these:<ul><li>http://foo.com/bar/reconcile?query=...string...</li><li>http://foo.com/bar/reconcile?query={...json object literal...}</li></ul>If the query parameter
            is a string, then it's an abbreviation
            of <em>query={"query":...string...}</em>.<em>NOTE:</em> We encourage all API consumers
            to consider the single query mode <b>DEPRECATED</b>.Refine
            currently only uses the multiple query mode,
            but other consumers of the API may
            use the single query option since it
            was included in the spec.
            queries: A call to a standard reconciliation service API
            for multiple queries looks like this:<ul><li>http://foo.com/bar/reconcile?queries={...json object literal...}</li></ul>The
            json object literal has zero or more key/value
            pairs with arbitrary keys where the value is
            in the same format as a single query,
            e.g.<ul><li>http://foo.com/bar/reconcile?queries={ "q0" : { "query" : "foo" },
            "q1" : { "query" : "bar" } }</li></ul>"q0"
            and "q1" can be arbitrary strings.
        """

        kwargs = {'query':query, 'queries':queries}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest(None, **kwargs)
        url = self._basePath + ('/refine/reconcile').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != None}
        return self._get('POST', url, requests_params)

    def suggestFromTerm(self, query=None, queries=None, callback=None):
        """ Reconcile terms from: /refine/reconcile
            Arguments:
            query: A call to a reconciliation service API
            for a single query looks like either
            of these:<ul><li>http://foo.com/bar/reconcile?query=...string...</li><li>http://foo.com/bar/reconcile?query={...json object literal...}</li></ul>If the query parameter
            is a string, then it's an abbreviation
            of <em>query={"query":...string...}</em>.<em>NOTE:</em> We encourage all API consumers
            to consider the single query mode <b>DEPRECATED</b>.Refine
            currently only uses the multiple query mode,
            but other consumers of the API may
            use the single query option since it
            was included in the spec.
            queries: A call to a standard reconciliation service API
            for multiple queries looks like this:<ul><li>http://foo.com/bar/reconcile?queries={...json object literal...}</li></ul>The
            json object literal has zero or more key/value
            pairs with arbitrary keys where the value is
            in the same format as a single query,
            e.g.<ul><li>http://foo.com/bar/reconcile?queries={ "q0" : { "query" : "foo" },
            "q1" : { "query" : "bar" } }</li></ul>"q0"
            and "q1" can be arbitrary strings.
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
        """

        kwargs = {'query':query, 'queries':queries, 'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest(None, **kwargs)
        url = self._basePath + ('/refine/reconcile').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != None}
        return self._get('GET', url, requests_params)


class Analyzer(restService):
    """ Analysis services """

    def __init__(self, basePath='http://matrix.neuinfo.org:9000/scigraph', quiet=True):
        self._basePath = basePath
        self._quiet = quiet

    def enrich(self, sample, ontologyClass, path, callback=None, output='application/json'):
        """ Class Enrichment Service from: /analyzer/enrichment
            Arguments:
            sample: A list of CURIEs for nodes whose attributes are to be tested for enrichment. For example, a list of genes.
            ontologyClass: CURIE for parent ontology class for the attribute to be tested. For example, GO biological process
            path: A path expression that connects sample nodes to attribute class nodes
            callback: Name of the JSONP callback ('fn' by default). Supplying this parameter or
            requesting a javascript media type will cause a JSONP response to be
            rendered.
            outputs:
                application/json
        """

        kwargs = {'sample':sample, 'ontologyClass':ontologyClass, 'path':path, 'callback':callback}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('path', **kwargs)
        url = self._basePath + ('/analyzer/enrichment').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'path'}
        return self._get('GET', url, requests_params, output)


class Cypher(restService):
    """ Cypher utility services """

    def __init__(self, basePath='http://matrix.neuinfo.org:9000/scigraph', quiet=True):
        self._basePath = basePath
        self._quiet = quiet

    def resolve(self, cypherQuery, output='text/plain'):
        """ Cypher query resolver from: /cypher/resolve
            Arguments:
            cypherQuery: The cypher query to resolve
            outputs:
                text/plain
        """

        kwargs = {'cypherQuery':cypherQuery}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('cypherQuery', **kwargs)
        url = self._basePath + ('/cypher/resolve').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'cypherQuery'}
        return self._get('GET', url, requests_params, output)


class Annotations(restService):
    """ Annotation services """

    def __init__(self, basePath='http://matrix.neuinfo.org:9000/scigraph', quiet=True):
        self._basePath = basePath
        self._quiet = quiet

    def getEntities(self, content, includeCat=None, excludeCat=None, minLength=4, longestOnly='false', includeAbbrev='false', includeAcronym='false', includeNumbers='false'):
        """ Get entities from text from: /annotations/entities
            Arguments:
            content: The content to annotate
            includeCat: A set of categories to include
            excludeCat: A set of categories to exclude
            minLength: The minimum number of characters in annotated entities
            longestOnly: Should only the longest entity be returned for an overlapping group
            includeAbbrev: Should abbreviations be included
            includeAcronym: Should acronyms be included
            includeNumbers: Should numbers be included
        """

        kwargs = {'content':content, 'includeCat':includeCat, 'excludeCat':excludeCat, 'minLength':minLength, 'longestOnly':longestOnly, 'includeAbbrev':includeAbbrev, 'includeAcronym':includeAcronym, 'includeNumbers':includeNumbers}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('content', **kwargs)
        url = self._basePath + ('/annotations/entities').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'content'}
        return self._get('GET', url, requests_params)

    def postEntities(self, content, includeCat=None, excludeCat=None, minLength=4, longestOnly='false', includeAbbrev='false', includeAcronym='false', includeNumbers='false'):
        """ Get entities from text from: /annotations/entities
            Arguments:
            content: The content to annotate
            includeCat: A set of categories to include
            excludeCat: A set of categories to exclude
            minLength: The minimum number of characters in annotated entities
            longestOnly: Should only the longest entity be returned for an overlapping group
            includeAbbrev: Should abbreviations be included
            includeAcronym: Should acronyms be included
            includeNumbers: Should numbers be included
        """

        kwargs = {'content':content, 'includeCat':includeCat, 'excludeCat':excludeCat, 'minLength':minLength, 'longestOnly':longestOnly, 'includeAbbrev':includeAbbrev, 'includeAcronym':includeAcronym, 'includeNumbers':includeNumbers}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('content', **kwargs)
        url = self._basePath + ('/annotations/entities').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'content'}
        return self._get('POST', url, requests_params)

    def annotate(self, content, includeCat=None, excludeCat=None, minLength=4, longestOnly='false', includeAbbrev='false', includeAcronym='false', includeNumbers='false', output='text/plain; charset=utf-8'):
        """ Annotate text from: /annotations
            Arguments:
            content: The content to annotate
            includeCat: A set of categories to include
            excludeCat: A set of categories to exclude
            minLength: The minimum number of characters in annotated entities
            longestOnly: Should only the longest entity be returned for an overlapping group
            includeAbbrev: Should abbreviations be included
            includeAcronym: Should acronyms be included
            includeNumbers: Should numbers be included
            outputs:
                text/plain; charset=utf-8
        """

        kwargs = {'content':content, 'includeCat':includeCat, 'excludeCat':excludeCat, 'minLength':minLength, 'longestOnly':longestOnly, 'includeAbbrev':includeAbbrev, 'includeAcronym':includeAcronym, 'includeNumbers':includeNumbers}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('content', **kwargs)
        url = self._basePath + ('/annotations').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'content'}
        return self._get('GET', url, requests_params, output)

    def annotatePost(self, content, includeCat=None, excludeCat=None, minLength=4, longestOnly='false', includeAbbrev='false', includeAcronym='false', includeNumbers='false', ignoreTag=None, stylesheet=None, scripts=None, targetId=None, targetClass=None):
        """ Annotate text from: /annotations
            Arguments:
            content: The content to annotate
            includeCat: A set of categories to include
            excludeCat: A set of categories to exclude
            minLength: The minimum number of characters in annotated entities
            longestOnly: Should only the longest entity be returned for an overlapping group
            includeAbbrev: Should abbreviations be included
            includeAcronym: Should acronyms be included
            includeNumbers: Should numbers be included
            ignoreTag: HTML tags that should not be annotated
            stylesheet: CSS stylesheets to add to the HEAD
            scripts: JavaScripts that should to add to the HEAD
            targetId: A set of element IDs to annotate
            targetClass: A set of CSS class names to annotate
        """

        kwargs = {'content':content, 'includeCat':includeCat, 'excludeCat':excludeCat, 'minLength':minLength, 'longestOnly':longestOnly, 'includeAbbrev':includeAbbrev, 'includeAcronym':includeAcronym, 'includeNumbers':includeNumbers, 'ignoreTag':ignoreTag, 'stylesheet':stylesheet, 'scripts':scripts, 'targetId':targetId, 'targetClass':targetClass}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('content', **kwargs)
        url = self._basePath + ('/annotations').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'content'}
        return self._get('POST', url, requests_params)

    def annotateUrl(self, url, includeCat=None, excludeCat=None, minLength=4, longestOnly='false', includeAbbrev='false', includeAcronym='false', includeNumbers='false', ignoreTag=None, stylesheet=None, scripts=None, targetId=None, targetClass=None, output='text/html'):
        """ Annotate a URL from: /annotations/url
            Arguments:
            url: 
            includeCat: A set of categories to include
            excludeCat: A set of categories to exclude
            minLength: The minimum number of characters in annotated entities
            longestOnly: Should only the longest entity be returned for an overlapping group
            includeAbbrev: Should abbreviations be included
            includeAcronym: Should acronyms be included
            includeNumbers: Should numbers be included
            ignoreTag: HTML tags that should not be annotated
            stylesheet: CSS stylesheets to add to the HEAD
            scripts: JavaScripts that should to add to the HEAD
            targetId: A set of element IDs to annotate
            targetClass: A set of CSS class names to annotate
            outputs:
                text/html
        """

        kwargs = {'url':url, 'includeCat':includeCat, 'excludeCat':excludeCat, 'minLength':minLength, 'longestOnly':longestOnly, 'includeAbbrev':includeAbbrev, 'includeAcronym':includeAcronym, 'includeNumbers':includeNumbers, 'ignoreTag':ignoreTag, 'stylesheet':stylesheet, 'scripts':scripts, 'targetId':targetId, 'targetClass':targetClass}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('url', **kwargs)
        url = self._basePath + ('/annotations/url').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'url'}
        return self._get('GET', url, requests_params, output)

    def getEntitiesAndContent(self, content, includeCat=None, excludeCat=None, minLength=4, longestOnly='false', includeAbbrev='false', includeAcronym='false', includeNumbers='false'):
        """ Get embedded annotations as well as a separate list from: /annotations/complete
            Arguments:
            content: The content to annotate
            includeCat: A set of categories to include
            excludeCat: A set of categories to exclude
            minLength: The minimum number of characters in annotated entities
            longestOnly: Should only the longest entity be returned for an overlapping group
            includeAbbrev: Should abbreviations be included
            includeAcronym: Should acronyms be included
            includeNumbers: Should numbers be included
        """

        kwargs = {'content':content, 'includeCat':includeCat, 'excludeCat':excludeCat, 'minLength':minLength, 'longestOnly':longestOnly, 'includeAbbrev':includeAbbrev, 'includeAcronym':includeAcronym, 'includeNumbers':includeNumbers}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('content', **kwargs)
        url = self._basePath + ('/annotations/complete').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'content'}
        return self._get('GET', url, requests_params)

    def postEntitiesAndContent(self, content, includeCat=None, excludeCat=None, minLength=4, longestOnly='false', includeAbbrev='false', includeAcronym='false', includeNumbers='false'):
        """ Get embedded annotations as well as a separate list from: /annotations/complete
            Arguments:
            content: The content to annotate
            includeCat: A set of categories to include
            excludeCat: A set of categories to exclude
            minLength: The minimum number of characters in annotated entities
            longestOnly: Should only the longest entity be returned for an overlapping group
            includeAbbrev: Should abbreviations be included
            includeAcronym: Should acronyms be included
            includeNumbers: Should numbers be included
        """

        kwargs = {'content':content, 'includeCat':includeCat, 'excludeCat':excludeCat, 'minLength':minLength, 'longestOnly':longestOnly, 'includeAbbrev':includeAbbrev, 'includeAcronym':includeAcronym, 'includeNumbers':includeNumbers}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('content', **kwargs)
        url = self._basePath + ('/annotations/complete').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'content'}
        return self._get('POST', url, requests_params)


class Lexical(restService):
    """ Lexical services """

    def __init__(self, basePath='http://matrix.neuinfo.org:9000/scigraph', quiet=True):
        self._basePath = basePath
        self._quiet = quiet

    def getChunks(self, text):
        """ Extract entities from text. from: /lexical/chunks
            Arguments:
            text: The text from which to extract chunks
        """

        kwargs = {'text':text}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('text', **kwargs)
        url = self._basePath + ('/lexical/chunks').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'text'}
        return self._get('GET', url, requests_params)

    def getEntities(self, text):
        """ Extract entities from text. from: /lexical/entities
            Arguments:
            text: The text from which to extract entities
        """

        kwargs = {'text':text}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('text', **kwargs)
        url = self._basePath + ('/lexical/entities').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'text'}
        return self._get('GET', url, requests_params)

    def getSentences(self, text):
        """ Split text into sentences. from: /lexical/sentences
            Arguments:
            text: The text to split
        """

        kwargs = {'text':text}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('text', **kwargs)
        url = self._basePath + ('/lexical/sentences').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'text'}
        return self._get('GET', url, requests_params)

    def getPos(self, text):
        """ Tag parts of speech. from: /lexical/pos
            Arguments:
            text: The text to tag
        """

        kwargs = {'text':text}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('text', **kwargs)
        url = self._basePath + ('/lexical/pos').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'text'}
        return self._get('GET', url, requests_params)


class Vocabulary(restService):
    """ Vocabulary services """

    def __init__(self, basePath='http://matrix.neuinfo.org:9000/scigraph', quiet=True):
        self._basePath = basePath
        self._quiet = quiet

    def getCategories(self):
        """ Get all categories from: /vocabulary/categories
            Arguments:
        """

        kwargs = {}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest(None, **kwargs)
        url = self._basePath + ('/vocabulary/categories').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != None}
        return self._get('GET', url, requests_params)

    def suggestFromTerm(self, term, limit=1):
        """ Suggest terms from: /vocabulary/suggestions/{term}
            Arguments:
            term: Mispelled term
            limit: Maximum result count
        """

        kwargs = {'term':term, 'limit':limit}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('term', **kwargs)
        url = self._basePath + ('/vocabulary/suggestions/{term}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'term'}
        return self._get('GET', url, requests_params)

    def findByPrefix(self, term, limit=20, searchSynonyms='true', searchAbbreviations='false', searchAcronyms='false', includeDeprecated='false', category=None, prefix=None):
        """ Find a concept by its prefix from: /vocabulary/autocomplete/{term}
            Arguments:
            term: Term prefix to find
            limit: Maximum result count
            searchSynonyms: Should synonyms be matched
            searchAbbreviations: Should abbreviations be matched
            searchAcronyms: Should acronyms be matched
            includeDeprecated: Should deprecated classes be included
            category: Categories to search (defaults to all)
            prefix: CURIE prefixes to search (defaults to all)
        """

        kwargs = {'term':term, 'limit':limit, 'searchSynonyms':searchSynonyms, 'searchAbbreviations':searchAbbreviations, 'searchAcronyms':searchAcronyms, 'includeDeprecated':includeDeprecated, 'category':category, 'prefix':prefix}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('term', **kwargs)
        url = self._basePath + ('/vocabulary/autocomplete/{term}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'term'}
        return self._get('GET', url, requests_params)

    def findByTerm(self, term, limit=20, searchSynonyms='true', searchAbbreviations='false', searchAcronyms='false', category=None, prefix=None):
        """ Find a concept from a term from: /vocabulary/term/{term}
            Arguments:
            term: Term to find
            limit: Maximum result count
            searchSynonyms: Should synonyms be matched
            searchAbbreviations: Should abbreviations be matched
            searchAcronyms: Should acronyms be matched
            category: Categories to search (defaults to all)
            prefix: CURIE prefixes to search (defaults to all)
        """

        kwargs = {'term':term, 'limit':limit, 'searchSynonyms':searchSynonyms, 'searchAbbreviations':searchAbbreviations, 'searchAcronyms':searchAcronyms, 'category':category, 'prefix':prefix}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('term', **kwargs)
        url = self._basePath + ('/vocabulary/term/{term}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'term'}
        return self._get('GET', url, requests_params)

    def findById(self, id):
        """ Find a concept by its ID from: /vocabulary/id/{id}
            Arguments:
            id: ID to find
        """

        kwargs = {'id':id}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('id', **kwargs)
        url = self._basePath + ('/vocabulary/id/{id}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'id'}
        return self._get('GET', url, requests_params)

    def searchByTerm(self, term, limit=20, searchSynonyms='true', searchAbbreviations='false', searchAcronyms='false', category=None, prefix=None):
        """ Find a concept from a term fragment from: /vocabulary/search/{term}
            Arguments:
            term: Term to find
            limit: Maximum result count
            searchSynonyms: Should synonyms be matched
            searchAbbreviations: Should abbreviations be matched
            searchAcronyms: Should acronyms be matched
            category: Categories to search (defaults to all)
            prefix: CURIE prefixes to search (defaults to all)
        """

        kwargs = {'term':term, 'limit':limit, 'searchSynonyms':searchSynonyms, 'searchAbbreviations':searchAbbreviations, 'searchAcronyms':searchAcronyms, 'category':category, 'prefix':prefix}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest('term', **kwargs)
        url = self._basePath + ('/vocabulary/search/{term}').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != 'term'}
        return self._get('GET', url, requests_params)

    def getCuriePrefixes(self):
        """ Get all CURIE prefixes from: /vocabulary/prefixes
            Arguments:
        """

        kwargs = {}
        kwargs = {k:dumps(v) if type(v) is dict else v for k, v in kwargs.items()}
        param_rest = self._make_rest(None, **kwargs)
        url = self._basePath + ('/vocabulary/prefixes').format(**kwargs)
        requests_params = {k:v for k, v in kwargs.items() if k != None}
        return self._get('GET', url, requests_params)
