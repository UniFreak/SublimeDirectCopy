中文文档请见 [这里][readmecn]

## Installation

There are two ways to install, the first and recommended way is via `Package Control`:

1. Make sure you have `Package Control` installed, see <https://packagecontrol.io/installation>
2. Search for `Direct Copy` using `Package Control` and install

Another way is to clone source from github:

1. Browse into your sublime text's package folder
2. Run `git clone https://github.com/UniFreak/SublimeDirectCopy.git`

## Configuration & Usage

There is already a configured `demo` entry in the setting file, you can add your own copy entries according to `demo` configuration. The entry name is configured by `title` and content by `content`, like this:

```json
{
    "entry":
    [
        {
            "title" : "demo",
            "content" : "demo contens copied from direct copy"
        },
    ]
}
```

After this, you can then bring up the copy entry selection pop-up by hitting `ctrl+shift+c` (Windows) or `super+shift+c` (Mac) and select one for copy. like this:

![example](./shot.png)

[readmecn]: https://github.com/UniFreak/SublimeDirectCopy/blob/master/README.cn.md
