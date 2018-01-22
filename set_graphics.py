import tkinter
from tkinter import *
from tkinter import ttk
 
class set_app(ttk.Frame):
    """The adders gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
 
    def on_quit(self):
        """Exits program."""
        quit()

    def on_clear(self):
        '''Clears all entries'''
        self.union.delete(0, 'end')
        self.diff.delete(0, 'end')
        self.superset.delete(0, 'end')
        self.subset_A.delete(0, 'end')
        self.subset_B.delete(0, 'end')
        self.inter.delete(0, 'end')
        self.exc_or.delete(0, 'end')
        self.comp_A.delete(0, 'end')
        self.comp_B.delete(0, 'end')

    def union_op(self, setA, setB):
        union = setA
        for i in range(len(setB)):
            if setB[i] not in setA:
                union.append(setB[i])
        return union

    def intersection(self, setA, setB):
        inter = []
        for i in range(len(setA)):
            if (setA[i] in setB):
                inter.append(setA[i])
        return inter

    def difference(self, setA, setB):
        diff = []
        for i in range(len(setA)):
            if (setA[i] not in setB):
                diff.append(setA[i])
        return diff

    def compliment(self, superset, setA):
        comp = []
        for i in range(len(superset)):
            if (superset[i] not in setA):
                comp.append(superset[i])
        return comp

    def exclusive_or(self, setA, setB):
        excl = []
        for i in range(len(setA)):
            if (setA[i] not in setB):
                excl.append(setA[i])
        for j in range(len(setB)):
            if (setB[j] not in setA) and (setB[j] not in excl):
                excl.append(setB[j])
                
        return excl

    def operations(self):
        """Calculates the sum of the two inputted numbers."""
        supersetU= str(self.superset.get())
        supersetU = [x.strip() for x in supersetU.split(',')]
        setA = str(self.subset_A.get())
        setA = [x.strip() for x in setA.split(',')]
        setB = str(self.subset_B.get())
        setB = [x.strip() for x in setB.split(',')]

        self.un.set(self.union_op(setA, setB))
        self.inte.set(self.intersection(setA, setB))
        self.dif.set(self.difference(setA, setB))
        self.compA.set(self.compliment(supersetU, setA))
        self.compB.set(self.compliment(supersetU, setB))
        self.excl.set(self.exclusive_or(setA, setB))
 
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Set Operations')
        self.root.option_add('*tearOff', 'FALSE')
 
        self.grid(column=0, row=0, sticky='nsew')
 
        self.menubar = tkinter.Menu(self.root)
 
        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)
 
        self.menu_edit = tkinter.Menu(self.menubar)
 
        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')
 
        self.root.config(menu=self.menubar)

        self.sp_set = StringVar()
        superset = '1,2,3,4,5,6,7,8,9'
        self.sp_set.set(superset)
        self.superset = ttk.Entry(self,textvariable=self.sp_set, width= 20)
        self.superset.grid(column=1, row = 2)
        self.superset.bind('<Return>', self.operations)

        self.sb_setA = StringVar()
        subset_A = '1,2,3,4,5'
        self.sb_setA.set(subset_A)
        self.subset_A = ttk.Entry(self,textvariable=self.sb_setA, width=20)
        self.subset_A.grid(column=3, row = 2)
        self.subset_A.bind('<Return>', self.operations)

        self.sb_setB = StringVar()
        subset_B = '1,3,5,7,9'
        self.sb_setB .set(subset_B)
        self.subset_B = ttk.Entry(self,textvariable=self.sb_setB, width=20)
        self.subset_B.grid(column=5, row=2)
        self.subset_B.bind('<Return>', self.operations)
 
        self.ops_button = ttk.Button(self, text='Operations',
                command=self.operations)
        self.ops_button.grid(column=0, row=4, columnspan=4)

        self.ops_button = ttk.Button(self, text='Clear',
                command=self.on_clear)
        self.ops_button.grid(column=0, row=11, columnspan=4)

        self.un = StringVar()
        self.union = ttk.Entry(self, textvariable=self.un, width= 20)
        self.union.grid(column=1, row = 5)

        self.dif = StringVar()
        self.diff = ttk.Entry(self, textvariable=self.dif, width=20)
        self.diff.grid(column=1, row = 6)

        self.compA = StringVar()
        self.comp_A = ttk.Entry(self, textvariable=self.compA, width=20)
        self.comp_A.grid(column=1, row=7)

        self.compB = StringVar()
        self.comp_B = ttk.Entry(self, textvariable=self.compB, width=20)
        self.comp_B.grid(column=1, row=8)

        self.inte = StringVar()
        self.inter = ttk.Entry(self, textvariable=self.inte, width= 20)
        self.inter.grid(column=1, row = 9)

        self.excl = StringVar()
        self.exc_or = ttk.Entry(self, textvariable=self.excl, width=20)
        self.exc_or.grid(column=1, row = 10)
 
 
 
        # Labels that remain constant throughout execution.
        ttk.Label(self, text='Set Operations').grid(column=0, row=0,
                columnspan=6)
        ttk.Label(self, text='superset U').grid(column=0, row=2,
                sticky='w')
        ttk.Label(self, text='subset A').grid(column=2, row=2,
                sticky='w')
        ttk.Label(self, text='subset B').grid(column=4, row=2,
                sticky='w')
        ttk.Separator(self, orient='horizontal').grid(column=0,
                row=3, columnspan=6, sticky='ew')
        ttk.Separator(self, orient='horizontal').grid(column=0,
                row=1, columnspan=6, sticky='ew')
        ttk.Label(self, text='Union A+B').grid(column=0, row=5,
                sticky='w')
        ttk.Label(self, text='Difference A-B').grid(column=0, row=6,
                sticky='w')
        ttk.Label(self, text="Complement A'").grid(column=0, row=7,
                sticky='w')
        ttk.Label(self, text="complement B'").grid(column=0, row=8,
                sticky='w')
        ttk.Label(self, text='Intersection').grid(column=0, row=9,
                sticky='w')
        ttk.Label(self, text='Exclusive Or').grid(column=0, row=10,
                sticky='w')
 
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
 
if __name__ == '__main__':
    root = tkinter.Tk()
    set_app(root)
    root.mainloop()
