from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, func, text ,row, col, font, color = 'dark-grey', span=1):
        super().__init__(
            master = parent, 
            text = text,
            command = func,
            corner_radius=STYLING['corner-radious'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text']
            )
        self.grid(row=row, column=col, sticky='NESW', columnspan=span)

class NumButton(Button):
    def __init__(self, parent, func, text ,row, col, font,span, color = 'light-grey'):
        super().__init__(
            parent = parent,
            func = func,
            text = text,
            row = row,
            col = col,
            font = font,
            color = color,
            span=span
        )


class ImageButton(CTkButton):
    """Button that has image inside"""
    def __doc__(self):
        return """Button that has image inside"""
        pass
    def __init__(self, parent, func, image, row, col, font, color = 'dark-grey'):
        super().__init__(
            master=parent,
            command=func,
            font = font,
            image=image,
            corner_radius=STYLING['corner-radious'],
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text']
        )
        self.grid(row=row, column=col, sticky='NSEW', padx=STYLING['gap'], pady=STYLING['gap'])

class Docsctrinsample1:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """
    def __doc__(self):
        return """Button that has image inside"""
    
class Docsctrinsample2:
    """Spreadsheet Column Printer

    This script allows the user to print to the console all columns in the
    spreadsheet. It is assumed that the first row of the spreadsheet is the
    location of the columns.

    This tool accepts comma separated value files (.csv) as well as excel
    (.xls, .xlsx) files.

    This script requires that `pandas` be installed within the Python
    environment you are running this script in.

    This file can also be imported as a module and contains the following
    functions:

        * get_spreadsheet_cols - returns the column headers of the file
        * main - the main function of the script
    """
    pass

class Docsctrinsample3:
    """
    If you need to provide custom file storage -- a common example is storing files
    on some remote system -- you can do so by defining a custom storage class.
    You'll need to follow these steps:

    #. Your custom storage system must be a subclass of
    ``django.core.files.storage.Storage``::

            from django.core.files.storage import Storage


            class MyStorage(Storage):
                ...

    #. Django must be able to instantiate your storage system without any arguments.
    This means that any settings should be taken from ``django.conf.settings``::

            from django.conf import settings
            from django.core.files.storage import Storage


            class MyStorage(Storage):
                def __init__(self, option=None):
                    if not option:
                        option = settings.CUSTOM_STORAGE_OPTIONS
                    ...

    #. Your storage class must implement the :meth:`_open()` and :meth:`_save()`
    methods, along with any other methods appropriate to your storage class. See
    below for more on these methods.

    In addition, if your class provides local file storage, it must override
    the ``path()`` method.

    #. Your storage class must be :ref:`deconstructible <custom-deconstruct-method>`
    so it can be serialized when it's used on a field in a migration. As long
    as your field has arguments that are themselves
    :ref:`serializable <migration-serializing>`, you can use the
    ``django.utils.deconstruct.deconstructible`` class decorator for this
    (that's what Django uses on FileSystemStorage).

    By default, the following methods raise ``NotImplementedError`` and will
    typically have to be overridden:

    * `Storage.delete`
    * :meth:`Storage.exists`
    * :meth:`Storage.listdir`
    * :meth:`Storage.size`
    * :meth:`Storage.url`

    You'll also usually want to use hooks specifically designed for custom storage
    objects. These are:

    .. method:: _open(name, mode='rb')


    .. versionadded:: 4.2

    Storages are then accessed by alias from from the
    :data:`django.core.files.storage.storages` dictionary::

        from django.core.files.storage import storages

        example_storage = storages["example"]"""
    pass
