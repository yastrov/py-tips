#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert JSON or Python Dict to Go (Golang) Structurest for unmarshalling.
"""
import sys
__version__ = "1.0"
__author__ = "Yuri (Yuriy) Astrov <yuriastrov@gmail.com>"

class JSONtoGoStructConverter(object):
    def __init__(self, output=None, dirtyInts=False):
        """
        output must be text writeble: io.StringIO or file or None (if last you have return as io.StringIO),
        flag dirtyInts you may set to True, if you have int encoded as JSON string, like:
        {"count":"3"}
        """
        #super().__init__()
        self._input = None
        self._output = output
        self._cache = {}
        self._dirtyInts = dirtyInts

    def _loadFromJSONString(self, inputData):
        import json
        self._input = json.loads(inputData)

    def make(self, inputData, output=None):
        """This is main function.
            inputData must be string or dict or readable (and return string)
            output must be text writeble: io.StringIO or file,
        """
        if isinstance(inputData, str):
            self._loadFromJSONString(inputData)
        elif isinstance(inputData, dict):
            self._input = inputData
        elif hasattr(inputData, 'read'):
            self._loadFromJSONString(inputData.read())
        else:
            raise Exception("Unknown type for input: "+str(type(inputData)))
        if output is None:
            import io
            self._output = io.StringIO()
        elif output:
            self._output = output
        self_process_Func = self._processObject
        self_process_Func(self._input)
        selfcache = self._cache
        _keys = []
        _keys_append = _keys.append
        while len(selfcache) > 0:
            _keys.clear() # No clear in Py 2.7!
            for key, value in selfcache.items():
                self_process_Func(value, rootName=key)
                _keys_append(key)
            for key in _keys:
                del selfcache[key]

    def getResult(self):
        return self._output

    def getReasultAsString(self):
        return self._output.getvalue()

    def _processObject(self, currentNode, rootName=None):
        __outputF = self._output.write
        __dirtyStringFlag = False
        _ttype_n = ""
        rootName = rootName or "RootObject"
        __outputF('type {className} struct '\
                    .format(className=rootName)+'{\n')
        for key, value in currentNode.items():
            __dirtyStringFlag = False
            nodeType = type(value)
            if nodeType == int:
                _ttype_n = 'int'
            elif nodeType == list:
                _ttype = type(value[0])
                _ttype_n = None
                if _ttype == int:
                    _ttype_n = 'int'
                elif _ttype == str:
                    _ttype_n = 'string'
                    if self._dirtyInts:
                        try:
                            _x = int(value)
                            _ttype_n = 'int'
                            __dirtyStringFlag = True
                        except:
                            pass
                elif _ttype == dict:
                    _ttype_n = self._getName(key)
                    self._cache[_ttype_n] = value
                    _ttype_n = '*' + _ttype_n
                else:
                    raise Exception(str(nodeType))
                _ttype_n = "[]"+_ttype_n
            elif nodeType == str:
                _ttype_n = 'string'
                if self._dirtyInts:
                    try:
                        _x = int(value)
                        _ttype_n = 'int'
                        __dirtyStringFlag = True
                    except:
                        pass
            elif nodeType == dict:
                _ttype_n = self._getName(key)
                self._cache[_ttype_n] = value
                _ttype_n = "*"+_ttype_n
            #preparing strings fro output
            varOrigName = key
            if __dirtyStringFlag:
                varOrigName = varOrigName + ',string'
            __outputF('{tname} {ttype} `json:"{name}"`\n'\
                            .format(tname=key.title(),
                                    ttype=_ttype_n, name=varOrigName))
        self._output.write('}\n\n')

    def _getName(self, _jsonItemName):
        name = _jsonItemName.title()
        name = name.replace(' ','')
        name = name.replace('-','')
        return name  + "Type"

def main():
    s = """{
"newcomments": {
"count": "0"
},
"discuss": {
"count": "1"
},
"emails": {
"count": "0"
},
"userinfo": {
"userid": "111",
"username": "User",
"shortname": "user"
}
}"""
    c = JSONtoGoStructConverter(dirtyInts=True)
    c.make(s)
    print(c.getReasultAsString())

if __name__ == "__main__":
    main()
