class PileException(Exception):
    """Ma classe"""

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"PileException: code={self.code}  msg={self.message}"


class PileExceptionVide(PileException):
    """Ma classe"""

    def __init__(self):
        PileException.__init__(self, 23, "PileException vide")

    def __str__(self):
        return f"PileExceptionVide: code={self.code}  msg={self.message}"

class PileExceptionPleine(PileException):
    """Ma classe"""

    def __init__(self):
        PileException.__init__(self, 24, "PileException pleine")

    def __str__(self):
        return f"PileExceptionPleine: code={self.code}  msg={self.message}"

