"""
GUI Module (tkinter) for chat room
"""
# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import tkinter as tk
from tkinter import ttk, filedialog
from typing import Text
import time
import Profile
from ds_messenger import DirectMessage, DirectMessenger


class Body(tk.Frame):
    """
    Body part of the tk window
    """
    def __init__(self, root, recipient_selected_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the Body instance
        self._draw()

    def node_select(self, event):
        """
        built-in caaling function allow
        user to switch between contact
        """
        print(event)
        idx = self.posts_tree.selection()
        if len(idx) > 0:
            index = int(self.posts_tree.selection()[0])
            entry = self._contacts[index]
            if self._select_callback is not None:
                self._select_callback(entry)

    def insert_contact(self, contact: str):
        """
        insert contact to contact tree
        """
        self._contacts.append(contact)
        id_ = len(self._contacts) - 1
        self._insert_contact_tree(id_, contact)

    def _insert_contact_tree(self, id_, contact: str):
        """
        contact tree that store the contact
        """
        if len(contact) > 25:
            entry = contact[:24] + "..."
        id_ = self.posts_tree.insert('', id_, id_, text=contact)

    def insert_user_message(self, message: str):
        """
        insert the message user send to the entry frame
        """
        self.entry_editor.insert(tk.END, message + '\n', 'entry-right')

    def clear_user_message(self):
        """
        clear out all the message
        """
        self.entry_editor.delete(1.0, tk.END)

    def insert_contact_message(self, message: str):
        """
        insert the message the contact send to the entry frame
        """
        self.entry_editor.insert(tk.END, message + '\n', 'entry-left')

    def get_text_entry(self) -> str:
        """
        get the text entered in the text entry
        """
        return self.message_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text: str):
        """
        set the text entry to specific text
        """
        self.message_editor.delete(1.0, tk.END)
        self.message_editor.insert(1.0, text)

    def _draw(self):
        posts_frame = tk.Frame(master=self, width=250)
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP,
                             expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        message_frame = tk.Frame(master=self, bg="yellow")
        message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        self.message_editor = tk.Text(message_frame, width=0, height=5)
        self.message_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                                 expand=True, padx=0, pady=0)

        self.entry_editor = tk.Text(editor_frame, width=0, height=5)
        self.entry_editor.tag_configure('entry-right', justify='right',
                                        foreground='yellow')
        self.entry_editor.tag_configure('entry-left', justify='left',
                                        foreground='pink')
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                               expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame,
                                              command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT,
                                    expand=False, padx=0, pady=0)


class Footer(tk.Frame):
    """
    Footer that contained send button
    """
    def __init__(self, root, send_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._draw()

    def send_click(self):
        """
        check if send button was clicked
        """
        if self._send_callback is not None:
            self._send_callback()

    def _draw(self):
        save_button = tk.Button(master=self, text="Send", width=20,
                                font=("Courier", 15),
                                command=self.send_click)
        # You must implement this.
        # Here you must configure the button to bind its click to
        # the send_click() function.
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)


class NewContactDialog(tk.simpledialog.Dialog):
    """
    Class used for configuring server and set up username and password
    """
    def __init__(self, root, title=None, user=None, pwd=None, server=None):
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        super().__init__(root, title)

    def body(self, frame):
        self.server_label = tk.Label(frame, width=30, text="DS Server Address")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, self.server)
        self.server_entry.pack()

        self.username_label = tk.Label(frame, width=30, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, self.user)
        self.username_entry.pack()

        self.password_label = tk.Label(frame, width=30, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(frame, width=30)
        self.password_entry['show'] = '*'
        self.password_entry.insert(tk.END, self.pwd)
        self.password_entry.pack()
        # You need to implement also the region for the user to enter
        # the Password. The code is similar to the Username you see above
        # but you will want to add self.password_entry['show'] = '*'
        # such that when the user types, the only thing that appears are
        # * symbols.
        # self.password...

    def apply(self):
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()
        self.server = self.server_entry.get()


class MainApp(tk.Frame):
    """
    Main class that handled most of functionalities in GUI
    """
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.username = ""
        self.password = ""
        self.server = ""
        self.recipient = None
        self.message = None
        self.direct_messenger = None
        self.dsu_path = ""
        self.profile = Profile.Profile()
        self.friend = None
        # You must implement this! You must configure and
        # instantiate your DirectMessenger instance after this line.
        # self.direct_messenger = ... continue!

        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the root frame
        self._draw()

    def open_file(self):
        """
        open the user selected dsu file
        """
        dsu_file = filedialog.askopenfilename(title="Select a dsu file",
                                              filetypes=[("Dsu files", "*.dsu")
                                                         ])
        try:
            with open(dsu_file, encoding='utf-8') as my_f:
                print(f"{dsu_file} is opened")
            self.profile.load_profile(dsu_file)
            self.username = self.profile.username
            self.password = self.profile.password
            self.server = self.profile.dsuserver
            self.friend = self.profile._friend
            single_friend = {}
            place_holder = 0
            for friend in self.friend:
                single_friend[friend] = place_holder
                place_holder += 1
            for key in single_friend.keys():
                self.body.insert_contact(key)
            self.message = self.profile._messages
            self.dsu_path = dsu_file
        except (FileNotFoundError, Profile.DsuFileError):
            tk.messagebox.showwarning(
                        message="You've cancelled to open the dsu file")
        except Profile.DsuProfileError:
            tk.messagebox.showwarning(
                        message="Unable to load empty file")

    def create_file(self):
        """
        create new dsu file
        """
        try:
            f_name = tk.simpledialog.askstring(
                "Ask file name", "Enter file name: ")
            with open(f_name + ".dsu", "w", encoding='utf-8') as file:
                pass
            print(f_name + ".dsu was created")
            self.dsu_path = f_name + ".dsu"
        except TypeError:
            tk.messagebox.showwarning(
                message="You've cancelled to create a file")

    def close_gui(self):
        """
        Exit the GUI
        """
        self.root.destroy()
        print('Exit')

    def send_message(self):
        """
        function for send button
        """
        try:
            msg = self.body.get_text_entry()
            send_check = self.direct_messenger.send(msg, self.recipient)
            if (self.recipient is not None) and send_check:
                self.body.insert_user_message(f'{self.username}: ' + msg)
                dir_msg = DirectMessage()
                dir_msg.set_attributes(msg, self.recipient,
                                       "[me]" + str(time.time()))
                self.message.append(dir_msg)
                self.profile.save_profile(self.dsu_path)

            self.body.set_text_entry("")
        except AttributeError:
            tk.messagebox.showwarning(
                message="Either choose friend to send message OR Entered \
                message to sent")
        except KeyError:
            tk.messagebox.showwarning(
                message="Invalid password or username")
        except ConnectionRefusedError:
            tk.messagebox.showwarning(message="Invalid server address")

    def add_contact(self):
        """
        add contact to the contact tree
        """
        try:
            name = tk.simpledialog.askstring(
                "Add Contact", "Enter friend name: ")
            self.body.insert_contact(name)
            self.profile._friend.append(name)
            self.profile.save_profile(self.dsu_path)
        except TypeError:
            tk.messagebox.showinfo(message="You've cancelled to add contact")

    def recipient_selected(self, recipient):
        """
        Handling the action when user switching the chat room
        """
        self.body.clear_user_message()
        all_msg = []
        for dm_ in self.message:
            if recipient == dm_["recipient"]:
                all_msg.append(dm_)
        all_msg.sort(key=lambda x: x["timestamp"].strip('[me]'))
        for msg in all_msg:
            if "[me]" in msg["timestamp"]:
                self.body.insert_user_message(
                    f'{self.username}: ' + msg["message"])
            else:
                self.body.insert_contact_message(
                    f'{recipient}: ' + msg["message"])
        self.recipient = recipient

    def configure_server(self):
        """
        funciton to connect to the server
        """
        try:
            ud_ = NewContactDialog(self.root, "Configure Account",
                                   self.username, self.password, self.server)
            self.username = ud_.user
            self.password = ud_.pwd
            self.server = ud_.server
            self.profile.username = self.username
            self.profile.password = self.password
            self.profile.dsuserver = self.server
            self.profile.save_profile(self.dsu_path)
            # You must implement this!
            # You must configure and instantiate your
            # DirectMessenger instance after this line.
            dir_messenger = DirectMessenger(self.server, self.username,
                                            self.password)
            self.direct_messenger = dir_messenger
        except Profile.DsuFileError:
            tk.messagebox.showinfo(
                message="You've cancelled to configured server")

    def check_new(self):
        """
        check if there are new message every 3 sec
        after connect to the server
        """
        if self.direct_messenger is not None:
            try:
                new_msg_lst = self.direct_messenger.retrieve_new()
                for dir_msg_obj in new_msg_lst:
                    self.body.insert_contact_message(
                        f'{self.recipient}: ' + dir_msg_obj.__dict__["message"]
                        )
                    if dir_msg_obj.__dict__["recipient"] in self.friend:
                        pass
                    else:
                        self.friend.append(dir_msg_obj.__dict__["recipient"])
                        self.body.insert_contact(
                            dir_msg_obj.__dict__["recipient"])
                    self.message.append(dir_msg_obj.__dict__)
                    self.profile.save_profile(self.dsu_path)
            except ConnectionRefusedError:
                tk.messagebox.showinfo(
                    message="You've cancelled to configured server")
        else:
            pass
        main.after(3000, app.check_new)

    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.create_file)
        menu_file.add_command(label='Open...', command=self.open_file)
        menu_file.add_command(label='Close', command=self.close_gui)

        settings_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=settings_file, label='Settings')
        settings_file.add_command(label='Add Contact',
                                  command=self.add_contact)
        settings_file.add_command(label='Configure DS Server',
                                  command=self.configure_server)

        # The Body and Footer classes must be initialized and
        # packed into the root window.
        self.body = Body(self.root,
                         recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.footer = Footer(self.root, send_callback=self.send_message)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)


if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social Messenger")

    # This is just an arbitrary starting point. You can change the value
    # around to see how the starting size of the window changes.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that
    # some modern OSes don't support. If you're curious, feel free to comment
    # out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the
    # widgets used in the program. All of the classes that we use,
    # subclass Tk.Frame, since our root frame is main, we initialize
    # the class with it.
    app = MainApp(main)

    # When update is called, we finalize the states of all widgets that
    # have been configured within the root frame. Here, update ensures that
    # we get an accurate width and height reading based on the types of widgets
    # we have used. minsize prevents the root window from resizing too small.
    # Feel free to comment it out and see how the resizing
    # behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    id_o = main.after(2000, app.check_new)
    print(id_o)
    # And finally, start up the event loop for the program (you can find
    # more on this in lectures of week 9 and 10).
    main.mainloop()
