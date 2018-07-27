"""wxPython Checkbox Tree Example"""

import wx
import wx.lib.agw.customtreectrl as ct


class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        self.make_menu()
        self.make_tree()
        self.CreateStatusBar()

        self.SetStatusText("Welcome to wxPython!")

    def make_tree(self):
        """Make an issue tree"""
        tree = ct.CustomTreeCtrl(self)
        
        root = tree.AddRoot('Issue', ct_type=1)
        tree.AppendItem(root, 'Analysis', ct_type=1)
        tree.AppendItem(root, 'Development', ct_type=1)
        tree.AppendItem(root, 'Testing', ct_type=1)

        tree.Expand(root)

    def make_menu(self):
        """Make main menu"""

        file_menu = wx.Menu()

        hello_item = file_menu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        menu = wx.MenuBar()
        menu.Append(file_menu, "&File")
        menu.Append(help_menu, "&Help")

        self.SetMenuBar(menu)

        self.Bind(wx.EVT_MENU, self.on_hello, hello_item)
        self.Bind(wx.EVT_MENU, self.on_exit,  exit_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)


    def on_exit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def on_hello(self, event):
        """Show About window"""
        wx.MessageBox("A little checkbox tree")


    def on_about(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Checkbox Tree')
    frm.Show()
    app.MainLoop()
