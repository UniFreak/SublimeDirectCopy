import sublime, sublime_plugin

settings = {}

def plugin_loaded():
    global settings
    settings = sublime.load_settings('DirectCopy.sublime-settings')


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
