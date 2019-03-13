import sublime, sublime_plugin

settings = {}

def plugin_loaded():
    global settings

    # if user-setting file is empty, load default setting into user-setting file
    defaultFile = 'Default.sublime-settings'
    userFile = 'DirectCopy.sublime-settings'

    userSettings = sublime.load_settings(userFile)
    if userSettings.get('entry') is None:
        default = sublime.load_settings(defaultFile)
        userSettings.set('entry', default.get('entry'))
        sublime.save_settings(userFile)

    settings = sublime.load_settings(userFile)


class DirectCopyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        entries = settings.get('entry')
        options = []
        self.contents = []

        for e in entries:
            options.append(e['title'])
            self.contents.append(e['content'])

        self.view.window().show_quick_panel(options, on_select = self.copy)

    def copy(self, index):
        if index != -1:
            sublime.set_clipboard(self.contents[index])
