# -*- coding: utf-8 -*-
from ..asm import CodePage
from .codeobject import CodeContainer
from .statements import Function

class CCode(CodeContainer):
    def __init__(self, code):
        CodeContainer.__init__(self, code)
        self.compiled = False
        self.globals = None
        self.asm = None
        self.codepage = None
        
    def compile(self):
        self.asm = []
        scope = {}
        for item in self.code:
            self.asm.extend(item.compile(scope))

        self.codepage = CodePage(self.asm)
        
        self.globals = {}
        for name, obj in scope.items():
            if isinstance(obj, Function):
                func = self.codepage.get_function(obj.name)
                self.globals[obj.name] = func
                setattr(self, obj.name, func)
        
    