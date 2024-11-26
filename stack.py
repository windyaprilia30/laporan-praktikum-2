undo_stack = []
redo_stack = []

def data (data):
    undo_stack.append(data)
    print("data", {data}, "ditambahkan.")

    redo_stack.clear()

def undo():
    if undo_stack:
        data = undo_stack.pop()
        redo_stack.append(data)
        print("undo: dihapus", {data}, "dari stack.")
    else:
        print("tidak ada data untuk di- undo!")

def redo():
    if redo_stack:
        data = redo_stack.pop()
        undo_stack.append(data)
        print("redo: dipulihkan", {data}, " ke stack")
    else:
        print("tidak ada data untuk di- redo!")

data("data 1")
data("data 2")
data("data 3")
print("melakukan operasi undo:")
undo()
undo()

print("melakukan operasi redo:")
redo()
redo()

print("akhir undo stack:", undo_stack)
print("akhir redo stack:", redo_stack)