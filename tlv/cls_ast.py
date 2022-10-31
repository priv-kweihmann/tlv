import os


class TLVAst(object):

    def __init__(self, filename, line_offset=0):
        self.Processed = []
        self.Raw = []
        self.Filename = filename
        self.LineOffset = line_offset


class TLVFinding(object):
    ID_DUPLICATE = "Duplicate"
    ID_TLV = "TooLessVariation"

    def __init__(self, first, second, match, _id):
        self.file_this = first.Filename
        self.file_other = second.Filename
        self.file_this_start_line, self.file_this_start_col = self.__get_pos(
            first, match.a)
        self.file_other_start_line, self.file_other_start_col = self.__get_pos(
            second, match.b)
        self.file_this_stop_line, self.file_this_stop_col = self.__get_pos(
            first, match.a + match.size)
        self.file_other_stop_line, self.file_other_stop_col = self.__get_pos(
            second, match.b + match.size)
        self.text_this = TLVFinding.get_text(
            first, match.a, match.a + match.size)
        self.text_other = TLVFinding.get_text(
            second, match.b, match.b + match.size)
        self.id = _id

    def Print(self, args):
        print(str(self))
        self.PrintDetails(args)

    def PrintDetails(self, args):
        if args.details:
            print(">>> {snip}".format(snip=self.text_this.replace(
                os.linesep, os.linesep + ">>> ")))
            print("<<<")
            if self.id == TLVFinding.ID_TLV:
                print(">>> {snip}".format(snip=self.text_other.replace(
                    os.linesep, os.linesep + ">>> ")))
                print("<<<")

    def __eq__(self, other):
        if isinstance(other, TLVFinding):
            return str(other) == str(self)
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        if self.id == TLVFinding.ID_DUPLICATE:
            msg = "is the same"
        elif self.id == TLVFinding.ID_TLV:
            msg = "is nearly the same"
        if self.file_this != self.file_other:
            path = os.path.relpath(self.file_other, self.file_this)
        else:
            path = "same file"
        return "{}:{}:{}:[{}]:Block till {}:{} {} as in {} from {}:{} till {}:{}".format(self.file_this,  # noqa: P101
                                                                                         self.file_this_start_line,
                                                                                         self.file_this_start_col,
                                                                                         self.id,
                                                                                         self.file_this_stop_line,
                                                                                         self.file_this_stop_col,
                                                                                         msg,
                                                                                         path,
                                                                                         self.file_other_start_line,
                                                                                         self.file_other_start_col,
                                                                                         self.file_other_stop_line,
                                                                                         self.file_other_stop_col)

    def __get_pos(self, obj, pos):
        _raw = TLVFinding.get_text(obj, 0, pos)
        _line = _raw.count(os.linesep)
        _col = len(_raw.split(os.linesep)[-1])
        return (_line + obj.LineOffset, _col)

    @staticmethod
    def get_text(obj, start, stop):
        return "".join([x[1] for x in obj.Raw[start:stop]])

    @staticmethod
    def Validate(args, first, second, match):
        chunk_a = TLVFinding.get_text(first, match.a, match.a + match.size)
        chunk_b = TLVFinding.get_text(second, match.b, match.b + match.size)
        if chunk_a.count(os.linesep) + 1 >= args.minlines and match.size >= args.mintoken:
            if chunk_a == chunk_b:
                return TLVFinding.ID_DUPLICATE
            else:
                return TLVFinding.ID_TLV
        return None
